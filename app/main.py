from fastapi import FastAPI

from app.controllers.user_controller import router as user_router
from app.database import Base, engine
from dotenv import load_dotenv
import os
import uvicorn


load_dotenv()

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the user routes
app.include_router(user_router, prefix="/api", tags=["users"])

if __name__ == "__main__":
    port = os.getenv("PORT", 8000)
    uvicorn.run(app, host="127.0 0.1", port=int(port), reload=True)


