from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime

app = FastAPI()

# Enable CORS so your Frontend can talk to your Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your actual frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Connection
MONGO_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client.abad_food_court

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.get("/api/status")
async def get_status():
    return {"status": "online", "timestamp": datetime.now()}

@app.post("/api/contact")
async def post_contact(form: ContactForm):
    try:
        result = await db.contacts.insert_one(form.dict())
        return {"success": True, "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database Error")