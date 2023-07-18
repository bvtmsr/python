import csv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn
app = FastAPI()

origin = [
    "http://localhost",
    "http://localhost:3000",
]

csv_data=[]

@app.on_event("startup")
async def load_csv_data():
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        csv_data.extend(list(reader))

@app.get('/')
def index():
  return {"message":"Hello Python"}

@app.get('/sample')
def apptest():
    return {"message":csv_data}

@app.get('/sample-api')
def getStoreList():
    df = pd.read_csv("data.csv")
    row_count= df.shape[0]
    json_data = df.to_json(orient="records",)
    data = {"storeList": json_data,"storeCount":row_count,"status": 200}
    return data;  



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)