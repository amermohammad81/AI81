from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from serpapi import GoogleSearch
from fastapi.middleware.cors import CORSMiddleware

# تحميل المفاتيح
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")


# LLM 
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=OPENAI_API_KEY)

# Tool
def search_web(query: str) -> str:
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": SERPAPI_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    try:
        return results["organic_results"][0]["snippet"]
    except:
        return "No results found."

tools = [
    Tool(
        name="WebSearch",
        func=search_web,
        description="Use this tool to search the web for recent or real-time information."
    )
]


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Agent (LLM + WebSearch)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)

# FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_agent(question: Question):
    try:
        response = agent.run(question.query)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def index():
    return {"message": "Agent API is running"}
