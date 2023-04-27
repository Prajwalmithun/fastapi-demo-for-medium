from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
async def root():
    return {"message": "Hello World"}


@app.get("/all")
async def root():
    return {"message": "Displaying all items in the inventory"}