# from fastapi import FastAPI
# from pydantic import BaseModel
# from agent import DoctorAppointmentAgent
# from langchain_core.messages import HumanMessage
# import os

# os.environ.pop("SSL_CERT_FILE", None)


# app = FastAPI()

# # Define Pydantic model to accept request body 
# class UserQuery(BaseModel):
#     id_number: int
#     messages: str
# # for the validation that what user are typing num must be int and mst string
# agent = DoctorAppointmentAgent()

# @app.post("/execute")
# def execute_agent(user_input: UserQuery):
#     app_graph = agent.workflow()
    
#     # Prepare agent state as expected by the workflow
#     input = [
#         HumanMessage(content=user_input.messages)
#     ]
#     query_data = {
#         "messages": input,
#         "id_number": user_input.id_number,
#         "next": "",
#         "query": "",
#         "current_reasoning": "",
#     }
#     #config = {"configurable": {"thread_id": "1", "recursion_limit": 100}}  

#     response = app_graph.invoke(query_data,config={"recursion_limit": 20})
#     return {"messages": response["messages"]}



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import DoctorAppointmentAgent
from langchain_core.messages import HumanMessage
import os

os.environ.pop("SSL_CERT_FILE", None)

app = FastAPI()

# Define Pydantic model for request body
class UserQuery(BaseModel):
    id_number: int
    messages: str

agent = DoctorAppointmentAgent()

@app.post("/execute")
async def execute_agent(user_input: UserQuery):
    try:
        app_graph = agent.workflow()
        
        # Prepare agent state
        input_messages = [HumanMessage(content=user_input.messages)]
        query_data = {
            "messages": input_messages,
            "id_number": user_input.id_number,
            "next": "",
            "query": "",
            "current_reasoning": "",
        }

        # Invoke agent with recursion limit
        response = app_graph.invoke(query_data, config={"recursion_limit": 50})
        
        # Ensure response has 'messages' key
        if "messages" not in response:
            raise ValueError("Agent response missing 'messages' key")
        
        return {"messages": response["messages"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")