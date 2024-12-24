from fastapi import FastAPI
from src.database import init_db
from src.routes.projects import router as pr_router
from src.routes.columns import router as cl_router
from src.routes.tasks import router as ts_router
from src.routes.users import router as us_router

app = FastAPI()

init_db()

app.include_router(us_router, prefix="/api", tags=["users"])
app.include_router(pr_router, prefix="/api", tags=["projects"])
app.include_router(cl_router, prefix="/api", tags=["columns"])
app.include_router(ts_router, prefix="/api", tags=["tasks"])

# uvicorn src.main:app --reload
# http://127.0.0.1:8000/docs

# pipreqs .