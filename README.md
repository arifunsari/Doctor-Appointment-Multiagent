
```markdown
# Doctor-Appointment-Multiagent

A multi-agent system for managing doctor appointments, leveraging LangChain, FastAPI (backend), and Streamlit (frontend). This project enables users to check doctor availability, book, cancel, or reschedule appointments through an intuitive interface, powered by intelligent agents.

## Features
- **Multi-Agent System**: Uses LangChain and LangGraph for agent-based query routing (information and booking).
- **FastAPI Backend**: Handles API requests and agent workflows.
- **Streamlit UI**: Provides a user-friendly interface for interacting with the system.
- **Tools**: Supports availability checks, appointment scheduling, cancellation, and rescheduling.
- **Scalable Design**: Modular structure for easy extension and maintenance.

## Folder Structure
```
Doctor-Appointment-Multiagent/
├── agent.py                # Agent logic and workflow
├── main.py                 # FastAPI application
├── streamlit_ui.py         # Streamlit frontend
├── data/                   # Data files (e.g., doctor_availability.csv)
├── data_models/            # Data models (e.g., models.py)
├── doctor_appointment_agentic.egg-info/  # Build artifacts
├── notebook/               # Jupyter notebooks (e.g., multiagent_system.ipynb)
├── prompt_library/         # Prompt definitions
├── requirements.txt        # Project dependencies
├── requirements_backup.txt # Backup of dependencies
├── setup.py                # Setup script
├── toolkit/                # Tools for agent actions
├── utils/                  # Utility functions (e.g., llms.py)
├── .gitignore              # Ignored files (e.g., .env, venv)
└── README.md               # This file
```

## Setup

### Prerequisites
- Python 3.10+
- Git (for cloning the repository)
- An OpenAI API key (for LangChain integration)

### Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/arifunsari/Doctor-Appointment-Multiagent.git
   cd Doctor-Appointment-Multiagent
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Add `.env` to `.gitignore` to avoid committing sensitive data.

4. **Run the Application**:
   - Start the FastAPI backend:
     ```
     python -m uvicorn main:app --reload --port 8002
     ```
   - In a separate terminal, start the Streamlit UI:
     ```
     python -m streamlit run streamlit_ui.py
     ```
   - Access the UI at `http://localhost:8501` (default Streamlit port).

## Usage
- **Enter User ID**: Input a valid integer ID in the Streamlit interface.
- **Submit Query**: Type a query (e.g., "Can you check if a dentist is available tomorrow at 10 AM?") and click "Submit Query".
- **Responses**: The system will display availability or booking status based on agent processing.

## Development
- **Adding Features**: Extend `agent.py` for new agent logic or `toolkit/toolkits.py` for additional tools.
- **Testing**: Use the Jupyter notebook (`notebook/multiagent_system.ipynb`) for experimentation.
- **Contributing**: Fork the repository, create a branch, and submit a pull request.

## Known Issues
- The system may report "technical issues" if the backend API or tools fail. Check `toolkit/toolkits.py` for database or API connectivity issues.
- Ensure the OpenAI API key is valid and has sufficient credits.

## License
This project is currently unlicensed. Consider adding a license (e.g., MIT) in the future via GitHub's license selector.

## Acknowledgments
- Built with inspiration from LangChain and Streamlit communities.
- Thanks to Grok for assistance in development!

```

---

### Explanation
- **Overview**: Introduces the project and its core features, aligning with your multi-agent system.
- **Folder Structure**: Lists your current files and directories, making it easy for others to navigate.
- **Setup**: Provides step-by-step instructions, including environment variable setup for security.
- **Usage**: Simple guide for end-users.
- **Development**: Encourages contributions and highlights the notebook for testing.
- **Known Issues**: Addresses the "technical issue" you mentioned earlier, guiding users to troubleshoot.
- **License and Acknowledgments**: Placeholder for future licensing and a nod to your development process.

```
conda create -p venv python=3.10 -y
```

```
conda activate ./venv
```

```
pip install -r requirements.txt


