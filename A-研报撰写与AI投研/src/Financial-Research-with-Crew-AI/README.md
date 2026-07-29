# Financial Researcher Crew

An automated two-agent CrewAI workflow that researches a company and produces a polished market-style report. The crew runs a researcher to gather facts, then an analyst to synthesize a final write-up saved to `output/report.md`.

## Requirements
- Python 3.10–3.12
- API keys for the models/tools you enable (e.g., `GROQ_API_KEY`, `DEEPSEEK_API_KEY`, optionally `SERPER_API_KEY` if you turn the Serper search tool back on)

## Setup
1) Create and activate a virtual environment.
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2) Install dependencies from the project metadata.
   ```bash
   pip install -e .
   ```
3) Export your API keys (or place them in a `.env` file that your environment loads).
   ```bash
   export GROQ_API_KEY=...
   export DEEPSEEK_API_KEY=...
   # export SERPER_API_KEY=...  # only if you enable SerperDevTool in crew.py
   ```

## Running the crew
Execute the entry point (uses `inputs = {'company': 'Apple'}` by default):
```bash
python -m financial_researcher.main
# or just
financial_researcher
```

The crew runs sequentially (research → analysis). The final markdown report is printed to the terminal and written to `output/report.md`.

## Customizing
- **Target company**: edit the `inputs` dict in `src/financial_researcher/main.py`.
- **Agent behavior**: adjust roles/goals/models in `src/financial_researcher/config/agents.yaml`.
- **Tasks & formatting**: tweak prompts and output file paths in `src/financial_researcher/config/tasks.yaml`.
- **Tools**: uncomment `SerperDevTool()` in `src/financial_researcher/crew.py` and set `SERPER_API_KEY` if you want web search.

## Project layout
- `src/financial_researcher/main.py` — CLI entry that kicks off the crew and writes the report.
- `src/financial_researcher/crew.py` — crew, agents, and task wiring.
- `src/financial_researcher/config/agents.yaml` — agent definitions (roles, goals, LLMs).
- `src/financial_researcher/config/tasks.yaml` — task prompts and output target.
- `output/report.md` — generated report (will be created/overwritten on each run).

## Notes
- The sample report in `output/report.md` is generated content; running the crew again will regenerate it for the configured company.
- CrewAI runs can be verbose; keep logs if you need traceability.
