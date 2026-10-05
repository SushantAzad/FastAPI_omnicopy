from fastapi import FastAPI,HTTPException, Response
from datetime import datetime
from typing import Any
import random
app = FastAPI(root_path="/api/v1")

data = [
    {"campaigns_id": 1,
     "name":"Black friday",
     "due_date": datetime.now(),
     "created_at":datetime.now()
     },
    {"campaigns_id": 2,
     "name":"BBD",
     "due_date": datetime.now(),
     "created_at":datetime.now()},
    {"campaigns_id": 3,
     "name":"amazon day",
     "due_date": datetime.now(),
     "created_at":datetime.now()}
]
# @app.get("/")
# async def root():
#     return{"message":"Hello world"}

@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns":data}

@app.get("/campaigns/{id}")
async def read_campaigns(id : int):
    for campaign in data:
        if campaign.get("campaigns_id")==id:
            return {"campaign": campaign}
    raise HTTPException(status_code=404)

@app.post("/campaigns/")
async def create_campaigns(body: dict[str,Any]):
    new : Any = {"campaigns_id": random.randint(100,1000),
     "name":body.get("name"),
     "due_date": body.get("due_date"),
     "created_at":datetime.now()}

    data.append(new)
    return{"campaign":new}

@app.patch("/campaigns/{id}")
async def update_campaigns(id: int, body: dict[str, Any]):
    for index, campaign in enumerate(data):
        if campaign.get("campaigns_id") == id:

            updated: Any = {
                "campaigns_id": id,
                "name": body.get("name"),
                "due_date": body.get("due_date"),
                "created_at": campaign.get("created_at")
            }

            data[index] = updated
            return {"campaign": updated}

    raise HTTPException(status_code=404)

@app.delete("/campaigns")
async def remove_campaign(id : int):
    for index, campaign in enumerate(data):
        if campaign.get("campaigns_id") == id:
            data.pop(index)
            return Response(status_code =204)
    raise HTTPException(status_code  = 404)
