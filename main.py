from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Doc Manager API is running"}
