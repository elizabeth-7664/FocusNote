from fastapi import FastAPI

app = FastAPI(title="FocusNote API")

@app.get("/")
def home():
    return {"message": "FocusNote backend is live "}