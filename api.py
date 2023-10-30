from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Initialize the Instrumentator
#  "/metrics" endpoint is exposed by default
Instrumentator().instrument(app).expose(app)

# /home
@app.get("/home")
async def root():
    return {"message": "Hello World"}

# /all
@app.get("/all")
async def root():
    return {"message": "Displaying all items in the inventory"}


# To run this app   
# uvicorn api:app --reload --port 8000