from fastapi import FastAPI
from app.api.v1.routes import solution

app = FastAPI(
    title="Domain API",
    description="Backend API for managing solutions",
    version="1.0.0"
)

app.include_router(solution.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Welcome to Domain API"}