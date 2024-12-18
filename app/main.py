from fastapi import FastAPI, HTTPException
from app.data_loader import load_json
from app.database.chromadb_handler import initialize_chromadb, ingest_data
from app.models.llama_handler import initialize_llama_model
from langchain.prompts import PromptTemplate
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))


llama_model = None
def get_llama_model():
    global llama_model
    if llama_model is None:
        api_key = os.getenv("GROQ_API_KEY")
        llama_model = initialize_llama_model(api_key)
    return llama_model

@app.post("/load")
def setup():
    try:
        data = load_json("data/sample_data.json")
        chromadb_collection = initialize_chromadb()
        ingest_data(chromadb_collection, data)
        return {"status": "success", "message": "Data loaded into ChromaDB successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading data: {str(e)}")

@app.post("/query")
def query_insight(request: QueryRequest):
    question = request.question
    if not question.strip():
        raise HTTPException(status_code=400, detail="Question Cannot be empty")
    try:
        chromadb_collection = initialize_chromadb()
        response = chromadb_collection.query(query_texts=question, n_results=2)
        
        prompt = PromptTemplate.from_template(
            """
                You are an assistant analyzing invoice data. Answer user queries based on the following data:
                {context}
                Question: {question}
                Answer:
            """
        )

        llama_model = get_llama_model()

        chain_insight = prompt | llama_model

        res = chain_insight.invoke({"context":str(response), "question":question})

        content = format_response(res.content)
        return content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def format_response(content: str) -> str:
    try:
        return "\n".join(line.strip() for line in content.splitlines() if line.strip())
    except Exception:
        return content
