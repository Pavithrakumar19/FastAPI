from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return "helloooooo"
@app.get("/hollo")
def hello():
    return {"message":"hiiiiiii"}