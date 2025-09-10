# FastAPI entrypoint
from fastapi import FastAPI


from backend.routers import query, recommendation, summarization

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Retail GenAI Backend Running"}

# Register routers
app.include_router(query.router)
app.include_router(recommendation.router)
app.include_router(summarization.router)
