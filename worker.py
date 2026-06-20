from celery import Celery
import time

celery_app = Celery( 
                    "media_worker",
                    broker = "redis://redis:6379/0",
                    backend = "redis://redis:6379/0")

@celery_app.task(name = "process_media_task")
def process_media(filename: str):
    print(f"[{filename}] Ticket pulled from Redis! Starting heavy AI processing...")
    time.sleep(10)
    
    print(f"[{filename}] Processing complete!")
    return {"filename": filename, "prediction": "simulated_ai_result", "confidence": 0.99}

