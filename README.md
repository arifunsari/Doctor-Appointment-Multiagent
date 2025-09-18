```
conda create -p venv python=3.10 -y
```

```
conda activate ./venv
```

```
pip install -r requirements.txt
```
# Doctor Appointment Multiagent System

A LangChain-based multi-agent system for checking doctor availability and booking appointments, using FastAPI (backend) and Streamlit (frontend).

## Setup
1. Clone the repo: `git clone https://github.com/yourusername/doctor-appointment-multiagent.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up `.env` with API keys (e.g., GROQ_API_KEY, OPENAI_API_KEY).
4. Run FastAPI: `python -m uvicorn main:app --reload --port 8002`
5. Run Streamlit: `python -m streamlit run streamlit_ui.py`

## Features
- Agent-based query routing for information and booking.
- Tools for availability checks and appointment management.

## Requirements
- Python 3.10+
- See `requirements.txt`.
