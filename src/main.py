from fastapi import FastAPI
from src.database import init_db
from src.routes.projects import router as pr_router

app = FastAPI()

init_db()

app.include_router(pr_router, prefix="/api", tags=["projects"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Kanban API"}

# uvicorn src.main:app --reload
# http://127.0.0.1:8000/docs

# Вопросы для ПП:
# 1. add и delete выводят ошибку, хоть и выполняет свою работу
# 2. В projectsModel.py created_at, update_at не работают с str и datetime