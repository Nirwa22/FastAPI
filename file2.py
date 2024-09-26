from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"Data":4536}
@app.get("/data")
def data():
    return "why"