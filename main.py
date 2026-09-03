from fastapi import FastAPI
from pydantic import BaseModel
from backend.database import init_db,insert_lead,all_leads
from backend.ai_agent import score_lead,generate_message
app=FastAPI(title="AI Lead Generation Agent")
class Lead(BaseModel):
    name:str; email:str; company:str=""; industry:str=""; budget:float=0; requirement:str=""; engagement:int=0
@app.on_event("startup")
def startup(): init_db()
@app.get("/")
def home(): return {"message":"AI Lead Generation Agent API is running"}
@app.post("/leads")
def create(lead:Lead):
    d=lead.model_dump(); d["score"],d["category"]=score_lead(d); d["ai_message"]=generate_message(d)
    return {"id":insert_lead(d),**d}
@app.get("/leads")
def get(): return all_leads()
