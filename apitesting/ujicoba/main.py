import json
from fastapi import FastAPI, HTTPException
with open("data.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get("/")
async def root():
    return {"Page": "Root"}

@app.get('/mhs/{item}')
async def read_mhs():
    dictMhs = []
    for dataMhs in data['data']:
        dictMhs.append(dataMhs)
    return dictMhs
    
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )