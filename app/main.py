from fastapi import FastAPI
from app.api.creative_routes import router

app = FastAPI(title="Creative Block API")

app.include_router(router)
