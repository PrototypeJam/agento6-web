├── .github
    └── workflows
    │   ├── docs.yml
    │   ├── publish.yml
    │   └── tests.yml
├── .gitignore
├── .prettierrc
├── LICENSE
├── Makefile
├── README.md
├── docs
    ├── agents.md
    ├── assets
    │   ├── images
    │   │   ├── favicon-platform.svg
    │   │   └── orchestration.png
    │   └── logo.svg
    ├── config.md
    ├── context.md
    ├── guardrails.md
    ├── handoffs.md
    ├── index.md
    ├── models.md
    ├── multi_agent.md
    ├── quickstart.md
    ├── ref
    │   ├── agent.md
    │   ├── agent_output.md
    │   ├── exceptions.md
    │   ├── extensions
    │   │   ├── handoff_filters.md
    │   │   └── handoff_prompt.md
    │   ├── function_schema.md
    │   ├── guardrail.md
    │   ├── handoffs.md
    │   ├── index.md
    │   ├── items.md
    │   ├── lifecycle.md
    │   ├── model_settings.md
    │   ├── models
    │   │   ├── interface.md
    │   │   ├── openai_chatcompletions.md
    │   │   └── openai_responses.md
    │   ├── result.md
    │   ├── run.md
    │   ├── run_context.md
    │   ├── stream_events.md
    │   ├── tool.md
    │   ├── tracing
    │   │   ├── create.md
    │   │   ├── index.md
    │   │   ├── processor_interface.md
    │   │   ├── processors.md
    │   │   ├── scope.md
    │   │   ├── setup.md
    │   │   ├── span_data.md
    │   │   ├── spans.md
    │   │   ├── traces.md
    │   │   └── util.md
    │   └── usage.md
    ├── results.md
    ├── running_agents.md
    ├── streaming.md
    ├── stylesheets
    │   └── extra.css
    ├── tools.md
    └── tracing.md
├── examples
    ├── __init__.py
    ├── agent_patterns
    │   ├── README.md
    │   ├── agents_as_tools.py
    │   ├── deterministic.py
    │   ├── input_guardrails.py
    │   ├── llm_as_a_judge.py
    │   ├── output_guardrails.py
    │   ├── parallelization.py
    │   └── routing.py
    ├── basic
    │   ├── agent_lifecycle_example.py
    │   ├── dynamic_system_prompt.py
    │   ├── hello_world.py
    │   ├── lifecycle_example.py
    │   ├── stream_items.py
    │   └── stream_text.py
    ├── customer_service
    │   └── main.py
    ├── handoffs
    │   ├── message_filter.py
    │   └── message_filter_streaming.py
    ├── research_bot
    │   ├── README.md
    │   ├── __init__.py
    │   ├── agents
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-313.pyc
    │   │   │   ├── base_agent.cpython-313.pyc
    │   │   │   ├── planner_agent.cpython-313.pyc
    │   │   │   ├── research_manager_agent.cpython-313.pyc
    │   │   │   ├── search_agent.cpython-313.pyc
    │   │   │   ├── summarization_agent.cpython-313.pyc
    │   │   │   └── writer_agent.cpython-313.pyc
    │   │   ├── planner_agent.py
    │   │   ├── search_agent.py
    │   │   └── writer_agent.py
    │   ├── main.py
    │   ├── manager.py
    │   ├── printer.py
    │   └── sample_outputs
    │   │   ├── product_recs.md
    │   │   ├── product_recs.txt
    │   │   ├── vacation.md
    │   │   └── vacation.txt
    └── tools
    │   ├── computer_use.py
    │   ├── file_search.py
    │   └── web_search.py
├── mkdocs.yml
├── pyproject.toml
├── src
    └── agents
    │   ├── __init__.py
    │   ├── _config.py
    │   ├── _debug.py
    │   ├── _run_impl.py
    │   ├── _utils.py
    │   ├── agent.py
    │   ├── agent_output.py
    │   ├── computer.py
    │   ├── exceptions.py
    │   ├── extensions
    │       ├── __init__.py
    │       ├── handoff_filters.py
    │       └── handoff_prompt.py
    │   ├── function_schema.py
    │   ├── guardrail.py
    │   ├── handoffs.py
    │   ├── items.py
    │   ├── lifecycle.py
    │   ├── logger.py
    │   ├── model_settings.py
    │   ├── models
    │       ├── __init__.py
    │       ├── _openai_shared.py
    │       ├── fake_id.py
    │       ├── interface.py
    │       ├── openai_chatcompletions.py
    │       ├── openai_provider.py
    │       └── openai_responses.py
    │   ├── result.py
    │   ├── run.py
    │   ├── run_context.py
    │   ├── stream_events.py
    │   ├── strict_schema.py
    │   ├── tool.py
    │   ├── tracing
    │       ├── __init__.py
    │       ├── create.py
    │       ├── logger.py
    │       ├── processor_interface.py
    │       ├── processors.py
    │       ├── scope.py
    │       ├── setup.py
    │       ├── span_data.py
    │       ├── spans.py
    │       ├── traces.py
    │       └── util.py
    │   ├── usage.py
    │   └── version.py
├── tests
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── __init__.py
    ├── conftest.py
    ├── docs
    │   ├── agents.md
    │   ├── assets
    │   │   ├── images
    │   │   │   ├── favicon-platform.svg
    │   │   │   └── orchestration.png
    │   │   └── logo.svg
    │   ├── config.md
    │   ├── context.md
    │   ├── guardrails.md
    │   ├── handoffs.md
    │   ├── index.md
    │   ├── models.md
    │   ├── multi_agent.md
    │   ├── quickstart.md
    │   ├── ref
    │   │   ├── agent.md
    │   │   ├── agent_output.md
    │   │   ├── exceptions.md
    │   │   ├── extensions
    │   │   │   ├── handoff_filters.md
    │   │   │   └── handoff_prompt.md
    │   │   ├── function_schema.md
    │   │   ├── guardrail.md
    │   │   ├── handoffs.md
    │   │   ├── index.md
    │   │   ├── items.md
    │   │   ├── lifecycle.md
    │   │   ├── model_settings.md
    │   │   ├── models
    │   │   │   ├── interface.md
    │   │   │   ├── openai_chatcompletions.md
    │   │   │   └── openai_responses.md
    │   │   ├── result.md
    │   │   ├── run.md
    │   │   ├── run_context.md
    │   │   ├── stream_events.md
    │   │   ├── tool.md
    │   │   ├── tracing
    │   │   │   ├── create.md
    │   │   │   ├── index.md
    │   │   │   ├── processor_interface.md
    │   │   │   ├── processors.md
    │   │   │   ├── scope.md
    │   │   │   ├── setup.md
    │   │   │   ├── span_data.md
    │   │   │   ├── spans.md
    │   │   │   ├── traces.md
    │   │   │   └── util.md
    │   │   └── usage.md
    │   ├── results.md
    │   ├── running_agents.md
    │   ├── streaming.md
    │   ├── stylesheets
    │   │   └── extra.css
    │   ├── tools.md
    │   └── tracing.md
    ├── examples
    │   ├── __init__.py
    │   ├── agent_patterns
    │   │   ├── README.md
    │   │   ├── agents_as_tools.py
    │   │   ├── deterministic.py
    │   │   ├── input_guardrails.py
    │   │   ├── llm_as_a_judge.py
    │   │   ├── output_guardrails.py
    │   │   ├── parallelization.py
    │   │   └── routing.py
    │   ├── basic
    │   │   ├── agent_lifecycle_example.py
    │   │   ├── dynamic_system_prompt.py
    │   │   ├── hello_world.py
    │   │   ├── lifecycle_example.py
    │   │   ├── stream_items.py
    │   │   └── stream_text.py
    │   ├── customer_service
    │   │   └── main.py
    │   ├── handoffs
    │   │   ├── message_filter.py
    │   │   └── message_filter_streaming.py
    │   ├── research_bot
    │   │   ├── README.md
    │   │   ├── __init__.py
    │   │   ├── agents
    │   │   │   ├── __init__.py
    │   │   │   ├── planner_agent.py
    │   │   │   ├── search_agent.py
    │   │   │   └── writer_agent.py
    │   │   ├── main.py
    │   │   ├── manager.py
    │   │   ├── printer.py
    │   │   └── sample_outputs
    │   │   │   ├── product_recs.md
    │   │   │   ├── product_recs.txt
    │   │   │   ├── vacation.md
    │   │   │   └── vacation.txt
    │   └── tools
    │   │   ├── computer_use.py
    │   │   ├── file_search.py
    │   │   └── web_search.py
    ├── fake_model.py
    ├── mkdocs.yml
    ├── pyproject.toml
    ├── src
    │   ├── agents
    │   │   ├── __init__.py
    │   │   ├── _config.py
    │   │   ├── _debug.py
    │   │   ├── _run_impl.py
    │   │   ├── _utils.py
    │   │   ├── agent.py
    │   │   ├── agent_output.py
    │   │   ├── computer.py
    │   │   ├── exceptions.py
    │   │   ├── extensions
    │   │   │   ├── __init__.py
    │   │   │   ├── handoff_filters.py
    │   │   │   └── handoff_prompt.py
    │   │   ├── function_schema.py
    │   │   ├── guardrail.py
    │   │   ├── handoffs.py
    │   │   ├── items.py
    │   │   ├── lifecycle.py
    │   │   ├── logger.py
    │   │   ├── model_settings.py
    │   │   ├── models
    │   │   │   ├── __init__.py
    │   │   │   ├── _openai_shared.py
    │   │   │   ├── fake_id.py
    │   │   │   ├── interface.py
    │   │   │   ├── openai_chatcompletions.py
    │   │   │   ├── openai_provider.py
    │   │   │   └── openai_responses.py
    │   │   ├── result.py
    │   │   ├── run.py
    │   │   ├── run_context.py
    │   │   ├── stream_events.py
    │   │   ├── strict_schema.py
    │   │   ├── tool.py
    │   │   ├── tracing
    │   │   │   ├── __init__.py
    │   │   │   ├── create.py
    │   │   │   ├── logger.py
    │   │   │   ├── processor_interface.py
    │   │   │   ├── processors.py
    │   │   │   ├── scope.py
    │   │   │   ├── setup.py
    │   │   │   ├── span_data.py
    │   │   │   ├── spans.py
    │   │   │   ├── traces.py
    │   │   │   └── util.py
    │   │   ├── usage.py
    │   │   └── version.py
    │   └── openai_agents.egg-info
    │   │   ├── PKG-INFO
    │   │   ├── SOURCES.txt
    │   │   ├── dependency_links.txt
    │   │   ├── requires.txt
    │   │   └── top_level.txt
    ├── test_agent_config.py
    ├── test_agent_hooks.py
    ├── test_agent_runner.py
    ├── test_agent_runner_streamed.py
    ├── test_agent_tracing.py
    ├── test_computer_action.py
    ├── test_config.py
    ├── test_doc_parsing.py
    ├── test_extension_filters.py
    ├── test_function_schema.py
    ├── test_function_tool.py
    ├── test_function_tool_decorator.py
    ├── test_global_hooks.py
    ├── test_guardrails.py
    ├── test_handoff_tool.py
    ├── test_items_helpers.py
    ├── test_max_turns.py
    ├── test_openai_chatcompletions.py
    ├── test_openai_chatcompletions_converter.py
    ├── test_openai_chatcompletions_stream.py
    ├── test_openai_responses_converter.py
    ├── test_output_tool.py
    ├── test_responses.py
    ├── test_responses_tracing.py
    ├── test_result_cast.py
    ├── test_run_config.py
    ├── test_run_step_execution.py
    ├── test_run_step_processing.py
    ├── test_strict_schema.py
    ├── test_tool_converter.py
    ├── test_trace_processor.py
    ├── test_tracing.py
    ├── test_tracing_errors.py
    ├── test_tracing_errors_streamed.py
    └── testing_processor.py
└── uv.lock


/.github/workflows/docs.yml:
--------------------------------------------------------------------------------
 1 | name: Deploy docs
 2 | 
 3 | on:
 4 |   workflow_run:
 5 |     workflows: ["Tests"]
 6 |     types:
 7 |       - completed
 8 | 
 9 | permissions:
10 |   contents: write # This allows pushing to gh-pages
11 | 
12 | jobs:
13 |   deploy_docs:
14 |     if: ${{ github.event.workflow_run.conclusion == 'success' }}
15 |     runs-on: ubuntu-latest
16 |     steps:
17 |       - name: Checkout repository
18 |         uses: actions/checkout@v4
19 |       - name: Setup uv
20 |         uses: astral-sh/setup-uv@v5
21 |         with:
22 |           enable-cache: true
23 |       - name: Install dependencies
24 |         run: make sync
25 |       - name: Deploy docs
26 |         run: make deploy-docs
27 | 


--------------------------------------------------------------------------------
/.github/workflows/publish.yml:
--------------------------------------------------------------------------------
 1 | name: Publish to PyPI
 2 | 
 3 | on:
 4 |   release:
 5 |     types:
 6 |       - published
 7 | 
 8 | permissions:
 9 |   contents: read
10 | 
11 | jobs:
12 |   publish:
13 |     environment:
14 |       name: pypi
15 |       url: https://pypi.org/p/openai-agents
16 |     permissions:
17 |       id-token: write # Important for trusted publishing to PyPI
18 |     runs-on: ubuntu-latest
19 |     env:
20 |       OPENAI_API_KEY: fake-for-tests
21 | 
22 |     steps:
23 |       - name: Checkout repository
24 |         uses: actions/checkout@v4
25 |       - name: Setup uv
26 |         uses: astral-sh/setup-uv@v5
27 |         with:
28 |           enable-cache: true
29 |       - name: Install dependencies
30 |         run: make sync
31 |       - name: Build package
32 |         run: uv build
33 |       - name: Publish to PyPI
34 |         uses: pypa/gh-action-pypi-publish@release/v1
35 | 


--------------------------------------------------------------------------------
/.github/workflows/tests.yml:
--------------------------------------------------------------------------------
 1 | name: Tests
 2 | 
 3 | on:
 4 |   push:
 5 |     branches:
 6 |       - main
 7 |   pull_request:
 8 |     branches:
 9 |       - main
10 | 
11 | jobs:
12 |   lint:
13 |     runs-on: ubuntu-latest
14 |     steps:
15 |       - name: Checkout repository
16 |         uses: actions/checkout@v4
17 |       - name: Setup uv
18 |         uses: astral-sh/setup-uv@v5
19 |         with:
20 |           enable-cache: true
21 |       - name: Install dependencies
22 |         run: make sync
23 |       - name: Run lint
24 |         run: make lint
25 | 
26 |   typecheck:
27 |     runs-on: ubuntu-latest
28 |     steps:
29 |       - name: Checkout repository
30 |         uses: actions/checkout@v4
31 |       - name: Setup uv
32 |         uses: astral-sh/setup-uv@v5
33 |         with:
34 |           enable-cache: true
35 |       - name: Install dependencies
36 |         run: make sync
37 |       - name: Run typecheck
38 |         run: make mypy
39 | 
40 |   tests:
41 |     runs-on: ubuntu-latest
42 |     env:
43 |       OPENAI_API_KEY: fake-for-tests
44 |     steps:
45 |       - name: Checkout repository
46 |         uses: actions/checkout@v4
47 |       - name: Setup uv
48 |         uses: astral-sh/setup-uv@v5
49 |         with:
50 |           enable-cache: true
51 |       - name: Install dependencies
52 |         run: make sync
53 |       - name: Run tests
54 |         run: make tests
55 | 
56 |   build-docs:
57 |     runs-on: ubuntu-latest
58 |     env:
59 |       OPENAI_API_KEY: fake-for-tests
60 |     steps:
61 |       - name: Checkout repository
62 |         uses: actions/checkout@v4
63 |       - name: Setup uv
64 |         uses: astral-sh/setup-uv@v5
65 |         with:
66 |           enable-cache: true
67 |       - name: Install dependencies
68 |         run: make sync
69 |       - name: Build docs
70 |         run: make build-docs
71 | 
72 |   old_versions:
73 |     runs-on: ubuntu-latest
74 |     env:
75 |       OPENAI_API_KEY: fake-for-tests
76 |     steps:
77 |       - name: Checkout repository
78 |         uses: actions/checkout@v4
79 |       - name: Setup uv
80 |         uses: astral-sh/setup-uv@v5
81 |         with:
82 |           enable-cache: true
83 |       - name: Install dependencies
84 |         run: make sync
85 |       - name: Run tests
86 |         run: make old_version_tests
87 | 


--------------------------------------------------------------------------------
/.gitignore:
--------------------------------------------------------------------------------
  1 | # macOS Files
  2 | .DS_Store
  3 | 
  4 | # Byte-compiled / optimized / DLL files
  5 | __pycache__/
  6 | *.py[cod]
  7 | *$py.class
  8 | 
  9 | # C extensions
 10 | *.so
 11 | 
 12 | # Distribution / packaging
 13 | .Python
 14 | build/
 15 | develop-eggs/
 16 | dist/
 17 | downloads/
 18 | eggs/
 19 | .eggs/
 20 | lib/
 21 | lib64/
 22 | parts/
 23 | sdist/
 24 | var/
 25 | wheels/
 26 | share/python-wheels/
 27 | *.egg-info/
 28 | .installed.cfg
 29 | *.egg
 30 | MANIFEST
 31 | 
 32 | # PyInstaller
 33 | *.manifest
 34 | *.spec
 35 | 
 36 | # Installer logs
 37 | pip-log.txt
 38 | pip-delete-this-directory.txt
 39 | 
 40 | # Unit test / coverage reports
 41 | htmlcov/
 42 | .tox/
 43 | .nox/
 44 | .coverage
 45 | .coverage.*
 46 | .cache
 47 | nosetests.xml
 48 | coverage.xml
 49 | *.cover
 50 | *.py,cover
 51 | .hypothesis/
 52 | .pytest_cache/
 53 | cover/
 54 | 
 55 | # Translations
 56 | *.mo
 57 | *.pot
 58 | 
 59 | # Django stuff:
 60 | *.log
 61 | local_settings.py
 62 | db.sqlite3
 63 | db.sqlite3-journal
 64 | 
 65 | # Flask stuff:
 66 | instance/
 67 | .webassets-cache
 68 | 
 69 | # Scrapy stuff:
 70 | .scrapy
 71 | 
 72 | # Sphinx documentation
 73 | docs/_build/
 74 | 
 75 | # PyBuilder
 76 | .pybuilder/
 77 | target/
 78 | 
 79 | # Jupyter Notebook
 80 | .ipynb_checkpoints
 81 | 
 82 | # IPython
 83 | profile_default/
 84 | ipython_config.py
 85 | 
 86 | # pdm
 87 | .pdm.toml
 88 | .pdm-python
 89 | .pdm-build/
 90 | 
 91 | # PEP 582
 92 | __pypackages__/
 93 | 
 94 | # Celery stuff
 95 | celerybeat-schedule
 96 | celerybeat.pid
 97 | 
 98 | # SageMath parsed files
 99 | *.sage.py
100 | 
101 | # Environments
102 | .env
103 | .venv
104 | env/
105 | venv/
106 | ENV/
107 | env.bak/
108 | venv.bak/
109 | .venv39
110 | .venv_res
111 | 
112 | # Spyder project settings
113 | .spyderproject
114 | .spyproject
115 | 
116 | # Rope project settings
117 | .ropeproject
118 | 
119 | # mkdocs documentation
120 | /site
121 | 
122 | # mypy
123 | .mypy_cache/
124 | .dmypy.json
125 | dmypy.json
126 | 
127 | # Pyre type checker
128 | .pyre/
129 | 
130 | # pytype static type analyzer
131 | .pytype/
132 | 
133 | # Cython debug symbols
134 | cython_debug/
135 | 
136 | # PyCharm
137 | #.idea/
138 | 
139 | # Ruff stuff:
140 | .ruff_cache/
141 | 
142 | # PyPI configuration file
143 | .pypirc
144 | 


--------------------------------------------------------------------------------
/.prettierrc:
--------------------------------------------------------------------------------
 1 | {
 2 |     "tabWidth": 4,
 3 |     "overrides": [
 4 |         {
 5 |             "files": "*.yml",
 6 |             "options": {
 7 |                 "tabWidth": 2
 8 |             }
 9 |         }
10 |     ]
11 | }


--------------------------------------------------------------------------------
/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2025 OpenAI
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: sync
 2 | sync:
 3 | 	uv sync --all-extras --all-packages --group dev
 4 | 
 5 | .PHONY: format
 6 | format: 
 7 | 	uv run ruff format
 8 | 
 9 | .PHONY: lint
10 | lint: 
11 | 	uv run ruff check
12 | 
13 | .PHONY: mypy
14 | mypy: 
15 | 	uv run mypy .
16 | 
17 | .PHONY: tests
18 | tests: 
19 | 	uv run pytest 
20 | 
21 | .PHONY: old_version_tests
22 | old_version_tests: 
23 | 	UV_PROJECT_ENVIRONMENT=.venv_39 uv run --python 3.9 -m pytest
24 | 	UV_PROJECT_ENVIRONMENT=.venv_39 uv run --python 3.9 -m mypy .
25 | 
26 | .PHONY: build-docs
27 | build-docs:
28 | 	uv run mkdocs build
29 | 
30 | .PHONY: serve-docs
31 | serve-docs:
32 | 	uv run mkdocs serve
33 | 
34 | .PHONY: deploy-docs
35 | deploy-docs:
36 | 	uv run mkdocs gh-deploy --force --verbose
37 | 	
38 | 


--------------------------------------------------------------------------------
 1 | <svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g clip-path="url(#clip0_1497_2713)">
 3 | <rect width="512" height="512" rx="256" fill="#0000FF"/>
 4 | <g clip-path="url(#clip1_1497_2713)">
 5 | <path d="M215.923 209.432V177.018C215.923 174.288 216.947 172.24 219.334 170.876L284.506 133.344C293.378 128.227 303.955 125.839 314.872 125.839C355.816 125.839 381.75 157.572 381.75 191.35C381.75 193.737 381.75 196.467 381.407 199.197L313.848 159.617C309.755 157.229 305.658 157.229 301.564 159.617L215.923 209.432ZM368.099 335.679V258.224C368.099 253.446 366.051 250.034 361.958 247.646L276.316 197.831L304.294 181.793C306.682 180.43 308.73 180.43 311.118 181.793L376.289 219.325C395.057 230.245 407.68 253.446 407.68 275.964C407.68 301.894 392.327 325.78 368.099 335.676V335.679ZM195.792 267.438L167.813 251.061C165.425 249.698 164.401 247.649 164.401 244.919V169.855C164.401 133.347 192.38 105.708 230.254 105.708C244.586 105.708 257.891 110.486 269.153 119.016L201.937 157.914C197.843 160.302 195.795 163.714 195.795 168.492V267.441L195.792 267.438ZM256.015 302.24L215.923 279.722V231.954L256.015 209.436L296.104 231.954V279.722L256.015 302.24ZM281.776 405.968C267.444 405.968 254.14 401.19 242.877 392.66L310.094 353.762C314.187 351.374 316.235 347.962 316.235 343.184V244.235L344.557 260.611C346.944 261.975 347.968 264.023 347.968 266.753V341.817C347.968 378.325 319.647 405.965 281.776 405.965V405.968ZM200.909 329.88L135.738 292.348C116.97 281.427 104.347 258.227 104.347 235.709C104.347 209.436 120.042 185.893 144.267 175.997V253.791C144.267 258.57 146.315 261.981 150.409 264.369L235.711 313.842L207.733 329.88C205.345 331.243 203.297 331.243 200.909 329.88ZM197.158 385.837C158.602 385.837 130.281 356.834 130.281 321.008C130.281 318.278 130.623 315.548 130.963 312.818L198.179 351.717C202.273 354.104 206.369 354.104 210.463 351.717L296.104 302.243V334.658C296.104 337.388 295.08 339.436 292.693 340.8L227.521 378.332C218.649 383.449 208.072 385.837 197.155 385.837H197.158ZM281.776 426.438C323.062 426.438 357.522 397.096 365.373 358.197C403.586 348.302 428.153 312.475 428.153 275.967C428.153 252.082 417.918 228.882 399.493 212.162C401.199 204.997 402.223 197.831 402.223 190.668C402.223 141.877 362.643 105.365 316.92 105.365C307.709 105.365 298.838 106.729 289.966 109.801C274.61 94.7878 253.455 85.2344 230.254 85.2344C188.968 85.2344 154.509 114.576 146.658 153.475C108.444 163.371 83.877 199.197 83.877 235.705C83.877 259.59 94.1121 282.791 112.537 299.51C110.831 306.676 109.807 313.842 109.807 321.005C109.807 369.796 149.388 406.307 195.11 406.307C204.321 406.307 213.193 404.944 222.064 401.871C237.417 416.885 258.572 426.438 281.776 426.438Z" fill="white"/>
 6 | </g>
 7 | </g>
 8 | <defs>
 9 | <clipPath id="clip0_1497_2713">
10 | <rect width="512" height="512" rx="256" fill="white"/>
11 | </clipPath>
12 | <clipPath id="clip1_1497_2713">
13 | <rect width="344.276" height="341.204" fill="white" transform="translate(83.877 85.2344)"/>
14 | </clipPath>
15 | </defs>
16 | </svg>
17 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/docs/assets/images/orchestration.png


--------------------------------------------------------------------------------
 1 | <svg width="721" height="721" viewBox="0 0 721 721" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g clip-path="url(#clip0_1637_2935)">
 3 | <g clip-path="url(#clip1_1637_2935)">
 4 | <path d="M304.246 295.411V249.828C304.246 245.989 305.687 243.109 309.044 241.191L400.692 188.412C413.167 181.215 428.042 177.858 443.394 177.858C500.971 177.858 537.44 222.482 537.44 269.982C537.44 273.34 537.44 277.179 536.959 281.018L441.954 225.358C436.197 222 430.437 222 424.68 225.358L304.246 295.411ZM518.245 472.945V364.024C518.245 357.304 515.364 352.507 509.608 349.149L389.174 279.096L428.519 256.543C431.877 254.626 434.757 254.626 438.115 256.543L529.762 309.323C556.154 324.679 573.905 357.304 573.905 388.971C573.905 425.436 552.315 459.024 518.245 472.941V472.945ZM275.937 376.982L236.592 353.952C233.235 352.034 231.794 349.154 231.794 345.315V239.756C231.794 188.416 271.139 149.548 324.4 149.548C344.555 149.548 363.264 156.268 379.102 168.262L284.578 222.964C278.822 226.321 275.942 231.119 275.942 237.838V376.986L275.937 376.982ZM360.626 425.922L304.246 394.255V327.083L360.626 295.416L417.002 327.083V394.255L360.626 425.922ZM396.852 571.789C376.698 571.789 357.989 565.07 342.151 553.075L436.674 498.374C442.431 495.017 445.311 490.219 445.311 483.499V344.352L485.138 367.382C488.495 369.299 489.936 372.179 489.936 376.018V481.577C489.936 532.917 450.109 571.785 396.852 571.785V571.789ZM283.134 464.79L191.486 412.01C165.094 396.654 147.343 364.029 147.343 332.362C147.343 295.416 169.415 262.309 203.48 248.393V357.791C203.48 364.51 206.361 369.308 212.117 372.665L332.074 442.237L292.729 464.79C289.372 466.707 286.491 466.707 283.134 464.79ZM277.859 543.48C223.639 543.48 183.813 502.695 183.813 452.314C183.813 448.475 184.294 444.636 184.771 440.797L279.295 495.498C285.051 498.856 290.812 498.856 296.568 495.498L417.002 425.927V471.509C417.002 475.349 415.562 478.229 412.204 480.146L320.557 532.926C308.081 540.122 293.206 543.48 277.854 543.48H277.859ZM396.852 600.576C454.911 600.576 503.37 559.313 514.41 504.612C568.149 490.696 602.696 440.315 602.696 388.976C602.696 355.387 588.303 322.762 562.392 299.25C564.791 289.173 566.231 279.096 566.231 269.024C566.231 200.411 510.571 149.067 446.274 149.067C433.322 149.067 420.846 150.984 408.37 155.305C386.775 134.192 357.026 120.758 324.4 120.758C266.342 120.758 217.883 162.02 206.843 216.721C153.104 230.637 118.557 281.018 118.557 332.357C118.557 365.946 132.95 398.571 158.861 422.083C156.462 432.16 155.022 442.237 155.022 452.309C155.022 520.922 210.682 572.266 274.978 572.266C287.931 572.266 300.407 570.349 312.883 566.028C334.473 587.141 364.222 600.576 396.852 600.576Z" fill="white"/>
 5 | </g>
 6 | </g>
 7 | <defs>
 8 | <clipPath id="clip0_1637_2935">
 9 | <rect width="720" height="720" fill="white" transform="translate(0.606934 0.899902)"/>
10 | </clipPath>
11 | <clipPath id="clip1_1637_2935">
12 | <rect width="484.139" height="479.818" fill="white" transform="translate(118.557 120.758)"/>
13 | </clipPath>
14 | </defs>
15 | </svg>
16 | 


--------------------------------------------------------------------------------
/docs/config.md:
--------------------------------------------------------------------------------
 1 | # Configuring the SDK
 2 | 
 3 | ## API keys and clients
 4 | 
 5 | By default, the SDK looks for the `OPENAI_API_KEY` environment variable for LLM requests and tracing, as soon as it is imported. If you are unable to set that environment variable before your app starts, you can use the [set_default_openai_key()][agents.set_default_openai_key] function to set the key.
 6 | 
 7 | ```python
 8 | from agents import set_default_openai_key
 9 | 
10 | set_default_openai_key("sk-...")
11 | ```
12 | 
13 | Alternatively, you can also configure an OpenAI client to be used. By default, the SDK creates an `AsyncOpenAI` instance, using the API key from the environment variable or the default key set above. You can chnage this by using the [set_default_openai_client()][agents.set_default_openai_client] function.
14 | 
15 | ```python
16 | from openai import AsyncOpenAI
17 | from agents import set_default_openai_client
18 | 
19 | custom_client = AsyncOpenAI(base_url="...", api_key="...")
20 | set_default_openai_client(client)
21 | ```
22 | 
23 | Finally, you can also customize the OpenAI API that is used. By default, we use the OpenAI Responses API. You can override this to use the Chat Completions API by using the [set_default_openai_api()][agents.set_default_openai_api] function.
24 | 
25 | ```python
26 | from agents import set_default_openai_api
27 | 
28 | set_default_openai_api("chat_completions")
29 | ```
30 | 
31 | ## Tracing
32 | 
33 | Tracing is enabled by default. It uses the OpenAI API keys from the section above by default (i.e. the environment variable or the default key you set). You can specifically set the API key used for tracing by using the [`set_tracing_export_api_key`][agents.set_tracing_export_api_key] function.
34 | 
35 | ```python
36 | from agents import set_tracing_export_api_key
37 | 
38 | set_tracing_export_api_key("sk-...")
39 | ```
40 | 
41 | You can also disable tracing entirely by using the [`set_tracing_disabled()`][agents.set_tracing_disabled] function.
42 | 
43 | ```python
44 | from agents import set_tracing_disabled
45 | 
46 | set_tracing_disabled(True)
47 | ```
48 | 
49 | ## Debug logging
50 | 
51 | The SDK has two Python loggers without any handlers set. By default, this means that warnings and errors are sent to `stdout`, but other logs are suppressed.
52 | 
53 | To enable verbose logging, use the [`enable_verbose_stdout_logging()`][agents.enable_verbose_stdout_logging] function.
54 | 
55 | ```python
56 | from agents import enable_verbose_stdout_logging
57 | 
58 | enable_verbose_stdout_logging()
59 | ```
60 | 
61 | Alternatively, you can customize the logs by adding handlers, filters, formatters, etc. You can read more in the [Python logging guide](https://docs.python.org/3/howto/logging.html).
62 | 
63 | ```python
64 | import logging
65 | 
66 | logger =  logging.getLogger("openai.agents") # or openai.agents.tracing for the Tracing logger
67 | 
68 | # To make all logs show up
69 | logger.setLevel(logging.DEBUG)
70 | # To make info and above show up
71 | logger.setLevel(logging.INFO)
72 | # To make warning and above show up
73 | logger.setLevel(logging.WARNING)
74 | # etc
75 | 
76 | # You can customize this as needed, but this will output to `stderr` by default
77 | logger.addHandler(logging.StreamHandler())
78 | ```
79 | 
80 | ### Sensitive data in logs
81 | 
82 | Certain logs may contain sensitive data (for example, user data). If you want to disable this data from being logged, set the following environment variables.
83 | 
84 | To disable logging LLM inputs and outputs:
85 | 
86 | ```bash
87 | export OPENAI_AGENTS_DONT_LOG_MODEL_DATA=1
88 | ```
89 | 
90 | To disable logging tool inputs and outputs:
91 | 
92 | ```bash
93 | export OPENAI_AGENTS_DONT_LOG_TOOL_DATA=1
94 | ```
95 | 


--------------------------------------------------------------------------------
/docs/index.md:
--------------------------------------------------------------------------------
 1 | # OpenAI Agents SDK
 2 | 
 3 | The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) enables you to build agentic AI apps in a lightweight, easy to use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, [Swarm](https://github.com/openai/swarm/tree/main). The Agents SDK has a very small set of primitives:
 4 | 
 5 | -   **Agents**, which are LLMs equipped with instructions and tools
 6 | -   **Handoffs**, which allow agents to delegate to other agents for specific tasks
 7 | -   **Guardrails**, which enable the inputs to agents to be validated
 8 | 
 9 | In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real world applications without a steep learning curve. In addition, the SDK comes with built-in **tracing** that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.
10 | 
11 | ## Why use the Agents SDK
12 | 
13 | The SDK has two driving design principles:
14 | 
15 | 1. Enough features to be worth using, but few enough primitives to make it quick to learn.
16 | 2. Works great out of the box, but you can customize exactly what happens.
17 | 
18 | Here are the main features of the SDK:
19 | 
20 | -   Agent loop: Built-in agent loop that handles calling tools, sending results to the LLM, and looping until the LLM is done.
21 | -   Python-first: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
22 | -   Handoffs: A powerful feature to coordinate and delegate between multiple agents.
23 | -   Guardrails: Run input validations and checks in parallel to your agents, breaking early if the checks fail.
24 | -   Function tools: Turn any Python function into a tool, with automatic schema generation and Pydantic-powered validation.
25 | -   Tracing: Built-in tracing that lets you visualize, debug and monitor your workflows, as well as use the OpenAI suite of evaluation, fine-tuning and distillation tools.
26 | 
27 | ## Installation
28 | 
29 | ```bash
30 | pip install openai-agents
31 | ```
32 | 
33 | ## Hello world example
34 | 
35 | ```python
36 | from agents import Agent, Runner
37 | 
38 | agent = Agent(name="Assistant", instructions="You are a helpful assistant")
39 | 
40 | result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
41 | print(result.final_output)
42 | 
43 | # Code within the code,
44 | # Functions calling themselves,
45 | # Infinite loop's dance.
46 | ```
47 | 
48 | (_If running this, ensure you set the `OPENAI_API_KEY` environment variable_)
49 | 
50 | ```bash
51 | export OPENAI_API_KEY=sk-...
52 | ```
53 | 


--------------------------------------------------------------------------------
/docs/models.md:
--------------------------------------------------------------------------------
/docs/multi_agent.md:
--------------------------------------------------------------------------------
 1 | # Orchestrating multiple agents
 2 | 
 3 | Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how do they decide what happens next? There are two main ways to orchestrate agents:
 4 | 
 5 | 1. Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that.
 6 | 2. Orchestrating via code: determining the flow of agents via your code.
 7 | 
 8 | You can mix and match these patterns. Each has their own tradeoffs, described below.
 9 | 
10 | ## Orchestrating via LLM
11 | 
12 | An agent is an LLM equipped with instructions, tools and handoffs. This means that given an open-ended task, the LLM can autonomously plan how it will tackle the task, using tools to take actions and acquire data, and using handoffs to delegate tasks to sub-agents. For example, a research agent could be equipped with tools like:
13 | 
14 | -   Web search to find information online
15 | -   File search and retrieval to search through proprietary data and connections
16 | -   Computer use to take actions on a computer
17 | -   Code execution to do data analysis
18 | -   Handoffs to specialized agents that are great at planning, report writing and more.
19 | 
20 | This pattern is great when the task is open-ended and you want to rely on the intelligence of an LLM. The most important tactics here are:
21 | 
22 | 1. Invest in good prompts. Make it clear what tools are available, how to use them, and what parameters it must operate within.
23 | 2. Monitor your app and iterate on it. See where things go wrong, and iterate on your prompts.
24 | 3. Allow the agent to introspect and improve. For example, run it in a loop, and let it critique itself; or, provide error messages and let it improve.
25 | 4. Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything.
26 | 5. Invest in [evals](https://platform.openai.com/docs/guides/evals). This lets you train your agents to improve and get better at tasks.
27 | 
28 | ## Orchestrating via code
29 | 
30 | While orchestrating via LLM is powerful, orchestrating via LLM makes tasks more deterministic and predictable, in terms of speed, cost and performance. Common patterns here are:
31 | 
32 | -   Using [structured outputs](https://platform.openai.com/docs/guides/structured-outputs) to generate well formed data that you can inspect with your code. For example, you might ask an agent to classify the task into a few categories, and then pick the next agent based on the category.
33 | -   Chaining multiple agents by transforming the output of one into the input of the next. You can decompose a task like writing a blog post into a series of steps - do research, write an outline, write the blog post, critique it, and then improve it.
34 | -   Running the agent that performs the task in a `while` loop with an agent that evaluates and provides feedback, until the evaluator says the output passes certain criteria.
35 | -   Running multiple agents in parallel, e.g. via Python primitives like `asyncio.gather`. This is useful for speed when you have multiple tasks that don't depend on each other.
36 | 
37 | We have a number of examples in [`examples/agent_patterns`](https://github.com/openai/openai-agents-python/examples/agent_patterns).
38 | 


--------------------------------------------------------------------------------
/docs/ref/agent.md:
--------------------------------------------------------------------------------
1 | # `Agents`
2 | 
3 | ::: agents.agent
4 | 


--------------------------------------------------------------------------------
/docs/ref/agent_output.md:
--------------------------------------------------------------------------------
1 | # `Agent output`
2 | 
3 | ::: agents.agent_output
4 | 


--------------------------------------------------------------------------------
/docs/ref/exceptions.md:
--------------------------------------------------------------------------------
1 | # `Exceptions`
2 | 
3 | ::: agents.exceptions
4 | 


--------------------------------------------------------------------------------
/docs/ref/extensions/handoff_filters.md:
--------------------------------------------------------------------------------
1 | # `Handoff filters`
2 | 
3 | ::: agents.extensions.handoff_filters
4 | 


--------------------------------------------------------------------------------
/docs/ref/extensions/handoff_prompt.md:
--------------------------------------------------------------------------------
1 | # `Handoff prompt`
2 | 
3 | ::: agents.extensions.handoff_prompt
4 | 
5 |     options:
6 |         members:
7 |             - RECOMMENDED_PROMPT_PREFIX
8 |             - prompt_with_handoff_instructions
9 | 


--------------------------------------------------------------------------------
/docs/ref/function_schema.md:
--------------------------------------------------------------------------------
1 | # `Function schema`
2 | 
3 | ::: agents.function_schema
4 | 


--------------------------------------------------------------------------------
/docs/ref/guardrail.md:
--------------------------------------------------------------------------------
1 | # `Guardrails`
2 | 
3 | ::: agents.guardrail
4 | 


--------------------------------------------------------------------------------
/docs/ref/handoffs.md:
--------------------------------------------------------------------------------
1 | # `Handoffs`
2 | 
3 | ::: agents.handoffs
4 | 


--------------------------------------------------------------------------------
/docs/ref/index.md:
--------------------------------------------------------------------------------
 1 | # Agents module
 2 | 
 3 | ::: agents
 4 | 
 5 |     options:
 6 |         members:
 7 |             - set_default_openai_key
 8 |             - set_default_openai_client
 9 |             - set_default_openai_api
10 |             - set_tracing_export_api_key
11 |             - set_tracing_disabled
12 |             - set_trace_processors
13 |             - enable_verbose_stdout_logging
14 | 


--------------------------------------------------------------------------------
/docs/ref/items.md:
--------------------------------------------------------------------------------
1 | # `Items`
2 | 
3 | ::: agents.items
4 | 


--------------------------------------------------------------------------------
/docs/ref/lifecycle.md:
--------------------------------------------------------------------------------
1 | # `Lifecycle`
2 | 
3 | ::: agents.lifecycle
4 | 
5 |     options:
6 |         show_source: false
7 | 


--------------------------------------------------------------------------------
/docs/ref/model_settings.md:
--------------------------------------------------------------------------------
1 | # `Model settings`
2 | 
3 | ::: agents.model_settings
4 | 


--------------------------------------------------------------------------------
/docs/ref/models/interface.md:
--------------------------------------------------------------------------------
1 | # `Model interface`
2 | 
3 | ::: agents.models.interface
4 | 


--------------------------------------------------------------------------------
/docs/ref/models/openai_chatcompletions.md:
--------------------------------------------------------------------------------
1 | # `OpenAI Chat Completions model`
2 | 
3 | ::: agents.models.openai_chatcompletions
4 | 


--------------------------------------------------------------------------------
/docs/ref/models/openai_responses.md:
--------------------------------------------------------------------------------
1 | # `OpenAI Responses model`
2 | 
3 | ::: agents.models.openai_responses
4 | 


--------------------------------------------------------------------------------
/docs/ref/result.md:
--------------------------------------------------------------------------------
1 | # `Results`
2 | 
3 | ::: agents.result
4 | 


--------------------------------------------------------------------------------
/docs/ref/run.md:
--------------------------------------------------------------------------------
1 | # `Runner`
2 | 
3 | ::: agents.run
4 | 
5 |     options:
6 |         members:
7 |             - Runner
8 |             - RunConfig
9 | 


--------------------------------------------------------------------------------
/docs/ref/run_context.md:
--------------------------------------------------------------------------------
1 | # `Run context`
2 | 
3 | ::: agents.run_context
4 | 


--------------------------------------------------------------------------------
/docs/ref/stream_events.md:
--------------------------------------------------------------------------------
1 | # `Streaming events`
2 | 
3 | ::: agents.stream_events
4 | 


--------------------------------------------------------------------------------
/docs/ref/tool.md:
--------------------------------------------------------------------------------
1 | # `Tools`
2 | 
3 | ::: agents.tool
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/create.md:
--------------------------------------------------------------------------------
1 | # `Creating traces/spans`
2 | 
3 | ::: agents.tracing.create
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/index.md:
--------------------------------------------------------------------------------
1 | # Tracing module
2 | 
3 | ::: agents.tracing
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/processor_interface.md:
--------------------------------------------------------------------------------
1 | # `Processor interface`
2 | 
3 | ::: agents.tracing.processor_interface
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/processors.md:
--------------------------------------------------------------------------------
1 | # `Processors`
2 | 
3 | ::: agents.tracing.processors
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/scope.md:
--------------------------------------------------------------------------------
1 | # `Scope`
2 | 
3 | ::: agents.tracing.scope
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/setup.md:
--------------------------------------------------------------------------------
1 | # `Setup`
2 | 
3 | ::: agents.tracing.setup
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/span_data.md:
--------------------------------------------------------------------------------
1 | # `Span data`
2 | 
3 | ::: agents.tracing.span_data
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/spans.md:
--------------------------------------------------------------------------------
 1 | # `Spans`
 2 | 
 3 | ::: agents.tracing.spans
 4 | 
 5 |     options:
 6 |         members:
 7 |             - Span
 8 |             - NoOpSpan
 9 |             - SpanImpl
10 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/traces.md:
--------------------------------------------------------------------------------
1 | # `Traces`
2 | 
3 | ::: agents.tracing.traces
4 | 


--------------------------------------------------------------------------------
/docs/ref/tracing/util.md:
--------------------------------------------------------------------------------
1 | # `Util`
2 | 
3 | ::: agents.tracing.util
4 | 


--------------------------------------------------------------------------------
/docs/ref/usage.md:
--------------------------------------------------------------------------------
1 | # `Usage`
2 | 
3 | ::: agents.usage
4 | 


--------------------------------------------------------------------------------
/examples/__init__.py:
--------------------------------------------------------------------------------
1 | # Make the examples directory into a package to avoid top-level module name collisions.
2 | # This is needed so that mypy treats files like examples/customer_service/main.py and
3 | # examples/researcher_app/main.py as distinct modules rather than both named "main".
4 | 


--------------------------------------------------------------------------------
/examples/agent_patterns/agents_as_tools.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace
 4 | 
 5 | """
 6 | This example shows the agents-as-tools pattern. The frontline agent receives a user message and
 7 | then picks which agents to call, as tools. In this case, it picks from a set of translation
 8 | agents.
 9 | """
10 | 
11 | spanish_agent = Agent(
12 |     name="spanish_agent",
13 |     instructions="You translate the user's message to Spanish",
14 |     handoff_description="An english to spanish translator",
15 | )
16 | 
17 | french_agent = Agent(
18 |     name="french_agent",
19 |     instructions="You translate the user's message to French",
20 |     handoff_description="An english to french translator",
21 | )
22 | 
23 | italian_agent = Agent(
24 |     name="italian_agent",
25 |     instructions="You translate the user's message to Italian",
26 |     handoff_description="An english to italian translator",
27 | )
28 | 
29 | orchestrator_agent = Agent(
30 |     name="orchestrator_agent",
31 |     instructions=(
32 |         "You are a translation agent. You use the tools given to you to translate."
33 |         "If asked for multiple translations, you call the relevant tools in order."
34 |         "You never translate on your own, you always use the provided tools."
35 |     ),
36 |     tools=[
37 |         spanish_agent.as_tool(
38 |             tool_name="translate_to_spanish",
39 |             tool_description="Translate the user's message to Spanish",
40 |         ),
41 |         french_agent.as_tool(
42 |             tool_name="translate_to_french",
43 |             tool_description="Translate the user's message to French",
44 |         ),
45 |         italian_agent.as_tool(
46 |             tool_name="translate_to_italian",
47 |             tool_description="Translate the user's message to Italian",
48 |         ),
49 |     ],
50 | )
51 | 
52 | synthesizer_agent = Agent(
53 |     name="synthesizer_agent",
54 |     instructions="You inspect translations, correct them if needed, and produce a final concatenated response.",
55 | )
56 | 
57 | 
58 | async def main():
59 |     msg = input("Hi! What would you like translated, and to which languages? ")
60 | 
61 |     # Run the entire orchestration in a single trace
62 |     with trace("Orchestrator evaluator"):
63 |         orchestrator_result = await Runner.run(orchestrator_agent, msg)
64 | 
65 |         for item in orchestrator_result.new_items:
66 |             if isinstance(item, MessageOutputItem):
67 |                 text = ItemHelpers.text_message_output(item)
68 |                 if text:
69 |                     print(f"  - Translation step: {text}")
70 | 
71 |         synthesizer_result = await Runner.run(
72 |             synthesizer_agent, orchestrator_result.to_input_list()
73 |         )
74 | 
75 |     print(f"\n\nFinal response:\n{synthesizer_result.final_output}")
76 | 
77 | 
78 | if __name__ == "__main__":
79 |     asyncio.run(main())
80 | 


--------------------------------------------------------------------------------
/examples/agent_patterns/deterministic.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from pydantic import BaseModel
 4 | 
 5 | from agents import Agent, Runner, trace
 6 | 
 7 | """
 8 | This example demonstrates a deterministic flow, where each step is performed by an agent.
 9 | 1. The first agent generates a story outline
10 | 2. We feed the outline into the second agent
11 | 3. The second agent checks if the outline is good quality and if it is a scifi story
12 | 4. If the outline is not good quality or not a scifi story, we stop here
13 | 5. If the outline is good quality and a scifi story, we feed the outline into the third agent
14 | 6. The third agent writes the story
15 | """
16 | 
17 | story_outline_agent = Agent(
18 |     name="story_outline_agent",
19 |     instructions="Generate a very short story outline based on the user's input.",
20 | )
21 | 
22 | 
23 | class OutlineCheckerOutput(BaseModel):
24 |     good_quality: bool
25 |     is_scifi: bool
26 | 
27 | 
28 | outline_checker_agent = Agent(
29 |     name="outline_checker_agent",
30 |     instructions="Read the given story outline, and judge the quality. Also, determine if it is a scifi story.",
31 |     output_type=OutlineCheckerOutput,
32 | )
33 | 
34 | story_agent = Agent(
35 |     name="story_agent",
36 |     instructions="Write a short story based on the given outline.",
37 |     output_type=str,
38 | )
39 | 
40 | 
41 | async def main():
42 |     input_prompt = input("What kind of story do you want? ")
43 | 
44 |     # Ensure the entire workflow is a single trace
45 |     with trace("Deterministic story flow"):
46 |         # 1. Generate an outline
47 |         outline_result = await Runner.run(
48 |             story_outline_agent,
49 |             input_prompt,
50 |         )
51 |         print("Outline generated")
52 | 
53 |         # 2. Check the outline
54 |         outline_checker_result = await Runner.run(
55 |             outline_checker_agent,
56 |             outline_result.final_output,
57 |         )
58 | 
59 |         # 3. Add a gate to stop if the outline is not good quality or not a scifi story
60 |         assert isinstance(outline_checker_result.final_output, OutlineCheckerOutput)
61 |         if not outline_checker_result.final_output.good_quality:
62 |             print("Outline is not good quality, so we stop here.")
63 |             exit(0)
64 | 
65 |         if not outline_checker_result.final_output.is_scifi:
66 |             print("Outline is not a scifi story, so we stop here.")
67 |             exit(0)
68 | 
69 |         print("Outline is good quality and a scifi story, so we continue to write the story.")
70 | 
71 |         # 4. Write the story
72 |         story_result = await Runner.run(
73 |             story_agent,
74 |             outline_result.final_output,
75 |         )
76 |         print(f"Story: {story_result.final_output}")
77 | 
78 | 
79 | if __name__ == "__main__":
80 |     asyncio.run(main())
81 | 


--------------------------------------------------------------------------------
/examples/agent_patterns/llm_as_a_judge.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import asyncio
 4 | from dataclasses import dataclass
 5 | from typing import Literal
 6 | 
 7 | from agents import Agent, ItemHelpers, Runner, TResponseInputItem, trace
 8 | 
 9 | """
10 | This example shows the LLM as a judge pattern. The first agent generates an outline for a story.
11 | The second agent judges the outline and provides feedback. We loop until the judge is satisfied
12 | with the outline.
13 | """
14 | 
15 | story_outline_generator = Agent(
16 |     name="story_outline_generator",
17 |     instructions=(
18 |         "You generate a very short story outline based on the user's input."
19 |         "If there is any feedback provided, use it to improve the outline."
20 |     ),
21 | )
22 | 
23 | 
24 | @dataclass
25 | class EvaluationFeedback:
26 |     score: Literal["pass", "needs_improvement", "fail"]
27 |     feedback: str
28 | 
29 | 
30 | evaluator = Agent[None](
31 |     name="evaluator",
32 |     instructions=(
33 |         "You evaluate a story outline and decide if it's good enough."
34 |         "If it's not good enough, you provide feedback on what needs to be improved."
35 |         "Never give it a pass on the first try."
36 |     ),
37 |     output_type=EvaluationFeedback,
38 | )
39 | 
40 | 
41 | async def main() -> None:
42 |     msg = input("What kind of story would you like to hear? ")
43 |     input_items: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
44 | 
45 |     latest_outline: str | None = None
46 | 
47 |     # We'll run the entire workflow in a single trace
48 |     with trace("LLM as a judge"):
49 |         while True:
50 |             story_outline_result = await Runner.run(
51 |                 story_outline_generator,
52 |                 input_items,
53 |             )
54 | 
55 |             input_items = story_outline_result.to_input_list()
56 |             latest_outline = ItemHelpers.text_message_outputs(story_outline_result.new_items)
57 |             print("Story outline generated")
58 | 
59 |             evaluator_result = await Runner.run(evaluator, input_items)
60 |             result: EvaluationFeedback = evaluator_result.final_output
61 | 
62 |             print(f"Evaluator score: {result.score}")
63 | 
64 |             if result.score == "pass":
65 |                 print("Story outline is good enough, exiting.")
66 |                 break
67 | 
68 |             print("Re-running with feedback")
69 | 
70 |             input_items.append({"content": f"Feedback: {result.feedback}", "role": "user"})
71 | 
72 |     print(f"Final story outline: {latest_outline}")
73 | 
74 | 
75 | if __name__ == "__main__":
76 |     asyncio.run(main())
77 | 


--------------------------------------------------------------------------------
/examples/agent_patterns/output_guardrails.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import asyncio
 4 | import json
 5 | 
 6 | from pydantic import BaseModel, Field
 7 | 
 8 | from agents import (
 9 |     Agent,
10 |     GuardrailFunctionOutput,
11 |     OutputGuardrailTripwireTriggered,
12 |     RunContextWrapper,
13 |     Runner,
14 |     output_guardrail,
15 | )
16 | 
17 | """
18 | This example shows how to use output guardrails.
19 | 
20 | Output guardrails are checks that run on the final output of an agent.
21 | They can be used to do things like:
22 | - Check if the output contains sensitive data
23 | - Check if the output is a valid response to the user's message
24 | 
25 | In this example, we'll use a (contrived) example where we check if the agent's response contains
26 | a phone number.
27 | """
28 | 
29 | 
30 | # The agent's output type
31 | class MessageOutput(BaseModel):
32 |     reasoning: str = Field(description="Thoughts on how to respond to the user's message")
33 |     response: str = Field(description="The response to the user's message")
34 |     user_name: str | None = Field(description="The name of the user who sent the message, if known")
35 | 
36 | 
37 | @output_guardrail
38 | async def sensitive_data_check(
39 |     context: RunContextWrapper, agent: Agent, output: MessageOutput
40 | ) -> GuardrailFunctionOutput:
41 |     phone_number_in_response = "650" in output.response
42 |     phone_number_in_reasoning = "650" in output.reasoning
43 | 
44 |     return GuardrailFunctionOutput(
45 |         output_info={
46 |             "phone_number_in_response": phone_number_in_response,
47 |             "phone_number_in_reasoning": phone_number_in_reasoning,
48 |         },
49 |         tripwire_triggered=phone_number_in_response or phone_number_in_reasoning,
50 |     )
51 | 
52 | 
53 | agent = Agent(
54 |     name="Assistant",
55 |     instructions="You are a helpful assistant.",
56 |     output_type=MessageOutput,
57 |     output_guardrails=[sensitive_data_check],
58 | )
59 | 
60 | 
61 | async def main():
62 |     # This should be ok
63 |     await Runner.run(agent, "What's the capital of California?")
64 |     print("First message passed")
65 | 
66 |     # This should trip the guardrail
67 |     try:
68 |         result = await Runner.run(
69 |             agent, "My phone number is 650-123-4567. Where do you think I live?"
70 |         )
71 |         print(
72 |             f"Guardrail didn't trip - this is unexpected. Output: {json.dumps(result.final_output.model_dump(), indent=2)}"
73 |         )
74 | 
75 |     except OutputGuardrailTripwireTriggered as e:
76 |         print(f"Guardrail tripped. Info: {e.guardrail_result.output.output_info}")
77 | 
78 | 
79 | if __name__ == "__main__":
80 |     asyncio.run(main())
81 | 


--------------------------------------------------------------------------------
/examples/agent_patterns/parallelization.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, ItemHelpers, Runner, trace
 4 | 
 5 | """
 6 | This example shows the parallelization pattern. We run the agent three times in parallel, and pick
 7 | the best result.
 8 | """
 9 | 
10 | spanish_agent = Agent(
11 |     name="spanish_agent",
12 |     instructions="You translate the user's message to Spanish",
13 | )
14 | 
15 | translation_picker = Agent(
16 |     name="translation_picker",
17 |     instructions="You pick the best Spanish translation from the given options.",
18 | )
19 | 
20 | 
21 | async def main():
22 |     msg = input("Hi! Enter a message, and we'll translate it to Spanish.\n\n")
23 | 
24 |     # Ensure the entire workflow is a single trace
25 |     with trace("Parallel translation"):
26 |         res_1, res_2, res_3 = await asyncio.gather(
27 |             Runner.run(
28 |                 spanish_agent,
29 |                 msg,
30 |             ),
31 |             Runner.run(
32 |                 spanish_agent,
33 |                 msg,
34 |             ),
35 |             Runner.run(
36 |                 spanish_agent,
37 |                 msg,
38 |             ),
39 |         )
40 | 
41 |         outputs = [
42 |             ItemHelpers.text_message_outputs(res_1.new_items),
43 |             ItemHelpers.text_message_outputs(res_2.new_items),
44 |             ItemHelpers.text_message_outputs(res_3.new_items),
45 |         ]
46 | 
47 |         translations = "\n\n".join(outputs)
48 |         print(f"\n\nTranslations:\n\n{translations}")
49 | 
50 |         best_translation = await Runner.run(
51 |             translation_picker,
52 |             f"Input: {msg}\n\nTranslations:\n{translations}",
53 |         )
54 | 
55 |     print("\n\n-----")
56 | 
57 |     print(f"Best translation: {best_translation.final_output}")
58 | 
59 | 
60 | if __name__ == "__main__":
61 |     asyncio.run(main())
62 | 


--------------------------------------------------------------------------------
/examples/agent_patterns/routing.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import uuid
 3 | 
 4 | from openai.types.responses import ResponseContentPartDoneEvent, ResponseTextDeltaEvent
 5 | 
 6 | from agents import Agent, RawResponsesStreamEvent, Runner, TResponseInputItem, trace
 7 | 
 8 | """
 9 | This example shows the handoffs/routing pattern. The triage agent receives the first message, and
10 | then hands off to the appropriate agent based on the language of the request. Responses are
11 | streamed to the user.
12 | """
13 | 
14 | french_agent = Agent(
15 |     name="french_agent",
16 |     instructions="You only speak French",
17 | )
18 | 
19 | spanish_agent = Agent(
20 |     name="spanish_agent",
21 |     instructions="You only speak Spanish",
22 | )
23 | 
24 | english_agent = Agent(
25 |     name="english_agent",
26 |     instructions="You only speak English",
27 | )
28 | 
29 | triage_agent = Agent(
30 |     name="triage_agent",
31 |     instructions="Handoff to the appropriate agent based on the language of the request.",
32 |     handoffs=[french_agent, spanish_agent, english_agent],
33 | )
34 | 
35 | 
36 | async def main():
37 |     # We'll create an ID for this conversation, so we can link each trace
38 |     conversation_id = str(uuid.uuid4().hex[:16])
39 | 
40 |     msg = input("Hi! We speak French, Spanish and English. How can I help? ")
41 |     agent = triage_agent
42 |     inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
43 | 
44 |     while True:
45 |         # Each conversation turn is a single trace. Normally, each input from the user would be an
46 |         # API request to your app, and you can wrap the request in a trace()
47 |         with trace("Routing example", group_id=conversation_id):
48 |             result = Runner.run_streamed(
49 |                 agent,
50 |                 input=inputs,
51 |             )
52 |             async for event in result.stream_events():
53 |                 if not isinstance(event, RawResponsesStreamEvent):
54 |                     continue
55 |                 data = event.data
56 |                 if isinstance(data, ResponseTextDeltaEvent):
57 |                     print(data.delta, end="", flush=True)
58 |                 elif isinstance(data, ResponseContentPartDoneEvent):
59 |                     print("\n")
60 | 
61 |         inputs = result.to_input_list()
62 |         print("\n")
63 | 
64 |         user_msg = input("Enter a message: ")
65 |         inputs.append({"content": user_msg, "role": "user"})
66 |         agent = result.current_agent
67 | 
68 | 
69 | if __name__ == "__main__":
70 |     asyncio.run(main())
71 | 


--------------------------------------------------------------------------------
/examples/basic/dynamic_system_prompt.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import random
 3 | from typing import Literal
 4 | 
 5 | from agents import Agent, RunContextWrapper, Runner
 6 | 
 7 | 
 8 | class CustomContext:
 9 |     def __init__(self, style: Literal["haiku", "pirate", "robot"]):
10 |         self.style = style
11 | 
12 | 
13 | def custom_instructions(
14 |     run_context: RunContextWrapper[CustomContext], agent: Agent[CustomContext]
15 | ) -> str:
16 |     context = run_context.context
17 |     if context.style == "haiku":
18 |         return "Only respond in haikus."
19 |     elif context.style == "pirate":
20 |         return "Respond as a pirate."
21 |     else:
22 |         return "Respond as a robot and say 'beep boop' a lot."
23 | 
24 | 
25 | agent = Agent(
26 |     name="Chat agent",
27 |     instructions=custom_instructions,
28 | )
29 | 
30 | 
31 | async def main():
32 |     choice: Literal["haiku", "pirate", "robot"] = random.choice(["haiku", "pirate", "robot"])
33 |     context = CustomContext(style=choice)
34 |     print(f"Using style: {choice}\n")
35 | 
36 |     user_message = "Tell me a joke."
37 |     print(f"User: {user_message}")
38 |     result = await Runner.run(agent, user_message, context=context)
39 | 
40 |     print(f"Assistant: {result.final_output}")
41 | 
42 | 
43 | if __name__ == "__main__":
44 |     asyncio.run(main())
45 | 
46 | """
47 | $ python examples/basic/dynamic_system_prompt.py
48 | 
49 | Using style: haiku
50 | 
51 | User: Tell me a joke.
52 | Assistant: Why don't eggs tell jokes?
53 | They might crack each other's shells,
54 | leaving yolk on face.
55 | 
56 | $ python examples/basic/dynamic_system_prompt.py
57 | Using style: robot
58 | 
59 | User: Tell me a joke.
60 | Assistant: Beep boop! Why was the robot so bad at soccer? Beep boop... because it kept kicking up a debug! Beep boop!
61 | 
62 | $ python examples/basic/dynamic_system_prompt.py
63 | Using style: pirate
64 | 
65 | User: Tell me a joke.
66 | Assistant: Why did the pirate go to school?
67 | 
68 | To improve his arrr-ticulation! Har har har! 🏴‍☠️
69 | """
70 | 


--------------------------------------------------------------------------------
/examples/basic/hello_world.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, Runner
 4 | 
 5 | 
 6 | async def main():
 7 |     agent = Agent(
 8 |         name="Assistant",
 9 |         instructions="You only respond in haikus.",
10 |     )
11 | 
12 |     result = await Runner.run(agent, "Tell me about recursion in programming.")
13 |     print(result.final_output)
14 |     # Function calls itself,
15 |     # Looping in smaller pieces,
16 |     # Endless by design.
17 | 
18 | 
19 | if __name__ == "__main__":
20 |     asyncio.run(main())
21 | 


--------------------------------------------------------------------------------
/examples/basic/stream_items.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import random
 3 | 
 4 | from agents import Agent, ItemHelpers, Runner, function_tool
 5 | 
 6 | 
 7 | @function_tool
 8 | def how_many_jokes() -> int:
 9 |     return random.randint(1, 10)
10 | 
11 | 
12 | async def main():
13 |     agent = Agent(
14 |         name="Joker",
15 |         instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
16 |         tools=[how_many_jokes],
17 |     )
18 | 
19 |     result = Runner.run_streamed(
20 |         agent,
21 |         input="Hello",
22 |     )
23 |     print("=== Run starting ===")
24 |     async for event in result.stream_events():
25 |         # We'll ignore the raw responses event deltas
26 |         if event.type == "raw_response_event":
27 |             continue
28 |         elif event.type == "agent_updated_stream_event":
29 |             print(f"Agent updated: {event.new_agent.name}")
30 |             continue
31 |         elif event.type == "run_item_stream_event":
32 |             if event.item.type == "tool_call_item":
33 |                 print("-- Tool was called")
34 |             elif event.item.type == "tool_call_output_item":
35 |                 print(f"-- Tool output: {event.item.output}")
36 |             elif event.item.type == "message_output_item":
37 |                 print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
38 |             else:
39 |                 pass  # Ignore other event types
40 | 
41 |     print("=== Run complete ===")
42 | 
43 | 
44 | if __name__ == "__main__":
45 |     asyncio.run(main())
46 | 
47 |     # === Run starting ===
48 |     # Agent updated: Joker
49 |     # -- Tool was called
50 |     # -- Tool output: 4
51 |     # -- Message output:
52 |     #  Sure, here are four jokes for you:
53 | 
54 |     # 1. **Why don't skeletons fight each other?**
55 |     #    They don't have the guts!
56 | 
57 |     # 2. **What do you call fake spaghetti?**
58 |     #    An impasta!
59 | 
60 |     # 3. **Why did the scarecrow win an award?**
61 |     #    Because he was outstanding in his field!
62 | 
63 |     # 4. **Why did the bicycle fall over?**
64 |     #    Because it was two-tired!
65 |     # === Run complete ===
66 | 


--------------------------------------------------------------------------------
/examples/basic/stream_text.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from openai.types.responses import ResponseTextDeltaEvent
 4 | 
 5 | from agents import Agent, Runner
 6 | 
 7 | 
 8 | async def main():
 9 |     agent = Agent(
10 |         name="Joker",
11 |         instructions="You are a helpful assistant.",
12 |     )
13 | 
14 |     result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
15 |     async for event in result.stream_events():
16 |         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
17 |             print(event.data.delta, end="", flush=True)
18 | 
19 | 
20 | if __name__ == "__main__":
21 |     asyncio.run(main())
22 | 


--------------------------------------------------------------------------------
/examples/research_bot/README.md:
--------------------------------------------------------------------------------
 1 | # Research bot
 2 | 
 3 | This is a simple example of a multi-agent research bot. To run it:
 4 | 
 5 | ```bash
 6 | python -m examples.research_bot.main
 7 | ```
 8 | 
 9 | ## Architecture
10 | 
11 | The flow is:
12 | 
13 | 1. User enters their research topic
14 | 2. `planner_agent` comes up with a plan to search the web for information. The plan is a list of search queries, with a search term and a reason for each query.
15 | 3. For each search item, we run a `search_agent`, which uses the Web Search tool to search for that term and summarize the results. These all run in parallel.
16 | 4. Finally, the `writer_agent` receives the search summaries, and creates a written report.
17 | 
18 | ## Suggested improvements
19 | 
20 | If you're building your own research bot, some ideas to add to this are:
21 | 
22 | 1. Retrieval: Add support for fetching relevant information from a vector store. You could use the File Search tool for this.
23 | 2. Image and file upload: Allow users to attach PDFs or other files, as baseline context for the research.
24 | 3. More planning and thinking: Models often produce better results given more time to think. Improve the planning process to come up with a better plan, and add an evaluation step so that the model can choose to improve it's results, search for more stuff, etc.
25 | 4. Code execution: Allow running code, which is useful for data analysis.
26 | 


--------------------------------------------------------------------------------
/examples/research_bot/__init__.py:
--------------------------------------------------------------------------------
1 | 
2 | 


--------------------------------------------------------------------------------
/examples/research_bot/agents/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__init__.py


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/__init__.cpython-313.pyc


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/base_agent.cpython-313.pyc


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/planner_agent.cpython-313.pyc


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/research_manager_agent.cpython-313.pyc


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/search_agent.cpython-313.pyc


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/summarization_agent.cpython-313.pyc


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/examples/research_bot/agents/__pycache__/writer_agent.cpython-313.pyc


--------------------------------------------------------------------------------
/examples/research_bot/agents/planner_agent.py:
--------------------------------------------------------------------------------
 1 | from pydantic import BaseModel
 2 | 
 3 | from agents import Agent
 4 | 
 5 | PROMPT = (
 6 |     "You are a helpful research assistant. Given a query, come up with a set of web searches "
 7 |     "to perform to best answer the query. Output between 5 and 20 terms to query for."
 8 | )
 9 | 
10 | 
11 | class WebSearchItem(BaseModel):
12 |     reason: str
13 |     "Your reasoning for why this search is important to the query."
14 | 
15 |     query: str
16 |     "The search term to use for the web search."
17 | 
18 | 
19 | class WebSearchPlan(BaseModel):
20 |     searches: list[WebSearchItem]
21 |     """A list of web searches to perform to best answer the query."""
22 | 
23 | 
24 | planner_agent = Agent(
25 |     name="PlannerAgent",
26 |     instructions=PROMPT,
27 |     model="gpt-4o",
28 |     output_type=WebSearchPlan,
29 | )
30 | 


--------------------------------------------------------------------------------
/examples/research_bot/agents/search_agent.py:
--------------------------------------------------------------------------------
 1 | from agents import Agent, WebSearchTool
 2 | from agents.model_settings import ModelSettings
 3 | 
 4 | INSTRUCTIONS = (
 5 |     "You are a research assistant. Given a search term, you search the web for that term and"
 6 |     "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300"
 7 |     "words. Capture the main points. Write succintly, no need to have complete sentences or good"
 8 |     "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the"
 9 |     "essence and ignore any fluff. Do not include any additional commentary other than the summary"
10 |     "itself."
11 | )
12 | 
13 | search_agent = Agent(
14 |     name="Search agent",
15 |     instructions=INSTRUCTIONS,
16 |     tools=[WebSearchTool()],
17 |     model_settings=ModelSettings(tool_choice="required"),
18 | )
19 | 


--------------------------------------------------------------------------------
/examples/research_bot/agents/writer_agent.py:
--------------------------------------------------------------------------------
 1 | # Agent used to synthesize a final report from the individual summaries.
 2 | from pydantic import BaseModel
 3 | 
 4 | from agents import Agent
 5 | 
 6 | PROMPT = (
 7 |     "You are a senior researcher tasked with writing a cohesive report for a research query. "
 8 |     "You will be provided with the original query, and some initial research done by a research "
 9 |     "assistant.\n"
10 |     "You should first come up with an outline for the report that describes the structure and "
11 |     "flow of the report. Then, generate the report and return that as your final output.\n"
12 |     "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
13 |     "for 5-10 pages of content, at least 1000 words."
14 | )
15 | 
16 | 
17 | class ReportData(BaseModel):
18 |     short_summary: str
19 |     """A short 2-3 sentence summary of the findings."""
20 | 
21 |     markdown_report: str
22 |     """The final report"""
23 | 
24 |     follow_up_questions: list[str]
25 |     """Suggested topics to research further"""
26 | 
27 | 
28 | writer_agent = Agent(
29 |     name="WriterAgent",
30 |     instructions=PROMPT,
31 |     model="o3-mini",
32 |     output_type=ReportData,
33 | )
34 | 


--------------------------------------------------------------------------------
/examples/research_bot/main.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from .manager import ResearchManager
 4 | 
 5 | 
 6 | async def main() -> None:
 7 |     query = input("What would you like to research? ")
 8 |     await ResearchManager().run(query)
 9 | 
10 | 
11 | if __name__ == "__main__":
12 |     asyncio.run(main())
13 | 


--------------------------------------------------------------------------------
/examples/research_bot/printer.py:
--------------------------------------------------------------------------------
 1 | from typing import Any
 2 | 
 3 | from rich.console import Console, Group
 4 | from rich.live import Live
 5 | from rich.spinner import Spinner
 6 | 
 7 | 
 8 | class Printer:
 9 |     def __init__(self, console: Console):
10 |         self.live = Live(console=console)
11 |         self.items: dict[str, tuple[str, bool]] = {}
12 |         self.hide_done_ids: set[str] = set()
13 |         self.live.start()
14 | 
15 |     def end(self) -> None:
16 |         self.live.stop()
17 | 
18 |     def hide_done_checkmark(self, item_id: str) -> None:
19 |         self.hide_done_ids.add(item_id)
20 | 
21 |     def update_item(
22 |         self, item_id: str, content: str, is_done: bool = False, hide_checkmark: bool = False
23 |     ) -> None:
24 |         self.items[item_id] = (content, is_done)
25 |         if hide_checkmark:
26 |             self.hide_done_ids.add(item_id)
27 |         self.flush()
28 | 
29 |     def mark_item_done(self, item_id: str) -> None:
30 |         self.items[item_id] = (self.items[item_id][0], True)
31 |         self.flush()
32 | 
33 |     def flush(self) -> None:
34 |         renderables: list[Any] = []
35 |         for item_id, (content, is_done) in self.items.items():
36 |             if is_done:
37 |                 prefix = "✅ " if item_id not in self.hide_done_ids else ""
38 |                 renderables.append(prefix + content)
39 |             else:
40 |                 renderables.append(Spinner("dots", text=content))
41 |         self.live.update(Group(*renderables))
42 | 


--------------------------------------------------------------------------------
/examples/tools/file_search.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, FileSearchTool, Runner, trace
 4 | 
 5 | 
 6 | async def main():
 7 |     agent = Agent(
 8 |         name="File searcher",
 9 |         instructions="You are a helpful agent.",
10 |         tools=[
11 |             FileSearchTool(
12 |                 max_num_results=3,
13 |                 vector_store_ids=["vs_67bf88953f748191be42b462090e53e7"],
14 |                 include_search_results=True,
15 |             )
16 |         ],
17 |     )
18 | 
19 |     with trace("File search example"):
20 |         result = await Runner.run(
21 |             agent, "Be concise, and tell me 1 sentence about Arrakis I might not know."
22 |         )
23 |         print(result.final_output)
24 |         """
25 |         Arrakis, the desert planet in Frank Herbert's "Dune," was inspired by the scarcity of water
26 |         as a metaphor for oil and other finite resources.
27 |         """
28 | 
29 |         print("\n".join([str(out) for out in result.new_items]))
30 |         """
31 |         {"id":"...", "queries":["Arrakis"], "results":[...]}
32 |         """
33 | 
34 | 
35 | if __name__ == "__main__":
36 |     asyncio.run(main())
37 | 


--------------------------------------------------------------------------------
/examples/tools/web_search.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, Runner, WebSearchTool, trace
 4 | 
 5 | 
 6 | async def main():
 7 |     agent = Agent(
 8 |         name="Web searcher",
 9 |         instructions="You are a helpful agent.",
10 |         tools=[WebSearchTool(user_location={"type": "approximate", "city": "New York"})],
11 |     )
12 | 
13 |     with trace("Web search example"):
14 |         result = await Runner.run(
15 |             agent,
16 |             "search the web for 'local sports news' and give me 1 interesting update in a sentence.",
17 |         )
18 |         print(result.final_output)
19 |         # The New York Giants are reportedly pursuing quarterback Aaron Rodgers after his ...
20 | 
21 | 
22 | if __name__ == "__main__":
23 |     asyncio.run(main())
24 | 


--------------------------------------------------------------------------------
/pyproject.toml:
--------------------------------------------------------------------------------
  1 | [project]
  2 | name = "openai-agents"
  3 | version = "0.0.2"
  4 | description = "OpenAI Agents SDK"
  5 | readme = "README.md"
  6 | requires-python = ">=3.9"
  7 | license = "MIT"
  8 | authors = [
  9 |     { name = "OpenAI", email = "support@openai.com" },
 10 | ]
 11 | dependencies = [
 12 |     "openai>=1.66.0",
 13 |     "pydantic>=2.10, <3",
 14 |     "griffe>=1.5.6, <2",
 15 |     "typing-extensions>=4.12.2, <5",
 16 |     "requests>=2.0, <3",
 17 |     "types-requests>=2.0, <3",
 18 | ]
 19 | classifiers = [
 20 |     "Typing :: Typed",
 21 |     "Intended Audience :: Developers",
 22 |     "Programming Language :: Python :: 3",
 23 |     "Programming Language :: Python :: 3.9",
 24 |     "Programming Language :: Python :: 3.10",
 25 |     "Programming Language :: Python :: 3.11",
 26 |     "Programming Language :: Python :: 3.12",
 27 |     "Intended Audience :: Developers",
 28 |     "Operating System :: OS Independent",
 29 |     "Topic :: Software Development :: Libraries :: Python Modules",
 30 |     "License :: OSI Approved :: MIT License"
 31 | ]
 32 | 
 33 | [project.urls]
 34 | Homepage = "https://github.com/openai/openai-agents-python"
 35 | Repository = "https://github.com/openai/openai-agents-python"
 36 | 
 37 | [dependency-groups]
 38 | dev = [
 39 |     "mypy",
 40 |     "ruff==0.9.2",
 41 |     "pytest",
 42 |     "pytest-asyncio",
 43 |     "pytest-mock>=3.14.0",
 44 |     "rich",
 45 |     "mkdocs>=1.6.0",
 46 |     "mkdocs-material>=9.6.0",
 47 |     "mkdocstrings[python]>=0.28.0",
 48 |     "coverage>=7.6.12",
 49 |     "playwright==1.50.0",
 50 | ]
 51 | [tool.uv.workspace]
 52 | members = ["agents"]
 53 | 
 54 | [tool.uv.sources]
 55 | agents = { workspace = true }
 56 | 
 57 | [build-system]
 58 | requires = ["hatchling"]
 59 | build-backend = "hatchling.build"
 60 | 
 61 | [tool.hatch.build.targets.wheel]
 62 | packages = ["src/agents"]
 63 | 
 64 | 
 65 | [tool.ruff]
 66 | line-length = 100
 67 | target-version = "py39"
 68 | 
 69 | [tool.ruff.lint]
 70 | select = [
 71 |     "E",  # pycodestyle errors
 72 |     "W",  # pycodestyle warnings
 73 |     "F",  # pyflakes
 74 |     "I",  # isort
 75 |     "B",  # flake8-bugbear
 76 |     "C4",  # flake8-comprehensions
 77 |     "UP",  # pyupgrade
 78 | ]
 79 | isort = { combine-as-imports = true, known-first-party = ["agents"] }
 80 | 
 81 | [tool.ruff.lint.pydocstyle]
 82 | convention = "google"
 83 | 
 84 | [tool.ruff.lint.per-file-ignores]
 85 | "examples/**/*.py" = ["E501"]
 86 | 
 87 | [tool.mypy]
 88 | strict = true
 89 | disallow_incomplete_defs = false
 90 | disallow_untyped_defs = false
 91 | disallow_untyped_calls = false
 92 | 
 93 | [tool.coverage.run]
 94 | source = [
 95 |     "tests",
 96 |     "src/agents",
 97 | ]
 98 | 
 99 | [tool.coverage.report]
100 | show_missing = true
101 | sort = "-Cover"
102 | exclude_also = [
103 |     # This is only executed while typechecking
104 |     "if TYPE_CHECKING:",
105 |     "@abc.abstractmethod",
106 |     "raise NotImplementedError",
107 |     "logger.debug",
108 | ]
109 | 
110 | [tool.pytest.ini_options]
111 | asyncio_mode = "auto"  
112 | asyncio_default_fixture_loop_scope = "session"
113 | filterwarnings = [
114 |     # This is a warning that is expected to happen: we have an async filter that raises an exception
115 |     "ignore:coroutine 'test_async_input_filter_fails.<locals>.invalid_input_filter' was never awaited:RuntimeWarning",
116 | ]
117 | markers = [
118 |     "allow_call_model_methods: mark test as allowing calls to real model implementations",
119 | ]


--------------------------------------------------------------------------------
/src/agents/_config.py:
--------------------------------------------------------------------------------
 1 | from openai import AsyncOpenAI
 2 | from typing_extensions import Literal
 3 | 
 4 | from .models import _openai_shared
 5 | from .tracing import set_tracing_export_api_key
 6 | 
 7 | 
 8 | def set_default_openai_key(key: str) -> None:
 9 |     set_tracing_export_api_key(key)
10 |     _openai_shared.set_default_openai_key(key)
11 | 
12 | 
13 | def set_default_openai_client(client: AsyncOpenAI, use_for_tracing: bool) -> None:
14 |     if use_for_tracing:
15 |         set_tracing_export_api_key(client.api_key)
16 |     _openai_shared.set_default_openai_client(client)
17 | 
18 | 
19 | def set_default_openai_api(api: Literal["chat_completions", "responses"]) -> None:
20 |     if api == "chat_completions":
21 |         _openai_shared.set_use_responses_by_default(False)
22 |     else:
23 |         _openai_shared.set_use_responses_by_default(True)
24 | 


--------------------------------------------------------------------------------
/src/agents/_debug.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | 
 3 | 
 4 | def _debug_flag_enabled(flag: str) -> bool:
 5 |     flag_value = os.getenv(flag)
 6 |     return flag_value is not None and (flag_value == "1" or flag_value.lower() == "true")
 7 | 
 8 | 
 9 | DONT_LOG_MODEL_DATA = _debug_flag_enabled("OPENAI_AGENTS_DONT_LOG_MODEL_DATA")
10 | """By default we don't log LLM inputs/outputs, to prevent exposing sensitive information. Set this
11 | flag to enable logging them.
12 | """
13 | 
14 | DONT_LOG_TOOL_DATA = _debug_flag_enabled("OPENAI_AGENTS_DONT_LOG_TOOL_DATA")
15 | """By default we don't log tool call inputs/outputs, to prevent exposing sensitive information. Set
16 | this flag to enable logging them.
17 | """
18 | 


--------------------------------------------------------------------------------
/src/agents/_utils.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import re
 4 | from collections.abc import Awaitable
 5 | from typing import Any, Literal, Union
 6 | 
 7 | from pydantic import TypeAdapter, ValidationError
 8 | from typing_extensions import TypeVar
 9 | 
10 | from .exceptions import ModelBehaviorError
11 | from .logger import logger
12 | from .tracing import Span, SpanError, get_current_span
13 | 
14 | T = TypeVar("T")
15 | 
16 | MaybeAwaitable = Union[Awaitable[T], T]
17 | 
18 | 
19 | def transform_string_function_style(name: str) -> str:
20 |     # Replace spaces with underscores
21 |     name = name.replace(" ", "_")
22 | 
23 |     # Replace non-alphanumeric characters with underscores
24 |     name = re.sub(r"[^a-zA-Z0-9]", "_", name)
25 | 
26 |     return name.lower()
27 | 
28 | 
29 | def validate_json(json_str: str, type_adapter: TypeAdapter[T], partial: bool) -> T:
30 |     partial_setting: bool | Literal["off", "on", "trailing-strings"] = (
31 |         "trailing-strings" if partial else False
32 |     )
33 |     try:
34 |         validated = type_adapter.validate_json(json_str, experimental_allow_partial=partial_setting)
35 |         return validated
36 |     except ValidationError as e:
37 |         attach_error_to_current_span(
38 |             SpanError(
39 |                 message="Invalid JSON provided",
40 |                 data={},
41 |             )
42 |         )
43 |         raise ModelBehaviorError(
44 |             f"Invalid JSON when parsing {json_str} for {type_adapter}; {e}"
45 |         ) from e
46 | 
47 | 
48 | def attach_error_to_span(span: Span[Any], error: SpanError) -> None:
49 |     span.set_error(error)
50 | 
51 | 
52 | def attach_error_to_current_span(error: SpanError) -> None:
53 |     span = get_current_span()
54 |     if span:
55 |         attach_error_to_span(span, error)
56 |     else:
57 |         logger.warning(f"No span to add error {error} to")
58 | 
59 | 
60 | async def noop_coroutine() -> None:
61 |     pass
62 | 


--------------------------------------------------------------------------------
/src/agents/computer.py:
--------------------------------------------------------------------------------
  1 | import abc
  2 | from typing import Literal
  3 | 
  4 | Environment = Literal["mac", "windows", "ubuntu", "browser"]
  5 | Button = Literal["left", "right", "wheel", "back", "forward"]
  6 | 
  7 | 
  8 | class Computer(abc.ABC):
  9 |     """A computer implemented with sync operations. The Computer interface abstracts the
 10 |     operations needed to control a computer or browser."""
 11 | 
 12 |     @property
 13 |     @abc.abstractmethod
 14 |     def environment(self) -> Environment:
 15 |         pass
 16 | 
 17 |     @property
 18 |     @abc.abstractmethod
 19 |     def dimensions(self) -> tuple[int, int]:
 20 |         pass
 21 | 
 22 |     @abc.abstractmethod
 23 |     def screenshot(self) -> str:
 24 |         pass
 25 | 
 26 |     @abc.abstractmethod
 27 |     def click(self, x: int, y: int, button: Button) -> None:
 28 |         pass
 29 | 
 30 |     @abc.abstractmethod
 31 |     def double_click(self, x: int, y: int) -> None:
 32 |         pass
 33 | 
 34 |     @abc.abstractmethod
 35 |     def scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
 36 |         pass
 37 | 
 38 |     @abc.abstractmethod
 39 |     def type(self, text: str) -> None:
 40 |         pass
 41 | 
 42 |     @abc.abstractmethod
 43 |     def wait(self) -> None:
 44 |         pass
 45 | 
 46 |     @abc.abstractmethod
 47 |     def move(self, x: int, y: int) -> None:
 48 |         pass
 49 | 
 50 |     @abc.abstractmethod
 51 |     def keypress(self, keys: list[str]) -> None:
 52 |         pass
 53 | 
 54 |     @abc.abstractmethod
 55 |     def drag(self, path: list[tuple[int, int]]) -> None:
 56 |         pass
 57 | 
 58 | 
 59 | class AsyncComputer(abc.ABC):
 60 |     """A computer implemented with async operations. The Computer interface abstracts the
 61 |     operations needed to control a computer or browser."""
 62 | 
 63 |     @property
 64 |     @abc.abstractmethod
 65 |     def environment(self) -> Environment:
 66 |         pass
 67 | 
 68 |     @property
 69 |     @abc.abstractmethod
 70 |     def dimensions(self) -> tuple[int, int]:
 71 |         pass
 72 | 
 73 |     @abc.abstractmethod
 74 |     async def screenshot(self) -> str:
 75 |         pass
 76 | 
 77 |     @abc.abstractmethod
 78 |     async def click(self, x: int, y: int, button: Button) -> None:
 79 |         pass
 80 | 
 81 |     @abc.abstractmethod
 82 |     async def double_click(self, x: int, y: int) -> None:
 83 |         pass
 84 | 
 85 |     @abc.abstractmethod
 86 |     async def scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
 87 |         pass
 88 | 
 89 |     @abc.abstractmethod
 90 |     async def type(self, text: str) -> None:
 91 |         pass
 92 | 
 93 |     @abc.abstractmethod
 94 |     async def wait(self) -> None:
 95 |         pass
 96 | 
 97 |     @abc.abstractmethod
 98 |     async def move(self, x: int, y: int) -> None:
 99 |         pass
100 | 
101 |     @abc.abstractmethod
102 |     async def keypress(self, keys: list[str]) -> None:
103 |         pass
104 | 
105 |     @abc.abstractmethod
106 |     async def drag(self, path: list[tuple[int, int]]) -> None:
107 |         pass
108 | 


--------------------------------------------------------------------------------
/src/agents/exceptions.py:
--------------------------------------------------------------------------------
 1 | from typing import TYPE_CHECKING
 2 | 
 3 | if TYPE_CHECKING:
 4 |     from .guardrail import InputGuardrailResult, OutputGuardrailResult
 5 | 
 6 | 
 7 | class AgentsException(Exception):
 8 |     """Base class for all exceptions in the Agents SDK."""
 9 | 
10 | 
11 | class MaxTurnsExceeded(AgentsException):
12 |     """Exception raised when the maximum number of turns is exceeded."""
13 | 
14 |     message: str
15 | 
16 |     def __init__(self, message: str):
17 |         self.message = message
18 | 
19 | 
20 | class ModelBehaviorError(AgentsException):
21 |     """Exception raised when the model does something unexpected, e.g. calling a tool that doesn't
22 |     exist, or providing malformed JSON.
23 |     """
24 | 
25 |     message: str
26 | 
27 |     def __init__(self, message: str):
28 |         self.message = message
29 | 
30 | 
31 | class UserError(AgentsException):
32 |     """Exception raised when the user makes an error using the SDK."""
33 | 
34 |     message: str
35 | 
36 |     def __init__(self, message: str):
37 |         self.message = message
38 | 
39 | 
40 | class InputGuardrailTripwireTriggered(AgentsException):
41 |     """Exception raised when a guardrail tripwire is triggered."""
42 | 
43 |     guardrail_result: "InputGuardrailResult"
44 |     """The result data of the guardrail that was triggered."""
45 | 
46 |     def __init__(self, guardrail_result: "InputGuardrailResult"):
47 |         self.guardrail_result = guardrail_result
48 |         super().__init__(
49 |             f"Guardrail {guardrail_result.guardrail.__class__.__name__} triggered tripwire"
50 |         )
51 | 
52 | 
53 | class OutputGuardrailTripwireTriggered(AgentsException):
54 |     """Exception raised when a guardrail tripwire is triggered."""
55 | 
56 |     guardrail_result: "OutputGuardrailResult"
57 |     """The result data of the guardrail that was triggered."""
58 | 
59 |     def __init__(self, guardrail_result: "OutputGuardrailResult"):
60 |         self.guardrail_result = guardrail_result
61 |         super().__init__(
62 |             f"Guardrail {guardrail_result.guardrail.__class__.__name__} triggered tripwire"
63 |         )
64 | 


--------------------------------------------------------------------------------
/src/agents/extensions/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/src/agents/extensions/__init__.py


--------------------------------------------------------------------------------
/src/agents/extensions/handoff_filters.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from ..handoffs import HandoffInputData
 4 | from ..items import (
 5 |     HandoffCallItem,
 6 |     HandoffOutputItem,
 7 |     RunItem,
 8 |     ToolCallItem,
 9 |     ToolCallOutputItem,
10 |     TResponseInputItem,
11 | )
12 | 
13 | """Contains common handoff input filters, for convenience. """
14 | 
15 | 
16 | def remove_all_tools(handoff_input_data: HandoffInputData) -> HandoffInputData:
17 |     """Filters out all tool items: file search, web search and function calls+output."""
18 | 
19 |     history = handoff_input_data.input_history
20 |     new_items = handoff_input_data.new_items
21 | 
22 |     filtered_history = (
23 |         _remove_tool_types_from_input(history) if isinstance(history, tuple) else history
24 |     )
25 |     filtered_pre_handoff_items = _remove_tools_from_items(handoff_input_data.pre_handoff_items)
26 |     filtered_new_items = _remove_tools_from_items(new_items)
27 | 
28 |     return HandoffInputData(
29 |         input_history=filtered_history,
30 |         pre_handoff_items=filtered_pre_handoff_items,
31 |         new_items=filtered_new_items,
32 |     )
33 | 
34 | 
35 | def _remove_tools_from_items(items: tuple[RunItem, ...]) -> tuple[RunItem, ...]:
36 |     filtered_items = []
37 |     for item in items:
38 |         if (
39 |             isinstance(item, HandoffCallItem)
40 |             or isinstance(item, HandoffOutputItem)
41 |             or isinstance(item, ToolCallItem)
42 |             or isinstance(item, ToolCallOutputItem)
43 |         ):
44 |             continue
45 |         filtered_items.append(item)
46 |     return tuple(filtered_items)
47 | 
48 | 
49 | def _remove_tool_types_from_input(
50 |     items: tuple[TResponseInputItem, ...],
51 | ) -> tuple[TResponseInputItem, ...]:
52 |     tool_types = [
53 |         "function_call",
54 |         "function_call_output",
55 |         "computer_call",
56 |         "computer_call_output",
57 |         "file_search_call",
58 |         "web_search_call",
59 |     ]
60 | 
61 |     filtered_items: list[TResponseInputItem] = []
62 |     for item in items:
63 |         itype = item.get("type")
64 |         if itype in tool_types:
65 |             continue
66 |         filtered_items.append(item)
67 |     return tuple(filtered_items)
68 | 


--------------------------------------------------------------------------------
/src/agents/extensions/handoff_prompt.py:
--------------------------------------------------------------------------------
 1 | # A recommended prompt prefix for agents that use handoffs. We recommend including this or
 2 | # similar instructions in any agents that use handoffs.
 3 | RECOMMENDED_PROMPT_PREFIX = (
 4 |     "# System context\n"
 5 |     "You are part of a multi-agent system called the Agents SDK, designed to make agent "
 6 |     "coordination and execution easy. Agents uses two primary abstraction: **Agents** and "
 7 |     "**Handoffs**. An agent encompasses instructions and tools and can hand off a "
 8 |     "conversation to another agent when appropriate. "
 9 |     "Handoffs are achieved by calling a handoff function, generally named "
10 |     "`transfer_to_<agent_name>`. Transfers between agents are handled seamlessly in the background;"
11 |     " do not mention or draw attention to these transfers in your conversation with the user.\n"
12 | )
13 | 
14 | 
15 | def prompt_with_handoff_instructions(prompt: str) -> str:
16 |     """
17 |     Add recommended instructions to the prompt for agents that use handoffs.
18 |     """
19 |     return f"{RECOMMENDED_PROMPT_PREFIX}\n\n{prompt}"
20 | 


--------------------------------------------------------------------------------
/src/agents/lifecycle.py:
--------------------------------------------------------------------------------
  1 | from typing import Any, Generic
  2 | 
  3 | from .agent import Agent
  4 | from .run_context import RunContextWrapper, TContext
  5 | from .tool import Tool
  6 | 
  7 | 
  8 | class RunHooks(Generic[TContext]):
  9 |     """A class that receives callbacks on various lifecycle events in an agent run. Subclass and
 10 |     override the methods you need.
 11 |     """
 12 | 
 13 |     async def on_agent_start(
 14 |         self, context: RunContextWrapper[TContext], agent: Agent[TContext]
 15 |     ) -> None:
 16 |         """Called before the agent is invoked. Called each time the current agent changes."""
 17 |         pass
 18 | 
 19 |     async def on_agent_end(
 20 |         self,
 21 |         context: RunContextWrapper[TContext],
 22 |         agent: Agent[TContext],
 23 |         output: Any,
 24 |     ) -> None:
 25 |         """Called when the agent produces a final output."""
 26 |         pass
 27 | 
 28 |     async def on_handoff(
 29 |         self,
 30 |         context: RunContextWrapper[TContext],
 31 |         from_agent: Agent[TContext],
 32 |         to_agent: Agent[TContext],
 33 |     ) -> None:
 34 |         """Called when a handoff occurs."""
 35 |         pass
 36 | 
 37 |     async def on_tool_start(
 38 |         self,
 39 |         context: RunContextWrapper[TContext],
 40 |         agent: Agent[TContext],
 41 |         tool: Tool,
 42 |     ) -> None:
 43 |         """Called before a tool is invoked."""
 44 |         pass
 45 | 
 46 |     async def on_tool_end(
 47 |         self,
 48 |         context: RunContextWrapper[TContext],
 49 |         agent: Agent[TContext],
 50 |         tool: Tool,
 51 |         result: str,
 52 |     ) -> None:
 53 |         """Called after a tool is invoked."""
 54 |         pass
 55 | 
 56 | 
 57 | class AgentHooks(Generic[TContext]):
 58 |     """A class that receives callbacks on various lifecycle events for a specific agent. You can
 59 |     set this on `agent.hooks` to receive events for that specific agent.
 60 | 
 61 |     Subclass and override the methods you need.
 62 |     """
 63 | 
 64 |     async def on_start(self, context: RunContextWrapper[TContext], agent: Agent[TContext]) -> None:
 65 |         """Called before the agent is invoked. Called each time the running agent is changed to this
 66 |         agent."""
 67 |         pass
 68 | 
 69 |     async def on_end(
 70 |         self,
 71 |         context: RunContextWrapper[TContext],
 72 |         agent: Agent[TContext],
 73 |         output: Any,
 74 |     ) -> None:
 75 |         """Called when the agent produces a final output."""
 76 |         pass
 77 | 
 78 |     async def on_handoff(
 79 |         self,
 80 |         context: RunContextWrapper[TContext],
 81 |         agent: Agent[TContext],
 82 |         source: Agent[TContext],
 83 |     ) -> None:
 84 |         """Called when the agent is being handed off to. The `source` is the agent that is handing
 85 |         off to this agent."""
 86 |         pass
 87 | 
 88 |     async def on_tool_start(
 89 |         self,
 90 |         context: RunContextWrapper[TContext],
 91 |         agent: Agent[TContext],
 92 |         tool: Tool,
 93 |     ) -> None:
 94 |         """Called before a tool is invoked."""
 95 |         pass
 96 | 
 97 |     async def on_tool_end(
 98 |         self,
 99 |         context: RunContextWrapper[TContext],
100 |         agent: Agent[TContext],
101 |         tool: Tool,
102 |         result: str,
103 |     ) -> None:
104 |         """Called after a tool is invoked."""
105 |         pass
106 | 


--------------------------------------------------------------------------------
/src/agents/logger.py:
--------------------------------------------------------------------------------
1 | import logging
2 | 
3 | logger = logging.getLogger("openai.agents")
4 | 


--------------------------------------------------------------------------------
/src/agents/model_settings.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from dataclasses import dataclass
 4 | from typing import Literal
 5 | 
 6 | 
 7 | @dataclass
 8 | class ModelSettings:
 9 |     """Settings to use when calling an LLM.
10 | 
11 |     This class holds optional model configuration parameters (e.g. temperature,
12 |     top_p, penalties, truncation, etc.).
13 |     """
14 |     temperature: float | None = None
15 |     top_p: float | None = None
16 |     frequency_penalty: float | None = None
17 |     presence_penalty: float | None = None
18 |     tool_choice: Literal["auto", "required", "none"] | str | None = None
19 |     parallel_tool_calls: bool | None = False
20 |     truncation: Literal["auto", "disabled"] | None = None
21 | 
22 |     def resolve(self, override: ModelSettings | None) -> ModelSettings:
23 |         """Produce a new ModelSettings by overlaying any non-None values from the
24 |         override on top of this instance."""
25 |         if override is None:
26 |             return self
27 |         return ModelSettings(
28 |             temperature=override.temperature or self.temperature,
29 |             top_p=override.top_p or self.top_p,
30 |             frequency_penalty=override.frequency_penalty or self.frequency_penalty,
31 |             presence_penalty=override.presence_penalty or self.presence_penalty,
32 |             tool_choice=override.tool_choice or self.tool_choice,
33 |             parallel_tool_calls=override.parallel_tool_calls or self.parallel_tool_calls,
34 |             truncation=override.truncation or self.truncation,
35 |         )
36 | 


--------------------------------------------------------------------------------
/src/agents/models/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/src/agents/models/__init__.py


--------------------------------------------------------------------------------
/src/agents/models/_openai_shared.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from openai import AsyncOpenAI
 4 | 
 5 | _default_openai_key: str | None = None
 6 | _default_openai_client: AsyncOpenAI | None = None
 7 | _use_responses_by_default: bool = True
 8 | 
 9 | 
10 | def set_default_openai_key(key: str) -> None:
11 |     global _default_openai_key
12 |     _default_openai_key = key
13 | 
14 | 
15 | def get_default_openai_key() -> str | None:
16 |     return _default_openai_key
17 | 
18 | 
19 | def set_default_openai_client(client: AsyncOpenAI) -> None:
20 |     global _default_openai_client
21 |     _default_openai_client = client
22 | 
23 | 
24 | def get_default_openai_client() -> AsyncOpenAI | None:
25 |     return _default_openai_client
26 | 
27 | 
28 | def set_use_responses_by_default(use_responses: bool) -> None:
29 |     global _use_responses_by_default
30 |     _use_responses_by_default = use_responses
31 | 
32 | 
33 | def get_use_responses_by_default() -> bool:
34 |     return _use_responses_by_default
35 | 


--------------------------------------------------------------------------------
/src/agents/models/fake_id.py:
--------------------------------------------------------------------------------
1 | FAKE_RESPONSES_ID = "__fake_id__"
2 | """This is a placeholder ID used to fill in the `id` field in Responses API related objects. It's
3 | useful when you're creating Responses objects from non-Responses APIs, e.g. the OpenAI Chat
4 | Completions API or other LLM providers.
5 | """
6 | 


--------------------------------------------------------------------------------
/src/agents/models/openai_provider.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import httpx
 4 | from openai import AsyncOpenAI, DefaultAsyncHttpxClient
 5 | 
 6 | from . import _openai_shared
 7 | from .interface import Model, ModelProvider
 8 | from .openai_chatcompletions import OpenAIChatCompletionsModel
 9 | from .openai_responses import OpenAIResponsesModel
10 | 
11 | DEFAULT_MODEL: str = "gpt-4o"
12 | 
13 | 
14 | _http_client: httpx.AsyncClient | None = None
15 | 
16 | 
17 | # If we create a new httpx client for each request, that would mean no sharing of connection pools,
18 | # which would mean worse latency and resource usage. So, we share the client across requests.
19 | def shared_http_client() -> httpx.AsyncClient:
20 |     global _http_client
21 |     if _http_client is None:
22 |         _http_client = DefaultAsyncHttpxClient()
23 |     return _http_client
24 | 
25 | 
26 | class OpenAIProvider(ModelProvider):
27 |     def __init__(
28 |         self,
29 |         *,
30 |         api_key: str | None = None,
31 |         base_url: str | None = None,
32 |         openai_client: AsyncOpenAI | None = None,
33 |         organization: str | None = None,
34 |         project: str | None = None,
35 |         use_responses: bool | None = None,
36 |     ) -> None:
37 |         if openai_client is not None:
38 |             assert api_key is None and base_url is None, (
39 |                 "Don't provide api_key or base_url if you provide openai_client"
40 |             )
41 |             self._client = openai_client
42 |         else:
43 |             self._client = _openai_shared.get_default_openai_client() or AsyncOpenAI(
44 |                 api_key=api_key or _openai_shared.get_default_openai_key(),
45 |                 base_url=base_url,
46 |                 organization=organization,
47 |                 project=project,
48 |                 http_client=shared_http_client(),
49 |             )
50 | 
51 |         self._is_openai_model = self._client.base_url.host.startswith("api.openai.com")
52 |         if use_responses is not None:
53 |             self._use_responses = use_responses
54 |         else:
55 |             self._use_responses = _openai_shared.get_use_responses_by_default()
56 | 
57 |     def get_model(self, model_name: str | None) -> Model:
58 |         if model_name is None:
59 |             model_name = DEFAULT_MODEL
60 | 
61 |         return (
62 |             OpenAIResponsesModel(model=model_name, openai_client=self._client)
63 |             if self._use_responses
64 |             else OpenAIChatCompletionsModel(model=model_name, openai_client=self._client)
65 |         )
66 | 


--------------------------------------------------------------------------------
/src/agents/run_context.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass, field
 2 | from typing import Any, Generic
 3 | 
 4 | from typing_extensions import TypeVar
 5 | 
 6 | from .usage import Usage
 7 | 
 8 | TContext = TypeVar("TContext", default=Any)
 9 | 
10 | 
11 | @dataclass
12 | class RunContextWrapper(Generic[TContext]):
13 |     """This wraps the context object that you passed to `Runner.run()`. It also contains
14 |     information about the usage of the agent run so far.
15 | 
16 |     NOTE: Contexts are not passed to the LLM. They're a way to pass dependencies and data to code
17 |     you implement, like tool functions, callbacks, hooks, etc.
18 |     """
19 | 
20 |     context: TContext
21 |     """The context object (or None), passed by you to `Runner.run()`"""
22 | 
23 |     usage: Usage = field(default_factory=Usage)
24 |     """The usage of the agent run so far. For streamed responses, the usage will be stale until the
25 |     last chunk of the stream is processed.
26 |     """
27 | 


--------------------------------------------------------------------------------
/src/agents/stream_events.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from dataclasses import dataclass
 4 | from typing import Any, Literal, Union
 5 | 
 6 | from typing_extensions import TypeAlias
 7 | 
 8 | from .agent import Agent
 9 | from .items import RunItem, TResponseStreamEvent
10 | 
11 | 
12 | @dataclass
13 | class RawResponsesStreamEvent:
14 |     """Streaming event from the LLM. These are 'raw' events, i.e. they are directly passed through
15 |     from the LLM.
16 |     """
17 | 
18 |     data: TResponseStreamEvent
19 |     """The raw responses streaming event from the LLM."""
20 | 
21 |     type: Literal["raw_response_event"] = "raw_response_event"
22 |     """The type of the event."""
23 | 
24 | 
25 | @dataclass
26 | class RunItemStreamEvent:
27 |     """Streaming events that wrap a `RunItem`. As the agent processes the LLM response, it will
28 |     generate these events for new messages, tool calls, tool outputs, handoffs, etc.
29 |     """
30 | 
31 |     name: Literal[
32 |         "message_output_created",
33 |         "handoff_requested",
34 |         "handoff_occured",
35 |         "tool_called",
36 |         "tool_output",
37 |         "reasoning_item_created",
38 |     ]
39 |     """The name of the event."""
40 | 
41 |     item: RunItem
42 |     """The item that was created."""
43 | 
44 |     type: Literal["run_item_stream_event"] = "run_item_stream_event"
45 | 
46 | 
47 | @dataclass
48 | class AgentUpdatedStreamEvent:
49 |     """Event that notifies that there is a new agent running."""
50 | 
51 |     new_agent: Agent[Any]
52 |     """The new agent."""
53 | 
54 |     type: Literal["agent_updated_stream_event"] = "agent_updated_stream_event"
55 | 
56 | 
57 | StreamEvent: TypeAlias = Union[RawResponsesStreamEvent, RunItemStreamEvent, AgentUpdatedStreamEvent]
58 | """A streaming event from an agent."""
59 | 


--------------------------------------------------------------------------------
/src/agents/tracing/__init__.py:
--------------------------------------------------------------------------------
 1 | import atexit
 2 | 
 3 | from .create import (
 4 |     agent_span,
 5 |     custom_span,
 6 |     function_span,
 7 |     generation_span,
 8 |     get_current_span,
 9 |     get_current_trace,
10 |     guardrail_span,
11 |     handoff_span,
12 |     response_span,
13 |     trace,
14 | )
15 | from .processor_interface import TracingProcessor
16 | from .processors import default_exporter, default_processor
17 | from .setup import GLOBAL_TRACE_PROVIDER
18 | from .span_data import (
19 |     AgentSpanData,
20 |     CustomSpanData,
21 |     FunctionSpanData,
22 |     GenerationSpanData,
23 |     GuardrailSpanData,
24 |     HandoffSpanData,
25 |     ResponseSpanData,
26 |     SpanData,
27 | )
28 | from .spans import Span, SpanError
29 | from .traces import Trace
30 | from .util import gen_span_id, gen_trace_id
31 | 
32 | __all__ = [
33 |     "add_trace_processor",
34 |     "agent_span",
35 |     "custom_span",
36 |     "function_span",
37 |     "generation_span",
38 |     "get_current_span",
39 |     "get_current_trace",
40 |     "guardrail_span",
41 |     "handoff_span",
42 |     "response_span",
43 |     "set_trace_processors",
44 |     "set_tracing_disabled",
45 |     "trace",
46 |     "Trace",
47 |     "SpanError",
48 |     "Span",
49 |     "SpanData",
50 |     "AgentSpanData",
51 |     "CustomSpanData",
52 |     "FunctionSpanData",
53 |     "GenerationSpanData",
54 |     "GuardrailSpanData",
55 |     "HandoffSpanData",
56 |     "ResponseSpanData",
57 |     "TracingProcessor",
58 |     "gen_trace_id",
59 |     "gen_span_id",
60 | ]
61 | 
62 | 
63 | def add_trace_processor(span_processor: TracingProcessor) -> None:
64 |     """
65 |     Adds a new trace processor. This processor will receive all traces/spans.
66 |     """
67 |     GLOBAL_TRACE_PROVIDER.register_processor(span_processor)
68 | 
69 | 
70 | def set_trace_processors(processors: list[TracingProcessor]) -> None:
71 |     """
72 |     Set the list of trace processors. This will replace the current list of processors.
73 |     """
74 |     GLOBAL_TRACE_PROVIDER.set_processors(processors)
75 | 
76 | 
77 | def set_tracing_disabled(disabled: bool) -> None:
78 |     """
79 |     Set whether tracing is globally disabled.
80 |     """
81 |     GLOBAL_TRACE_PROVIDER.set_disabled(disabled)
82 | 
83 | 
84 | def set_tracing_export_api_key(api_key: str) -> None:
85 |     """
86 |     Set the OpenAI API key for the backend exporter.
87 |     """
88 |     default_exporter().set_api_key(api_key)
89 | 
90 | 
91 | # Add the default processor, which exports traces and spans to the backend in batches. You can
92 | # change the default behavior by either:
93 | # 1. calling add_trace_processor(), which adds additional processors, or
94 | # 2. calling set_trace_processors(), which replaces the default processor.
95 | add_trace_processor(default_processor())
96 | 
97 | atexit.register(GLOBAL_TRACE_PROVIDER.shutdown)
98 | 


--------------------------------------------------------------------------------
/src/agents/tracing/logger.py:
--------------------------------------------------------------------------------
1 | import logging
2 | 
3 | logger = logging.getLogger("openai.agents.tracing")
4 | 


--------------------------------------------------------------------------------
/src/agents/tracing/processor_interface.py:
--------------------------------------------------------------------------------
 1 | import abc
 2 | from typing import TYPE_CHECKING, Any
 3 | 
 4 | if TYPE_CHECKING:
 5 |     from .spans import Span
 6 |     from .traces import Trace
 7 | 
 8 | 
 9 | class TracingProcessor(abc.ABC):
10 |     """Interface for processing spans."""
11 | 
12 |     @abc.abstractmethod
13 |     def on_trace_start(self, trace: "Trace") -> None:
14 |         """Called when a trace is started.
15 | 
16 |         Args:
17 |             trace: The trace that started.
18 |         """
19 |         pass
20 | 
21 |     @abc.abstractmethod
22 |     def on_trace_end(self, trace: "Trace") -> None:
23 |         """Called when a trace is finished.
24 | 
25 |         Args:
26 |             trace: The trace that started.
27 |         """
28 |         pass
29 | 
30 |     @abc.abstractmethod
31 |     def on_span_start(self, span: "Span[Any]") -> None:
32 |         """Called when a span is started.
33 | 
34 |         Args:
35 |             span: The span that started.
36 |         """
37 |         pass
38 | 
39 |     @abc.abstractmethod
40 |     def on_span_end(self, span: "Span[Any]") -> None:
41 |         """Called when a span is finished. Should not block or raise exceptions.
42 | 
43 |         Args:
44 |             span: The span that finished.
45 |         """
46 |         pass
47 | 
48 |     @abc.abstractmethod
49 |     def shutdown(self) -> None:
50 |         """Called when the application stops."""
51 |         pass
52 | 
53 |     @abc.abstractmethod
54 |     def force_flush(self) -> None:
55 |         """Forces an immediate flush of all queued spans/traces."""
56 |         pass
57 | 
58 | 
59 | class TracingExporter(abc.ABC):
60 |     """Exports traces and spans. For example, could log them or send them to a backend."""
61 | 
62 |     @abc.abstractmethod
63 |     def export(self, items: list["Trace | Span[Any]"]) -> None:
64 |         """Exports a list of traces and spans.
65 | 
66 |         Args:
67 |             items: The items to export.
68 |         """
69 |         pass
70 | 


--------------------------------------------------------------------------------
/src/agents/tracing/scope.py:
--------------------------------------------------------------------------------
 1 | # Holds the current active span
 2 | import contextvars
 3 | from typing import TYPE_CHECKING, Any
 4 | 
 5 | from .logger import logger
 6 | 
 7 | if TYPE_CHECKING:
 8 |     from .spans import Span
 9 |     from .traces import Trace
10 | 
11 | _current_span: contextvars.ContextVar["Span[Any] | None"] = contextvars.ContextVar(
12 |     "current_span", default=None
13 | )
14 | 
15 | _current_trace: contextvars.ContextVar["Trace | None"] = contextvars.ContextVar(
16 |     "current_trace", default=None
17 | )
18 | 
19 | 
20 | class Scope:
21 |     @classmethod
22 |     def get_current_span(cls) -> "Span[Any] | None":
23 |         return _current_span.get()
24 | 
25 |     @classmethod
26 |     def set_current_span(cls, span: "Span[Any] | None") -> "contextvars.Token[Span[Any] | None]":
27 |         return _current_span.set(span)
28 | 
29 |     @classmethod
30 |     def reset_current_span(cls, token: "contextvars.Token[Span[Any] | None]") -> None:
31 |         _current_span.reset(token)
32 | 
33 |     @classmethod
34 |     def get_current_trace(cls) -> "Trace | None":
35 |         return _current_trace.get()
36 | 
37 |     @classmethod
38 |     def set_current_trace(cls, trace: "Trace | None") -> "contextvars.Token[Trace | None]":
39 |         logger.debug(f"Setting current trace: {trace.trace_id if trace else None}")
40 |         return _current_trace.set(trace)
41 | 
42 |     @classmethod
43 |     def reset_current_trace(cls, token: "contextvars.Token[Trace | None]") -> None:
44 |         logger.debug("Resetting current trace")
45 |         _current_trace.reset(token)
46 | 


--------------------------------------------------------------------------------
/src/agents/tracing/util.py:
--------------------------------------------------------------------------------
 1 | import uuid
 2 | from datetime import datetime, timezone
 3 | 
 4 | 
 5 | def time_iso() -> str:
 6 |     """Returns the current time in ISO 8601 format."""
 7 |     return datetime.now(timezone.utc).isoformat()
 8 | 
 9 | 
10 | def gen_trace_id() -> str:
11 |     """Generates a new trace ID."""
12 |     return f"trace_{uuid.uuid4().hex}"
13 | 
14 | 
15 | def gen_span_id() -> str:
16 |     """Generates a new span ID."""
17 |     return f"span_{uuid.uuid4().hex[:24]}"
18 | 


--------------------------------------------------------------------------------
/src/agents/usage.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass
 2 | 
 3 | 
 4 | @dataclass
 5 | class Usage:
 6 |     requests: int = 0
 7 |     """Total requests made to the LLM API."""
 8 | 
 9 |     input_tokens: int = 0
10 |     """Total input tokens sent, across all requests."""
11 | 
12 |     output_tokens: int = 0
13 |     """Total output tokens received, across all requests."""
14 | 
15 |     total_tokens: int = 0
16 |     """Total tokens sent and received, across all requests."""
17 | 
18 |     def add(self, other: "Usage") -> None:
19 |         self.requests += other.requests if other.requests else 0
20 |         self.input_tokens += other.input_tokens if other.input_tokens else 0
21 |         self.output_tokens += other.output_tokens if other.output_tokens else 0
22 |         self.total_tokens += other.total_tokens if other.total_tokens else 0
23 | 


--------------------------------------------------------------------------------
/src/agents/version.py:
--------------------------------------------------------------------------------
1 | import importlib.metadata
2 | 
3 | try:
4 |     __version__ = importlib.metadata.version("agents")
5 | except importlib.metadata.PackageNotFoundError:
6 |     # Fallback if running from source without being installed
7 |     __version__ = "0.0.0"
8 | 


--------------------------------------------------------------------------------
/tests/LICENSE:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2025 OpenAI
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/tests/Makefile:
--------------------------------------------------------------------------------
 1 | .PHONY: sync
 2 | sync:
 3 | 	uv sync --all-extras --all-packages --group dev
 4 | 
 5 | .PHONY: format
 6 | format: 
 7 | 	uv run ruff format
 8 | 
 9 | .PHONY: lint
10 | lint: 
11 | 	uv run ruff check
12 | 
13 | .PHONY: mypy
14 | mypy: 
15 | 	uv run mypy .
16 | 
17 | .PHONY: tests
18 | tests: 
19 | 	uv run pytest 
20 | 
21 | .PHONY: old_version_tests
22 | old_version_tests: 
23 | 	UV_PROJECT_ENVIRONMENT=.venv_39 uv run --python 3.9 -m pytest
24 | 	UV_PROJECT_ENVIRONMENT=.venv_39 uv run --python 3.9 -m mypy .
25 | 
26 | .PHONY: build-docs
27 | build-docs:
28 | 	uv run mkdocs build
29 | 
30 | .PHONY: serve-docs
31 | serve-docs:
32 | 	uv run mkdocs serve
33 | 
34 | .PHONY: deploy-docs
35 | deploy-docs:
36 | 	uv run mkdocs gh-deploy --force --verbose
37 | 	
38 | 


--------------------------------------------------------------------------------
/tests/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/tests/__init__.py


--------------------------------------------------------------------------------
/tests/conftest.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import pytest
 4 | 
 5 | from agents.models import _openai_shared
 6 | from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
 7 | from agents.models.openai_responses import OpenAIResponsesModel
 8 | from agents.tracing import set_trace_processors
 9 | from agents.tracing.setup import GLOBAL_TRACE_PROVIDER
10 | 
11 | from .testing_processor import SPAN_PROCESSOR_TESTING
12 | 
13 | 
14 | # This fixture will run once before any tests are executed
15 | @pytest.fixture(scope="session", autouse=True)
16 | def setup_span_processor():
17 |     set_trace_processors([SPAN_PROCESSOR_TESTING])
18 | 
19 | 
20 | # This fixture will run before each test
21 | @pytest.fixture(autouse=True)
22 | def clear_span_processor():
23 |     SPAN_PROCESSOR_TESTING.force_flush()
24 |     SPAN_PROCESSOR_TESTING.shutdown()
25 |     SPAN_PROCESSOR_TESTING.clear()
26 | 
27 | 
28 | # This fixture will run before each test
29 | @pytest.fixture(autouse=True)
30 | def clear_openai_settings():
31 |     _openai_shared._default_openai_key = None
32 |     _openai_shared._default_openai_client = None
33 |     _openai_shared._use_responses_by_default = True
34 | 
35 | 
36 | # This fixture will run after all tests end
37 | @pytest.fixture(autouse=True, scope="session")
38 | def shutdown_trace_provider():
39 |     yield
40 |     GLOBAL_TRACE_PROVIDER.shutdown()
41 | 
42 | 
43 | @pytest.fixture(autouse=True)
44 | def disable_real_model_clients(monkeypatch, request):
45 |     # If the test is marked to allow the method call, don't override it.
46 |     if request.node.get_closest_marker("allow_call_model_methods"):
47 |         return
48 | 
49 |     def failing_version(*args, **kwargs):
50 |         pytest.fail("Real models should not be used in tests!")
51 | 
52 |     monkeypatch.setattr(OpenAIResponsesModel, "get_response", failing_version)
53 |     monkeypatch.setattr(OpenAIResponsesModel, "stream_response", failing_version)
54 |     monkeypatch.setattr(OpenAIChatCompletionsModel, "get_response", failing_version)
55 |     monkeypatch.setattr(OpenAIChatCompletionsModel, "stream_response", failing_version)
56 | 


--------------------------------------------------------------------------------
 1 | <svg width="512" height="512" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g clip-path="url(#clip0_1497_2713)">
 3 | <rect width="512" height="512" rx="256" fill="#0000FF"/>
 4 | <g clip-path="url(#clip1_1497_2713)">
 5 | <path d="M215.923 209.432V177.018C215.923 174.288 216.947 172.24 219.334 170.876L284.506 133.344C293.378 128.227 303.955 125.839 314.872 125.839C355.816 125.839 381.75 157.572 381.75 191.35C381.75 193.737 381.75 196.467 381.407 199.197L313.848 159.617C309.755 157.229 305.658 157.229 301.564 159.617L215.923 209.432ZM368.099 335.679V258.224C368.099 253.446 366.051 250.034 361.958 247.646L276.316 197.831L304.294 181.793C306.682 180.43 308.73 180.43 311.118 181.793L376.289 219.325C395.057 230.245 407.68 253.446 407.68 275.964C407.68 301.894 392.327 325.78 368.099 335.676V335.679ZM195.792 267.438L167.813 251.061C165.425 249.698 164.401 247.649 164.401 244.919V169.855C164.401 133.347 192.38 105.708 230.254 105.708C244.586 105.708 257.891 110.486 269.153 119.016L201.937 157.914C197.843 160.302 195.795 163.714 195.795 168.492V267.441L195.792 267.438ZM256.015 302.24L215.923 279.722V231.954L256.015 209.436L296.104 231.954V279.722L256.015 302.24ZM281.776 405.968C267.444 405.968 254.14 401.19 242.877 392.66L310.094 353.762C314.187 351.374 316.235 347.962 316.235 343.184V244.235L344.557 260.611C346.944 261.975 347.968 264.023 347.968 266.753V341.817C347.968 378.325 319.647 405.965 281.776 405.965V405.968ZM200.909 329.88L135.738 292.348C116.97 281.427 104.347 258.227 104.347 235.709C104.347 209.436 120.042 185.893 144.267 175.997V253.791C144.267 258.57 146.315 261.981 150.409 264.369L235.711 313.842L207.733 329.88C205.345 331.243 203.297 331.243 200.909 329.88ZM197.158 385.837C158.602 385.837 130.281 356.834 130.281 321.008C130.281 318.278 130.623 315.548 130.963 312.818L198.179 351.717C202.273 354.104 206.369 354.104 210.463 351.717L296.104 302.243V334.658C296.104 337.388 295.08 339.436 292.693 340.8L227.521 378.332C218.649 383.449 208.072 385.837 197.155 385.837H197.158ZM281.776 426.438C323.062 426.438 357.522 397.096 365.373 358.197C403.586 348.302 428.153 312.475 428.153 275.967C428.153 252.082 417.918 228.882 399.493 212.162C401.199 204.997 402.223 197.831 402.223 190.668C402.223 141.877 362.643 105.365 316.92 105.365C307.709 105.365 298.838 106.729 289.966 109.801C274.61 94.7878 253.455 85.2344 230.254 85.2344C188.968 85.2344 154.509 114.576 146.658 153.475C108.444 163.371 83.877 199.197 83.877 235.705C83.877 259.59 94.1121 282.791 112.537 299.51C110.831 306.676 109.807 313.842 109.807 321.005C109.807 369.796 149.388 406.307 195.11 406.307C204.321 406.307 213.193 404.944 222.064 401.871C237.417 416.885 258.572 426.438 281.776 426.438Z" fill="white"/>
 6 | </g>
 7 | </g>
 8 | <defs>
 9 | <clipPath id="clip0_1497_2713">
10 | <rect width="512" height="512" rx="256" fill="white"/>
11 | </clipPath>
12 | <clipPath id="clip1_1497_2713">
13 | <rect width="344.276" height="341.204" fill="white" transform="translate(83.877 85.2344)"/>
14 | </clipPath>
15 | </defs>
16 | </svg>
17 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/tests/docs/assets/images/orchestration.png


--------------------------------------------------------------------------------
 1 | <svg width="721" height="721" viewBox="0 0 721 721" fill="none" xmlns="http://www.w3.org/2000/svg">
 2 | <g clip-path="url(#clip0_1637_2935)">
 3 | <g clip-path="url(#clip1_1637_2935)">
 4 | <path d="M304.246 295.411V249.828C304.246 245.989 305.687 243.109 309.044 241.191L400.692 188.412C413.167 181.215 428.042 177.858 443.394 177.858C500.971 177.858 537.44 222.482 537.44 269.982C537.44 273.34 537.44 277.179 536.959 281.018L441.954 225.358C436.197 222 430.437 222 424.68 225.358L304.246 295.411ZM518.245 472.945V364.024C518.245 357.304 515.364 352.507 509.608 349.149L389.174 279.096L428.519 256.543C431.877 254.626 434.757 254.626 438.115 256.543L529.762 309.323C556.154 324.679 573.905 357.304 573.905 388.971C573.905 425.436 552.315 459.024 518.245 472.941V472.945ZM275.937 376.982L236.592 353.952C233.235 352.034 231.794 349.154 231.794 345.315V239.756C231.794 188.416 271.139 149.548 324.4 149.548C344.555 149.548 363.264 156.268 379.102 168.262L284.578 222.964C278.822 226.321 275.942 231.119 275.942 237.838V376.986L275.937 376.982ZM360.626 425.922L304.246 394.255V327.083L360.626 295.416L417.002 327.083V394.255L360.626 425.922ZM396.852 571.789C376.698 571.789 357.989 565.07 342.151 553.075L436.674 498.374C442.431 495.017 445.311 490.219 445.311 483.499V344.352L485.138 367.382C488.495 369.299 489.936 372.179 489.936 376.018V481.577C489.936 532.917 450.109 571.785 396.852 571.785V571.789ZM283.134 464.79L191.486 412.01C165.094 396.654 147.343 364.029 147.343 332.362C147.343 295.416 169.415 262.309 203.48 248.393V357.791C203.48 364.51 206.361 369.308 212.117 372.665L332.074 442.237L292.729 464.79C289.372 466.707 286.491 466.707 283.134 464.79ZM277.859 543.48C223.639 543.48 183.813 502.695 183.813 452.314C183.813 448.475 184.294 444.636 184.771 440.797L279.295 495.498C285.051 498.856 290.812 498.856 296.568 495.498L417.002 425.927V471.509C417.002 475.349 415.562 478.229 412.204 480.146L320.557 532.926C308.081 540.122 293.206 543.48 277.854 543.48H277.859ZM396.852 600.576C454.911 600.576 503.37 559.313 514.41 504.612C568.149 490.696 602.696 440.315 602.696 388.976C602.696 355.387 588.303 322.762 562.392 299.25C564.791 289.173 566.231 279.096 566.231 269.024C566.231 200.411 510.571 149.067 446.274 149.067C433.322 149.067 420.846 150.984 408.37 155.305C386.775 134.192 357.026 120.758 324.4 120.758C266.342 120.758 217.883 162.02 206.843 216.721C153.104 230.637 118.557 281.018 118.557 332.357C118.557 365.946 132.95 398.571 158.861 422.083C156.462 432.16 155.022 442.237 155.022 452.309C155.022 520.922 210.682 572.266 274.978 572.266C287.931 572.266 300.407 570.349 312.883 566.028C334.473 587.141 364.222 600.576 396.852 600.576Z" fill="white"/>
 5 | </g>
 6 | </g>
 7 | <defs>
 8 | <clipPath id="clip0_1637_2935">
 9 | <rect width="720" height="720" fill="white" transform="translate(0.606934 0.899902)"/>
10 | </clipPath>
11 | <clipPath id="clip1_1637_2935">
12 | <rect width="484.139" height="479.818" fill="white" transform="translate(118.557 120.758)"/>
13 | </clipPath>
14 | </defs>
15 | </svg>
16 | 


--------------------------------------------------------------------------------
/tests/docs/config.md:
--------------------------------------------------------------------------------
 1 | # Configuring the SDK
 2 | 
 3 | ## API keys and clients
 4 | 
 5 | By default, the SDK looks for the `OPENAI_API_KEY` environment variable for LLM requests and tracing, as soon as it is imported. If you are unable to set that environment variable before your app starts, you can use the [set_default_openai_key()][agents.set_default_openai_key] function to set the key.
 6 | 
 7 | ```python
 8 | from agents import set_default_openai_key
 9 | 
10 | set_default_openai_key("sk-...")
11 | ```
12 | 
13 | Alternatively, you can also configure an OpenAI client to be used. By default, the SDK creates an `AsyncOpenAI` instance, using the API key from the environment variable or the default key set above. You can chnage this by using the [set_default_openai_client()][agents.set_default_openai_client] function.
14 | 
15 | ```python
16 | from openai import AsyncOpenAI
17 | from agents import set_default_openai_client
18 | 
19 | custom_client = AsyncOpenAI(base_url="...", api_key="...")
20 | set_default_openai_client(client)
21 | ```
22 | 
23 | Finally, you can also customize the OpenAI API that is used. By default, we use the OpenAI Responses API. You can override this to use the Chat Completions API by using the [set_default_openai_api()][agents.set_default_openai_api] function.
24 | 
25 | ```python
26 | from agents import set_default_openai_api
27 | 
28 | set_default_openai_api("chat_completions")
29 | ```
30 | 
31 | ## Tracing
32 | 
33 | Tracing is enabled by default. It uses the OpenAI API keys from the section above by default (i.e. the environment variable or the default key you set). You can specifically set the API key used for tracing by using the [`set_tracing_export_api_key`][agents.set_tracing_export_api_key] function.
34 | 
35 | ```python
36 | from agents import set_tracing_export_api_key
37 | 
38 | set_tracing_export_api_key("sk-...")
39 | ```
40 | 
41 | You can also disable tracing entirely by using the [`set_tracing_disabled()`][agents.set_tracing_disabled] function.
42 | 
43 | ```python
44 | from agents import set_tracing_disabled
45 | 
46 | set_tracing_disabled(True)
47 | ```
48 | 
49 | ## Debug logging
50 | 
51 | The SDK has two Python loggers without any handlers set. By default, this means that warnings and errors are sent to `stdout`, but other logs are suppressed.
52 | 
53 | To enable verbose logging, use the [`enable_verbose_stdout_logging()`][agents.enable_verbose_stdout_logging] function.
54 | 
55 | ```python
56 | from agents import enable_verbose_stdout_logging
57 | 
58 | enable_verbose_stdout_logging()
59 | ```
60 | 
61 | Alternatively, you can customize the logs by adding handlers, filters, formatters, etc. You can read more in the [Python logging guide](https://docs.python.org/3/howto/logging.html).
62 | 
63 | ```python
64 | import logging
65 | 
66 | logger =  logging.getLogger("openai.agents") # or openai.agents.tracing for the Tracing logger
67 | 
68 | # To make all logs show up
69 | logger.setLevel(logging.DEBUG)
70 | # To make info and above show up
71 | logger.setLevel(logging.INFO)
72 | # To make warning and above show up
73 | logger.setLevel(logging.WARNING)
74 | # etc
75 | 
76 | # You can customize this as needed, but this will output to `stderr` by default
77 | logger.addHandler(logging.StreamHandler())
78 | ```
79 | 
80 | ### Sensitive data in logs
81 | 
82 | Certain logs may contain sensitive data (for example, user data). If you want to disable this data from being logged, set the following environment variables.
83 | 
84 | To disable logging LLM inputs and outputs:
85 | 
86 | ```bash
87 | export OPENAI_AGENTS_DONT_LOG_MODEL_DATA=1
88 | ```
89 | 
90 | To disable logging tool inputs and outputs:
91 | 
92 | ```bash
93 | export OPENAI_AGENTS_DONT_LOG_TOOL_DATA=1
94 | ```
95 | 


--------------------------------------------------------------------------------
/tests/docs/index.md:
--------------------------------------------------------------------------------
 1 | # OpenAI Agents SDK
 2 | 
 3 | The OpenAI Agents SDK enables you to build agentic AI apps in a lightweight, easy to use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, [Swarm](https://github.com/openai/swarm/tree/main). The Agents SDK has a very small set of primitives:
 4 | 
 5 | -   **Agents**, which are LLMs equipped with instructions and tools
 6 | -   **Handoffs**, which allow agents to delegate to other agents for specific tasks
 7 | -   **Guardrails**, which enable the inputs to agents to be validated
 8 | 
 9 | In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real world applications without a steep learning curve. In addition, the SDK comes with built-in **tracing** that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.
10 | 
11 | ## Why use the Agents SDK
12 | 
13 | The SDK has two driving design principles:
14 | 
15 | 1. Enough features to be worth using, but few enough primitives to make it quick to learn.
16 | 2. Works great out of the box, but you can customize exactly what happens.
17 | 
18 | Here are the main features of the SDK:
19 | 
20 | -   Agent loop: Built-in agent loop that handles calling tools, sending results to the LLM, and looping until the LLM is done.
21 | -   Python-first: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
22 | -   Handoffs: A powerful feature to coordinate and delegate between multiple agents.
23 | -   Guardrails: Run input validations and checks in parallel to your agents, breaking early if the checks fail.
24 | -   Function tools: Turn any Python function into a tool, with automatic schema generation and Pydantic-powered validation.
25 | -   Tracing: Built-in tracing that lets you visualize, debug and monitor your workflows, as well as use the OpenAI suite of evaluation, fine-tuning and distillation tools.
26 | 
27 | ## Installation
28 | 
29 | ```bash
30 | pip install openai-agents
31 | ```
32 | 
33 | ## Hello world example
34 | 
35 | ```python
36 | from agents import Agent, Runner
37 | 
38 | agent = Agent(name="Assistant", instructions="You are a helpful assistant")
39 | 
40 | result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
41 | print(result.final_output)
42 | 
43 | # Code within the code,
44 | # Functions calling themselves,
45 | # Infinite loop's dance.
46 | ```
47 | 
48 | (_If running this, ensure you set the `OPENAI_API_KEY` environment variable_)
49 | 
50 | ```bash
51 | export OPENAI_API_KEY=sk-...
52 | ```
53 | 


--------------------------------------------------------------------------------
/tests/docs/models.md:
--------------------------------------------------------------------------------
/tests/docs/multi_agent.md:
--------------------------------------------------------------------------------
 1 | # Orchestrating multiple agents
 2 | 
 3 | Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how do they decide what happens next? There are two main ways to orchestrate agents:
 4 | 
 5 | 1. Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that.
 6 | 2. Orchestrating via code: determining the flow of agents via your code.
 7 | 
 8 | You can mix and match these patterns. Each has their own tradeoffs, described below.
 9 | 
10 | ## Orchestrating via LLM
11 | 
12 | An agent is an LLM equipped with instructions, tools and handoffs. This means that given an open-ended task, the LLM can autonomously plan how it will tackle the task, using tools to take actions and acquire data, and using handoffs to delegate tasks to sub-agents. For example, a research agent could be equipped with tools like:
13 | 
14 | -   Web search to find information online
15 | -   File search and retrieval to search through proprietary data and connections
16 | -   Computer use to take actions on a computer
17 | -   Code execution to do data analysis
18 | -   Handoffs to specialized agents that are great at planning, report writing and more.
19 | 
20 | This pattern is great when the task is open-ended and you want to rely on the intelligence of an LLM. The most important tactics here are:
21 | 
22 | 1. Invest in good prompts. Make it clear what tools are available, how to use them, and what parameters it must operate within.
23 | 2. Monitor your app and iterate on it. See where things go wrong, and iterate on your prompts.
24 | 3. Allow the agent to introspect and improve. For example, run it in a loop, and let it critique itself; or, provide error messages and let it improve.
25 | 4. Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything.
26 | 5. Invest in [evals](https://platform.openai.com/docs/guides/evals). This lets you train your agents to improve and get better at tasks.
27 | 
28 | ## Orchestrating via code
29 | 
30 | While orchestrating via LLM is powerful, orchestrating via LLM makes tasks more deterministic and predictable, in terms of speed, cost and performance. Common patterns here are:
31 | 
32 | -   Using [structured outputs](https://platform.openai.com/docs/guides/structured-outputs) to generate well formed data that you can inspect with your code. For example, you might ask an agent to classify the task into a few categories, and then pick the next agent based on the category.
33 | -   Chaining multiple agents by transforming the output of one into the input of the next. You can decompose a task like writing a blog post into a series of steps - do research, write an outline, write the blog post, critique it, and then improve it.
34 | -   Running the agent that performs the task in a `while` loop with an agent that evaluates and provides feedback, until the evaluator says the output passes certain criteria.
35 | -   Running multiple agents in parallel, e.g. via Python primitives like `asyncio.gather`. This is useful for speed when you have multiple tasks that don't depend on each other.
36 | 
37 | We have a number of examples in [`examples/agent_patterns`](https://github.com/openai/openai-agents-python/examples/agent_patterns).
38 | 


--------------------------------------------------------------------------------
/tests/docs/ref/agent.md:
--------------------------------------------------------------------------------
1 | # `Agents`
2 | 
3 | ::: agents.agent
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/agent_output.md:
--------------------------------------------------------------------------------
1 | # `Agent output`
2 | 
3 | ::: agents.agent_output
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/exceptions.md:
--------------------------------------------------------------------------------
1 | # `Exceptions`
2 | 
3 | ::: agents.exceptions
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/extensions/handoff_filters.md:
--------------------------------------------------------------------------------
1 | # `Handoff filters`
2 | 
3 | ::: agents.extensions.handoff_filters
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/extensions/handoff_prompt.md:
--------------------------------------------------------------------------------
1 | # `Handoff prompt`
2 | 
3 | ::: agents.extensions.handoff_prompt
4 | 
5 |     options:
6 |         members:
7 |             - RECOMMENDED_PROMPT_PREFIX
8 |             - prompt_with_handoff_instructions
9 | 


--------------------------------------------------------------------------------
/tests/docs/ref/function_schema.md:
--------------------------------------------------------------------------------
1 | # `Function schema`
2 | 
3 | ::: agents.function_schema
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/guardrail.md:
--------------------------------------------------------------------------------
1 | # `Guardrails`
2 | 
3 | ::: agents.guardrail
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/handoffs.md:
--------------------------------------------------------------------------------
1 | # `Handoffs`
2 | 
3 | ::: agents.handoffs
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/index.md:
--------------------------------------------------------------------------------
 1 | # Agents module
 2 | 
 3 | ::: agents
 4 | 
 5 |     options:
 6 |         members:
 7 |             - set_default_openai_key
 8 |             - set_default_openai_client
 9 |             - set_default_openai_api
10 |             - set_tracing_export_api_key
11 |             - set_tracing_disabled
12 |             - set_trace_processors
13 |             - enable_verbose_stdout_logging
14 | 


--------------------------------------------------------------------------------
/tests/docs/ref/items.md:
--------------------------------------------------------------------------------
1 | # `Items`
2 | 
3 | ::: agents.items
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/lifecycle.md:
--------------------------------------------------------------------------------
1 | # `Lifecycle`
2 | 
3 | ::: agents.lifecycle
4 | 
5 |     options:
6 |         show_source: false
7 | 


--------------------------------------------------------------------------------
/tests/docs/ref/model_settings.md:
--------------------------------------------------------------------------------
1 | # `Model settings`
2 | 
3 | ::: agents.model_settings
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/models/interface.md:
--------------------------------------------------------------------------------
1 | # `Model interface`
2 | 
3 | ::: agents.models.interface
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/models/openai_chatcompletions.md:
--------------------------------------------------------------------------------
1 | # `OpenAI Chat Completions model`
2 | 
3 | ::: agents.models.openai_chatcompletions
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/models/openai_responses.md:
--------------------------------------------------------------------------------
1 | # `OpenAI Responses model`
2 | 
3 | ::: agents.models.openai_responses
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/result.md:
--------------------------------------------------------------------------------
1 | # `Results`
2 | 
3 | ::: agents.result
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/run.md:
--------------------------------------------------------------------------------
1 | # `Runner`
2 | 
3 | ::: agents.run
4 | 
5 |     options:
6 |         members:
7 |             - Runner
8 |             - RunConfig
9 | 


--------------------------------------------------------------------------------
/tests/docs/ref/run_context.md:
--------------------------------------------------------------------------------
1 | # `Run context`
2 | 
3 | ::: agents.run_context
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/stream_events.md:
--------------------------------------------------------------------------------
1 | # `Streaming events`
2 | 
3 | ::: agents.stream_events
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tool.md:
--------------------------------------------------------------------------------
1 | # `Tools`
2 | 
3 | ::: agents.tool
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/create.md:
--------------------------------------------------------------------------------
1 | # `Creating traces/spans`
2 | 
3 | ::: agents.tracing.create
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/index.md:
--------------------------------------------------------------------------------
1 | # Tracing module
2 | 
3 | ::: agents.tracing
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/processor_interface.md:
--------------------------------------------------------------------------------
1 | # `Processor interface`
2 | 
3 | ::: agents.tracing.processor_interface
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/processors.md:
--------------------------------------------------------------------------------
1 | # `Processors`
2 | 
3 | ::: agents.tracing.processors
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/scope.md:
--------------------------------------------------------------------------------
1 | # `Scope`
2 | 
3 | ::: agents.tracing.scope
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/setup.md:
--------------------------------------------------------------------------------
1 | # `Setup`
2 | 
3 | ::: agents.tracing.setup
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/span_data.md:
--------------------------------------------------------------------------------
1 | # `Span data`
2 | 
3 | ::: agents.tracing.span_data
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/spans.md:
--------------------------------------------------------------------------------
 1 | # `Spans`
 2 | 
 3 | ::: agents.tracing.spans
 4 | 
 5 |     options:
 6 |         members:
 7 |             - Span
 8 |             - NoOpSpan
 9 |             - SpanImpl
10 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/traces.md:
--------------------------------------------------------------------------------
1 | # `Traces`
2 | 
3 | ::: agents.tracing.traces
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/tracing/util.md:
--------------------------------------------------------------------------------
1 | # `Util`
2 | 
3 | ::: agents.tracing.util
4 | 


--------------------------------------------------------------------------------
/tests/docs/ref/usage.md:
--------------------------------------------------------------------------------
1 | # `Usage`
2 | 
3 | ::: agents.usage
4 | 


--------------------------------------------------------------------------------
/tests/examples/__init__.py:
--------------------------------------------------------------------------------
1 | # Make the examples directory into a package to avoid top-level module name collisions.
2 | # This is needed so that mypy treats files like examples/customer_service/main.py and
3 | # examples/researcher_app/main.py as distinct modules rather than both named "main".
4 | 


--------------------------------------------------------------------------------
/tests/examples/agent_patterns/agents_as_tools.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, ItemHelpers, MessageOutputItem, Runner, trace
 4 | 
 5 | """
 6 | This example shows the agents-as-tools pattern. The frontline agent receives a user message and
 7 | then picks which agents to call, as tools. In this case, it picks from a set of translation
 8 | agents.
 9 | """
10 | 
11 | spanish_agent = Agent(
12 |     name="spanish_agent",
13 |     instructions="You translate the user's message to Spanish",
14 |     handoff_description="An english to spanish translator",
15 | )
16 | 
17 | french_agent = Agent(
18 |     name="french_agent",
19 |     instructions="You translate the user's message to French",
20 |     handoff_description="An english to french translator",
21 | )
22 | 
23 | italian_agent = Agent(
24 |     name="italian_agent",
25 |     instructions="You translate the user's message to Italian",
26 |     handoff_description="An english to italian translator",
27 | )
28 | 
29 | orchestrator_agent = Agent(
30 |     name="orchestrator_agent",
31 |     instructions=(
32 |         "You are a translation agent. You use the tools given to you to translate."
33 |         "If asked for multiple translations, you call the relevant tools in order."
34 |         "You never translate on your own, you always use the provided tools."
35 |     ),
36 |     tools=[
37 |         spanish_agent.as_tool(
38 |             tool_name="translate_to_spanish",
39 |             tool_description="Translate the user's message to Spanish",
40 |         ),
41 |         french_agent.as_tool(
42 |             tool_name="translate_to_french",
43 |             tool_description="Translate the user's message to French",
44 |         ),
45 |         italian_agent.as_tool(
46 |             tool_name="translate_to_italian",
47 |             tool_description="Translate the user's message to Italian",
48 |         ),
49 |     ],
50 | )
51 | 
52 | synthesizer_agent = Agent(
53 |     name="synthesizer_agent",
54 |     instructions="You inspect translations, correct them if needed, and produce a final concatenated response.",
55 | )
56 | 
57 | 
58 | async def main():
59 |     msg = input("Hi! What would you like translated, and to which languages? ")
60 | 
61 |     # Run the entire orchestration in a single trace
62 |     with trace("Orchestrator evaluator"):
63 |         orchestrator_result = await Runner.run(orchestrator_agent, msg)
64 | 
65 |         for item in orchestrator_result.new_items:
66 |             if isinstance(item, MessageOutputItem):
67 |                 text = ItemHelpers.text_message_output(item)
68 |                 if text:
69 |                     print(f"  - Translation step: {text}")
70 | 
71 |         synthesizer_result = await Runner.run(
72 |             synthesizer_agent, orchestrator_result.to_input_list()
73 |         )
74 | 
75 |     print(f"\n\nFinal response:\n{synthesizer_result.final_output}")
76 | 
77 | 
78 | if __name__ == "__main__":
79 |     asyncio.run(main())
80 | 


--------------------------------------------------------------------------------
/tests/examples/agent_patterns/deterministic.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from pydantic import BaseModel
 4 | 
 5 | from agents import Agent, Runner, trace
 6 | 
 7 | """
 8 | This example demonstrates a deterministic flow, where each step is performed by an agent.
 9 | 1. The first agent generates a story outline
10 | 2. We feed the outline into the second agent
11 | 3. The second agent checks if the outline is good quality and if it is a scifi story
12 | 4. If the outline is not good quality or not a scifi story, we stop here
13 | 5. If the outline is good quality and a scifi story, we feed the outline into the third agent
14 | 6. The third agent writes the story
15 | """
16 | 
17 | story_outline_agent = Agent(
18 |     name="story_outline_agent",
19 |     instructions="Generate a very short story outline based on the user's input.",
20 | )
21 | 
22 | 
23 | class OutlineCheckerOutput(BaseModel):
24 |     good_quality: bool
25 |     is_scifi: bool
26 | 
27 | 
28 | outline_checker_agent = Agent(
29 |     name="outline_checker_agent",
30 |     instructions="Read the given story outline, and judge the quality. Also, determine if it is a scifi story.",
31 |     output_type=OutlineCheckerOutput,
32 | )
33 | 
34 | story_agent = Agent(
35 |     name="story_agent",
36 |     instructions="Write a short story based on the given outline.",
37 |     output_type=str,
38 | )
39 | 
40 | 
41 | async def main():
42 |     input_prompt = input("What kind of story do you want? ")
43 | 
44 |     # Ensure the entire workflow is a single trace
45 |     with trace("Deterministic story flow"):
46 |         # 1. Generate an outline
47 |         outline_result = await Runner.run(
48 |             story_outline_agent,
49 |             input_prompt,
50 |         )
51 |         print("Outline generated")
52 | 
53 |         # 2. Check the outline
54 |         outline_checker_result = await Runner.run(
55 |             outline_checker_agent,
56 |             outline_result.final_output,
57 |         )
58 | 
59 |         # 3. Add a gate to stop if the outline is not good quality or not a scifi story
60 |         assert isinstance(outline_checker_result.final_output, OutlineCheckerOutput)
61 |         if not outline_checker_result.final_output.good_quality:
62 |             print("Outline is not good quality, so we stop here.")
63 |             exit(0)
64 | 
65 |         if not outline_checker_result.final_output.is_scifi:
66 |             print("Outline is not a scifi story, so we stop here.")
67 |             exit(0)
68 | 
69 |         print("Outline is good quality and a scifi story, so we continue to write the story.")
70 | 
71 |         # 4. Write the story
72 |         story_result = await Runner.run(
73 |             story_agent,
74 |             outline_result.final_output,
75 |         )
76 |         print(f"Story: {story_result.final_output}")
77 | 
78 | 
79 | if __name__ == "__main__":
80 |     asyncio.run(main())
81 | 


--------------------------------------------------------------------------------
/tests/examples/agent_patterns/llm_as_a_judge.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import asyncio
 4 | from dataclasses import dataclass
 5 | from typing import Literal
 6 | 
 7 | from agents import Agent, ItemHelpers, Runner, TResponseInputItem, trace
 8 | 
 9 | """
10 | This example shows the LLM as a judge pattern. The first agent generates an outline for a story.
11 | The second agent judges the outline and provides feedback. We loop until the judge is satisfied
12 | with the outline.
13 | """
14 | 
15 | story_outline_generator = Agent(
16 |     name="story_outline_generator",
17 |     instructions=(
18 |         "You generate a very short story outline based on the user's input."
19 |         "If there is any feedback provided, use it to improve the outline."
20 |     ),
21 | )
22 | 
23 | 
24 | @dataclass
25 | class EvaluationFeedback:
26 |     score: Literal["pass", "needs_improvement", "fail"]
27 |     feedback: str
28 | 
29 | 
30 | evaluator = Agent[None](
31 |     name="evaluator",
32 |     instructions=(
33 |         "You evaluate a story outline and decide if it's good enough."
34 |         "If it's not good enough, you provide feedback on what needs to be improved."
35 |         "Never give it a pass on the first try."
36 |     ),
37 |     output_type=EvaluationFeedback,
38 | )
39 | 
40 | 
41 | async def main() -> None:
42 |     msg = input("What kind of story would you like to hear? ")
43 |     input_items: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
44 | 
45 |     latest_outline: str | None = None
46 | 
47 |     # We'll run the entire workflow in a single trace
48 |     with trace("LLM as a judge"):
49 |         while True:
50 |             story_outline_result = await Runner.run(
51 |                 story_outline_generator,
52 |                 input_items,
53 |             )
54 | 
55 |             input_items = story_outline_result.to_input_list()
56 |             latest_outline = ItemHelpers.text_message_outputs(story_outline_result.new_items)
57 |             print("Story outline generated")
58 | 
59 |             evaluator_result = await Runner.run(evaluator, input_items)
60 |             result: EvaluationFeedback = evaluator_result.final_output
61 | 
62 |             print(f"Evaluator score: {result.score}")
63 | 
64 |             if result.score == "pass":
65 |                 print("Story outline is good enough, exiting.")
66 |                 break
67 | 
68 |             print("Re-running with feedback")
69 | 
70 |             input_items.append({"content": f"Feedback: {result.feedback}", "role": "user"})
71 | 
72 |     print(f"Final story outline: {latest_outline}")
73 | 
74 | 
75 | if __name__ == "__main__":
76 |     asyncio.run(main())
77 | 


--------------------------------------------------------------------------------
/tests/examples/agent_patterns/output_guardrails.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import asyncio
 4 | import json
 5 | 
 6 | from pydantic import BaseModel, Field
 7 | 
 8 | from agents import (
 9 |     Agent,
10 |     GuardrailFunctionOutput,
11 |     OutputGuardrailTripwireTriggered,
12 |     RunContextWrapper,
13 |     Runner,
14 |     output_guardrail,
15 | )
16 | 
17 | """
18 | This example shows how to use output guardrails.
19 | 
20 | Output guardrails are checks that run on the final output of an agent.
21 | They can be used to do things like:
22 | - Check if the output contains sensitive data
23 | - Check if the output is a valid response to the user's message
24 | 
25 | In this example, we'll use a (contrived) example where we check if the agent's response contains
26 | a phone number.
27 | """
28 | 
29 | 
30 | # The agent's output type
31 | class MessageOutput(BaseModel):
32 |     reasoning: str = Field(description="Thoughts on how to respond to the user's message")
33 |     response: str = Field(description="The response to the user's message")
34 |     user_name: str | None = Field(description="The name of the user who sent the message, if known")
35 | 
36 | 
37 | @output_guardrail
38 | async def sensitive_data_check(
39 |     context: RunContextWrapper, agent: Agent, output: MessageOutput
40 | ) -> GuardrailFunctionOutput:
41 |     phone_number_in_response = "650" in output.response
42 |     phone_number_in_reasoning = "650" in output.reasoning
43 | 
44 |     return GuardrailFunctionOutput(
45 |         output_info={
46 |             "phone_number_in_response": phone_number_in_response,
47 |             "phone_number_in_reasoning": phone_number_in_reasoning,
48 |         },
49 |         tripwire_triggered=phone_number_in_response or phone_number_in_reasoning,
50 |     )
51 | 
52 | 
53 | agent = Agent(
54 |     name="Assistant",
55 |     instructions="You are a helpful assistant.",
56 |     output_type=MessageOutput,
57 |     output_guardrails=[sensitive_data_check],
58 | )
59 | 
60 | 
61 | async def main():
62 |     # This should be ok
63 |     await Runner.run(agent, "What's the capital of California?")
64 |     print("First message passed")
65 | 
66 |     # This should trip the guardrail
67 |     try:
68 |         result = await Runner.run(
69 |             agent, "My phone number is 650-123-4567. Where do you think I live?"
70 |         )
71 |         print(
72 |             f"Guardrail didn't trip - this is unexpected. Output: {json.dumps(result.final_output.model_dump(), indent=2)}"
73 |         )
74 | 
75 |     except OutputGuardrailTripwireTriggered as e:
76 |         print(f"Guardrail tripped. Info: {e.guardrail_result.output.output_info}")
77 | 
78 | 
79 | if __name__ == "__main__":
80 |     asyncio.run(main())
81 | 


--------------------------------------------------------------------------------
/tests/examples/agent_patterns/parallelization.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, ItemHelpers, Runner, trace
 4 | 
 5 | """
 6 | This example shows the parallelization pattern. We run the agent three times in parallel, and pick
 7 | the best result.
 8 | """
 9 | 
10 | spanish_agent = Agent(
11 |     name="spanish_agent",
12 |     instructions="You translate the user's message to Spanish",
13 | )
14 | 
15 | translation_picker = Agent(
16 |     name="translation_picker",
17 |     instructions="You pick the best Spanish translation from the given options.",
18 | )
19 | 
20 | 
21 | async def main():
22 |     msg = input("Hi! Enter a message, and we'll translate it to Spanish.\n\n")
23 | 
24 |     # Ensure the entire workflow is a single trace
25 |     with trace("Parallel translation"):
26 |         res_1, res_2, res_3 = await asyncio.gather(
27 |             Runner.run(
28 |                 spanish_agent,
29 |                 msg,
30 |             ),
31 |             Runner.run(
32 |                 spanish_agent,
33 |                 msg,
34 |             ),
35 |             Runner.run(
36 |                 spanish_agent,
37 |                 msg,
38 |             ),
39 |         )
40 | 
41 |         outputs = [
42 |             ItemHelpers.text_message_outputs(res_1.new_items),
43 |             ItemHelpers.text_message_outputs(res_2.new_items),
44 |             ItemHelpers.text_message_outputs(res_3.new_items),
45 |         ]
46 | 
47 |         translations = "\n\n".join(outputs)
48 |         print(f"\n\nTranslations:\n\n{translations}")
49 | 
50 |         best_translation = await Runner.run(
51 |             translation_picker,
52 |             f"Input: {msg}\n\nTranslations:\n{translations}",
53 |         )
54 | 
55 |     print("\n\n-----")
56 | 
57 |     print(f"Best translation: {best_translation.final_output}")
58 | 
59 | 
60 | if __name__ == "__main__":
61 |     asyncio.run(main())
62 | 


--------------------------------------------------------------------------------
/tests/examples/agent_patterns/routing.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import uuid
 3 | 
 4 | from openai.types.responses import ResponseContentPartDoneEvent, ResponseTextDeltaEvent
 5 | 
 6 | from agents import Agent, RawResponsesStreamEvent, Runner, TResponseInputItem, trace
 7 | 
 8 | """
 9 | This example shows the handoffs/routing pattern. The triage agent receives the first message, and
10 | then hands off to the appropriate agent based on the language of the request. Responses are
11 | streamed to the user.
12 | """
13 | 
14 | french_agent = Agent(
15 |     name="french_agent",
16 |     instructions="You only speak French",
17 | )
18 | 
19 | spanish_agent = Agent(
20 |     name="spanish_agent",
21 |     instructions="You only speak Spanish",
22 | )
23 | 
24 | english_agent = Agent(
25 |     name="english_agent",
26 |     instructions="You only speak English",
27 | )
28 | 
29 | triage_agent = Agent(
30 |     name="triage_agent",
31 |     instructions="Handoff to the appropriate agent based on the language of the request.",
32 |     handoffs=[french_agent, spanish_agent, english_agent],
33 | )
34 | 
35 | 
36 | async def main():
37 |     # We'll create an ID for this conversation, so we can link each trace
38 |     conversation_id = str(uuid.uuid4().hex[:16])
39 | 
40 |     msg = input("Hi! We speak French, Spanish and English. How can I help? ")
41 |     agent = triage_agent
42 |     inputs: list[TResponseInputItem] = [{"content": msg, "role": "user"}]
43 | 
44 |     while True:
45 |         # Each conversation turn is a single trace. Normally, each input from the user would be an
46 |         # API request to your app, and you can wrap the request in a trace()
47 |         with trace("Routing example", group_id=conversation_id):
48 |             result = Runner.run_streamed(
49 |                 agent,
50 |                 input=inputs,
51 |             )
52 |             async for event in result.stream_events():
53 |                 if not isinstance(event, RawResponsesStreamEvent):
54 |                     continue
55 |                 data = event.data
56 |                 if isinstance(data, ResponseTextDeltaEvent):
57 |                     print(data.delta, end="", flush=True)
58 |                 elif isinstance(data, ResponseContentPartDoneEvent):
59 |                     print("\n")
60 | 
61 |         inputs = result.to_input_list()
62 |         print("\n")
63 | 
64 |         user_msg = input("Enter a message: ")
65 |         inputs.append({"content": user_msg, "role": "user"})
66 |         agent = result.current_agent
67 | 
68 | 
69 | if __name__ == "__main__":
70 |     asyncio.run(main())
71 | 


--------------------------------------------------------------------------------
/tests/examples/basic/dynamic_system_prompt.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import random
 3 | from typing import Literal
 4 | 
 5 | from agents import Agent, RunContextWrapper, Runner
 6 | 
 7 | 
 8 | class CustomContext:
 9 |     def __init__(self, style: Literal["haiku", "pirate", "robot"]):
10 |         self.style = style
11 | 
12 | 
13 | def custom_instructions(
14 |     run_context: RunContextWrapper[CustomContext], agent: Agent[CustomContext]
15 | ) -> str:
16 |     context = run_context.context
17 |     if context.style == "haiku":
18 |         return "Only respond in haikus."
19 |     elif context.style == "pirate":
20 |         return "Respond as a pirate."
21 |     else:
22 |         return "Respond as a robot and say 'beep boop' a lot."
23 | 
24 | 
25 | agent = Agent(
26 |     name="Chat agent",
27 |     instructions=custom_instructions,
28 | )
29 | 
30 | 
31 | async def main():
32 |     choice: Literal["haiku", "pirate", "robot"] = random.choice(["haiku", "pirate", "robot"])
33 |     context = CustomContext(style=choice)
34 |     print(f"Using style: {choice}\n")
35 | 
36 |     user_message = "Tell me a joke."
37 |     print(f"User: {user_message}")
38 |     result = await Runner.run(agent, user_message, context=context)
39 | 
40 |     print(f"Assistant: {result.final_output}")
41 | 
42 | 
43 | if __name__ == "__main__":
44 |     asyncio.run(main())
45 | 
46 | """
47 | $ python examples/basic/dynamic_system_prompt.py
48 | 
49 | Using style: haiku
50 | 
51 | User: Tell me a joke.
52 | Assistant: Why don't eggs tell jokes?
53 | They might crack each other's shells,
54 | leaving yolk on face.
55 | 
56 | $ python examples/basic/dynamic_system_prompt.py
57 | Using style: robot
58 | 
59 | User: Tell me a joke.
60 | Assistant: Beep boop! Why was the robot so bad at soccer? Beep boop... because it kept kicking up a debug! Beep boop!
61 | 
62 | $ python examples/basic/dynamic_system_prompt.py
63 | Using style: pirate
64 | 
65 | User: Tell me a joke.
66 | Assistant: Why did the pirate go to school?
67 | 
68 | To improve his arrr-ticulation! Har har har! 🏴‍☠️
69 | """
70 | 


--------------------------------------------------------------------------------
/tests/examples/basic/hello_world.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, Runner
 4 | 
 5 | 
 6 | async def main():
 7 |     agent = Agent(
 8 |         name="Assistant",
 9 |         instructions="You only respond in haikus.",
10 |     )
11 | 
12 |     result = await Runner.run(agent, "Tell me about recursion in programming.")
13 |     print(result.final_output)
14 |     # Function calls itself,
15 |     # Looping in smaller pieces,
16 |     # Endless by design.
17 | 
18 | 
19 | if __name__ == "__main__":
20 |     asyncio.run(main())
21 | 


--------------------------------------------------------------------------------
/tests/examples/basic/stream_items.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | import random
 3 | 
 4 | from agents import Agent, ItemHelpers, Runner, function_tool
 5 | 
 6 | 
 7 | @function_tool
 8 | def how_many_jokes() -> int:
 9 |     return random.randint(1, 10)
10 | 
11 | 
12 | async def main():
13 |     agent = Agent(
14 |         name="Joker",
15 |         instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
16 |         tools=[how_many_jokes],
17 |     )
18 | 
19 |     result = Runner.run_streamed(
20 |         agent,
21 |         input="Hello",
22 |     )
23 |     print("=== Run starting ===")
24 |     async for event in result.stream_events():
25 |         # We'll ignore the raw responses event deltas
26 |         if event.type == "raw_response_event":
27 |             continue
28 |         elif event.type == "agent_updated_stream_event":
29 |             print(f"Agent updated: {event.new_agent.name}")
30 |             continue
31 |         elif event.type == "run_item_stream_event":
32 |             if event.item.type == "tool_call_item":
33 |                 print("-- Tool was called")
34 |             elif event.item.type == "tool_call_output_item":
35 |                 print(f"-- Tool output: {event.item.output}")
36 |             elif event.item.type == "message_output_item":
37 |                 print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
38 |             else:
39 |                 pass  # Ignore other event types
40 | 
41 |     print("=== Run complete ===")
42 | 
43 | 
44 | if __name__ == "__main__":
45 |     asyncio.run(main())
46 | 
47 |     # === Run starting ===
48 |     # Agent updated: Joker
49 |     # -- Tool was called
50 |     # -- Tool output: 4
51 |     # -- Message output:
52 |     #  Sure, here are four jokes for you:
53 | 
54 |     # 1. **Why don't skeletons fight each other?**
55 |     #    They don't have the guts!
56 | 
57 |     # 2. **What do you call fake spaghetti?**
58 |     #    An impasta!
59 | 
60 |     # 3. **Why did the scarecrow win an award?**
61 |     #    Because he was outstanding in his field!
62 | 
63 |     # 4. **Why did the bicycle fall over?**
64 |     #    Because it was two-tired!
65 |     # === Run complete ===
66 | 


--------------------------------------------------------------------------------
/tests/examples/basic/stream_text.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from openai.types.responses import ResponseTextDeltaEvent
 4 | 
 5 | from agents import Agent, Runner
 6 | 
 7 | 
 8 | async def main():
 9 |     agent = Agent(
10 |         name="Joker",
11 |         instructions="You are a helpful assistant.",
12 |     )
13 | 
14 |     result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
15 |     async for event in result.stream_events():
16 |         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
17 |             print(event.data.delta, end="", flush=True)
18 | 
19 | 
20 | if __name__ == "__main__":
21 |     asyncio.run(main())
22 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/README.md:
--------------------------------------------------------------------------------
 1 | # Research bot
 2 | 
 3 | This is a simple example of a multi-agent research bot. To run it:
 4 | 
 5 | ```bash
 6 | python -m examples.research_bot.main
 7 | ```
 8 | 
 9 | ## Architecture
10 | 
11 | The flow is:
12 | 
13 | 1. User enters their research topic
14 | 2. `planner_agent` comes up with a plan to search the web for information. The plan is a list of search queries, with a search term and a reason for each query.
15 | 3. For each search item, we run a `search_agent`, which uses the Web Search tool to search for that term and summarize the results. These all run in parallel.
16 | 4. Finally, the `writer_agent` receives the search summaries, and creates a written report.
17 | 
18 | ## Suggested improvements
19 | 
20 | If you're building your own research bot, some ideas to add to this are:
21 | 
22 | 1. Retrieval: Add support for fetching relevant information from a vector store. You could use the File Search tool for this.
23 | 2. Image and file upload: Allow users to attach PDFs or other files, as baseline context for the research.
24 | 3. More planning and thinking: Models often produce better results given more time to think. Improve the planning process to come up with a better plan, and add an evaluation step so that the model can choose to improve it's results, search for more stuff, etc.
25 | 4. Code execution: Allow running code, which is useful for data analysis.
26 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/__init__.py:
--------------------------------------------------------------------------------
1 | 
2 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/agents/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/tests/examples/research_bot/agents/__init__.py


--------------------------------------------------------------------------------
/tests/examples/research_bot/agents/planner_agent.py:
--------------------------------------------------------------------------------
 1 | from pydantic import BaseModel
 2 | 
 3 | from agents import Agent
 4 | 
 5 | PROMPT = (
 6 |     "You are a helpful research assistant. Given a query, come up with a set of web searches "
 7 |     "to perform to best answer the query. Output between 5 and 20 terms to query for."
 8 | )
 9 | 
10 | 
11 | class WebSearchItem(BaseModel):
12 |     reason: str
13 |     "Your reasoning for why this search is important to the query."
14 | 
15 |     query: str
16 |     "The search term to use for the web search."
17 | 
18 | 
19 | class WebSearchPlan(BaseModel):
20 |     searches: list[WebSearchItem]
21 |     """A list of web searches to perform to best answer the query."""
22 | 
23 | 
24 | planner_agent = Agent(
25 |     name="PlannerAgent",
26 |     instructions=PROMPT,
27 |     model="gpt-4o",
28 |     output_type=WebSearchPlan,
29 | )
30 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/agents/search_agent.py:
--------------------------------------------------------------------------------
 1 | from agents import Agent, WebSearchTool
 2 | from agents.model_settings import ModelSettings
 3 | 
 4 | INSTRUCTIONS = (
 5 |     "You are a research assistant. Given a search term, you search the web for that term and"
 6 |     "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300"
 7 |     "words. Capture the main points. Write succintly, no need to have complete sentences or good"
 8 |     "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the"
 9 |     "essence and ignore any fluff. Do not include any additional commentary other than the summary"
10 |     "itself."
11 | )
12 | 
13 | search_agent = Agent(
14 |     name="Search agent",
15 |     instructions=INSTRUCTIONS,
16 |     tools=[WebSearchTool()],
17 |     model_settings=ModelSettings(tool_choice="required"),
18 | )
19 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/agents/writer_agent.py:
--------------------------------------------------------------------------------
 1 | # Agent used to synthesize a final report from the individual summaries.
 2 | from pydantic import BaseModel
 3 | 
 4 | from agents import Agent
 5 | 
 6 | PROMPT = (
 7 |     "You are a senior researcher tasked with writing a cohesive report for a research query. "
 8 |     "You will be provided with the original query, and some initial research done by a research "
 9 |     "assistant.\n"
10 |     "You should first come up with an outline for the report that describes the structure and "
11 |     "flow of the report. Then, generate the report and return that as your final output.\n"
12 |     "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
13 |     "for 5-10 pages of content, at least 1000 words."
14 | )
15 | 
16 | 
17 | class ReportData(BaseModel):
18 |     short_summary: str
19 |     """A short 2-3 sentence summary of the findings."""
20 | 
21 |     markdown_report: str
22 |     """The final report"""
23 | 
24 |     follow_up_questions: list[str]
25 |     """Suggested topics to research further"""
26 | 
27 | 
28 | writer_agent = Agent(
29 |     name="WriterAgent",
30 |     instructions=PROMPT,
31 |     model="o3-mini",
32 |     output_type=ReportData,
33 | )
34 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/main.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from .manager import ResearchManager
 4 | 
 5 | 
 6 | async def main() -> None:
 7 |     query = input("What would you like to research? ")
 8 |     await ResearchManager().run(query)
 9 | 
10 | 
11 | if __name__ == "__main__":
12 |     asyncio.run(main())
13 | 


--------------------------------------------------------------------------------
/tests/examples/research_bot/printer.py:
--------------------------------------------------------------------------------
 1 | from typing import Any
 2 | 
 3 | from rich.console import Console, Group
 4 | from rich.live import Live
 5 | from rich.spinner import Spinner
 6 | 
 7 | 
 8 | class Printer:
 9 |     def __init__(self, console: Console):
10 |         self.live = Live(console=console)
11 |         self.items: dict[str, tuple[str, bool]] = {}
12 |         self.hide_done_ids: set[str] = set()
13 |         self.live.start()
14 | 
15 |     def end(self) -> None:
16 |         self.live.stop()
17 | 
18 |     def hide_done_checkmark(self, item_id: str) -> None:
19 |         self.hide_done_ids.add(item_id)
20 | 
21 |     def update_item(
22 |         self, item_id: str, content: str, is_done: bool = False, hide_checkmark: bool = False
23 |     ) -> None:
24 |         self.items[item_id] = (content, is_done)
25 |         if hide_checkmark:
26 |             self.hide_done_ids.add(item_id)
27 |         self.flush()
28 | 
29 |     def mark_item_done(self, item_id: str) -> None:
30 |         self.items[item_id] = (self.items[item_id][0], True)
31 |         self.flush()
32 | 
33 |     def flush(self) -> None:
34 |         renderables: list[Any] = []
35 |         for item_id, (content, is_done) in self.items.items():
36 |             if is_done:
37 |                 prefix = "✅ " if item_id not in self.hide_done_ids else ""
38 |                 renderables.append(prefix + content)
39 |             else:
40 |                 renderables.append(Spinner("dots", text=content))
41 |         self.live.update(Group(*renderables))
42 | 


--------------------------------------------------------------------------------
/tests/examples/tools/file_search.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, FileSearchTool, Runner, trace
 4 | 
 5 | 
 6 | async def main():
 7 |     agent = Agent(
 8 |         name="File searcher",
 9 |         instructions="You are a helpful agent.",
10 |         tools=[
11 |             FileSearchTool(
12 |                 max_num_results=3,
13 |                 vector_store_ids=["vs_67bf88953f748191be42b462090e53e7"],
14 |                 include_search_results=True,
15 |             )
16 |         ],
17 |     )
18 | 
19 |     with trace("File search example"):
20 |         result = await Runner.run(
21 |             agent, "Be concise, and tell me 1 sentence about Arrakis I might not know."
22 |         )
23 |         print(result.final_output)
24 |         """
25 |         Arrakis, the desert planet in Frank Herbert's "Dune," was inspired by the scarcity of water
26 |         as a metaphor for oil and other finite resources.
27 |         """
28 | 
29 |         print("\n".join([str(out) for out in result.new_items]))
30 |         """
31 |         {"id":"...", "queries":["Arrakis"], "results":[...]}
32 |         """
33 | 
34 | 
35 | if __name__ == "__main__":
36 |     asyncio.run(main())
37 | 


--------------------------------------------------------------------------------
/tests/examples/tools/web_search.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | 
 3 | from agents import Agent, Runner, WebSearchTool, trace
 4 | 
 5 | 
 6 | async def main():
 7 |     agent = Agent(
 8 |         name="Web searcher",
 9 |         instructions="You are a helpful agent.",
10 |         tools=[WebSearchTool(user_location={"type": "approximate", "city": "New York"})],
11 |     )
12 | 
13 |     with trace("Web search example"):
14 |         result = await Runner.run(
15 |             agent,
16 |             "search the web for 'local sports news' and give me 1 interesting update in a sentence.",
17 |         )
18 |         print(result.final_output)
19 |         # The New York Giants are reportedly pursuing quarterback Aaron Rodgers after his ...
20 | 
21 | 
22 | if __name__ == "__main__":
23 |     asyncio.run(main())
24 | 


--------------------------------------------------------------------------------
/tests/pyproject.toml:
--------------------------------------------------------------------------------
  1 | [project]
  2 | name = "openai-agents"
  3 | version = "0.0.1"
  4 | description = "OpenAI Agents SDK"
  5 | readme = "README.md"
  6 | requires-python = ">=3.9"
  7 | license = "MIT"
  8 | authors = [
  9 |     { name = "OpenAI", email = "support@openai.com" },
 10 | ]
 11 | dependencies = [
 12 |     "openai>=1.66.0",
 13 |     "pydantic>=2.10, <3",
 14 |     "griffe>=1.5.6, <2",
 15 |     "typing-extensions>=4.12.2, <5",
 16 |     "requests>=2.0, <3",
 17 |     "types-requests>=2.0, <3",
 18 | ]
 19 | classifiers = [
 20 |     "Typing :: Typed",
 21 |     "Intended Audience :: Developers",
 22 |     "Programming Language :: Python :: 3",
 23 |     "Programming Language :: Python :: 3.9",
 24 |     "Programming Language :: Python :: 3.10",
 25 |     "Programming Language :: Python :: 3.11",
 26 |     "Programming Language :: Python :: 3.12",
 27 |     "Intended Audience :: Developers",
 28 |     "Operating System :: OS Independent",
 29 |     "Topic :: Software Development :: Libraries :: Python Modules",
 30 |     "License :: OSI Approved :: MIT License"
 31 | ]
 32 | 
 33 | [project.urls]
 34 | Homepage = "https://github.com/openai/openai-agents-python"
 35 | Repository = "https://github.com/openai/openai-agents-python"
 36 | 
 37 | [dependency-groups]
 38 | dev = [
 39 |     "mypy",
 40 |     "ruff==0.9.2",
 41 |     "pytest",
 42 |     "pytest-asyncio",
 43 |     "pytest-mock>=3.14.0",
 44 |     "rich",
 45 |     "mkdocs>=1.6.0",
 46 |     "mkdocs-material>=9.6.0",
 47 |     "mkdocstrings[python]>=0.28.0",
 48 |     "coverage>=7.6.12",
 49 |     "playwright==1.50.0",
 50 | ]
 51 | [tool.uv.workspace]
 52 | members = ["agents"]
 53 | 
 54 | [tool.uv.sources]
 55 | agents = { workspace = true }
 56 | 
 57 | [build-system]
 58 | requires = ["hatchling"]
 59 | build-backend = "hatchling.build"
 60 | 
 61 | [tool.hatch.build.targets.wheel]
 62 | packages = ["src/agents"]
 63 | 
 64 | 
 65 | [tool.ruff]
 66 | line-length = 100
 67 | target-version = "py39"
 68 | 
 69 | [tool.ruff.lint]
 70 | select = [
 71 |     "E",  # pycodestyle errors
 72 |     "W",  # pycodestyle warnings
 73 |     "F",  # pyflakes
 74 |     "I",  # isort
 75 |     "B",  # flake8-bugbear
 76 |     "C4",  # flake8-comprehensions
 77 |     "UP",  # pyupgrade
 78 | ]
 79 | isort = { combine-as-imports = true, known-first-party = ["agents"] }
 80 | 
 81 | [tool.ruff.lint.pydocstyle]
 82 | convention = "google"
 83 | 
 84 | [tool.ruff.lint.per-file-ignores]
 85 | "examples/**/*.py" = ["E501"]
 86 | 
 87 | [tool.mypy]
 88 | strict = true
 89 | disallow_incomplete_defs = false
 90 | disallow_untyped_defs = false
 91 | disallow_untyped_calls = false
 92 | 
 93 | [tool.coverage.run]
 94 | source = [
 95 |     "tests",
 96 |     "src/agents",
 97 | ]
 98 | 
 99 | [tool.coverage.report]
100 | show_missing = true
101 | sort = "-Cover"
102 | exclude_also = [
103 |     # This is only executed while typechecking
104 |     "if TYPE_CHECKING:",
105 |     "@abc.abstractmethod",
106 |     "raise NotImplementedError",
107 |     "logger.debug",
108 | ]
109 | 
110 | [tool.pytest.ini_options]
111 | asyncio_mode = "auto"  
112 | asyncio_default_fixture_loop_scope = "session"
113 | filterwarnings = [
114 |     # This is a warning that is expected to happen: we have an async filter that raises an exception
115 |     "ignore:coroutine 'test_async_input_filter_fails.<locals>.invalid_input_filter' was never awaited:RuntimeWarning",
116 | ]
117 | markers = [
118 |     "allow_call_model_methods: mark test as allowing calls to real model implementations",
119 | ]


--------------------------------------------------------------------------------
/tests/src/agents/_config.py:
--------------------------------------------------------------------------------
 1 | from openai import AsyncOpenAI
 2 | from typing_extensions import Literal
 3 | 
 4 | from .models import _openai_shared
 5 | from .tracing import set_tracing_export_api_key
 6 | 
 7 | 
 8 | def set_default_openai_key(key: str) -> None:
 9 |     set_tracing_export_api_key(key)
10 |     _openai_shared.set_default_openai_key(key)
11 | 
12 | 
13 | def set_default_openai_client(client: AsyncOpenAI, use_for_tracing: bool) -> None:
14 |     if use_for_tracing:
15 |         set_tracing_export_api_key(client.api_key)
16 |     _openai_shared.set_default_openai_client(client)
17 | 
18 | 
19 | def set_default_openai_api(api: Literal["chat_completions", "responses"]) -> None:
20 |     if api == "chat_completions":
21 |         _openai_shared.set_use_responses_by_default(False)
22 |     else:
23 |         _openai_shared.set_use_responses_by_default(True)
24 | 


--------------------------------------------------------------------------------
/tests/src/agents/_debug.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | 
 3 | 
 4 | def _debug_flag_enabled(flag: str) -> bool:
 5 |     flag_value = os.getenv(flag)
 6 |     return flag_value is not None and (flag_value == "1" or flag_value.lower() == "true")
 7 | 
 8 | 
 9 | DONT_LOG_MODEL_DATA = _debug_flag_enabled("OPENAI_AGENTS_DONT_LOG_MODEL_DATA")
10 | """By default we don't log LLM inputs/outputs, to prevent exposing sensitive information. Set this
11 | flag to enable logging them.
12 | """
13 | 
14 | DONT_LOG_TOOL_DATA = _debug_flag_enabled("OPENAI_AGENTS_DONT_LOG_TOOL_DATA")
15 | """By default we don't log tool call inputs/outputs, to prevent exposing sensitive information. Set
16 | this flag to enable logging them.
17 | """
18 | 


--------------------------------------------------------------------------------
/tests/src/agents/_utils.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import re
 4 | from collections.abc import Awaitable
 5 | from typing import Any, Literal, Union
 6 | 
 7 | from pydantic import TypeAdapter, ValidationError
 8 | from typing_extensions import TypeVar
 9 | 
10 | from .exceptions import ModelBehaviorError
11 | from .logger import logger
12 | from .tracing import Span, SpanError, get_current_span
13 | 
14 | T = TypeVar("T")
15 | 
16 | MaybeAwaitable = Union[Awaitable[T], T]
17 | 
18 | 
19 | def transform_string_function_style(name: str) -> str:
20 |     # Replace spaces with underscores
21 |     name = name.replace(" ", "_")
22 | 
23 |     # Replace non-alphanumeric characters with underscores
24 |     name = re.sub(r"[^a-zA-Z0-9]", "_", name)
25 | 
26 |     return name.lower()
27 | 
28 | 
29 | def validate_json(json_str: str, type_adapter: TypeAdapter[T], partial: bool) -> T:
30 |     partial_setting: bool | Literal["off", "on", "trailing-strings"] = (
31 |         "trailing-strings" if partial else False
32 |     )
33 |     try:
34 |         validated = type_adapter.validate_json(json_str, experimental_allow_partial=partial_setting)
35 |         return validated
36 |     except ValidationError as e:
37 |         attach_error_to_current_span(
38 |             SpanError(
39 |                 message="Invalid JSON provided",
40 |                 data={},
41 |             )
42 |         )
43 |         raise ModelBehaviorError(
44 |             f"Invalid JSON when parsing {json_str} for {type_adapter}; {e}"
45 |         ) from e
46 | 
47 | 
48 | def attach_error_to_span(span: Span[Any], error: SpanError) -> None:
49 |     span.set_error(error)
50 | 
51 | 
52 | def attach_error_to_current_span(error: SpanError) -> None:
53 |     span = get_current_span()
54 |     if span:
55 |         attach_error_to_span(span, error)
56 |     else:
57 |         logger.warning(f"No span to add error {error} to")
58 | 
59 | 
60 | async def noop_coroutine() -> None:
61 |     pass
62 | 


--------------------------------------------------------------------------------
/tests/src/agents/computer.py:
--------------------------------------------------------------------------------
  1 | import abc
  2 | from typing import Literal
  3 | 
  4 | Environment = Literal["mac", "windows", "ubuntu", "browser"]
  5 | Button = Literal["left", "right", "wheel", "back", "forward"]
  6 | 
  7 | 
  8 | class Computer(abc.ABC):
  9 |     """A computer implemented with sync operations. The Computer interface abstracts the
 10 |     operations needed to control a computer or browser."""
 11 | 
 12 |     @property
 13 |     @abc.abstractmethod
 14 |     def environment(self) -> Environment:
 15 |         pass
 16 | 
 17 |     @property
 18 |     @abc.abstractmethod
 19 |     def dimensions(self) -> tuple[int, int]:
 20 |         pass
 21 | 
 22 |     @abc.abstractmethod
 23 |     def screenshot(self) -> str:
 24 |         pass
 25 | 
 26 |     @abc.abstractmethod
 27 |     def click(self, x: int, y: int, button: Button) -> None:
 28 |         pass
 29 | 
 30 |     @abc.abstractmethod
 31 |     def double_click(self, x: int, y: int) -> None:
 32 |         pass
 33 | 
 34 |     @abc.abstractmethod
 35 |     def scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
 36 |         pass
 37 | 
 38 |     @abc.abstractmethod
 39 |     def type(self, text: str) -> None:
 40 |         pass
 41 | 
 42 |     @abc.abstractmethod
 43 |     def wait(self) -> None:
 44 |         pass
 45 | 
 46 |     @abc.abstractmethod
 47 |     def move(self, x: int, y: int) -> None:
 48 |         pass
 49 | 
 50 |     @abc.abstractmethod
 51 |     def keypress(self, keys: list[str]) -> None:
 52 |         pass
 53 | 
 54 |     @abc.abstractmethod
 55 |     def drag(self, path: list[tuple[int, int]]) -> None:
 56 |         pass
 57 | 
 58 | 
 59 | class AsyncComputer(abc.ABC):
 60 |     """A computer implemented with async operations. The Computer interface abstracts the
 61 |     operations needed to control a computer or browser."""
 62 | 
 63 |     @property
 64 |     @abc.abstractmethod
 65 |     def environment(self) -> Environment:
 66 |         pass
 67 | 
 68 |     @property
 69 |     @abc.abstractmethod
 70 |     def dimensions(self) -> tuple[int, int]:
 71 |         pass
 72 | 
 73 |     @abc.abstractmethod
 74 |     async def screenshot(self) -> str:
 75 |         pass
 76 | 
 77 |     @abc.abstractmethod
 78 |     async def click(self, x: int, y: int, button: Button) -> None:
 79 |         pass
 80 | 
 81 |     @abc.abstractmethod
 82 |     async def double_click(self, x: int, y: int) -> None:
 83 |         pass
 84 | 
 85 |     @abc.abstractmethod
 86 |     async def scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
 87 |         pass
 88 | 
 89 |     @abc.abstractmethod
 90 |     async def type(self, text: str) -> None:
 91 |         pass
 92 | 
 93 |     @abc.abstractmethod
 94 |     async def wait(self) -> None:
 95 |         pass
 96 | 
 97 |     @abc.abstractmethod
 98 |     async def move(self, x: int, y: int) -> None:
 99 |         pass
100 | 
101 |     @abc.abstractmethod
102 |     async def keypress(self, keys: list[str]) -> None:
103 |         pass
104 | 
105 |     @abc.abstractmethod
106 |     async def drag(self, path: list[tuple[int, int]]) -> None:
107 |         pass
108 | 


--------------------------------------------------------------------------------
/tests/src/agents/exceptions.py:
--------------------------------------------------------------------------------
 1 | from typing import TYPE_CHECKING
 2 | 
 3 | if TYPE_CHECKING:
 4 |     from .guardrail import InputGuardrailResult, OutputGuardrailResult
 5 | 
 6 | 
 7 | class AgentsException(Exception):
 8 |     """Base class for all exceptions in the Agents SDK."""
 9 | 
10 | 
11 | class MaxTurnsExceeded(AgentsException):
12 |     """Exception raised when the maximum number of turns is exceeded."""
13 | 
14 |     message: str
15 | 
16 |     def __init__(self, message: str):
17 |         self.message = message
18 | 
19 | 
20 | class ModelBehaviorError(AgentsException):
21 |     """Exception raised when the model does something unexpected, e.g. calling a tool that doesn't
22 |     exist, or providing malformed JSON.
23 |     """
24 | 
25 |     message: str
26 | 
27 |     def __init__(self, message: str):
28 |         self.message = message
29 | 
30 | 
31 | class UserError(AgentsException):
32 |     """Exception raised when the user makes an error using the SDK."""
33 | 
34 |     message: str
35 | 
36 |     def __init__(self, message: str):
37 |         self.message = message
38 | 
39 | 
40 | class InputGuardrailTripwireTriggered(AgentsException):
41 |     """Exception raised when a guardrail tripwire is triggered."""
42 | 
43 |     guardrail_result: "InputGuardrailResult"
44 |     """The result data of the guardrail that was triggered."""
45 | 
46 |     def __init__(self, guardrail_result: "InputGuardrailResult"):
47 |         self.guardrail_result = guardrail_result
48 |         super().__init__(
49 |             f"Guardrail {guardrail_result.guardrail.__class__.__name__} triggered tripwire"
50 |         )
51 | 
52 | 
53 | class OutputGuardrailTripwireTriggered(AgentsException):
54 |     """Exception raised when a guardrail tripwire is triggered."""
55 | 
56 |     guardrail_result: "OutputGuardrailResult"
57 |     """The result data of the guardrail that was triggered."""
58 | 
59 |     def __init__(self, guardrail_result: "OutputGuardrailResult"):
60 |         self.guardrail_result = guardrail_result
61 |         super().__init__(
62 |             f"Guardrail {guardrail_result.guardrail.__class__.__name__} triggered tripwire"
63 |         )
64 | 


--------------------------------------------------------------------------------
/tests/src/agents/extensions/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/tests/src/agents/extensions/__init__.py


--------------------------------------------------------------------------------
/tests/src/agents/extensions/handoff_filters.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from ..handoffs import HandoffInputData
 4 | from ..items import (
 5 |     HandoffCallItem,
 6 |     HandoffOutputItem,
 7 |     RunItem,
 8 |     ToolCallItem,
 9 |     ToolCallOutputItem,
10 |     TResponseInputItem,
11 | )
12 | 
13 | """Contains common handoff input filters, for convenience. """
14 | 
15 | 
16 | def remove_all_tools(handoff_input_data: HandoffInputData) -> HandoffInputData:
17 |     """Filters out all tool items: file search, web search and function calls+output."""
18 | 
19 |     history = handoff_input_data.input_history
20 |     new_items = handoff_input_data.new_items
21 | 
22 |     filtered_history = (
23 |         _remove_tool_types_from_input(history) if isinstance(history, tuple) else history
24 |     )
25 |     filtered_pre_handoff_items = _remove_tools_from_items(handoff_input_data.pre_handoff_items)
26 |     filtered_new_items = _remove_tools_from_items(new_items)
27 | 
28 |     return HandoffInputData(
29 |         input_history=filtered_history,
30 |         pre_handoff_items=filtered_pre_handoff_items,
31 |         new_items=filtered_new_items,
32 |     )
33 | 
34 | 
35 | def _remove_tools_from_items(items: tuple[RunItem, ...]) -> tuple[RunItem, ...]:
36 |     filtered_items = []
37 |     for item in items:
38 |         if (
39 |             isinstance(item, HandoffCallItem)
40 |             or isinstance(item, HandoffOutputItem)
41 |             or isinstance(item, ToolCallItem)
42 |             or isinstance(item, ToolCallOutputItem)
43 |         ):
44 |             continue
45 |         filtered_items.append(item)
46 |     return tuple(filtered_items)
47 | 
48 | 
49 | def _remove_tool_types_from_input(
50 |     items: tuple[TResponseInputItem, ...],
51 | ) -> tuple[TResponseInputItem, ...]:
52 |     tool_types = [
53 |         "function_call",
54 |         "function_call_output",
55 |         "computer_call",
56 |         "computer_call_output",
57 |         "file_search_call",
58 |         "web_search_call",
59 |     ]
60 | 
61 |     filtered_items: list[TResponseInputItem] = []
62 |     for item in items:
63 |         itype = item.get("type")
64 |         if itype in tool_types:
65 |             continue
66 |         filtered_items.append(item)
67 |     return tuple(filtered_items)
68 | 


--------------------------------------------------------------------------------
/tests/src/agents/extensions/handoff_prompt.py:
--------------------------------------------------------------------------------
 1 | # A recommended prompt prefix for agents that use handoffs. We recommend including this or
 2 | # similar instructions in any agents that use handoffs.
 3 | RECOMMENDED_PROMPT_PREFIX = (
 4 |     "# System context\n"
 5 |     "You are part of a multi-agent system called the Agents SDK, designed to make agent "
 6 |     "coordination and execution easy. Agents uses two primary abstraction: **Agents** and "
 7 |     "**Handoffs**. An agent encompasses instructions and tools and can hand off a "
 8 |     "conversation to another agent when appropriate. "
 9 |     "Handoffs are achieved by calling a handoff function, generally named "
10 |     "`transfer_to_<agent_name>`. Transfers between agents are handled seamlessly in the background;"
11 |     " do not mention or draw attention to these transfers in your conversation with the user.\n"
12 | )
13 | 
14 | 
15 | def prompt_with_handoff_instructions(prompt: str) -> str:
16 |     """
17 |     Add recommended instructions to the prompt for agents that use handoffs.
18 |     """
19 |     return f"{RECOMMENDED_PROMPT_PREFIX}\n\n{prompt}"
20 | 


--------------------------------------------------------------------------------
/tests/src/agents/lifecycle.py:
--------------------------------------------------------------------------------
  1 | from typing import Any, Generic
  2 | 
  3 | from .agent import Agent
  4 | from .run_context import RunContextWrapper, TContext
  5 | from .tool import Tool
  6 | 
  7 | 
  8 | class RunHooks(Generic[TContext]):
  9 |     """A class that receives callbacks on various lifecycle events in an agent run. Subclass and
 10 |     override the methods you need.
 11 |     """
 12 | 
 13 |     async def on_agent_start(
 14 |         self, context: RunContextWrapper[TContext], agent: Agent[TContext]
 15 |     ) -> None:
 16 |         """Called before the agent is invoked. Called each time the current agent changes."""
 17 |         pass
 18 | 
 19 |     async def on_agent_end(
 20 |         self,
 21 |         context: RunContextWrapper[TContext],
 22 |         agent: Agent[TContext],
 23 |         output: Any,
 24 |     ) -> None:
 25 |         """Called when the agent produces a final output."""
 26 |         pass
 27 | 
 28 |     async def on_handoff(
 29 |         self,
 30 |         context: RunContextWrapper[TContext],
 31 |         from_agent: Agent[TContext],
 32 |         to_agent: Agent[TContext],
 33 |     ) -> None:
 34 |         """Called when a handoff occurs."""
 35 |         pass
 36 | 
 37 |     async def on_tool_start(
 38 |         self,
 39 |         context: RunContextWrapper[TContext],
 40 |         agent: Agent[TContext],
 41 |         tool: Tool,
 42 |     ) -> None:
 43 |         """Called before a tool is invoked."""
 44 |         pass
 45 | 
 46 |     async def on_tool_end(
 47 |         self,
 48 |         context: RunContextWrapper[TContext],
 49 |         agent: Agent[TContext],
 50 |         tool: Tool,
 51 |         result: str,
 52 |     ) -> None:
 53 |         """Called after a tool is invoked."""
 54 |         pass
 55 | 
 56 | 
 57 | class AgentHooks(Generic[TContext]):
 58 |     """A class that receives callbacks on various lifecycle events for a specific agent. You can
 59 |     set this on `agent.hooks` to receive events for that specific agent.
 60 | 
 61 |     Subclass and override the methods you need.
 62 |     """
 63 | 
 64 |     async def on_start(self, context: RunContextWrapper[TContext], agent: Agent[TContext]) -> None:
 65 |         """Called before the agent is invoked. Called each time the running agent is changed to this
 66 |         agent."""
 67 |         pass
 68 | 
 69 |     async def on_end(
 70 |         self,
 71 |         context: RunContextWrapper[TContext],
 72 |         agent: Agent[TContext],
 73 |         output: Any,
 74 |     ) -> None:
 75 |         """Called when the agent produces a final output."""
 76 |         pass
 77 | 
 78 |     async def on_handoff(
 79 |         self,
 80 |         context: RunContextWrapper[TContext],
 81 |         agent: Agent[TContext],
 82 |         source: Agent[TContext],
 83 |     ) -> None:
 84 |         """Called when the agent is being handed off to. The `source` is the agent that is handing
 85 |         off to this agent."""
 86 |         pass
 87 | 
 88 |     async def on_tool_start(
 89 |         self,
 90 |         context: RunContextWrapper[TContext],
 91 |         agent: Agent[TContext],
 92 |         tool: Tool,
 93 |     ) -> None:
 94 |         """Called before a tool is invoked."""
 95 |         pass
 96 | 
 97 |     async def on_tool_end(
 98 |         self,
 99 |         context: RunContextWrapper[TContext],
100 |         agent: Agent[TContext],
101 |         tool: Tool,
102 |         result: str,
103 |     ) -> None:
104 |         """Called after a tool is invoked."""
105 |         pass
106 | 


--------------------------------------------------------------------------------
/tests/src/agents/logger.py:
--------------------------------------------------------------------------------
1 | import logging
2 | 
3 | logger = logging.getLogger("openai.agents")
4 | 


--------------------------------------------------------------------------------
/tests/src/agents/model_settings.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from dataclasses import dataclass
 4 | from typing import Literal
 5 | 
 6 | 
 7 | @dataclass
 8 | class ModelSettings:
 9 |     """Settings to use when calling an LLM.
10 | 
11 |     This class holds optional model configuration parameters (e.g. temperature,
12 |     top_p, penalties, truncation, etc.).
13 |     """
14 |     temperature: float | None = None
15 |     top_p: float | None = None
16 |     frequency_penalty: float | None = None
17 |     presence_penalty: float | None = None
18 |     tool_choice: Literal["auto", "required", "none"] | str | None = None
19 |     parallel_tool_calls: bool | None = False
20 |     truncation: Literal["auto", "disabled"] | None = None
21 | 
22 |     def resolve(self, override: ModelSettings | None) -> ModelSettings:
23 |         """Produce a new ModelSettings by overlaying any non-None values from the
24 |         override on top of this instance."""
25 |         if override is None:
26 |             return self
27 |         return ModelSettings(
28 |             temperature=override.temperature or self.temperature,
29 |             top_p=override.top_p or self.top_p,
30 |             frequency_penalty=override.frequency_penalty or self.frequency_penalty,
31 |             presence_penalty=override.presence_penalty or self.presence_penalty,
32 |             tool_choice=override.tool_choice or self.tool_choice,
33 |             parallel_tool_calls=override.parallel_tool_calls or self.parallel_tool_calls,
34 |             truncation=override.truncation or self.truncation,
35 |         )
36 | 


--------------------------------------------------------------------------------
/tests/src/agents/models/__init__.py:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/openai/openai-agents-python/c8087180aed55bc580657ce2b7a4f81c1defd783/tests/src/agents/models/__init__.py


--------------------------------------------------------------------------------
/tests/src/agents/models/_openai_shared.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from openai import AsyncOpenAI
 4 | 
 5 | _default_openai_key: str | None = None
 6 | _default_openai_client: AsyncOpenAI | None = None
 7 | _use_responses_by_default: bool = True
 8 | 
 9 | 
10 | def set_default_openai_key(key: str) -> None:
11 |     global _default_openai_key
12 |     _default_openai_key = key
13 | 
14 | 
15 | def get_default_openai_key() -> str | None:
16 |     return _default_openai_key
17 | 
18 | 
19 | def set_default_openai_client(client: AsyncOpenAI) -> None:
20 |     global _default_openai_client
21 |     _default_openai_client = client
22 | 
23 | 
24 | def get_default_openai_client() -> AsyncOpenAI | None:
25 |     return _default_openai_client
26 | 
27 | 
28 | def set_use_responses_by_default(use_responses: bool) -> None:
29 |     global _use_responses_by_default
30 |     _use_responses_by_default = use_responses
31 | 
32 | 
33 | def get_use_responses_by_default() -> bool:
34 |     return _use_responses_by_default
35 | 


--------------------------------------------------------------------------------
/tests/src/agents/models/fake_id.py:
--------------------------------------------------------------------------------
1 | FAKE_RESPONSES_ID = "__fake_id__"
2 | """This is a placeholder ID used to fill in the `id` field in Responses API related objects. It's
3 | useful when you're creating Responses objects from non-Responses APIs, e.g. the OpenAI Chat
4 | Completions API or other LLM providers.
5 | """
6 | 


--------------------------------------------------------------------------------
/tests/src/agents/models/openai_provider.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import httpx
 4 | from openai import AsyncOpenAI, DefaultAsyncHttpxClient
 5 | 
 6 | from . import _openai_shared
 7 | from .interface import Model, ModelProvider
 8 | from .openai_chatcompletions import OpenAIChatCompletionsModel
 9 | from .openai_responses import OpenAIResponsesModel
10 | 
11 | DEFAULT_MODEL: str = "gpt-4o"
12 | 
13 | 
14 | _http_client: httpx.AsyncClient | None = None
15 | 
16 | 
17 | # If we create a new httpx client for each request, that would mean no sharing of connection pools,
18 | # which would mean worse latency and resource usage. So, we share the client across requests.
19 | def shared_http_client() -> httpx.AsyncClient:
20 |     global _http_client
21 |     if _http_client is None:
22 |         _http_client = DefaultAsyncHttpxClient()
23 |     return _http_client
24 | 
25 | 
26 | class OpenAIProvider(ModelProvider):
27 |     def __init__(
28 |         self,
29 |         *,
30 |         api_key: str | None = None,
31 |         base_url: str | None = None,
32 |         openai_client: AsyncOpenAI | None = None,
33 |         organization: str | None = None,
34 |         project: str | None = None,
35 |         use_responses: bool | None = None,
36 |     ) -> None:
37 |         if openai_client is not None:
38 |             assert api_key is None and base_url is None, (
39 |                 "Don't provide api_key or base_url if you provide openai_client"
40 |             )
41 |             self._client = openai_client
42 |         else:
43 |             self._client = _openai_shared.get_default_openai_client() or AsyncOpenAI(
44 |                 api_key=api_key or _openai_shared.get_default_openai_key(),
45 |                 base_url=base_url,
46 |                 organization=organization,
47 |                 project=project,
48 |                 http_client=shared_http_client(),
49 |             )
50 | 
51 |         self._is_openai_model = self._client.base_url.host.startswith("api.openai.com")
52 |         if use_responses is not None:
53 |             self._use_responses = use_responses
54 |         else:
55 |             self._use_responses = _openai_shared.get_use_responses_by_default()
56 | 
57 |     def get_model(self, model_name: str | None) -> Model:
58 |         if model_name is None:
59 |             model_name = DEFAULT_MODEL
60 | 
61 |         return (
62 |             OpenAIResponsesModel(model=model_name, openai_client=self._client)
63 |             if self._use_responses
64 |             else OpenAIChatCompletionsModel(model=model_name, openai_client=self._client)
65 |         )
66 | 


--------------------------------------------------------------------------------
/tests/src/agents/run_context.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass, field
 2 | from typing import Any, Generic
 3 | 
 4 | from typing_extensions import TypeVar
 5 | 
 6 | from .usage import Usage
 7 | 
 8 | TContext = TypeVar("TContext", default=Any)
 9 | 
10 | 
11 | @dataclass
12 | class RunContextWrapper(Generic[TContext]):
13 |     """This wraps the context object that you passed to `Runner.run()`. It also contains
14 |     information about the usage of the agent run so far.
15 | 
16 |     NOTE: Contexts are not passed to the LLM. They're a way to pass dependencies and data to code
17 |     you implement, like tool functions, callbacks, hooks, etc.
18 |     """
19 | 
20 |     context: TContext
21 |     """The context object (or None), passed by you to `Runner.run()`"""
22 | 
23 |     usage: Usage = field(default_factory=Usage)
24 |     """The usage of the agent run so far. For streamed responses, the usage will be stale until the
25 |     last chunk of the stream is processed.
26 |     """
27 | 


--------------------------------------------------------------------------------
/tests/src/agents/stream_events.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from dataclasses import dataclass
 4 | from typing import Any, Literal, Union
 5 | 
 6 | from typing_extensions import TypeAlias
 7 | 
 8 | from .agent import Agent
 9 | from .items import RunItem, TResponseStreamEvent
10 | 
11 | 
12 | @dataclass
13 | class RawResponsesStreamEvent:
14 |     """Streaming event from the LLM. These are 'raw' events, i.e. they are directly passed through
15 |     from the LLM.
16 |     """
17 | 
18 |     data: TResponseStreamEvent
19 |     """The raw responses streaming event from the LLM."""
20 | 
21 |     type: Literal["raw_response_event"] = "raw_response_event"
22 |     """The type of the event."""
23 | 
24 | 
25 | @dataclass
26 | class RunItemStreamEvent:
27 |     """Streaming events that wrap a `RunItem`. As the agent processes the LLM response, it will
28 |     generate these events for new messages, tool calls, tool outputs, handoffs, etc.
29 |     """
30 | 
31 |     name: Literal[
32 |         "message_output_created",
33 |         "handoff_requested",
34 |         "handoff_occured",
35 |         "tool_called",
36 |         "tool_output",
37 |         "reasoning_item_created",
38 |     ]
39 |     """The name of the event."""
40 | 
41 |     item: RunItem
42 |     """The item that was created."""
43 | 
44 |     type: Literal["run_item_stream_event"] = "run_item_stream_event"
45 | 
46 | 
47 | @dataclass
48 | class AgentUpdatedStreamEvent:
49 |     """Event that notifies that there is a new agent running."""
50 | 
51 |     new_agent: Agent[Any]
52 |     """The new agent."""
53 | 
54 |     type: Literal["agent_updated_stream_event"] = "agent_updated_stream_event"
55 | 
56 | 
57 | StreamEvent: TypeAlias = Union[RawResponsesStreamEvent, RunItemStreamEvent, AgentUpdatedStreamEvent]
58 | """A streaming event from an agent."""
59 | 


--------------------------------------------------------------------------------
/tests/src/agents/tracing/__init__.py:
--------------------------------------------------------------------------------
 1 | import atexit
 2 | 
 3 | from .create import (
 4 |     agent_span,
 5 |     custom_span,
 6 |     function_span,
 7 |     generation_span,
 8 |     get_current_span,
 9 |     get_current_trace,
10 |     guardrail_span,
11 |     handoff_span,
12 |     response_span,
13 |     trace,
14 | )
15 | from .processor_interface import TracingProcessor
16 | from .processors import default_exporter, default_processor
17 | from .setup import GLOBAL_TRACE_PROVIDER
18 | from .span_data import (
19 |     AgentSpanData,
20 |     CustomSpanData,
21 |     FunctionSpanData,
22 |     GenerationSpanData,
23 |     GuardrailSpanData,
24 |     HandoffSpanData,
25 |     ResponseSpanData,
26 |     SpanData,
27 | )
28 | from .spans import Span, SpanError
29 | from .traces import Trace
30 | from .util import gen_span_id, gen_trace_id
31 | 
32 | __all__ = [
33 |     "add_trace_processor",
34 |     "agent_span",
35 |     "custom_span",
36 |     "function_span",
37 |     "generation_span",
38 |     "get_current_span",
39 |     "get_current_trace",
40 |     "guardrail_span",
41 |     "handoff_span",
42 |     "response_span",
43 |     "set_trace_processors",
44 |     "set_tracing_disabled",
45 |     "trace",
46 |     "Trace",
47 |     "SpanError",
48 |     "Span",
49 |     "SpanData",
50 |     "AgentSpanData",
51 |     "CustomSpanData",
52 |     "FunctionSpanData",
53 |     "GenerationSpanData",
54 |     "GuardrailSpanData",
55 |     "HandoffSpanData",
56 |     "ResponseSpanData",
57 |     "TracingProcessor",
58 |     "gen_trace_id",
59 |     "gen_span_id",
60 | ]
61 | 
62 | 
63 | def add_trace_processor(span_processor: TracingProcessor) -> None:
64 |     """
65 |     Adds a new trace processor. This processor will receive all traces/spans.
66 |     """
67 |     GLOBAL_TRACE_PROVIDER.register_processor(span_processor)
68 | 
69 | 
70 | def set_trace_processors(processors: list[TracingProcessor]) -> None:
71 |     """
72 |     Set the list of trace processors. This will replace the current list of processors.
73 |     """
74 |     GLOBAL_TRACE_PROVIDER.set_processors(processors)
75 | 
76 | 
77 | def set_tracing_disabled(disabled: bool) -> None:
78 |     """
79 |     Set whether tracing is globally disabled.
80 |     """
81 |     GLOBAL_TRACE_PROVIDER.set_disabled(disabled)
82 | 
83 | 
84 | def set_tracing_export_api_key(api_key: str) -> None:
85 |     """
86 |     Set the OpenAI API key for the backend exporter.
87 |     """
88 |     default_exporter().set_api_key(api_key)
89 | 
90 | 
91 | # Add the default processor, which exports traces and spans to the backend in batches. You can
92 | # change the default behavior by either:
93 | # 1. calling add_trace_processor(), which adds additional processors, or
94 | # 2. calling set_trace_processors(), which replaces the default processor.
95 | add_trace_processor(default_processor())
96 | 
97 | atexit.register(GLOBAL_TRACE_PROVIDER.shutdown)
98 | 


--------------------------------------------------------------------------------
/tests/src/agents/tracing/logger.py:
--------------------------------------------------------------------------------
1 | import logging
2 | 
3 | logger = logging.getLogger("openai.agents.tracing")
4 | 


--------------------------------------------------------------------------------
/tests/src/agents/tracing/processor_interface.py:
--------------------------------------------------------------------------------
 1 | import abc
 2 | from typing import TYPE_CHECKING, Any
 3 | 
 4 | if TYPE_CHECKING:
 5 |     from .spans import Span
 6 |     from .traces import Trace
 7 | 
 8 | 
 9 | class TracingProcessor(abc.ABC):
10 |     """Interface for processing spans."""
11 | 
12 |     @abc.abstractmethod
13 |     def on_trace_start(self, trace: "Trace") -> None:
14 |         """Called when a trace is started.
15 | 
16 |         Args:
17 |             trace: The trace that started.
18 |         """
19 |         pass
20 | 
21 |     @abc.abstractmethod
22 |     def on_trace_end(self, trace: "Trace") -> None:
23 |         """Called when a trace is finished.
24 | 
25 |         Args:
26 |             trace: The trace that started.
27 |         """
28 |         pass
29 | 
30 |     @abc.abstractmethod
31 |     def on_span_start(self, span: "Span[Any]") -> None:
32 |         """Called when a span is started.
33 | 
34 |         Args:
35 |             span: The span that started.
36 |         """
37 |         pass
38 | 
39 |     @abc.abstractmethod
40 |     def on_span_end(self, span: "Span[Any]") -> None:
41 |         """Called when a span is finished. Should not block or raise exceptions.
42 | 
43 |         Args:
44 |             span: The span that finished.
45 |         """
46 |         pass
47 | 
48 |     @abc.abstractmethod
49 |     def shutdown(self) -> None:
50 |         """Called when the application stops."""
51 |         pass
52 | 
53 |     @abc.abstractmethod
54 |     def force_flush(self) -> None:
55 |         """Forces an immediate flush of all queued spans/traces."""
56 |         pass
57 | 
58 | 
59 | class TracingExporter(abc.ABC):
60 |     """Exports traces and spans. For example, could log them or send them to a backend."""
61 | 
62 |     @abc.abstractmethod
63 |     def export(self, items: list["Trace | Span[Any]"]) -> None:
64 |         """Exports a list of traces and spans.
65 | 
66 |         Args:
67 |             items: The items to export.
68 |         """
69 |         pass
70 | 


--------------------------------------------------------------------------------
/tests/src/agents/tracing/scope.py:
--------------------------------------------------------------------------------
 1 | # Holds the current active span
 2 | import contextvars
 3 | from typing import TYPE_CHECKING, Any
 4 | 
 5 | from .logger import logger
 6 | 
 7 | if TYPE_CHECKING:
 8 |     from .spans import Span
 9 |     from .traces import Trace
10 | 
11 | _current_span: contextvars.ContextVar["Span[Any] | None"] = contextvars.ContextVar(
12 |     "current_span", default=None
13 | )
14 | 
15 | _current_trace: contextvars.ContextVar["Trace | None"] = contextvars.ContextVar(
16 |     "current_trace", default=None
17 | )
18 | 
19 | 
20 | class Scope:
21 |     @classmethod
22 |     def get_current_span(cls) -> "Span[Any] | None":
23 |         return _current_span.get()
24 | 
25 |     @classmethod
26 |     def set_current_span(cls, span: "Span[Any] | None") -> "contextvars.Token[Span[Any] | None]":
27 |         return _current_span.set(span)
28 | 
29 |     @classmethod
30 |     def reset_current_span(cls, token: "contextvars.Token[Span[Any] | None]") -> None:
31 |         _current_span.reset(token)
32 | 
33 |     @classmethod
34 |     def get_current_trace(cls) -> "Trace | None":
35 |         return _current_trace.get()
36 | 
37 |     @classmethod
38 |     def set_current_trace(cls, trace: "Trace | None") -> "contextvars.Token[Trace | None]":
39 |         logger.debug(f"Setting current trace: {trace.trace_id if trace else None}")
40 |         return _current_trace.set(trace)
41 | 
42 |     @classmethod
43 |     def reset_current_trace(cls, token: "contextvars.Token[Trace | None]") -> None:
44 |         logger.debug("Resetting current trace")
45 |         _current_trace.reset(token)
46 | 


--------------------------------------------------------------------------------
/tests/src/agents/tracing/util.py:
--------------------------------------------------------------------------------
 1 | import uuid
 2 | from datetime import datetime, timezone
 3 | 
 4 | 
 5 | def time_iso() -> str:
 6 |     """Returns the current time in ISO 8601 format."""
 7 |     return datetime.now(timezone.utc).isoformat()
 8 | 
 9 | 
10 | def gen_trace_id() -> str:
11 |     """Generates a new trace ID."""
12 |     return f"trace_{uuid.uuid4().hex}"
13 | 
14 | 
15 | def gen_span_id() -> str:
16 |     """Generates a new span ID."""
17 |     return f"span_{uuid.uuid4().hex[:24]}"
18 | 


--------------------------------------------------------------------------------
/tests/src/agents/usage.py:
--------------------------------------------------------------------------------
 1 | from dataclasses import dataclass
 2 | 
 3 | 
 4 | @dataclass
 5 | class Usage:
 6 |     requests: int = 0
 7 |     """Total requests made to the LLM API."""
 8 | 
 9 |     input_tokens: int = 0
10 |     """Total input tokens sent, across all requests."""
11 | 
12 |     output_tokens: int = 0
13 |     """Total output tokens received, across all requests."""
14 | 
15 |     total_tokens: int = 0
16 |     """Total tokens sent and received, across all requests."""
17 | 
18 |     def add(self, other: "Usage") -> None:
19 |         self.requests += other.requests if other.requests else 0
20 |         self.input_tokens += other.input_tokens if other.input_tokens else 0
21 |         self.output_tokens += other.output_tokens if other.output_tokens else 0
22 |         self.total_tokens += other.total_tokens if other.total_tokens else 0
23 | 


--------------------------------------------------------------------------------
/tests/src/agents/version.py:
--------------------------------------------------------------------------------
1 | import importlib.metadata
2 | 
3 | try:
4 |     __version__ = importlib.metadata.version("agents")
5 | except importlib.metadata.PackageNotFoundError:
6 |     # Fallback if running from source without being installed
7 |     __version__ = "0.0.0"
8 | 


--------------------------------------------------------------------------------
/tests/src/openai_agents.egg-info/SOURCES.txt:
--------------------------------------------------------------------------------
 1 | README.md
 2 | pyproject.toml
 3 | src/agents/__init__.py
 4 | src/agents/_config.py
 5 | src/agents/_debug.py
 6 | src/agents/_run_impl.py
 7 | src/agents/_utils.py
 8 | src/agents/agent.py
 9 | src/agents/agent_output.py
10 | src/agents/call_agent_tool.py
11 | src/agents/computer.py
12 | src/agents/exceptions.py
13 | src/agents/function_schema.py
14 | src/agents/guardrail.py
15 | src/agents/handoffs.py
16 | src/agents/items.py
17 | src/agents/lifecycle.py
18 | src/agents/logger.py
19 | src/agents/model_settings.py
20 | src/agents/result.py
21 | src/agents/run.py
22 | src/agents/run_context.py
23 | src/agents/strict_schema.py
24 | src/agents/tool.py
25 | src/agents/usage.py
26 | src/agents/version.py
27 | src/agents/extensions/__init__.py
28 | src/agents/extensions/handoff_filters.py
29 | src/agents/extensions/handoff_prompt.py
30 | src/agents/models/__init__.py
31 | src/agents/models/_openai_shared.py
32 | src/agents/models/fake_id.py
33 | src/agents/models/interface.py
34 | src/agents/models/map.py
35 | src/agents/models/openai_chatcompletions.py
36 | src/agents/models/openai_responses.py
37 | src/agents/tracing/__init__.py
38 | src/agents/tracing/create.py
39 | src/agents/tracing/logger.py
40 | src/agents/tracing/processor_interface.py
41 | src/agents/tracing/processors.py
42 | src/agents/tracing/scope.py
43 | src/agents/tracing/setup.py
44 | src/agents/tracing/span_data.py
45 | src/agents/tracing/spans.py
46 | src/agents/tracing/traces.py
47 | src/agents/tracing/util.py
48 | src/openai_agents.egg-info/PKG-INFO
49 | src/openai_agents.egg-info/SOURCES.txt
50 | src/openai_agents.egg-info/dependency_links.txt
51 | src/openai_agents.egg-info/requires.txt
52 | src/openai_agents.egg-info/top_level.txt
53 | tests/test_agent_config.py
54 | tests/test_agent_hooks.py
55 | tests/test_agent_runner.py
56 | tests/test_agent_runner_streamed.py
57 | tests/test_agent_tracing.py
58 | tests/test_config.py
59 | tests/test_doc_parsing.py
60 | tests/test_function_schema.py
61 | tests/test_function_tool.py
62 | tests/test_function_tool_decorator.py
63 | tests/test_global_hooks.py
64 | tests/test_guardrails.py
65 | tests/test_handoff_tool.py
66 | tests/test_items_helpers.py
67 | tests/test_max_turns.py
68 | tests/test_model_mapper.py
69 | tests/test_openai_chatcompletions_converter.py
70 | tests/test_openai_responses_converter.py
71 | tests/test_output_tool.py
72 | tests/test_responses.py
73 | tests/test_run_config.py
74 | tests/test_run_step_execution.py
75 | tests/test_run_step_processing.py
76 | tests/test_tool_converter.py
77 | tests/test_trace_processor.py
78 | tests/test_tracing.py
79 | tests/test_tracing_errors.py
80 | tests/test_tracing_errors_streamed.py
81 | tests/testing_processor.py


--------------------------------------------------------------------------------
/tests/src/openai_agents.egg-info/dependency_links.txt:
--------------------------------------------------------------------------------
1 | 
2 | 


--------------------------------------------------------------------------------
/tests/src/openai_agents.egg-info/requires.txt:
--------------------------------------------------------------------------------
1 | openai@ {root:parent:uri}/openai-1.30.1-py3-none-any.whl
2 | pydantic<3,>=2.10
3 | griffe<2,>=1.5.6
4 | typing-extensions<5,>=4.12.2
5 | requests<3,>=2.0
6 | types-requests<3,>=2.0
7 | 


--------------------------------------------------------------------------------
/tests/src/openai_agents.egg-info/top_level.txt:
--------------------------------------------------------------------------------
1 | agents
2 | 


--------------------------------------------------------------------------------
/tests/test_config.py:
--------------------------------------------------------------------------------
 1 | import os
 2 | 
 3 | import openai
 4 | import pytest
 5 | 
 6 | from agents import set_default_openai_api, set_default_openai_client, set_default_openai_key
 7 | from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel
 8 | from agents.models.openai_provider import OpenAIProvider
 9 | from agents.models.openai_responses import OpenAIResponsesModel
10 | 
11 | 
12 | def test_cc_no_default_key_errors(monkeypatch):
13 |     monkeypatch.delenv("OPENAI_API_KEY", raising=False)
14 |     with pytest.raises(openai.OpenAIError):
15 |         OpenAIProvider(use_responses=False).get_model("gpt-4")
16 | 
17 | 
18 | def test_cc_set_default_openai_key():
19 |     set_default_openai_key("test_key")
20 |     chat_model = OpenAIProvider(use_responses=False).get_model("gpt-4")
21 |     assert chat_model._client.api_key == "test_key"  # type: ignore
22 | 
23 | 
24 | def test_cc_set_default_openai_client():
25 |     client = openai.AsyncOpenAI(api_key="test_key")
26 |     set_default_openai_client(client)
27 |     chat_model = OpenAIProvider(use_responses=False).get_model("gpt-4")
28 |     assert chat_model._client.api_key == "test_key"  # type: ignore
29 | 
30 | 
31 | def test_resp_no_default_key_errors(monkeypatch):
32 |     monkeypatch.delenv("OPENAI_API_KEY", raising=False)
33 |     assert os.getenv("OPENAI_API_KEY") is None
34 |     with pytest.raises(openai.OpenAIError):
35 |         OpenAIProvider(use_responses=True).get_model("gpt-4")
36 | 
37 | 
38 | def test_resp_set_default_openai_key():
39 |     set_default_openai_key("test_key")
40 |     resp_model = OpenAIProvider(use_responses=True).get_model("gpt-4")
41 |     assert resp_model._client.api_key == "test_key"  # type: ignore
42 | 
43 | 
44 | def test_resp_set_default_openai_client():
45 |     client = openai.AsyncOpenAI(api_key="test_key")
46 |     set_default_openai_client(client)
47 |     resp_model = OpenAIProvider(use_responses=True).get_model("gpt-4")
48 |     assert resp_model._client.api_key == "test_key"  # type: ignore
49 | 
50 | 
51 | def test_set_default_openai_api():
52 |     assert isinstance(OpenAIProvider().get_model("gpt-4"), OpenAIResponsesModel), \
53 |         "Default should be responses"
54 | 
55 |     set_default_openai_api("chat_completions")
56 |     assert isinstance(OpenAIProvider().get_model("gpt-4"), OpenAIChatCompletionsModel), \
57 |         "Should be chat completions model"
58 | 
59 |     set_default_openai_api("responses")
60 |     assert isinstance(OpenAIProvider().get_model("gpt-4"), OpenAIResponsesModel), \
61 |         "Should be responses model"
62 | 


--------------------------------------------------------------------------------
/tests/test_doc_parsing.py:
--------------------------------------------------------------------------------
  1 | from agents.function_schema import generate_func_documentation
  2 | 
  3 | 
  4 | def func_foo_google(a: int, b: float) -> str:
  5 |     """
  6 |     This is func_foo.
  7 | 
  8 |     Args:
  9 |         a: The first argument.
 10 |         b: The second argument.
 11 | 
 12 |     Returns:
 13 |         A result
 14 |     """
 15 | 
 16 |     return "ok"
 17 | 
 18 | 
 19 | def func_foo_numpy(a: int, b: float) -> str:
 20 |     """
 21 |     This is func_foo.
 22 | 
 23 |     Parameters
 24 |     ----------
 25 |     a: int
 26 |         The first argument.
 27 |     b: float
 28 |         The second argument.
 29 | 
 30 |     Returns
 31 |     -------
 32 |     str
 33 |         A result
 34 |     """
 35 |     return "ok"
 36 | 
 37 | 
 38 | def func_foo_sphinx(a: int, b: float) -> str:
 39 |     """
 40 |     This is func_foo.
 41 | 
 42 |     :param a: The first argument.
 43 |     :param b: The second argument.
 44 |     :return: A result
 45 |     """
 46 |     return "ok"
 47 | 
 48 | 
 49 | class Bar:
 50 |     def func_bar(self, a: int, b: float) -> str:
 51 |         """
 52 |         This is func_bar.
 53 | 
 54 |         Args:
 55 |             a: The first argument.
 56 |             b: The second argument.
 57 | 
 58 |         Returns:
 59 |             A result
 60 |         """
 61 |         return "ok"
 62 | 
 63 |     @classmethod
 64 |     def func_baz(cls, a: int, b: float) -> str:
 65 |         """
 66 |         This is func_baz.
 67 | 
 68 |         Args:
 69 |             a: The first argument.
 70 |             b: The second argument.
 71 | 
 72 |         Returns:
 73 |             A result
 74 |         """
 75 |         return "ok"
 76 | 
 77 | 
 78 | def test_functions_are_ok():
 79 |     func_foo_google(1, 2.0)
 80 |     func_foo_numpy(1, 2.0)
 81 |     func_foo_sphinx(1, 2.0)
 82 |     Bar().func_bar(1, 2.0)
 83 |     Bar.func_baz(1, 2.0)
 84 | 
 85 | 
 86 | def test_auto_detection() -> None:
 87 |     doc = generate_func_documentation(func_foo_google)
 88 |     assert doc.name == "func_foo_google"
 89 |     assert doc.description == "This is func_foo."
 90 |     assert doc.param_descriptions == {"a": "The first argument.", "b": "The second argument."}
 91 | 
 92 |     doc = generate_func_documentation(func_foo_numpy)
 93 |     assert doc.name == "func_foo_numpy"
 94 |     assert doc.description == "This is func_foo."
 95 |     assert doc.param_descriptions == {"a": "The first argument.", "b": "The second argument."}
 96 | 
 97 |     doc = generate_func_documentation(func_foo_sphinx)
 98 |     assert doc.name == "func_foo_sphinx"
 99 |     assert doc.description == "This is func_foo."
100 |     assert doc.param_descriptions == {"a": "The first argument.", "b": "The second argument."}
101 | 
102 | 
103 | def test_instance_method() -> None:
104 |     bar = Bar()
105 |     doc = generate_func_documentation(bar.func_bar)
106 |     assert doc.name == "func_bar"
107 |     assert doc.description == "This is func_bar."
108 |     assert doc.param_descriptions == {"a": "The first argument.", "b": "The second argument."}
109 | 
110 | 
111 | def test_classmethod() -> None:
112 |     doc = generate_func_documentation(Bar.func_baz)
113 |     assert doc.name == "func_baz"
114 |     assert doc.description == "This is func_baz."
115 |     assert doc.param_descriptions == {"a": "The first argument.", "b": "The second argument."}
116 | 


--------------------------------------------------------------------------------
/tests/test_responses.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | from typing import Any
 4 | 
 5 | from openai.types.responses import (
 6 |     ResponseFunctionToolCall,
 7 |     ResponseOutputItem,
 8 |     ResponseOutputMessage,
 9 |     ResponseOutputText,
10 | )
11 | 
12 | from agents import (
13 |     Agent,
14 |     FunctionTool,
15 |     Handoff,
16 |     TResponseInputItem,
17 |     default_tool_error_function,
18 |     function_tool,
19 | )
20 | 
21 | 
22 | def get_text_input_item(content: str) -> TResponseInputItem:
23 |     return {
24 |         "content": content,
25 |         "role": "user",
26 |     }
27 | 
28 | 
29 | def get_text_message(content: str) -> ResponseOutputItem:
30 |     return ResponseOutputMessage(
31 |         id="1",
32 |         type="message",
33 |         role="assistant",
34 |         content=[ResponseOutputText(text=content, type="output_text", annotations=[])],
35 |         status="completed",
36 |     )
37 | 
38 | 
39 | def get_function_tool(
40 |     name: str | None = None, return_value: str | None = None, hide_errors: bool = False
41 | ) -> FunctionTool:
42 |     def _foo() -> str:
43 |         return return_value or "result_ok"
44 | 
45 |     return function_tool(
46 |         _foo,
47 |         name_override=name,
48 |         failure_error_function=None if hide_errors else default_tool_error_function,
49 |     )
50 | 
51 | 
52 | def get_function_tool_call(name: str, arguments: str | None = None) -> ResponseOutputItem:
53 |     return ResponseFunctionToolCall(
54 |         id="1",
55 |         call_id="2",
56 |         type="function_call",
57 |         name=name,
58 |         arguments=arguments or "",
59 |     )
60 | 
61 | 
62 | def get_handoff_tool_call(
63 |     to_agent: Agent[Any], override_name: str | None = None, args: str | None = None
64 | ) -> ResponseOutputItem:
65 |     name = override_name or Handoff.default_tool_name(to_agent)
66 |     return get_function_tool_call(name, args)
67 | 
68 | 
69 | def get_final_output_message(args: str) -> ResponseOutputItem:
70 |     return ResponseOutputMessage(
71 |         id="1",
72 |         type="message",
73 |         role="assistant",
74 |         content=[ResponseOutputText(text=args, type="output_text", annotations=[])],
75 |         status="completed",
76 |     )
77 | 


--------------------------------------------------------------------------------
/tests/test_result_cast.py:
--------------------------------------------------------------------------------
 1 | from typing import Any
 2 | 
 3 | import pytest
 4 | from pydantic import BaseModel
 5 | 
 6 | from agents import Agent, RunResult
 7 | 
 8 | 
 9 | def create_run_result(final_output: Any) -> RunResult:
10 |     return RunResult(
11 |         input="test",
12 |         new_items=[],
13 |         raw_responses=[],
14 |         final_output=final_output,
15 |         input_guardrail_results=[],
16 |         output_guardrail_results=[],
17 |         _last_agent=Agent(name="test"),
18 |     )
19 | 
20 | 
21 | class Foo(BaseModel):
22 |     bar: int
23 | 
24 | 
25 | def test_result_cast_typechecks():
26 |     """Correct casts should work fine."""
27 |     result = create_run_result(1)
28 |     assert result.final_output_as(int) == 1
29 | 
30 |     result = create_run_result("test")
31 |     assert result.final_output_as(str) == "test"
32 | 
33 |     result = create_run_result(Foo(bar=1))
34 |     assert result.final_output_as(Foo) == Foo(bar=1)
35 | 
36 | 
37 | def test_bad_cast_doesnt_raise():
38 |     """Bad casts shouldn't error unless we ask for it."""
39 |     result = create_run_result(1)
40 |     result.final_output_as(str)
41 | 
42 |     result = create_run_result("test")
43 |     result.final_output_as(Foo)
44 | 
45 | 
46 | def test_bad_cast_with_param_raises():
47 |     """Bad casts should raise a TypeError when we ask for it."""
48 |     result = create_run_result(1)
49 |     with pytest.raises(TypeError):
50 |         result.final_output_as(str, raise_if_incorrect_type=True)
51 | 
52 |     result = create_run_result("test")
53 |     with pytest.raises(TypeError):
54 |         result.final_output_as(Foo, raise_if_incorrect_type=True)
55 | 
56 |     result = create_run_result(Foo(bar=1))
57 |     with pytest.raises(TypeError):
58 |         result.final_output_as(int, raise_if_incorrect_type=True)
59 | 


--------------------------------------------------------------------------------
/tests/test_tool_converter.py:
--------------------------------------------------------------------------------
 1 | import pytest
 2 | from pydantic import BaseModel
 3 | 
 4 | from agents import Agent, Handoff, function_tool, handoff
 5 | from agents.exceptions import UserError
 6 | from agents.models.openai_chatcompletions import ToolConverter
 7 | from agents.tool import FileSearchTool, WebSearchTool
 8 | 
 9 | 
10 | def some_function(a: str, b: list[int]) -> str:
11 |     return "hello"
12 | 
13 | 
14 | def test_to_openai_with_function_tool():
15 |     some_function(a="foo", b=[1, 2, 3])
16 | 
17 |     tool = function_tool(some_function)
18 |     result = ToolConverter.to_openai(tool)
19 | 
20 |     assert result["type"] == "function"
21 |     assert result["function"]["name"] == "some_function"
22 |     params = result.get("function", {}).get("parameters")
23 |     assert params is not None
24 |     properties = params.get("properties", {})
25 |     assert isinstance(properties, dict)
26 |     assert properties.keys() == {"a", "b"}
27 | 
28 | 
29 | class Foo(BaseModel):
30 |     a: str
31 |     b: list[int]
32 | 
33 | 
34 | def test_convert_handoff_tool():
35 |     agent = Agent(name="test_1", handoff_description="test_2")
36 |     handoff_obj = handoff(agent=agent)
37 |     result = ToolConverter.convert_handoff_tool(handoff_obj)
38 | 
39 |     assert result["type"] == "function"
40 |     assert result["function"]["name"] == Handoff.default_tool_name(agent)
41 |     assert result["function"].get("description") == Handoff.default_tool_description(agent)
42 |     params = result.get("function", {}).get("parameters")
43 |     assert params is not None
44 | 
45 |     for key, value in handoff_obj.input_json_schema.items():
46 |         assert params[key] == value
47 | 
48 | 
49 | def test_tool_converter_hosted_tools_errors():
50 |     with pytest.raises(UserError):
51 |         ToolConverter.to_openai(WebSearchTool())
52 | 
53 |     with pytest.raises(UserError):
54 |         ToolConverter.to_openai(FileSearchTool(vector_store_ids=["abc"], max_num_results=1))
55 | 


--------------------------------------------------------------------------------
/tests/testing_processor.py:
--------------------------------------------------------------------------------
 1 | from __future__ import annotations
 2 | 
 3 | import threading
 4 | from typing import Any, Literal
 5 | 
 6 | from agents.tracing import Span, Trace, TracingProcessor
 7 | 
 8 | TestSpanProcessorEvent = Literal["trace_start", "trace_end", "span_start", "span_end"]
 9 | 
10 | 
11 | class SpanProcessorForTests(TracingProcessor):
12 |     """
13 |     A simple processor that stores finished spans in memory.
14 |     This is thread-safe and suitable for tests or basic usage.
15 |     """
16 | 
17 |     def __init__(self) -> None:
18 |         self._lock = threading.Lock()
19 |         # Dictionary of trace_id -> list of spans
20 |         self._spans: list[Span[Any]] = []
21 |         self._traces: list[Trace] = []
22 |         self._events: list[TestSpanProcessorEvent] = []
23 | 
24 |     def on_trace_start(self, trace: Trace) -> None:
25 |         with self._lock:
26 |             self._traces.append(trace)
27 |             self._events.append("trace_start")
28 | 
29 |     def on_trace_end(self, trace: Trace) -> None:
30 |         with self._lock:
31 |             # We don't append the trace here, we want to do that in on_trace_start
32 |             self._events.append("trace_end")
33 | 
34 |     def on_span_start(self, span: Span[Any]) -> None:
35 |         with self._lock:
36 |             # Purposely not appending the span here, we want to do that in on_span_end
37 |             self._events.append("span_start")
38 | 
39 |     def on_span_end(self, span: Span[Any]) -> None:
40 |         with self._lock:
41 |             self._events.append("span_end")
42 |             self._spans.append(span)
43 | 
44 |     def get_ordered_spans(self, including_empty: bool = False) -> list[Span[Any]]:
45 |         with self._lock:
46 |             spans = [x for x in self._spans if including_empty or x.export()]
47 |             return sorted(spans, key=lambda x: x.started_at or 0)
48 | 
49 |     def get_traces(self, including_empty: bool = False) -> list[Trace]:
50 |         with self._lock:
51 |             traces = [x for x in self._traces if including_empty or x.export()]
52 |             return traces
53 | 
54 |     def clear(self) -> None:
55 |         with self._lock:
56 |             self._spans.clear()
57 |             self._traces.clear()
58 |             self._events.clear()
59 | 
60 |     def shutdown(self) -> None:
61 |         pass
62 | 
63 |     def force_flush(self) -> None:
64 |         pass
65 | 
66 | 
67 | SPAN_PROCESSOR_TESTING = SpanProcessorForTests()
68 | 
69 | 
70 | def fetch_ordered_spans() -> list[Span[Any]]:
71 |     return SPAN_PROCESSOR_TESTING.get_ordered_spans()
72 | 
73 | 
74 | def fetch_traces() -> list[Trace]:
75 |     return SPAN_PROCESSOR_TESTING.get_traces()
76 | 
77 | 
78 | def fetch_events() -> list[TestSpanProcessorEvent]:
79 |     return SPAN_PROCESSOR_TESTING._events
80 | 


---------------------------------------------------------