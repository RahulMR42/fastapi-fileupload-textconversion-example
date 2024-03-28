import os
import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


from routers import files

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(files.router)

@app.get("/")
async def health():
    return {"message": "Hello Wish you Good Health!"}

if __name__ == "__main__":
    port = os.getenv('PORT', default=5000)
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
