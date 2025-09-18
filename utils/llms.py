import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

class LLMModel:
    def __init__(self, model_name="gpt-4o"): # checking the model name is there or not if not then error
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name  # other wise i am taking the model name and initializin
        self.openai_model=ChatOpenAI(model=self.model_name)
        
    def get_model(self):
        return self.openai_model

if __name__ == "__main__":
    llm_instance = LLMModel()  
    llm_model = llm_instance.get_model()
    response=llm_model.invoke("hi")

# this is for the testing file that model is woring or not.

    print(response)
    
    # created the class for LLM model, LLMModel
    