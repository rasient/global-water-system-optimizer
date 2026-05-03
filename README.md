## 🧠 Part of Systems Lab

This project is part of a broader exploration:

→ understanding how systems behave when treated as interconnected

Main repo:
https://github.com/rasient/systems-lab

# Global Water System Optimizer

A Streamlit prototype that translates systems-thinking water posts into an interactive decision-support tool.

The core idea:

> Water scarcity is often not only a supply problem. It is a system design problem: retention, soil, infrastructure, irrigation efficiency, reuse, governance, and climate pressure interact.

## What the app does

- Models a simplified regional water system
- Lets users change water-system parameters with sliders
- Calculates a Water System Resilience Score
- Shows bottlenecks such as runoff, poor retention, weak governance, low irrigation efficiency, and urban drainage loss
- Recommends interventions such as:
  - water retention
  - soil restoration
  - precision irrigation
  - reuse and leak reduction
  - landscape-level interventions
  - smart urban design
  - governance and coordination improvements
- Optionally uses the OpenAI API to generate a strategy memo from the current scenario

## Why this matters

The project is based on a systems-thinking framing:

- We are not just “watering crops”.
- We are optimizing a constrained resource inside a climate-stressed system.
- More water supply does not solve the issue if the system keeps losing water.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
streamlit run app/main.py
```

## Optional ChatGPT / OpenAI connector

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

Then enable the AI strategy memo inside the Streamlit app.

If no API key is provided, the app still works fully with rule-based recommendations.

## Project structure

```text
global_water_system_optimizer/
├── app/
│   ├── main.py
│   ├── water_model.py
│   └── ai_connector.py
├── data/
│   └── example_scenarios.csv
├── docs/
│   └── linkedin_announcement.md
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Example use cases

- LinkedIn portfolio project
- Sustainability / water systems demo
- Systems-thinking proof of work
- AI + infrastructure + climate strategy prototype
- Consulting-style scenario simulator

## Disclaimer

This is an educational prototype, not a hydrological engineering model. Real-world water planning requires local data, expert validation, legal review, and environmental assessment.
