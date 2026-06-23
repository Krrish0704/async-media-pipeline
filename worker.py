from celery import Celery
import time
from database import SessionLocal, Report

celery_app = Celery( 
                    "media_worker",
                    broker = "redis://redis:6379/0",
                    backend = "redis://redis:6379/0")

@celery_app.task(bind=True, name="process_media_task")
def process_media_task(self, filename: str):
    print(f"[{filename}] Ticket pulled from Redis! Starting heavy AI processing...")
    
    time.sleep(10)
    
    prediction = "simulated_ai_result"
    confidence = 0.99

    print(f"[{filename}] Processing complete! Saving to Vault...")

    db = SessionLocal()
    try:
        new_report = Report(
            task_id=self.request.id,
            filename=filename,
            prediction=prediction,
            confidence=confidence
        )
        db.add(new_report)
        db.commit()
    except Exception as e:
        print(f"Database error: {e}")
        db.rollback()
    finally:
        db.close()

    return {"filename": filename, "prediction": prediction, "confidence": confidence}