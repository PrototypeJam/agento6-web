# OpenAI Agent SDK - Goal-to-Plan Open Source Implementation

## Overview
This project demonstrates a flexible, modular agent-based planning system built with the OpenAI Agent SDK. It provides a general approach to transform ANY initial goal or idea into a solid, well-structured plan with iterative refinement and evaluation.  I call this design approach "Agento"

OpenAI just launched a new open-source AI Agents SDK and I think it's the best agent framework out there. I was very fortunate to be granted early access and have been playing around with it, building imaginative ideas at nearly the speed of thought because its capabilities are powerful yet it's easy to work with.

I'd like to thank OpenAI for the early access to their Agents SDK. This project was initially built on a pre-release version and has been updated to work with the much-improved release version. The Dyson Sphere example shown in the code was suggested during a live demo at the AgentOps pre-release hack-night with OpenAI, which you can see here: https://x.com/AlexReibman/status/1899533549893746925

**OpenAI Announcement:** https://openai.com/index/new-tools-for-building-agents/  
**Documentation:** https://platform.openai.com/docs/guides/agents  
**SDK docs:** https://openai.github.io/openai-agents-python/  
**GitHub repo:** https://github.com/openai/openai-agents-python  
**Agent SDK video walkthrough and demo:** https://x.com/OpenAIDevs/status/1899531225468969240?t=617

## The General Approach

The true power of this system is its generality - it can handle virtually any goal or idea you provide, from business strategies to creative projects, from engineering designs to educational curricula. The system:

1. **Grounds the process with search**: Leverages knowledge to ensure plans are realistic and well-informed
2. **Establishes specific success metrics**: Tailored exactly to your unique goal
3. **Leverages multi-agent collaboration**: Different specialized agents handle different aspects of planning
4. **Provides iterative refinement**: Continuously improves plans based on evaluation against success criteria
5. **Offers complete modularity**: Each component can be swapped or modified independently

## Project Structure

The project consists of five modules that work together in a modular pipeline:

### Module 1: Criteria Generation (`module1.py`)
- Takes any user goal as input
- Uses a specialized agent to identify key success criteria specific to your goal
- Produces detailed reasoning and ratings for each criterion
- Creates a ranked list of criteria for project success

### Module 2: Plan Generation (`module2.py`)
- Takes the goal and success criteria from Module 1
- Uses a planning agent to generate multiple potential approaches
- Creates detailed outlines with reasoning for each approach
- Uses an evaluation agent to rank and select the best approach

### Module 3: Plan Expansion and Evaluation (`module3.py`)
- Takes the selected plan from Module 2
- Uses an expansion agent to flesh out each plan item in detail
- Evaluates each expanded item against the success criteria
- Creates a detailed evaluation summary for the expanded plan

### Module 4: Revision Identification (`module4.py`)
- Analyzes evaluation results from Module 3
- Identifies items that need revision based on criteria assessment
- Generates specific revision requests for items that don't fully meet criteria
- Evaluates potential impact of proposed revisions

### Module 5: Revision Implementation (`module5.py`)
- Takes approved revisions from Module 4
- Implements the revision requests into the plan items
- Evaluates how well the revisions address criteria
- Creates a final, revised plan with improvements

## Modularity and Interoperability

One of the most powerful features of this system is its modularity:

- **Framework Independence**: Each module can use a different agent framework (OpenAI Agents, AutoGen, Crew, LangGraph, etc.)
- **Standard Interfaces**: Modules communicate via standardized JSON formats
- **Plug-and-Play**: Replace any module with your own implementation as long as it respects the interface
- **Team Collaboration**: Different teams can work on different modules simultaneously
- **Experimentation**: Try different approaches for specific modules without disrupting the whole pipeline

This approach allows developers to leverage the strengths of various agent frameworks and work together efficiently even in distributed teams.

## Running the Project

### Prerequisites
- Python 3.9+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/dazzagreenwood/goal-to-plan-agent-system.git
cd goal-to-plan-agent-system
```

2. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your_api_key_here
```

### Running the Modules

You can run each module sequentially:

```bash
python module1.py  # Generates success criteria
python module2.py  # Creates and selects a plan
python module3.py  # Expands and evaluates the plan
python module4.py  # Identifies needed revisions
python module5.py  # Implements revisions into a final plan
```

Each module saves its output to a JSON file in the `data` directory, which serves as input for the next module.

Alternatively, you can run the entire pipeline:

```bash
python run_pipeline.py
```

## Contribution and Extension

I encourage you to experiment with this system:

- **Build your own modules**: Create alternative implementations of any stage
- **Make pull requests**: Share improvements or bug fixes
- **Report issues**: Let me know if you encounter problems
- **Share extensions**: If you build something cool based on this, shoot me a link!

This project is meant to demonstrate an approach to agent-based planning that can be extended and improved by the community.

## License

This project is licensed under MIT License - see the LICENSE file for details.