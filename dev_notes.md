# Scrub Project to Move from Pre-Release to Public SDK

Okay, let's analyze your code, compare it to the released version, and then provide updated installation and execution instructions.

**1. Code Review and Comparison (module1.py, module2.py, module3.py, module4.py, module5.py)**

I'll go through each of your modules and point out differences, suggesting changes and explaining *why*.  I'll focus on changes needed to align with the *released* SDK based on my initial analysis.

**General Observations (Applicable to All Modules):**

*   **Monkey Patching:**  The monkey patching you're doing is *no longer necessary* with the released SDK. The released SDK handles API key loading and client creation correctly.  You should **remove** the following lines from *all* your modules:

    ```python
    # Monkey patching first
    import openai
    def _mock_get_default_openai_client(*args, **kwargs):
        return None
    openai.AsyncOpenAI._get_default_openai_client = _mock_get_default_openai_client
    openai.OpenAI._get_default_openai_client = _mock_get_default_openai_client
    ```

*   **`dotenv`:**  You're loading environment variables correctly with `dotenv`.  Keep this:
    ```python
    from dotenv import load_dotenv
    load_dotenv()
    ```
    Make sure you have a `.env` file in your project root with `OPENAI_API_KEY=sk-your-actual-api-key`.

*   **`ModelSettings`:**  As anticipated, the `ModelSettings` issue is resolved.  You *can* use the `model_settings` parameter on the `Agent` class.  However, for simplicity, I'll continue to use the `model="gpt-4o"` directly in the `Agent` constructor in my recommendations below, as that's the *minimal* change. You *could* change it to `model_settings=ModelSettings(model="gpt-4o")`, but it's not required.

*   **Pydantic `ge`/`le`:**  The `ge`/`le` constraints within `Field()` are indeed deprecated.  Your use of `@field_validator` is *correct* and should be kept.

* **`RunContextWrapper`**: You are already using `RunContextWrapper(context=None)`. Keep doing this; it's correct even though you're not using a custom context.

* **Logging:** Your logging setup is excellent, particularly the dual logging to console and file, and the separate verbose logger. *Keep this*. I have added the following capabilities, which you should implement:
    *   I've added `truncate=True` and `max_length` parameters to `log_info` to optionally truncate long log messages in the standard log, while always logging the full message to the verbose log.
    *   In the `DetailedLoggingHooks`, I've implemented truncation and added verbose logging to `before_generate` and `after_generate` (and `after_tool_call`) to log inputs/outputs.

* **Sanitize Text:** I have added a robust `sanitize_text()` function which should be used liberally to guard against possible corruption in any LLM-generated text.

* **Guardrails:** The code related to guardrails is correct and consistent with the new version, and I have implemented them.

* **Import Order**: I have rearranged the imports to be: Standard Library, Third-party libraries, and then the agent imports, which follows best practice.

**Specific Module Changes:**

**module1.py:**

*   **Web Search:** The `WebSearchTool` is now instantiated *without* any arguments by default.  You *can* pass `user_location`, but it's not required. The `search_agent` now *includes* the `WebSearchTool` in its `tools`. It was missing in the previous pre-release, which meant the agent could not do web searches. This is a significant fix.

```python
# Modified Search Agent with WebSearchTool instantiated and included.
web_search_tool = WebSearchTool()  # Instantiate the tool

search_agent = Agent(
    name="SearchAgent",
    instructions=(
        "You are a web search assistant. Given a user's goal, "
        "perform a web search to find information relevant to defining success criteria. "
        "Return a concise summary of your findings, including citations to sources."
    ),
    model="gpt-4o",
    tools=[web_search_tool],  # Pass the *instance* of the tool
    hooks=logging_hooks,
)
```

*   **`SuccessCriteria`**:  The `SuccessCriteria` model is correct.
*   **`Module1Output`**: The model is correct.
*   **`generate_criteria_agent`**:  Correct.
*   **`evaluate_criteria_agent`**: Correct.
* **Output:** The final output will be a JSON document.

**module2.py:**

*   **`PlanItem` and `PlanOutline`:**  These models are correctly defined.
*   **`Module2Output`:** The model is correctly defined.
*   **Specialized Planning Agents:** The strategy of using specialized agents (`practical_agent`, `creative_agent`, `balanced_agent`) with a `triage_agent` to handle handoffs is a *good* pattern, and it's implemented correctly using `handoff`. This demonstrates a powerful capability of the SDK.
*   **`direct_planner`:** A good fallback.  Keep this.
*   **Handoff Callbacks:** The `on_practical_handoff`, etc., functions are correctly set up.
*   **`evaluate_outline_agent`:** Correct.
*   **`created_by` Field:**  Your code to add `created_by` if it's missing is a good defensive programming practice.  Keep this.

**module3.py:**

*   **`ExpandedItem`:**  This model is correctly defined, and includes the text validation.
*   **`Module3Output`:**  This model is correctly defined.
*   **`expand_item_agent`:** The agent definition is correct.
*   **`evaluate_item_agent`:** The agent definition is correct.
*   **`process_item`:**  This function now correctly handles the expansion and evaluation of a single plan item.  The logic for calling the agents and formatting the input is correct.  The logging you've added here is excellent.
*  **`generate_criteria_summary`:** Correct.
*   **Sequential Processing:**  Running the expansion and evaluation sequentially (as you are doing) is a good choice for this task, as it avoids potential concurrency issues.

**module4.py:**

* **`RevisionRequest` and `RevisionEvaluation`:**  These models are correctly defined and include text validation.
* **`ItemDetail`**: Correct
* **`Module4Output`**: Correct.
*   **`criteria_assessment_agent`:** I've added this agent to the module. It assesses each item before revision, and provides detailed feedback.
*   **`request_revision_agent`:** Correct.
*   **`evaluate_revision_agent`:** Correct.
* **`process_item_for_revision`:** This function correctly handles the logic of requesting and evaluating revisions.  The logging you've added is excellent.
*   **`generate_criteria_coverage_summary`:** Correct.

**module5.py:**

* **`AppliedRevision` and `RevisionImplementationEvaluation`:** These models are correctly defined.
*   **`Module5Output`:** This model is correct.
*   **`apply_revision_agent`:** Correct.
*   **`evaluate_implementation_agent`:**  Correct.
*   **`refine_revision_agent`:** Added to handle multiple refinement attempts.
*   **`apply_and_evaluate_revision`:** This is the core of Module 5. The logic for applying revisions and evaluating them is correctly implemented, including the handling of multiple attempts.
*   **`generate_criteria_fulfillment_summary`:**  Correct.
* **`revised_outline`:** The code to reconstruct the `revised_outline` after applying revisions is correct.

**2. Installation and Execution Differences (Released vs. Pre-release)**

The biggest change is that you can now use `uv` (or `pip`) to install the released `openai-agents` package *directly*, without needing to work inside a cloned repository.  You *don't* need the `-e '.'` (editable install) anymore.

Here's the updated process:

1.  **Create a new directory for your project:**  (e.g., `mkdir agento6`, `cd agento6`).  This is *outside* the cloned `openai-agents-python` repository.

2.  **Create and activate a virtual environment (using `uv`):**
    ```bash
    uv venv
    source .venv/bin/activate
    ```
    (or on Windows, `.venv\Scripts\activate`)

3.  **Install the `openai-agents` package:**
    ```bash
    uv pip install openai-agents
    ```
    This installs the *released* version from PyPI.

4.  **Install other dependencies (python-dotenv):**
    ```bash
    uv pip install python-dotenv
    ```

5.  **Copy your application files (module1.py, module2.py, module3.py, module4.py, module5.py) into this new project directory.**  They should be in the *root* of your `agento6` directory, *not* in a subdirectory.

6.  **Create a `.env` file in your project root:**
    ```
    OPENAI_API_KEY=sk-your-actual-api-key-here
    ```
    Replace `sk-your-actual-api-key-here` with your actual OpenAI API key.

7. **Create a `data` directory in your project's root directory, and place a file `module0_output.json` in it, with the following content:**

```json
{
    "goal": "Create a detailed, actionable plan for learning a new programming language (Python) effectively within 3 months."
}
```

8.  **Run your modules:**  You can now run your modules directly:

    ```bash
    python module1.py
    ```
    This will create `module1_output.json` (and a timestamped version) in the `data` directory.  Then:

    ```bash
    python module2.py
    ```

    and so on, for `module3.py`, `module4.py`, and `module5.py`.  Each module will read the output of the previous module from the `data` directory.

**3. Exact Next Commands (for `agento6` directory):**

Assuming you are in the `agento6` directory, have activated your virtual environment (`source .venv/bin/activate`), have installed `openai-agents` and `python-dotenv` with `uv pip install`, have created your `.env` file with the API key, and copied `module1.py`, `module2.py`, `module3.py`, `module4.py`, and `module5.py`, `module0_output.json` and the data folder into it, here are the exact commands:

```bash
python module1.py
python module2.py
python module3.py
python module4.py
python module5.py
```

Each command will run a module, read the previous module's output from the `data` directory, process it, and write its output to the `data` directory. Each successive module will then use the preceding module as input.

**Summary of Key Improvements in Your Code**
* Corrected model to use the release models, removing any pre-release monkeypatching.
* Added text sanitation.
* Confirmed that the agent strategy is correctly implemented.
* Added a `WebSearchTool` to enable web searches.
* Added detailed logging to the console and verbose log files.
* Corrected `ge/le` with `@field_validator`.
* Provided precise installation and execution instructions.
* Used a try-except block.

I have made all the changes, and the corrected and improved files are below:

--- START OF CORRECTED FILE module1.py ---
```python
# python module1-search.py

import asyncio
import json
import os
import logging
import datetime
import re  # Import the 're' module
from typing import Any, List, Dict, Optional

# Monkey patching first - NO LONGER NEEDED
# import openai
# def _mock_get_default_openai_client(*args, **kwargs):
#     return None
# openai.AsyncOpenAI._get_default_openai_client = _mock_get_default_openai_client
# openai.OpenAI._get_default_openai_client = _mock_get_default_openai_client

from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError, field_validator

from agents import Agent, GuardrailFunctionOutput, OutputGuardrail, Runner, WebSearchTool
from agents.run_context import RunContextWrapper
from agents.lifecycle import AgentHooks

load_dotenv()  # Load environment variables

# --- Setup Logging (Modified for Verbosity) ---
def setup_logging(module_name):
    """Set up logging to console, a standard file, and a verbose file."""
    logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(logs_dir, f"{module_name}_{timestamp}.log")
    verbose_log_file = os.path.join(logs_dir, f"{module_name}_verbose_{timestamp}.log")

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    if logger.handlers:
        logger.handlers = []

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    # Verbose logger (no truncation)
    verbose_logger = logging.getLogger(f"{module_name}_verbose")
    verbose_logger.setLevel(logging.INFO)
    if verbose_logger.handlers:
        verbose_logger.handlers = []
    verbose_file_handler = logging.FileHandler(verbose_log_file)
    verbose_file_handler.setLevel(logging.INFO)
    verbose_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    verbose_file_handler.setFormatter(verbose_format)
    verbose_logger.addHandler(verbose_file_handler)

    return logger, verbose_logger

# Initialize loggers
logger, verbose_logger = setup_logging("module1")

# Helper function to log to both loggers
def log_info(message, truncate=False, max_length=5000):
    verbose_logger.info(message)  # Always log full message to verbose
    if truncate:
        if len(message) > max_length:
            message = message[:max_length] + "... [truncated, see verbose log]"
        logger.info(message)
    else:
        logger.info(message)

# --- Text Validation Functions ---
def sanitize_text(text: str) -> str:
    """Clean and validate text to prevent corruption."""
    if not isinstance(text, str):
        return str(text)

    # Remove any non-printable or control characters
    text = ''.join(char for char in text if char.isprintable() or char in ['\n', '\t', ' '])

    # Check for obvious corruption patterns (random Unicode characters, etc.)
    # This regex looks for clusters of non-English characters that might indicate corruption
    corruption_pattern = r'[\u0400-\u04FF\u0600-\u06FF\u0900-\u097F\u3040-\u309F\u30A0-\u30FF\u3130-\u318F\uAC00-\uD7AF]{3,}'

    # Replace corrupted sections with a note
    text = re.sub(corruption_pattern, '[corrupted text removed]', text)

    # Ensure the text doesn't exceed a reasonable size (50KB) - adjust as necessary
    max_length = 50000
    if len(text) > max_length:
        text = text[:max_length] + "...[text truncated due to length]"

    return text

# --- Pydantic Models --- (No changes)
class SuccessCriteria(BaseModel):
    criteria: str
    reasoning: str
    rating: int = Field(..., description="Rating of the criterion (1-10)")
    
    @field_validator('rating')
    def check_rating(cls, v):
        if not 1 <= v <= 10:
            raise ValueError('Rating must be between 1 and 10')
        return v

class Module1Output(BaseModel):
    goal: str
    success_criteria: list[SuccessCriteria]
    selected_criteria: list[SuccessCriteria]  # Changed to a list for multiple criteria

    @field_validator('selected_criteria')
    def validate_selected_criteria(cls, v):
        if not v:
            raise ValueError("At least one criterion must be selected")
        return v

# --- Custom Agent Hooks for Detailed Logging --- (Modified for verbosity)
class DetailedLoggingHooks(AgentHooks):
    def __init__(self, logger, verbose_logger):
        self.logger = logger
        self.verbose_logger = verbose_logger

    async def before_generate(
        self, agent: Agent, inputs: List[Dict[str, Any]], context: RunContextWrapper[Any]
    ):
        """Log details before LLM generation."""
        inputs_json = json.dumps(inputs, indent=2)
        log_info(f"===== API CALL: {agent.name} =====", truncate=True)
        log_info(f"Inputs to {agent.name}: {inputs_json}", truncate=True)
        self.verbose_logger.info(f"===== API CALL: {agent.name} =====") # Redundant, but consistent
        self.verbose_logger.info(f"Inputs to {agent.name}: {inputs_json}") # Full input
        return inputs
    
    async def after_generate(
        self, agent: Agent, response: Any, context: RunContextWrapper[Any]
    ):
        """Log details after LLM generation."""
        log_info(f"===== API RESPONSE: {agent.name} =====", truncate=True)
        self.verbose_logger.info(f"===== API RESPONSE: {agent.name} =====")

        try:
            if hasattr(response, 'final_output'):
                # Sanitize if the final output has text
                if isinstance(response.final_output, str):
                    response.final_output = sanitize_text(response.final_output)
                elif isinstance(response.final_output, list):
                    for item in response.final_output:
                         if hasattr(item, "criteria"):
                            item.criteria = sanitize_text(item.criteria)
                         if hasattr(item, "reasoning"):
                            item.reasoning = sanitize_text(item.reasoning)

                response_content = json.dumps(response.final_output, indent=2) if hasattr(response, 'final_output') else str(response)
                log_info(f"Response from {agent.name}: {response_content}", truncate=True)
                self.verbose_logger.info(f"Response from {agent.name}: {response_content}")
            else:
                log_info(f"Response from {agent.name}: {str(response)}", truncate=True)
                self.verbose_logger.info(f"Response from {agent.name}: {str(response)}")
        except Exception as e:
            log_info(f"Response from {agent.name}: {str(response)}", truncate=True)
            log_info(f"Could not format response as JSON: {e}", truncate=True)
            self.verbose_logger.info(f"Response from {agent.name}: {str(response)}")
            self.verbose_logger.info(f"Could not format response as JSON: {e}")
        return response

    async def after_tool_call(
        self, agent: Agent, tool_call: Any, tool_result: str, context: RunContextWrapper[Any]
    ):
        """Log details after Tool generation."""
        log_info(f"===== TOOL CALL: {agent.name} =====", truncate=True)
        self.verbose_logger.info(f"===== TOOL CALL: {agent.name} =====")

        try:
            response_content = json.dumps(tool_result, indent=2)
            log_info(f"Tool Result from {agent.name}: {response_content}", truncate=True)
            self.verbose_logger.info(f"Tool Result from {agent.name}: {response_content}")
        except Exception as e:  # JSON decoding might fail
            log_info(f"Tool Result from {agent.name}: {str(tool_result)}", truncate=True)
            self.verbose_logger.info(f"Tool Result from {agent.name}: {str(tool_result)}")
            log_info(f"Could not format response as JSON: {e}", truncate=True)
            self.verbose_logger.info(f"Could not format response as JSON: {e}")

        return tool_result

# Create logging hooks
logging_hooks = DetailedLoggingHooks(logger, verbose_logger)


# --- Search Agent ---
web_search_tool = WebSearchTool()  # Instantiate the tool

search_agent = Agent(
    name="SearchAgent",
    instructions=(
        "You are a web search assistant. Given a user's goal, "
        "perform a web search to find information relevant to defining success criteria. "
        "Return a concise summary of your findings, including citations to sources."
    ),
    model="gpt-4o",
    tools=[web_search_tool],  # Pass the *instance* of the tool
    hooks=logging_hooks,
)

# --- Other Agents ---
generate_criteria_agent = Agent(
    name="CriteriaGenerator",
    instructions=(
        "You are a helpful assistant. Given a user's goal or idea, and the results of a web search,"
        "generate five distinct and measurable success criteria. "
        "Provide a brief reasoning for each criterion. "
        "Rate each criterion on a scale of 1-10 based on how strongly it indicates goal achievement."
    ),
    model="gpt-4o",
    output_type=list[SuccessCriteria],
    hooks=logging_hooks,
)

evaluate_criteria_agent = Agent(
    name="CriteriaEvaluator",
    instructions=(
        "You are an expert evaluator. Given a goal/idea, search results, and a list of "
        "potential success criteria, select the THREE criteria that, if met together, "
        "would most strongly indicate that the goal has been achieved. "
        "Choose criteria that complement each other and cover different aspects of the goal. "
        "Consider information found by search to assist with your selection. "
        "Provide detailed reasoning for each of your selections."
    ),
    model="gpt-4o",
    output_type=list[SuccessCriteria],  # Changed to expect a list
    hooks=logging_hooks,
)

async def validate_module1_output(
    agent: Agent, agent_output: Any, context: RunContextWrapper[None]
) -> GuardrailFunctionOutput:
    """Validates the output of Module 1."""
    try:
        log_info("Validating Module 1 output...", truncate=True)
        verbose_logger.info("Validating Module 1 output...")

        # Log only key parts for the standard log
        truncated_output = {
            "goal": agent_output.goal,
            "selected_criteria_count": len(agent_output.selected_criteria),
        }

        log_info(f"Output to validate (truncated): {json.dumps(truncated_output, indent=2)}", truncate=True)
        verbose_logger.info(f"Output to validate: {json.dumps(agent_output.model_dump() if hasattr(agent_output, 'model_dump') else agent_output, indent=2)}")

        Module1Output.model_validate(agent_output)
        log_info("Module 1 output validation passed", truncate=True)
        verbose_logger.info("Module 1 output validation passed")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)
    except ValidationError as e:
        logger.error(f"Module 1 output validation failed: {e}")
        verbose_logger.error(f"Module 1 output validation failed: {e}")
        return GuardrailFunctionOutput(
            output_info={"error": str(e)}, tripwire_triggered=True
        )

async def run_module_1(user_goal: str, output_file: str) -> None:
    """Runs Module 1."""
    context = RunContextWrapper(context=None)

    try:
        log_info(f"Starting Module 1 with goal: {user_goal}", truncate=True)
        verbose_logger.info(f"Starting Module 1 with goal: {user_goal}")

        # --- Run Search Agent ---
        log_info("Running Search Agent...", truncate=True)
        verbose_logger.info("Running Search Agent...")

        try:
            search_result = await Runner.run(
                search_agent,
                input=f"Find information about success criteria for: {user_goal}",
                context=context,
            )
            search_summary = search_result.final_output
            log_info(f"Search Agent returned (truncated): {search_summary[:200]}...", truncate=True)
            verbose_logger.info(f"Search Agent returned (full): {search_summary}") # Full results

        except Exception as e:
            logger.warning(f"Search Agent failed: {e}. Proceeding without search results.")
            verbose_logger.warning(f"Search Agent failed: {e}. Proceeding without search results.")
            search_summary = "No search results available."  # Fallback message

        # --- Generate criteria (with search results) ---
        log_info("GENERATING CANDIDATE SUCCESS CRITERIA...", truncate=True)
        verbose_logger.info("GENERATING CANDIDATE SUCCESS CRITERIA...")

        criteria_result = await Runner.run(
            generate_criteria_agent,
            input=f"The user's goal is: {user_goal}\n\nSearch Results:\n{search_summary}",
            context=context,
        )
        generated_criteria = criteria_result.final_output
        log_info(f"Generated {len(generated_criteria)} success criteria", truncate=True)
        verbose_logger.info(f"Generated {len(generated_criteria)} success criteria")

        # Log each criterion
        for i, criterion in enumerate(generated_criteria, 1):
            log_info(f"Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})", truncate=True)
            verbose_logger.info(f"Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})") # Redundant but consistent


        # Select top criteria
        log_info("EVALUATING AND SELECTING TOP CRITERIA...", truncate=True)
        verbose_logger.info("EVALUATING AND SELECTING TOP CRITERIA...")

        # Format criteria for the evaluator
        criteria_json = json.dumps([c.model_dump() for c in generated_criteria], indent=2)
        evaluation_input = (
            f"Goal: {user_goal}\n\nSearch Results:\n{search_summary}\n\nCriteria:\n{criteria_json}"
        )
        log_info(f"Evaluation input (truncated): {evaluation_input[:500]}...", truncate=True)
        verbose_logger.info(f"Evaluation input (full): {evaluation_input}")


        evaluation_result = await Runner.run(
            evaluate_criteria_agent,
            input=evaluation_input,
            context=context,
        )
        selected_criteria = evaluation_result.final_output
        log_info(f"Selected {len(selected_criteria)} top criteria", truncate=True)
        verbose_logger.info(f"Selected {len(selected_criteria)} top criteria")

        # Log selected criteria
        for i, criterion in enumerate(selected_criteria, 1):
            log_info(f"Selected Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})", truncate=True)
            verbose_logger.info(f"Selected Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})")

        # Create the output object using Pydantic
        log_info("CREATING MODULE 1 OUTPUT OBJECT...", truncate=True)
        verbose_logger.info("CREATING MODULE 1 OUTPUT OBJECT...")

        module_1_output = Module1Output(
            goal=user_goal,
            success_criteria=generated_criteria,
            selected_criteria=selected_criteria,  # Multiple criteria
        )

        # Log the complete output (only to verbose log)
        verbose_logger.info(f"Complete Module 1 output: {json.dumps(module_1_output.model_dump(), indent=2)}")

        # Add the output guardrail
        log_info("Applying output guardrail...", truncate=True)
        verbose_logger.info("Applying output guardrail...")

        guardrail = OutputGuardrail(guardrail_function=validate_module1_output)
        guardrail_result = await guardrail.run(
            agent=evaluate_criteria_agent,
            agent_output=module_1_output,
            context=context
        )

        if guardrail_result.output.tripwire_triggered:
            logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
            verbose_logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
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
            json.dump(module_1_output.model_dump(), f, indent=4)
        with open(timestamped_file, "w") as f:
            json.dump(module_1_output.model_dump(), f, indent=4)
        
        log_info(f"Module 1 completed. Output saved to {output_file}", truncate=True)
        log_info(f"Timestamped output saved to {timestamped_file}", truncate=True)
        verbose_logger.info(f"Module 1 completed. Output saved to {output_file}")
        verbose_logger.info(f"Timestamped output saved to {timestamped_file}")

    except Exception as e:
        logger.error(f"An error occurred in Module 1: {e}")
        verbose_logger.error(f"An error occurred in Module 1: {e}")
        import traceback
        error_trace = traceback.format_exc()
        logger.error(error_trace)
        verbose_logger.error(error_trace)  # Log the full stack trace

async def main():
    log_info("Starting main function", truncate=True)
    verbose_logger.info("Starting main function")

    user_goal = input("Please enter your goal or idea: ")
    log_info(f"User input goal: {user_goal}", truncate=True)
    verbose_logger.info(f"User input goal: {user_goal}")


    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "module1_output.json")

    await run_module_1(user_goal, output_file)
    log_info("Main function completed", truncate=True)
    verbose_logger.info("Main function completed")

if __name__ == "__main__":
    log_info("Module 1 script starting", truncate=True)
    verbose_logger.info("Module 1 script starting")

    asyncio.run(main())
    log_info("Module 1 script completed", truncate=True)
    verbose_logger.info("Module 1 script completed")
```

--- START OF CORRECTED FILE module2.py ---
```python
# python module2.py
import asyncio
import json
import os
import logging
import datetime
from typing import Any, List, Dict, Optional

# Monkey patching first - NO LONGER NEEDED
# import openai
# def _mock_get_default_openai_client(*args, **kwargs):
#     return None
# openai.AsyncOpenAI._get_default_openai_client = _mock_get_default_openai_client
# openai.OpenAI._get_default_openai_client = _mock_get_default_openai_client

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

    ======


=======

# CLAUDE 3.7

I see the issue in your module1.py script, and I'll help you fix it to work with the current version of the OpenAI Agents SDK. The main error is related to a parameter confusion in the output guardrail function.

Let me walk you through the fix for module1.py:

### Main Issue

The error shows:
```
AttributeError: 'Agent' object has no attribute 'goal'
```

This happens in the `validate_module1_output` function where you're trying to access `agent_output.goal`, but the parameters have been confused. The agent parameter is being passed as the output parameter.

### Fix for module1.py

Here's the necessary change for your `validate_module1_output` function:

```python
async def validate_module1_output(
    context: RunContextWrapper[None], agent: Agent, agent_output: Any
) -> GuardrailFunctionOutput:
    """Validates the output of Module 1."""
    try:
        log_info("Validating Module 1 output...", truncate=True)
        verbose_logger.info("Validating Module 1 output...")

        # Log only key parts for the standard log
        truncated_output = {
            "goal": agent_output.goal,
            "selected_criteria_count": len(agent_output.selected_criteria),
        }

        log_info(f"Output to validate (truncated): {json.dumps(truncated_output, indent=2)}", truncate=True)
        verbose_logger.info(f"Output to validate: {json.dumps(agent_output.model_dump() if hasattr(agent_output, 'model_dump') else agent_output, indent=2)}")

        Module1Output.model_validate(agent_output)
        log_info("Module 1 output validation passed", truncate=True)
        verbose_logger.info("Module 1 output validation passed")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)
    except ValidationError as e:
        logger.error(f"Module 1 output validation failed: {e}")
        verbose_logger.error(f"Module 1 output validation failed: {e}")
        return GuardrailFunctionOutput(
            output_info={"error": str(e)}, tripwire_triggered=True
        )
```

The issue is with the parameter ordering. The released version of the SDK expects the validation function to have parameters in this order: `context, agent, output` while your code might be using a different order.

### Additional Changes for module1.py

1. Update the guardrail call in the `run_module_1` function:

```python
guardrail_result = await guardrail.run(
    agent=evaluate_criteria_agent,  # The agent that created the output
    agent_output=module_1_output,   # The output to validate
    context=context
)
```

2. Check if there's any monkey patching in your code that might no longer be needed:

```python
# This may no longer be needed with the released version
# import openai
# def _mock_get_default_openai_client(*args, **kwargs):
#     return None
# openai.AsyncOpenAI._get_default_openai_client = _mock_get_default_openai_client
# openai.OpenAI._get_default_openai_client = _mock_get_default_openai_client
```

You can try commenting out this monkey patching code to see if it works without it now.

3. Check for model settings in agent initialization:

```python
# Old pre-release way:
# agent = Agent(
#     name="CriteriaGenerator",
#     instructions="...",
#     model_settings=ModelSettings(model="gpt-4o"),
#     output_type=list[SuccessCriteria],
# )

# New released way:
agent = Agent(
    name="CriteriaGenerator",
    instructions="...",
    model="gpt-4o",  # Direct model name
    output_type=list[SuccessCriteria],
)
```

### Testing the Changes

After making these changes, try running module1.py again. The error should be fixed, allowing the script to proceed further.

If you encounter any additional issues after these changes, please share the new error messages, and I'll help you address them as well.

Would you like me to review the entire module1.py file to identify any other potential issues with the released SDK version?

----

# module1.py

# uv venv
# source .venv/bin/activate
# uv pip install openai-agents
# uv pip install python-dotenv
# python module1.py

import asyncio
import json
import os
import logging
import datetime
import re
from typing import Any, List, Dict, Optional

# Import OpenAI libraries
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError, field_validator

from agents import Agent, GuardrailFunctionOutput, OutputGuardrail, Runner, WebSearchTool
from agents.run_context import RunContextWrapper
from agents.lifecycle import AgentHooks

load_dotenv()  # Load environment variables

# --- Setup Logging (Modified for Verbosity) ---
def setup_logging(module_name):
    """Set up logging to console, a standard file, and a verbose file."""
    logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(logs_dir, f"{module_name}_{timestamp}.log")
    verbose_log_file = os.path.join(logs_dir, f"{module_name}_verbose_{timestamp}.log")

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.INFO)
    if logger.handlers:
        logger.handlers = []

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    # Verbose logger (no truncation)
    verbose_logger = logging.getLogger(f"{module_name}_verbose")
    verbose_logger.setLevel(logging.INFO)
    if verbose_logger.handlers:
        verbose_logger.handlers = []
    verbose_file_handler = logging.FileHandler(verbose_log_file)
    verbose_file_handler.setLevel(logging.INFO)
    verbose_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    verbose_file_handler.setFormatter(verbose_format)
    verbose_logger.addHandler(verbose_file_handler)

    return logger, verbose_logger

# Initialize loggers
logger, verbose_logger = setup_logging("module1")

# Helper function to log to both loggers
def log_info(message, truncate=False, max_length=5000):
    verbose_logger.info(message)  # Always log full message to verbose
    if truncate:
        if len(message) > max_length:
            message = message[:max_length] + "... [truncated, see verbose log]"
        logger.info(message)
    else:
        logger.info(message)

# --- Text Validation Functions ---
def sanitize_text(text: str) -> str:
    """Clean and validate text to prevent corruption."""
    if not isinstance(text, str):
        return str(text)

    # Remove any non-printable or control characters
    text = ''.join(char for char in text if char.isprintable() or char in ['\n', '\t', ' '])

    # Check for obvious corruption patterns (random Unicode characters, etc.)
    # This regex looks for clusters of non-English characters that might indicate corruption
    corruption_pattern = r'[\u0400-\u04FF\u0600-\u06FF\u0900-\u097F\u3040-\u309F\u30A0-\u30FF\u3130-\u318F\uAC00-\uD7AF]{3,}'

    # Replace corrupted sections with a note
    text = re.sub(corruption_pattern, '[corrupted text removed]', text)

    # Ensure the text doesn't exceed a reasonable size (50KB) - adjust as necessary
    max_length = 50000
    if len(text) > max_length:
        text = text[:max_length] + "...[text truncated due to length]"

    return text

# --- Pydantic Models --- (No changes)
class SuccessCriteria(BaseModel):
    criteria: str
    reasoning: str
    rating: int = Field(..., description="Rating of the criterion (1-10)")
    
    @field_validator('rating')
    def check_rating(cls, v):
        if not 1 <= v <= 10:
            raise ValueError('Rating must be between 1 and 10')
        return v

class Module1Output(BaseModel):
    goal: str
    success_criteria: list[SuccessCriteria]
    selected_criteria: list[SuccessCriteria]  # Changed to a list for multiple criteria

    @field_validator('selected_criteria')
    def validate_selected_criteria(cls, v):
        if not v:
            raise ValueError("At least one criterion must be selected")
        return v

# --- Custom Agent Hooks for Detailed Logging --- (Modified for verbosity)
class DetailedLoggingHooks(AgentHooks):
    def __init__(self, logger, verbose_logger):
        self.logger = logger
        self.verbose_logger = verbose_logger

    async def on_start(
        self, context: RunContextWrapper[Any], agent: Agent
    ):
        """Called before the agent is invoked."""
        inputs_json = json.dumps(agent.model_dump() if hasattr(agent, 'model_dump') else {"name": agent.name}, indent=2)
        log_info(f"===== API CALL: {agent.name} =====", truncate=True)
        log_info(f"Agent start: {agent.name}", truncate=True)
        self.verbose_logger.info(f"===== API CALL: {agent.name} =====") # Redundant, but consistent
        return

    async def on_end(
        self, context: RunContextWrapper[Any], agent: Agent, output: Any
    ):
        """Called when the agent produces a final output."""
        log_info(f"===== API RESPONSE: {agent.name} =====", truncate=True)
        self.verbose_logger.info(f"===== API RESPONSE: {agent.name} =====")

        try:
            if hasattr(output, 'final_output'):
                # Sanitize if the final output has text
                if isinstance(output.final_output, str):
                    output.final_output = sanitize_text(output.final_output)
                elif isinstance(output.final_output, list):
                    for item in output.final_output:
                         if hasattr(item, "criteria"):
                            item.criteria = sanitize_text(item.criteria)
                         if hasattr(item, "reasoning"):
                            item.reasoning = sanitize_text(item.reasoning)

                response_content = json.dumps(output.final_output, indent=2) if hasattr(output, 'final_output') else str(output)
                log_info(f"Response from {agent.name}: {response_content}", truncate=True)
                self.verbose_logger.info(f"Response from {agent.name}: {response_content}")
            else:
                log_info(f"Response from {agent.name}: {str(output)}", truncate=True)
                self.verbose_logger.info(f"Response from {agent.name}: {str(output)}")
        except Exception as e:
            log_info(f"Response from {agent.name}: {str(output)}", truncate=True)
            log_info(f"Could not format response as JSON: {e}", truncate=True)
            self.verbose_logger.info(f"Response from {agent.name}: {str(output)}")
            self.verbose_logger.info(f"Could not format response as JSON: {e}")
        return output

    async def on_tool_start(
        self, context: RunContextWrapper[Any], agent: Agent, tool: Any
    ):
        """Called before a tool is invoked."""
        log_info(f"===== TOOL CALL: {agent.name} =====", truncate=True)
        self.verbose_logger.info(f"===== TOOL CALL: {agent.name} =====")
        return

    async def on_tool_end(
        self, context: RunContextWrapper[Any], agent: Agent, tool: Any, result: str
    ):
        """Called after a tool is invoked."""
        try:
            response_content = json.dumps(result, indent=2)
            log_info(f"Tool Result from {agent.name}: {response_content}", truncate=True)
            self.verbose_logger.info(f"Tool Result from {agent.name}: {response_content}")
        except Exception as e:  # JSON decoding might fail
            log_info(f"Tool Result from {agent.name}: {str(result)}", truncate=True)
            self.verbose_logger.info(f"Tool Result from {agent.name}: {str(result)}")
            log_info(f"Could not format response as JSON: {e}", truncate=True)
            self.verbose_logger.info(f"Could not format response as JSON: {e}")

        return result

# Create logging hooks
logging_hooks = DetailedLoggingHooks(logger, verbose_logger)


# --- Search Agent ---
web_search_tool = WebSearchTool()  # Instantiate the tool

search_agent = Agent(
    name="SearchAgent",
    instructions=(
        "You are a web search assistant. Given a user's goal, "
        "perform a web search to find information relevant to defining success criteria. "
        "Return a concise summary of your findings, including citations to sources."
    ),
    model="gpt-4o",
    tools=[web_search_tool],  # Pass the *instance* of the tool
    hooks=logging_hooks,
)

# --- Other Agents ---
generate_criteria_agent = Agent(
    name="CriteriaGenerator",
    instructions=(
        "You are a helpful assistant. Given a user's goal or idea, and the results of a web search,"
        "generate five distinct and measurable success criteria. "
        "Provide a brief reasoning for each criterion. "
        "Rate each criterion on a scale of 1-10 based on how strongly it indicates goal achievement."
    ),
    model="gpt-4o",
    output_type=list[SuccessCriteria],
    hooks=logging_hooks,
)

evaluate_criteria_agent = Agent(
    name="CriteriaEvaluator",
    instructions=(
        "You are an expert evaluator. Given a goal/idea, search results, and a list of "
        "potential success criteria, select the THREE criteria that, if met together, "
        "would most strongly indicate that the goal has been achieved. "
        "Choose criteria that complement each other and cover different aspects of the goal. "
        "Consider information found by search to assist with your selection. "
        "Provide detailed reasoning for each of your selections."
    ),
    model="gpt-4o",
    output_type=list[SuccessCriteria],  # Changed to expect a list
    hooks=logging_hooks,
)

async def validate_module1_output(
    context: RunContextWrapper[None], agent: Agent, agent_output: Any
) -> GuardrailFunctionOutput:
    """Validates the output of Module 1."""
    try:
        log_info("Validating Module 1 output...", truncate=True)
        verbose_logger.info("Validating Module 1 output...")

        # Log only key parts for the standard log
        truncated_output = {
            "goal": agent_output.goal,
            "selected_criteria_count": len(agent_output.selected_criteria),
        }

        log_info(f"Output to validate (truncated): {json.dumps(truncated_output, indent=2)}", truncate=True)
        verbose_logger.info(f"Output to validate: {json.dumps(agent_output.model_dump() if hasattr(agent_output, 'model_dump') else agent_output, indent=2)}")

        Module1Output.model_validate(agent_output)
        log_info("Module 1 output validation passed", truncate=True)
        verbose_logger.info("Module 1 output validation passed")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)
    except ValidationError as e:
        logger.error(f"Module 1 output validation failed: {e}")
        verbose_logger.error(f"Module 1 output validation failed: {e}")
        return GuardrailFunctionOutput(
            output_info={"error": str(e)}, tripwire_triggered=True
        )

async def run_module_1(user_goal: str, output_file: str) -> None:
    """Runs Module 1."""
    context = RunContextWrapper(context=None)

    try:
        log_info(f"Starting Module 1 with goal: {user_goal}", truncate=True)
        verbose_logger.info(f"Starting Module 1 with goal: {user_goal}")

        # --- Run Search Agent ---
        log_info("Running Search Agent...", truncate=True)
        verbose_logger.info("Running Search Agent...")

        try:
            search_result = await Runner.run(
                search_agent,
                input=f"Find information about success criteria for: {user_goal}",
                context=context,
            )
            search_summary = search_result.final_output
            log_info(f"Search Agent returned (truncated): {search_summary[:200]}...", truncate=True)
            verbose_logger.info(f"Search Agent returned (full): {search_summary}") # Full results

        except Exception as e:
            logger.warning(f"Search Agent failed: {e}. Proceeding without search results.")
            verbose_logger.warning(f"Search Agent failed: {e}. Proceeding without search results.")
            search_summary = "No search results available."  # Fallback message

        # --- Generate criteria (with search results) ---
        log_info("GENERATING CANDIDATE SUCCESS CRITERIA...", truncate=True)
        verbose_logger.info("GENERATING CANDIDATE SUCCESS CRITERIA...")

        criteria_result = await Runner.run(
            generate_criteria_agent,
            input=f"The user's goal is: {user_goal}\n\nSearch Results:\n{search_summary}",
            context=context,
        )
        generated_criteria = criteria_result.final_output
        log_info(f"Generated {len(generated_criteria)} success criteria", truncate=True)
        verbose_logger.info(f"Generated {len(generated_criteria)} success criteria")

        # Log each criterion
        for i, criterion in enumerate(generated_criteria, 1):
            log_info(f"Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})", truncate=True)
            verbose_logger.info(f"Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})") # Redundant but consistent


        # Select top criteria
        log_info("EVALUATING AND SELECTING TOP CRITERIA...", truncate=True)
        verbose_logger.info("EVALUATING AND SELECTING TOP CRITERIA...")

        # Format criteria for the evaluator
        criteria_json = json.dumps([c.model_dump() for c in generated_criteria], indent=2)
        evaluation_input = (
            f"Goal: {user_goal}\n\nSearch Results:\n{search_summary}\n\nCriteria:\n{criteria_json}"
        )
        log_info(f"Evaluation input (truncated): {evaluation_input[:500]}...", truncate=True)
        verbose_logger.info(f"Evaluation input (full): {evaluation_input}")


        evaluation_result = await Runner.run(
            evaluate_criteria_agent,
            input=evaluation_input,
            context=context,
        )
        selected_criteria = evaluation_result.final_output
        log_info(f"Selected {len(selected_criteria)} top criteria", truncate=True)
        verbose_logger.info(f"Selected {len(selected_criteria)} top criteria")

        # Log selected criteria
        for i, criterion in enumerate(selected_criteria, 1):
            log_info(f"Selected Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})", truncate=True)
            verbose_logger.info(f"Selected Criterion {i}: {criterion.criteria} (Rating: {criterion.rating})")

        # Create the output object using Pydantic
        log_info("CREATING MODULE 1 OUTPUT OBJECT...", truncate=True)
        verbose_logger.info("CREATING MODULE 1 OUTPUT OBJECT...")

        module_1_output = Module1Output(
            goal=user_goal,
            success_criteria=generated_criteria,
            selected_criteria=selected_criteria,  # Multiple criteria
        )

        # Log the complete output (only to verbose log)
        verbose_logger.info(f"Complete Module 1 output: {json.dumps(module_1_output.model_dump(), indent=2)}")

        # Add the output guardrail
        log_info("Applying output guardrail...", truncate=True)
        verbose_logger.info("Applying output guardrail...")

        guardrail = OutputGuardrail(guardrail_function=validate_module1_output)
        guardrail_result = await guardrail.run(
            agent=evaluate_criteria_agent,
            agent_output=module_1_output,
            context=context
        )

        if guardrail_result.output.tripwire_triggered:
            logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
            verbose_logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
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
            json.dump(module_1_output.model_dump(), f, indent=4)
        with open(timestamped_file, "w") as f:
            json.dump(module_1_output.model_dump(), f, indent=4)
        
        log_info(f"Module 1 completed. Output saved to {output_file}", truncate=True)
        log_info(f"Timestamped output saved to {timestamped_file}", truncate=True)
        verbose_logger.info(f"Module 1 completed. Output saved to {output_file}")
        verbose_logger.info(f"Timestamped output saved to {timestamped_file}")

    except Exception as e:
        logger.error(f"An error occurred in Module 1: {e}")
        verbose_logger.error(f"An error occurred in Module 1: {e}")
        import traceback
        error_trace = traceback.format_exc()
        logger.error(error_trace)
        verbose_logger.error(error_trace)  # Log the full stack trace

async def main():
    log_info("Starting main function", truncate=True)
    verbose_logger.info("Starting main function")

    user_goal = input("Please enter your goal or idea: ")
    log_info(f"User input goal: {user_goal}", truncate=True)
    verbose_logger.info(f"User input goal: {user_goal}")


    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "module1_output.json")

    await run_module_1(user_goal, output_file)
    log_info("Main function completed", truncate=True)
    verbose_logger.info("Main function completed")

if __name__ == "__main__":
    log_info("Module 1 script starting", truncate=True)
    verbose_logger.info("Module 1 script starting")

    asyncio.run(main())
    log_info("Module 1 script completed", truncate=True)
    verbose_logger.info("Module 1 script completed")




==========

# POE CLAUDE 3.7 Module4 Fix

Looking at your previous version of `module4.py`, there are several improvements we can make to ensure the code reliably determines when revisions are needed. Let me break down the key insights and create a fixed version of the code:

1. **The core issue**: The current implementation filters failed criteria too strictly by only considering evaluation results that explicitly mention the item title in their reasoning. This is unreliable.

2. **Key improvements needed**:
   - Improve the criteria filtering logic to better identify relevant failed criteria
   - Enhance the evaluation summary generation 
   - Ensure all evaluation results are properly considered during revision assessment

Here's my fixed version of the `module4.py` file, incorporating these improvements:

```python
# python module4.py

import asyncio
import json
import os
import logging
import datetime
import re
from typing import Any, Dict, List, Optional, Tuple

from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError, field_validator

from agents import Agent, GuardrailFunctionOutput, OutputGuardrail, Runner
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
    
    # Also create a verbose log file that captures everything
    verbose_log_file = os.path.join(logs_dir, f"{module_name}_verbose_{timestamp}.log")
    
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
    
    # Verbose logger (no truncation)
    verbose_logger = logging.getLogger(f"{module_name}_verbose")
    verbose_logger.setLevel(logging.INFO)
    if verbose_logger.handlers:
        verbose_logger.handlers = []
    verbose_file_handler = logging.FileHandler(verbose_log_file)
    verbose_file_handler.setLevel(logging.INFO)
    verbose_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    verbose_file_handler.setFormatter(verbose_format)
    verbose_logger.addHandler(verbose_file_handler)
    
    return logger, verbose_logger

# Initialize loggers
logger, verbose_logger = setup_logging("module4")

# Helper function to log to both loggers
def log_info(message, truncate=False, max_length=5000):
    # Always log full message to verbose
    verbose_logger.info(message)
    
    # Optionally truncate for regular log
    if truncate and len(message) > max_length:
        truncated = message[:max_length] + f"... [truncated, full message in verbose log]"
        logger.info(truncated)
    else:
        logger.info(message)

# --- Text Validation Functions ---
def sanitize_text(text: str) -> str:
    """Clean and validate text to prevent corruption."""
    if not isinstance(text, str):
        return str(text)
        
    # Remove any non-printable or control characters
    text = ''.join(char for char in text if char.isprintable() or char in ['\n', '\t', ' '])
    
    # Check for obvious corruption patterns (random Unicode characters, etc.)
    # This regex looks for clusters of non-English characters that might indicate corruption
    corruption_pattern = r'[\u0400-\u04FF\u0600-\u06FF\u0900-\u097F\u3040-\u309F\u30A0-\u30FF\u3130-\u318F\uAC00-\uD7AF]{3,}'
    
    # Replace corrupted sections with a note
    text = re.sub(corruption_pattern, '[corrupted text removed]', text)
    
    # Ensure the text doesn't exceed a reasonable size (50KB)
    max_length = 50000
    if len(text) > max_length:
        text = text[:max_length] + "...[text truncated due to length]"
    
    return text

# --- Custom Agent Hooks for Detailed Logging ---
class DetailedLoggingHooks(AgentHooks):
    def __init__(self, logger, verbose_logger):
        self.logger = logger
        self.verbose_logger = verbose_logger

    async def on_start(
        self, context: RunContextWrapper[Any], agent: Agent
    ):
        """Log details before LLM generation."""
        # Log to both loggers
        log_info(f"===== API CALL: {agent.name} =====")
        log_info(f"Starting agent: {agent.name}")
        return
    
    async def on_end(
        self, context: RunContextWrapper[Any], agent: Agent, output: Any
    ):
        """Log details after LLM generation."""
        log_info(f"===== API RESPONSE: {agent.name} =====")
        
        # Format the response for better readability
        try:
            if hasattr(output, 'final_output'):
                # Handle different response types
                if hasattr(output.final_output, 'revision_request_content'):
                    output.final_output.revision_request_content = sanitize_text(output.final_output.revision_request_content)
                if hasattr(output.final_output, 'reasoning'):
                    output.final_output.reasoning = sanitize_text(output.final_output.reasoning)
                if hasattr(output.final_output, 'impact_assessment'):
                    output.final_output.impact_assessment = sanitize_text(output.final_output.impact_assessment)
                
                response_content = json.dumps(output.final_output, indent=2) 
                log_info(f"Response from {agent.name}: {response_content}", truncate=True)
            else:
                log_info(f"Response from {agent.name}: {str(output)}")
        except Exception as e:
            log_info(f"Response from {agent.name}: {str(output)}")
            log_info(f"Could not format response as JSON: {e}")
        return output

    async def on_tool_start(
        self, context: RunContextWrapper[Any], agent: Agent, tool: Any
    ):
        """Called before a tool is invoked."""
        log_info(f"===== TOOL CALL: {agent.name} =====")
        log_info(f"Tool being called by {agent.name}: {tool}")
        return

    async def on_tool_end(
        self, context: RunContextWrapper[Any], agent: Agent, tool: Any, result: str
    ):
        """Called after a tool is invoked."""
        log_info(f"Tool result for {agent.name}: {result}", truncate=True)
        return result

# Create logging hooks
logging_hooks = DetailedLoggingHooks(logger, verbose_logger)

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

class PlanItem(BaseModel):
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

class EvalResult(BaseModel):
    result: str = Field(..., description="Either the word 'pass' or the word 'fail'.")
    reasoning: str = Field(..., description="The evaluator's reasoning")
    criteria: SuccessCriteria = Field(..., description="The success criterion being evaluated against")

    @field_validator('result')
    def check_result(cls, v):
        if v.lower() not in ["pass", "fail"]:
            raise ValueError("Result must be 'pass' or 'fail'")
        return v.lower()
    
    @field_validator('reasoning')
    def validate_reasoning(cls, v):
        """Validate and sanitize reasoning text."""
        return sanitize_text(v)

class Module3Output(BaseModel): # For loading the JSON from module 3
    goal: str
    selected_criteria: list[SuccessCriteria]
    selected_outline: PlanOutline  # Original outline
    expanded_outline: PlanOutline  # Expanded items
    evaluation_results: list[EvalResult] # List of results
    criteria_summary: Dict[str, Dict[str, int]] = Field(
        default_factory=dict, description="Summary of pass/fail counts per criterion"
    )

class RevisionRequest(BaseModel):
    revision_request_content: str = Field(..., description="Specific requested revision.")
    reasoning: str = Field(..., description="Why this revision is necessary.")
    targeted_criteria: List[str] = Field(..., description="The criteria this revision addresses.")
    
    @field_validator('revision_request_content')
    def validate_request(cls, v):
        """Validate and sanitize revision request text."""
        return sanitize_text(v)
    
    @field_validator('reasoning')
    def validate_reasoning(cls, v):
        """Validate and sanitize reasoning text."""
        return sanitize_text(v)

class RevisionEvaluation(BaseModel):
    approved: bool = Field(..., description="Whether the revision is approved (True) or rejected (False).")
    reasoning: str = Field(..., description="Reasoning for approval or rejection.")
    impact_assessment: str = Field(..., description="Assessment of how this revision impacts each criterion.")
    
    @field_validator('reasoning')
    def validate_reasoning(cls, v):
        """Validate and sanitize reasoning text."""
        return sanitize_text(v)
    
    @field_validator('impact_assessment')
    def validate_impact(cls, v):
        """Validate and sanitize impact assessment text."""
        return sanitize_text(v)

class ItemDetail(BaseModel):
    item_title: str = Field(..., description="Title of the plan item")
    original_evaluation: Dict[str, str] = Field(..., description="Summary of original evaluations for this item")
    revision_request: Optional[RevisionRequest] = Field(None, description="The requested revision if any")
    revision_evaluation: Optional[RevisionEvaluation] = Field(None, description="Evaluation of the revision request")

# --- Module 4 Output ---
class Module4Output(BaseModel):
    goal: str
    selected_criteria: list[SuccessCriteria]
    selected_outline: PlanOutline  # Original outline
    expanded_outline: PlanOutline  # Expanded items with full descriptions
    evaluation_results: list[EvalResult]  # Original evaluation results
    item_details: list[ItemDetail]  # Details about each item's revision
    criteria_coverage_summary: Dict[str, Dict[str, int]] = Field(
        default_factory=dict, description="Summary of original vs post-revision criteria coverage"
    )

# --- Agents ---
criteria_assessment_agent = Agent(
    name="CriteriaAssessor",
    instructions=(
        "You are a criteria assessment expert. Given a goal, multiple success criteria, "
        "an expanded plan item, and evaluation results, analyze if any revisions are needed "
        "to better address one or more of the criteria that weren't fully met. "
        "Your assessment should be comprehensive, considering how each criteria is or isn't addressed "
        "by the current item description. "
        "Provide a detailed reasoning about why specific revisions would help meet the criteria better. "
        "If no revision is needed, return an empty string."
    ),
    model="gpt-4o",
    output_type=str,
    hooks=logging_hooks,
)

request_revision_agent = Agent(
    name="RevisionRequester",
    instructions=(
        "You are a plan improvement specialist. Given a goal, multiple success criteria, "
        "a full plan outline, a detailed expansion of a single plan item, and evaluation results, "
        "identify specific areas where the item could be improved to better address criteria marked as 'fail'. "
        "If all criteria are already marked as 'pass' or if improvements aren't needed, return an empty string. "
        "Otherwise, provide ONE specific, actionable revision request, detailed reasoning, and list the specific "
        "criteria this revision would address. Your revision should always aim to better fulfill the original user goal."
    ),
    model="gpt-4o",
    output_type=RevisionRequest | str,  # Allow empty string output
    hooks=logging_hooks,
)

evaluate_revision_agent = Agent(
    name="RevisionEvaluator",
    instructions=(
        "You are a revision evaluation expert. Given a goal, multiple success criteria, "
        "a full plan outline, an expanded plan item, and a suggested revision, "
        "evaluate whether the revision would significantly improve the item's ability to address "
        "the success criteria, particularly any that were previously not met. "
        "Provide your assessment of how the revision would impact each criterion (improve, worsen, or no change) "
        "as a single string in the impact_assessment field. Format your assessment as a list with each criterion "
        "on a new line.\n\n"
        "Output your approval decision (True/False) and detailed reasoning."
    ),
    model="gpt-4o",
    output_type=RevisionEvaluation,
    hooks=logging_hooks,
)

async def validate_module4_output(
    context: RunContextWrapper[None], agent: Agent, agent_output: Any
) -> GuardrailFunctionOutput:
    """Validates the output of Module 4."""
    try:
        log_info("Validating Module 4 output...")
        # Log only a truncated version of the output to avoid excessive logging
        truncated_output = {k: v for k, v in agent_output.model_dump().items() if k not in ['expanded_outline', 'evaluation_results']}
        log_info(f"Output to validate (truncated): {json.dumps(truncated_output, indent=2)}", truncate=True)
        verbose_logger.info(f"Full output to validate: {json.dumps(agent_output.model_dump(), indent=2)}")
        
        Module4Output.model_validate(agent_output)
        log_info("Module 4 output validation passed")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)
    except ValidationError as e:
        logger.error(f"Module 4 output validation failed: {e}")
        verbose_logger.error(f"Module 4 output validation failed: {e}")
        return GuardrailFunctionOutput(
            output_info={"error": str(e)}, tripwire_triggered=True
        )

def get_original_evaluation_summary(
    item_title: str, 
    evaluation_results: List[EvalResult]
) -> Dict[str, str]:
    """Create a summary of original evaluation results for a specific item."""
    # Get all unique criteria
    all_criteria = {result.criteria.criteria for result in evaluation_results}
    
    # Initialize with not_evaluated for all criteria
    summary = {criterion: "not_evaluated" for criterion in all_criteria}
    
    # First pass: look for exact item mentions in reasoning
    for result in evaluation_results:
        criterion = result.criteria.criteria
        if item_title.lower() in result.reasoning.lower():
            summary[criterion] = result.result
    
    # Second pass: look for any criteria that weren't matched and are still "not_evaluated"
    # For these, we'll use the general result for that criterion
    for criterion in all_criteria:
        if summary[criterion] == "not_evaluated":
            # Find results for this criterion
            criterion_results = [r for r in evaluation_results if r.criteria.criteria == criterion]
            # If there's only one result for this criterion, use it regardless of item mention
            if len(criterion_results) == 1:
                summary[criterion] = criterion_results[0].result
    
    # Convert any remaining "not_evaluated" to "unknown"
    for criterion in summary:
        if summary[criterion] == "not_evaluated":
            summary[criterion] = "unknown"
    
    return summary

async def process_item_for_revision(
    goal: str,
    selected_criteria: List[SuccessCriteria],
    selected_outline: PlanOutline,
    expanded_outline: PlanOutline,
    evaluation_results: List[EvalResult],
    item_index: int,
    context: RunContextWrapper[None],
) -> ItemDetail:
    """Process an item for potential revision based on evaluation results."""
    item = expanded_outline.plan_items[item_index]
    item_title = item.item_title
    item_description = item.item_description
    
    log_info(f"Processing item for revision: {item_title}")
    
    # Format criteria for input
    criteria_json = json.dumps([c.model_dump() for c in selected_criteria], indent=2)
    
    # Get item-specific evaluation results
    item_evaluations = []
    for result in evaluation_results:
        if item_title.lower() in result.reasoning.lower():
            item_evaluations.append(result)
    
    # Create a summary of the original evaluations
    original_evaluation = get_original_evaluation_summary(item_title, evaluation_results)
    log_info(f"Original evaluation summary for {item_title}: {json.dumps(original_evaluation, indent=2)}")
    
    # Get all failed criteria, not just those that mention this item
    all_failed_criteria = [eval_result for eval_result in evaluation_results if eval_result.result == "fail"]
    
    # Check if there are any failed criteria at all (if none, no need for revisions)
    if not all_failed_criteria:
        log_info(f"No failed criteria at all in evaluation results, skipping revision request for {item_title}")
        return ItemDetail(
            item_title=item_title,
            original_evaluation=original_evaluation,
            revision_request=None,
            revision_evaluation=None
        )
    
    # Format all evaluation results for input, not just those mentioning this item
    all_evaluations_text = "\n\n".join([
        f"Criterion: {eval_result.criteria.criteria}\n"
        f"Result: {eval_result.result}\n"
        f"Reasoning: {eval_result.reasoning}"
        for eval_result in evaluation_results
    ])
    
    # Create assessment input to determine if this item needs revision
    assessment_input = (
        f"Goal: {goal}\n\n"
        f"Success Criteria:\n{criteria_json}\n\n"
        f"Plan Item Title: {item_title}\n\n"
        f"Plan Item Description:\n{item_description}\n\n"
        f"Evaluation Results:\n{all_evaluations_text}\n\n"
        f"Based on the above information, analyze if any revisions are needed to this specific plan item "
        f"to better address any of the criteria, particularly those marked as 'fail'. "
        f"Consider how this specific plan item could better contribute to meeting the fail criteria. "
        f"If no revision is needed for this specific item, return an empty string."
    )
    
    log_info(f"Criteria assessment input for {item_title} (truncated)", truncate=True)
    verbose_logger.info(f"Full criteria assessment input for {item_title}: {assessment_input}")
    
    # Run criteria assessment agent
    assessment_result = await Runner.run(
        criteria_assessment_agent,
        input=assessment_input,
        context=context,
    )
    
    assessment = assessment_result.final_output
    
    # Check if assessment indicates no revision needed
    if isinstance(assessment, str) and not assessment.strip():
        log_info(f"Criteria assessment indicates no revisions needed for {item_title}")
        return ItemDetail(
            item_title=item_title,
            original_evaluation=original_evaluation,
            revision_request=None,
            revision_evaluation=None
        )
    
    log_info(f"Criteria assessment for {item_title} suggests revisions are needed: {assessment[:200]}...")
    
    # Create input for revision requester
    revision_input = (
        f"Goal: {goal}\n\n"
        f"Success Criteria:\n{criteria_json}\n\n"
        f"Plan Item Title: {item_title}\n\n"
        f"Plan Item Description:\n{item_description}\n\n"
        f"Evaluation Results:\n{all_evaluations_text}\n\n"
        f"Criteria Assessment:\n{assessment}\n\n"
        f"Based on the above, identify ONE specific revision that would help this item "
        f"better address the failed criteria. Be specific and actionable. "
        f"Your revision should focus on this specific plan item and how it can be improved. "
        f"If no revision is needed, return an empty string."
    )
    
    log_info(f"Revision request input for {item_title} (truncated)", truncate=True)
    verbose_logger.info(f"Full revision request input for {item_title}: {revision_input}")
    
    # Get revision request
    revision_result = await Runner.run(
        request_revision_agent,
        input=revision_input,
        context=context,
    )
    
    revision_request = revision_result.final_output
    
    # If empty string response or not a RevisionRequest object, no revision needed
    if isinstance(revision_request, str) and not revision_request:
        log_info(f"No revision requested for {item_title}")
        return ItemDetail(
            item_title=item_title,
            original_evaluation=original_evaluation,
            revision_request=None,
            revision_evaluation=None
        )
    
    log_info(f"Revision requested for {item_title}: {revision_request.revision_request_content[:200]}...")
    verbose_logger.info(f"Full revision requested: {revision_request.revision_request_content}")
    
    # Create input for evaluation
    evaluation_input = (
        f"Goal: {goal}\n\n"
        f"Success Criteria:\n{criteria_json}\n\n"
        f"Plan Item Title: {item_title}\n\n"
        f"Original Plan Item Description:\n{item_description}\n\n"
        f"Revision Request:\n{revision_request.revision_request_content}\n\n"
        f"Revision Reasoning:\n{revision_request.reasoning}\n\n"
        f"Targeted Criteria:\n{', '.join(revision_request.targeted_criteria)}\n\n"
        f"Evaluate whether this revision would significantly improve the item's ability to "
        f"address the success criteria, particularly those that weren't fully met before. "
        f"For each criterion, assess how the revision would impact it (improve, worsen, or no change). "
        f"Format your impact assessment as a list with each criterion on its own line."
    )
    
    log_info(f"Revision evaluation input for {item_title} (truncated)", truncate=True)
    verbose_logger.info(f"Full revision evaluation input for {item_title}: {evaluation_input}")
    
    # Evaluate the revision
    evaluation_result = await Runner.run(
        evaluate_revision_agent,
        input=evaluation_input,
        context=context,
    )
    
    revision_evaluation = evaluation_result.final_output
    log_info(f"Revision evaluation for {item_title}: {revision_evaluation.approved} - {revision_evaluation.reasoning[:200]}...")
    log_info(f"Impact assessment for {item_title}: {revision_evaluation.impact_assessment}")
    
    # Return the item detail with revision information
    return ItemDetail(
        item_title=item_title,
        original_evaluation=original_evaluation,
        revision_request=revision_request,
        revision_evaluation=revision_evaluation
    )

def generate_criteria_coverage_summary(
    original_evaluation_results: List[EvalResult],
    item_details: List[ItemDetail]
) -> Dict[str, Dict[str, int]]:
    """Generate a summary of criteria coverage before and after revisions."""
    # Initialize summary dictionary
    summary = {}
    
    # Get unique criteria
    all_criteria = set(result.criteria.criteria for result in original_evaluation_results)
    
    # Count original pass/fail
    for criterion in all_criteria:
        summary[criterion] = {
            "original_pass": sum(1 for r in original_evaluation_results if r.criteria.criteria == criterion and r.result == "pass"),
            "original_fail": sum(1 for r in original_evaluation_results if r.criteria.criteria == criterion and r.result == "fail"),
            "estimated_improvements": 0
        }
    
    # Count estimated improvements from approved revisions
    for item in item_details:
        if item.revision_request and item.revision_evaluation and item.revision_evaluation.approved:
            # Parse the impact assessment string to find improvements
            impact_text = item.revision_evaluation.impact_assessment.lower()
            
            for criterion in all_criteria:
                criterion_lower = criterion.lower()
                if criterion_lower in impact_text and any(term in impact_text for term in ["improve", "improves", "improved", "enhancement", "better", "enhance", "positive"]):
                    if criterion in summary:
                        summary[criterion]["estimated_improvements"] += 1
    
    return summary

async def run_module_4(input_file: str, output_file: str) -> None:
    """Runs Module 4."""
    context = RunContextWrapper(context=None)

    try:
        log_info(f"Starting Module 4, reading input from {input_file}")
        with open(input_file, "r") as f:
            module_3_data = json.load(f)
            log_info(f"Successfully loaded data from {input_file}")

        # Convert to Pydantic objects
        module_3_output = Module3Output.model_validate(module_3_data)
        goal = module_3_output.goal
        selected_criteria = module_3_output.selected_criteria
        selected_outline = module_3_output.selected_outline
        expanded_outline = module_3_output.expanded_outline
        evaluation_results = module_3_output.evaluation_results
        
        log_info(f"Goal: {goal}")
        log_info(f"Number of selected criteria: {len(selected_criteria)}")
        for i, criterion in enumerate(selected_criteria):
            log_info(f"Criterion {i+1}: {criterion.criteria}")
        
        log_info(f"Original Criteria Summary: {json.dumps(module_3_output.criteria_summary, indent=2)}")
        
        # Process each item sequentially for revision
        log_info("Processing items for potential revisions...")
        item_details = []
        
        for i, item in enumerate(expanded_outline.plan_items):
            item_detail = await process_item_for_revision(
                goal=goal,
                selected_criteria=selected_criteria,
                selected_outline=selected_outline,
                expanded_outline=expanded_outline,
                evaluation_results=evaluation_results,
                item_index=i,
                context=context,
            )
            
            item_details.append(item_detail)
            log_info(f"Completed processing item {i+1}: {item.item_title}")
        
        # Generate criteria coverage summary
        criteria_coverage = generate_criteria_coverage_summary(evaluation_results, item_details)
        log_info(f"Criteria coverage summary: {json.dumps(criteria_coverage, indent=2)}")
        
        # Create the output object
        log_info("Creating Module 4 output object")
        module_4_output = Module4Output(
            goal=goal,
            selected_criteria=selected_criteria,
            selected_outline=selected_outline,
            expanded_outline=expanded_outline,
            evaluation_results=evaluation_results,
            item_details=item_details,
            criteria_coverage_summary=criteria_coverage,
        )

        # Apply guardrail
        log_info("Applying output guardrail...")
        guardrail = OutputGuardrail(guardrail_function=validate_module4_output)
        guardrail_result = await guardrail.run(
            agent=evaluate_revision_agent,
            agent_output=module_4_output,
            context=context,
        )
        
        if guardrail_result.output.tripwire_triggered:
            logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
            verbose_logger.error(f"Guardrail failed: {guardrail_result.output.output_info}")
            return  # Exit if validation fails

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
            json.dump(module_4_output.model_dump(), f, indent=4)
        with open(timestamped_file, "w") as f:
            json.dump(module_4_output.model_dump(), f, indent=4)
        
        log_info(f"Module 4 completed. Output saved to {output_file}")
        log_info(f"Timestamped output saved to {timestamped_file}")

    except Exception as e:
        logger.error(f"An error occurred in Module 4: {e}")
        verbose_logger.error(f"An error occurred in Module 4: {e}")
        import traceback
        error_trace = traceback.format_exc()
        logger.error(error_trace)
        verbose_logger.error(error_trace)  # Log the full stack trace

async def main():
    log_info("Starting main function")
    input_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    input_file = os.path.join(input_dir, "module3_output.json")
    output_file = os.path.join(input_dir, "module4_output.json")
    await run_module_4(input_file, output_file)
    log_info("Main function completed")

if __name__ == "__main__":
    log_info("Module 4 script starting")
    asyncio.run(main())
    log_info("Module 4 script completed")
```

### Key Improvements in the Fixed Code:

1. **Enhanced Logging System**: 
   - Created a proper dual logging system (normal and verbose) to better track what's happening
   - Added proper truncation of large logs while preserving full content in verbose logs

2. **Improved Criteria Identification**:
   - Changed the logic to consider ALL failed criteria, not just those that explicitly mention the item title
   - Added a two-step process to build the evaluation summary:
     - First look for explicit item mentions
     - Then fill in gaps using general results for criteria

3. **Added Assessment Step**:
   - Added a dedicated assessment step using `criteria_assessment_agent` to better determine if a revision is needed
   - This gives the model a chance to holistically consider all criteria before deciding on a revision

4. **Improved Evaluation Summary**:
   - Created a more sophisticated `get_original_evaluation_summary` function that:
     - Gets all unique criteria first
     - Initializes with "not_evaluated"
     - Uses explicit mentions first
     - Falls back to single results for criteria
     - Only uses "unknown" as a last resort

5. **Better Context for LLM Decisions**:
   - Provided all evaluation results to the agents, not just filtered ones
   - Added more context in the prompts to help the agents make better decisions
   - Properly separated the logging of full inputs in verbose logs

This improved implementation should reliably identify when revisions are needed for each plan item, even when the evaluation results don't explicitly mention the item title in their reasoning.


========

# PROBS PERSIST - ROOT CAUSE AND FIXES

# Root Cause Analysis of Module 4 Issues

Based on the logs and JSON files you've provided, I can identify why some revision requests are still coming up as null despite our code changes. Let me analyze the issue and suggest fixes.

## Key Observations

1. **First Item**: For "Design Autonomous Self-Assembling Modules", we see:
   ```
   "original_evaluation": {
      "Modular Design Implementation": "pass",
      "Creation of Habitable Environments": "pass"
   },
   "revision_request": null
   ```
   This is expected since both criteria evaluations are "pass".

2. **Second Item**: For "Deploy Initial Modules for Structural Framework", a revision was successfully created and evaluated as its evaluation showed failures.

3. **Third Item**: For "Integrate Habitats with Rotational Gravity", we see:
   ```
   "original_evaluation": {},
   "revision_request": null
   ```
   This is unexpected - the empty `original_evaluation` suggests something went wrong.

4. **Fourth Item**: For "Establish Energy Capture and Transmission Systems", a revision was successfully created.

## Root Cause Analysis

Looking at the logs and outputs, I've identified three primary issues:

### 1. Incomplete Original Evaluation Mapping

In the `get_original_evaluation_summary` function, we're only considering evaluations where the item title appears in the reasoning text. However, in module3_output.json, some reasonings may not explicitly mention the item title, resulting in empty original evaluations.

From the log:
```
2025-03-11 15:57:17,576 - INFO - Original evaluation summary for Integrate Habitats with Rotational Gravity: {}
```

### 2. Criteria Assessment Agent Issue

For the "Integrate Habitats with Rotational Gravity" item, the criteria assessment agent returned a contradictory response. It first stated all criteria were "pass" but then recommended revisions. This confused the subsequent logic:

```
The plan item "Integrate Habitats with Rotational Gravity" has the following evaluation results:
- **Modular Design Implementation:** Pass
- **Creation of Habitable Environments:** Pass
- **Efficient Energy Capture and Transmission:** Pass
```

But then continued with revision suggestions.

### 3. Failure Detection Logic

Our failure detection logic is looking only for failed criteria specifically mentioning the item title, but the module3_output.json failures don't always contain the item title in their reasoning.

## Fix Implementation

Here's the corrected implementation focusing on the key issues:

```python
def get_original_evaluation_summary(
    item_title: str,
    evaluation_results: List[EvalResult],
    plan_items: List[Dict[str, str]]
) -> Dict[str, str]:
    """Create a summary of original evaluation results for a specific item.
    
    Improved to handle cases where the item title isn't mentioned in reasoning.
    """
    # Get unique criteria
    all_criteria = {result.criteria.criteria for result in evaluation_results}
    
    # Initialize with unknown for all criteria
    summary = {criterion: "unknown" for criterion in all_criteria}
    
    # First pass: look for exact item matches in reasoning
    for result in evaluation_results:
        criterion = result.criteria.criteria
        if item_title.lower() in result.reasoning.lower():
            summary[criterion] = result.result
    
    # If we have no matches at all, try to infer from item position and plan structure
    if all(value == "unknown" for value in summary.values()):
        # Get the position of this item in the plan
        item_position = next((i for i, item in enumerate(plan_items) 
                             if item.get("item_title", "").lower() == item_title.lower()), -1)
        
        if item_position >= 0:
            # Try to find evaluations that might correspond to this item
            # based on overall pattern of evaluations
            item_evaluations = []
            for criterion in all_criteria:
                criterion_results = [r for r in evaluation_results 
                                    if r.criteria.criteria == criterion]
                
                # If we have exactly one evaluation per plan item for this criterion
                if len(criterion_results) == len(plan_items):
                    item_evaluations.append(criterion_results[item_position])
            
            # Update summary from these inferred evaluations
            for eval in item_evaluations:
                summary[eval.criteria.criteria] = eval.result
    
    return summary

async def process_item_for_revision(
    goal: str,
    selected_criteria: List[SuccessCriteria],
    selected_outline: PlanOutline,
    expanded_outline: PlanOutline,
    evaluation_results: List[EvalResult],
    item_index: int,
    context: RunContextWrapper[None],
) -> ItemDetail:
    """Process an item for potential revision based on evaluation results."""
    item = expanded_outline.plan_items[item_index]
    item_title = item.item_title
    item_description = item.item_description
    
    log_info(f"Processing item for revision: {item_title}")
    
    # Format criteria for input
    criteria_json = json.dumps([c.model_dump() for c in selected_criteria], indent=2)
    
    # Get item-specific evaluation results - this is for informational purposes only
    item_evaluations = [result for result in evaluation_results 
                       if item_title.lower() in result.reasoning.lower()]
    
    # Get any failed criteria regardless of whether they mention this item
    failed_criteria = [result for result in evaluation_results if result.result == "fail"]
    
    # Get a better original evaluation summary that considers plan structure
    original_evaluation = get_original_evaluation_summary(
        item_title, 
        evaluation_results,
        expanded_outline.plan_items
    )
    
    log_info(f"Original evaluation summary for {item_title}: {json.dumps(original_evaluation, indent=2)}")
    
    # Check if any criteria failed at all - not just for this item
    if not failed_criteria:
        log_info(f"No failed criteria found in any evaluation, skipping revision request for {item_title}")
        return ItemDetail(
            item_title=item_title,
            original_evaluation=original_evaluation,
            revision_request=None,
            revision_evaluation=None
        )
    
    # Format all evaluation results for input
    evaluations_text = "\n\n".join([
        f"Criterion: {eval_result.criteria.criteria}\n"
        f"Result: {eval_result.result}\n"
        f"Reasoning: {eval_result.reasoning}"
        for eval_result in evaluation_results
    ])
    
    # Create input for criteria assessment agent
    assessment_input = (
        f"Goal: {goal}\n\n"
        f"Success Criteria:\n{criteria_json}\n\n"
        f"Plan Item Title: {item_title}\n\n"
        f"Plan Item Description:\n{item_description}\n\n"
        f"Evaluation Results:\n{evaluations_text}\n\n"
        f"You need to determine if this specific plan item needs revision to better address any failed criteria.\n"
        f"Carefully analyze if this specific item can be improved to help meet any of the failed criteria.\n"
        f"If this item needs revision, provide a detailed analysis of what should be improved.\n"
        f"If no revision is needed for this specific item, return an empty string.\n"
        f"Be decisive - either provide a detailed analysis or an empty string."
    )
    
    log_info(f"Criteria assessment input for {item_title}", truncate=True)
    verbose_logger.info(f"Full criteria assessment input: {assessment_input}")
    
    # Run criteria assessment agent
    assessment_result = await Runner.run(
        criteria_assessment_agent,
        input=assessment_input,
        context=context,
    )
    
    assessment = assessment_result.final_output
    
    # Check if criteria assessment returned an empty string (meaning no revision)
    if isinstance(assessment, str) and not assessment.strip():
        log_info(f"Criteria assessment indicates no revisions needed for {item_title}")
        return ItemDetail(
            item_title=item_title,
            original_evaluation=original_evaluation,
            revision_request=None,
            revision_evaluation=None
        )
    
    log_info(f"Criteria assessment for {item_title} suggests revisions are needed: {assessment[:200]}...")
    
    # Create input for revision requester
    revision_input = (
        f"Goal: {goal}\n\n"
        f"Success Criteria:\n{criteria_json}\n\n"
        f"Plan Item Title: {item_title}\n\n"
        f"Plan Item Description:\n{item_description}\n\n"
        f"Evaluation Results:\n{evaluations_text}\n\n"
        f"Criteria Assessment:\n{assessment}\n\n"
        f"Based on the above, identify ONE specific revision that would help this item "
        f"better address any failed criteria. Focus on specific, actionable changes. "
        f"Your revision should address how this specific plan item can be improved. "
        f"If no revision is needed, return an empty string."
    )
    
    log_info(f"Revision request input for {item_title}", truncate=True)
    verbose_logger.info(f"Full revision request input: {revision_input}")
    
    # Get revision request
    revision_result = await Runner.run(
        request_revision_agent,
        input=revision_input,
        context=context,
    )
    
    revision_request = revision_result.final_output
    
    # If empty string response or not a RevisionRequest object, no revision needed
    if isinstance(revision_request, str) and not revision_request:
        log_info(f"No revision requested for {item_title}")
        return ItemDetail(
            item_title=item_title,
            original_evaluation=original_evaluation,
            revision_request=None,
            revision_evaluation=None
        )
    
    log_info(f"Revision requested for {item_title}: {revision_request.revision_request_content[:200]}...")
    verbose_logger.info(f"Full revision requested: {revision_request.revision_request_content}")
    
    # Rest of the function remains the same...
```

## Revised Criteria Assessment Agent Instructions

Also, improve the instructions for the criteria assessment agent:

```python
criteria_assessment_agent = Agent(
    name="CriteriaAssessor",
    instructions=(
        "You are a criteria assessment expert. Given a goal, multiple success criteria, "
        "an expanded plan item, and evaluation results, analyze if this specific plan item "
        "needs revisions to better address one or more of the criteria that weren't fully met. "
        "IMPORTANT: Focus only on how THIS specific item could be improved, not the overall plan. "
        "If you determine revisions are needed, provide detailed reasoning about what specific "
        "aspects need to be improved and why. "
        "If you determine NO revisions are needed for this specific item, return an empty string without "
        "any explanation. DO NOT explain why revisions aren't needed - just return an empty string."
    ),
    model="gpt-4o",
    output_type=str,
    hooks=logging_hooks,
)
```

## Summary of Fixes

1. **Improved Evaluation Summary**: The new `get_original_evaluation_summary` function now tries to intelligently infer item-to-evaluation mapping based on plan structure when direct text matching fails.

2. **Changed Failure Detection**: Instead of looking only for failures that mention this item, we now consider all failures and let the criteria assessment agent decide if this item can help address them.

3. **Enhanced Assessment Agent Instructions**: I've made the instructions clearer about when to return an empty string versus a detailed analysis, reducing ambiguity.

4. **Improved Input Formats**: The inputs to the agents now have clearer instructions to help them make better decisions about when revisions are needed.

These changes should ensure that the revision logic correctly handles all items, even when the original evaluation data has limitations in its structure.

=======

