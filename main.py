from fastapi import FastAPI
from routes.results import router

app = FastAPI(title="SaberResults API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "SaberResults API is running"}
