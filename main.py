from fastapi import FastAPI
from routes.humboldt_routes import router

app = FastAPI(title="SaberResults API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "SaberResults API is running"}
