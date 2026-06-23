from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel, Field
from worker import process_media_task
from celery.result import AsyncResult
from worker import celery_app
from database import Report, engine, Base, SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:     
        yield db
    finally: 
        db.close()

class MediaReport(BaseModel):
    filename: str
    content_type: str
    prediction: str = Field(..., description="The AI's top classification label")
    confidence: float = Field(..., description="Confidence score from 0.0 to 1.0")


@app.get("/health")
def check_status():
    return {
        "project": "The Hidden Eye", 
        "status": "online",
        "version": "1.0.0"
    }


@app.post("/analyze")
async def analyze_media(file: UploadFile = File(...)):
    task = process_media_task.delay(file.filename)
    return {"message": "Order received! AI is processing...", "task_id": task.id}

@app.get("/result/{task_id}")
async def get_result(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    
    if task_result.ready():
        return {"status": "complete", "result": task_result.result}

    return {"status": "processing"}

@app.get("/history")
def get_all_reports(db: Session = Depends(get_db)):
    reports = db.query(Report).all()
    
    formatted_history = []
    for report in reports:
        formatted_history.append({
            "task_id": report.task_id,
            "filename": report.filename,
            "prediction": report.prediction,
            "confidence": report.confidence,
            "created_at": report.created_at
        })
        
    return {"total_reports": len(reports), "history": formatted_history}