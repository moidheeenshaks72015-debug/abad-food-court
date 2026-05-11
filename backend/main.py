from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    phone: str
    message: str

@app.get("/")
def read_root():
    return {"status": "Abad Food Court API is running"}

@app.post("/contact")
async def contact(form: ContactForm):
    # This is a placeholder for your DB logic
    return {"message": "Success"}
