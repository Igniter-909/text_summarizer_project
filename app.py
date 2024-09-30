from fastapi import FastAPI
import uvicorn
import sys
import os
import pandas as pd
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction_pipeline import PredictPipeline

text:str = "What is Text Summarization?"
app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Succesful !!")
    except Exception as e:
        return Response(f"Error: {str(e)}")
    
@app.post("/predict")
async def prediction(text):
    try:
        obj = PredictPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)