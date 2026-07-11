
from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="Data Scraper V2")
app.include_router(health_router)

@app.get("/")
def root():
    return {"message":"Data Scraper V2 API"}
