from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.health_routes import router as health_router
from routes.report_routes import router as report_router
from routes.medicine_routes import router as medicine_router

app = FastAPI(title="Healthcare AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/health")
app.include_router(report_router, prefix="/api/report")
app.include_router(medicine_router, prefix="/api/medicine")


@app.get("/")
def home():
    return {"message": "Healthcare AI Agent is running"}