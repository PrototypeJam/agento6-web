# python module2.py
import asyncio
import json
import os
import logging
import datetime
from typing import Any, List, Dict, Optional

# Monkey patching first
import openai
def _mock_get_default_openai_client(*args, **kwargs):
    return None
openai.AsyncOpenAI._get_default_openai_client = _mock_get_default_openai_client
openai.OpenAI._get_default_openai_client = _mock_get_default_openai_client

from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError, field_validator

from agents import Agent, GuardrailFunctionOutput, OutputGuardrail, Runner, handoff
from agents.handoffs import Handoff
from agents.run_context import RunContextWrapper
from agents.lifecycle import AgentHooks

load_dotenv()  # Load environment variables

# --- Setup Logging ---
def setup_logging(module_name):
    """Set up logging to both console and file."""
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create a timestamp for the log filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(logs_dir, f"{module_name}_{timestamp}.log")
    
    # Configure logging
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    
    # Clear any existing handlers
    if logger.handlers:
        logger.handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    
    return logger

# Initialize logger
logger = setup_logging("module2")

# --- Custom Agent Hooks for Detailed Logging ---
class DetailedLoggingHooks(AgentHooks):
    def __init__(self, logger):
        self.logger = logger

    async def before_generate(
        self, agent: Agent, inputs: List[Dict[str, Any]], context: RunContextWrapper[Any]
    ):
        """Log details before LLM generation."""
        self.logger.info(f"===== API CALL: {agent.name} =====")
        self.logger.info(f"Inputs to {agent.name}: {json.dumps(inputs, indent=2)}")
        return inputs
    
    async def after_generate(
        self, agent: Agent, response: Any, context: RunContextWrapper[Any]
    ):
        """Log details after LLM generation."""
        self.logger.info(f"===== API RESPONSE: {agent.name} =====")
        # Format the response for better readability
        try:
            response_content = json.dumps(response.final_output, indent=2) if hasattr(response, 'final_output') else str(response)
            self.logger.info(f"Response from {agent.name}: {response_content}")
        except Exception as e:
            self.logger.info(f"Response from {agent.name}: {str(response)}")
            self.logger.info(f"Could not format response as JSON: {e}")
        return response

# Create logging hooks
logging_hooks = DetailedLoggingHooks(logger)

# --- Pydantic Models ---
class SuccessCriteria(BaseModel):
    criteria: str
    reasoning: str
    rating: int = Field(..., description="Rating of the criterion (1-10)")
    
    @field_validator('rating')
    def check_rating(cls, v):
        if not 1 <= v <= 10:
            raise ValueError('Rating must be between 1 and 10')
        return v

class Module1Output(BaseModel):  # Updated to match the new Module 1 output
    goal: str
    success_criteria: list[SuccessCriteria]
    selected_criteria: list[SuccessCriteria]  # Now a list of criteria

class PlanItem(BaseModel):  # Represents a single item *within* a plan
    item_title: str = Field(..., description="A concise title for this plan item.")
    item_description: str = Field(..., description="A description of this step in the plan.")

class PlanOutline(BaseModel):
    plan_title: str = Field(..., description="A title for the overall plan.")
    plan_description: str = Field(..., description="A brief summary of the plan approach")
    plan_items: list[PlanItem] = Field(..., description="A list of plan items.")
    reasoning: str = Field(..., description="Reasoning for why this plan is suitable.")
    rating: int = Field(..., description="Rating of the plan's suitability (1-10).")
    created_by: str = Field(..., description="The name of the agent that created this plan")

    @field_validator('plan_items')
    def check_plan_items(cls, v):
        if len(v) < 3:
            raise ValueError('Must provide at least three plan items')
        return v

    @field_validator('rating')
    def check_rating(cls, v):
        if not 1 <= v <= 10:
            raise ValueError('Rating must be between 1 and 10')
        return v

class Module2Output(BaseModel):
    goal: str
    selected_criteria: list[SuccessCriteria]  # Updated to list
    plan_outlines: list[PlanOutline]
    selected_outline: PlanOutline

# --- Specialized Planning Agents ---

# Base instructions for plan generators
base_plan_instructions = """
You are a strategic planner specialized in {domain}. Given a goal and success criteria, 
generate THREE distinct, high-level outlines for plans to achieve the goal. 
Each plan outline MUST consist of a title, an overall approach description, and at least THREE distinct plan items.
Each plan item should have a short title and a concise description of the step.
Provide a brief reasoning for each overall plan and a rating from 1 to 10.
Ensure that your plans address ALL of the success criteria.

Important: For each plan outline, include a 'created_by' field with your agent name.
"""

# Three specialized agents with different planning focuses
practical_agent = Agent(
    name="Practical Planner",
    instructions=base_plan_instructions.format(domain="practical, actionable plans"),
    model="gpt-4o",
    output_type=list[PlanOutline],
    handoff_description="Creates practical, actionable plans with concrete steps",
    hooks=logging_hooks,
)

creative_agent = Agent(
    name="Creative Planner",
    instructions=base_plan_instructions.format(domain="creative, innovative approaches"),
    model="gpt-4o",
    output_type=list[PlanOutline],
    handoff_description="Creates innovative, out-of-the-box plans with creative approaches",
    hooks=logging_hooks,
)

balanced_agent = Agent(
    name="Balanced Planner",
    instructions=base_plan_instructions.format(domain="balanced, well-rounded solutions"),
    model="gpt-4o",
    output_type=list[PlanOutline],
    handoff_description="Creates balanced plans that combine practical and creative elements",
    hooks=logging_hooks,
)

# Create a direct planner without handoffs as a fallback
direct_planner = Agent(
    name="Direct Planner",
    instructions=(
        "You are a strategic planner. Given a goal and success criteria, "
        "generate THREE distinct, high-level outlines for plans to achieve that goal. "
        "Each plan outline MUST consist of a title, an overall approach description, and at least THREE distinct plan items. "
        "Each plan item should have a short title and a concise description of the step. "
        "Provide a brief reasoning for each overall plan and a rating from 1 to 10. "
        "Ensure that your plans address ALL of the success criteria. "
        "Include 'Direct Planner' as the created_by field for each plan."
    ),
    model="gpt-4o",
    output_type=list[PlanOutline],
    hooks=logging_hooks,
)

# Handoff callbacks for logging
async def on_practical_handoff(ctx: RunContextWrapper[None]):
    logger.info("Handing off to Practical Planner agent")

async def on_creative_handoff(ctx: RunContextWrapper[None]):
    logger.info("Handing off to Creative Planner agent")

async def on_balanced_handoff(ctx: RunContextWrapper[None]):
    logger.info("Handing off to Balanced Planner agent")

# Triage agent that will hand off to the specialized agents
triage_agent = Agent(
    name="Planning Triage",
    instructions=(
        "You are a planning coordinator. Based on the user's goal and success criteria, "
        "decide which specialized planning agent would be most appropriate to handle this request. "
        "You have three options:\n"
        "1. Practical Planner: For goals that need structured, actionable plans\n"
        "2. Creative Planner: For goals that need innovative, out-of-the-box thinking\n"
        "3. Balanced Planner: For goals that need a mix of practical and creative approaches\n"
        "Consider the goal carefully and make your selection by using the appropriate handoff."
    ),
    model="gpt-4o",
    handoffs=[
        handoff(practical_agent, on_handoff=on_practical_handoff),
        handoff(creative_agent, on_handoff=on_creative_handoff),
        handoff(balanced_agent, on_handoff=on_balanced_handoff)
    ],
    hooks=logging_hooks,
)

# Evaluation agent to select the best plan
evaluate_outline_agent = Agent(
    name="PlanEvaluator",
    instructions=(
        "You are an expert plan evaluator. You are given a goal, multiple success "
        "criteria, and several plan outlines. Each plan outline contains multiple items. "
        "Select the ONE plan outline that, if implemented, would be most likely "
        "to achieve the goal and satisfy ALL of the success criteria. "
        "Consider how well each plan addresses each criterion. "
        "Provide detailed reasoning for your selection. Output only the selected plan."
    ),
    model="gpt-4o",
    output_type=PlanOutline,
    hooks=logging_hooks,
)

async def validate_module2_output(
    agent: Agent, agent_output: Any, context: RunContextWrapper[None]
) -> GuardrailFunctionOutput:
    """Validates the output of Module 2."""
    try:
        logger.info("Validating Module 2 output...")
        logger.info(f"Output to validate: {json.dumps(agent_output.model_dump() if hasattr(agent_output, 'model_dump') else agent_output, indent=2)}")
        Module2Output.model_validate(agent_output)
        logger.info("Module 2 output validation passed")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)
    except ValidationError as e:
        logger.error(f"Module 2 output validation failed: {e}")
        return GuardrailFunctionOutput(
            output_info={"error": str(e)}, tripwire_triggered=True
        )

async def run_module_2(input_file: str, output_file: str) -> None:
    """Runs Module 2."""
    context = RunContextWrapper(context=None)
    
    try:
        logger.info(f"Starting Module 2, reading input from {input_file}")
        with open(input_file, "r") as f:
            module_1_data = json.load(f)
            logger.info(f"Successfully loaded data from {input_file}")
            
        # Convert to Pydantic objects and extract key information
        module_1_output = Module1Output.model_validate(module_1_data)
        goal = module_1_output.goal
        selected_criteria = module_1_output.selected_criteria
        
        logger.info(f"Goal: {goal}")
        logger.info(f"Number of selected criteria: {len(selected_criteria)}")
        for i, criterion in enumerate(selected_criteria, 1):
            logger.info(f"Criterion {i}: {criterion.criteria}")

        # Prepare input for triage agent
        criteria_text = "\n".join([f"- {c.criteria}" for c in selected_criteria])
        triage_input = (
            f"Goal: {goal}\n\n"
            f"Success Criteria:\n{criteria_text}\n\n"
            f"Based on this goal and these success criteria, hand off to the most appropriate specialized planning agent."
        )
        
        # Log the full input being sent to the triage agent
        logger.info(f"Triage agent input: {triage_input}")
        
        # Try running the triage agent with handoffs
        try:
            # Run triage agent to select the appropriate specialized agent
            logger.info("Running triage agent to select specialized planner...")
            triage_result = await Runner.run(
                triage_agent,
                input=triage_input,
                context=context,
            )
            
            # The triage agent should have handed off to a specialized agent
            # Check which agent was used through handoffs
            logger.info("Retrieving plans from specialized agent...")
            last_agent_name = triage_result.last_agent.name
            logger.info(f"Last agent used: {last_agent_name}")
            
            # Extract the results, which should be a list of PlanOutlines
            plan_outlines = triage_result.final_output
            
            # Log the raw output from the agent
            logger.info(f"Raw plan outlines output: {json.dumps(plan_outlines, indent=2) if isinstance(plan_outlines, list) else str(plan_outlines)}")
            
        except Exception as e:
            # If triage fails, fall back to direct planner
            logger.error(f"Triage agent failed with error: {e}. Using direct planner as fallback.")
            
            # Format criteria for direct planning
            criteria_json = json.dumps([c.model_dump() for c in selected_criteria], indent=2)
            direct_input = (
                f"Goal: {goal}\n\n"
                f"Success Criteria: {criteria_json}\n\n"
                f"Please create three plan outlines that address this goal and all success criteria."
            )
            
            # Log the direct planner input
            logger.info(f"Direct planner input: {direct_input}")
            
            # Run the direct planner
            direct_result = await Runner.run(
                direct_planner,
                input=direct_input,
                context=context,
            )
            
            # Use the direct planner's output
            plan_outlines = direct_result.final_output
            logger.info(f"Generated {len(plan_outlines)} plans using direct planner")
        
        # Ensure each plan has the created_by field
        logger.info("Processing plan outlines...")
        processed_plan_outlines = []
        for i, plan in enumerate(plan_outlines):
            # Log the plan details
            logger.info(f"Plan {i+1}: {plan.plan_title}")
            # Convert plan to dictionary for processing
            plan_dict = plan.model_dump()
            if 'created_by' not in plan_dict or not plan_dict['created_by']:
                plan_dict['created_by'] = "Default Planner"
                logger.info(f"Added missing created_by field for plan: {plan.plan_title}")
            
            # Create a new PlanOutline from the processed dictionary
            processed_plan = PlanOutline.model_validate(plan_dict)
            processed_plan_outlines.append(processed_plan)
            logger.info(f"Processed plan: '{processed_plan.plan_title}' by {processed_plan.created_by}")
        
        # Format criteria for evaluation input
        criteria_json = json.dumps([c.model_dump() for c in selected_criteria], indent=2)
        
        # Evaluate plan outlines
        logger.info("Evaluating plan outlines...")
        evaluation_input = (
            f"Goal: {goal}\n"
            f"Success Criteria: {criteria_json}\n\n"
            f"Outlines:\n{json.dumps([o.model_dump() for o in processed_plan_outlines], indent=2)}"
        )
        logger.info(f"Evaluation agent input: {evaluation_input[:500]}...")
        
        evaluation_result = await Runner.run(
            evaluate_outline_agent,
            input=evaluation_input,
            context=context,
        )
        
        selected_outline = evaluation_result.final_output
        logger.info(f"Selected outline: '{selected_outline.plan_title}'")
        logger.info(f"Full selected outline: {json.dumps(selected_outline.model_dump(), indent=2)}")

        # Prepare and Save Output
        module_2_output = Module2Output(
            goal=goal,
            selected_criteria=selected_criteria,
            plan_outlines=processed_plan_outlines,
            selected_outline=selected_outline,
        )

        # Apply guardrail
        logger.info("Applying output guardrail...")
        guardrail = OutputGuardrail(guardrail_function=validate_module2_output)
        guardrail_result = await guardrail.run(
            agent=evaluate_outline_agent,
            agent_output=module_2_output,
            context=context,
        )
        if guardrail_result.output.tripwire_triggered:
            logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
            return

        # --- Smart JSON Export ---
        # Create data directory if it doesn't exist
        output_dir = os.path.dirname(output_file)
        os.makedirs(output_dir, exist_ok=True)
        
        # Create timestamped version
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.basename(output_file)
        name, ext = os.path.splitext(filename)
        timestamped_file = os.path.join(output_dir, f"{name}_{timestamp}{ext}")
        
        # Export both versions
        with open(output_file, "w") as f:
            json.dump(module_2_output.model_dump(), f, indent=4)
        with open(timestamped_file, "w") as f:
            json.dump(module_2_output.model_dump(), f, indent=4)
        
        logger.info(f"Module 2 completed. Output saved to {output_file}")
        logger.info(f"Timestamped output saved to {timestamped_file}")

    except Exception as e:
        logger.error(f"An error occurred in Module 2: {e}")
        import traceback
        logger.error(traceback.format_exc())  # Log the full stack trace

async def main():
    logger.info("Starting main function")
    input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    input_file = os.path.join(input_dir, "module1_output.json")
    output_file = os.path.join(input_dir, "module2_output.json")
    await run_module_2(input_file, output_file)
    logger.info("Main function completed")

if __name__ == "__main__":
    logger.info("Module 2 script starting")
    asyncio.run(main())
    logger.info("Module 2 script completed")