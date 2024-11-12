from fastapi import FastAPI, Request
from requests.exceptions import HTTPError
from fastapi.responses import JSONResponse

from server.routes.api import router, user_router, message_router

app = FastAPI()

@app.exception_handler(HTTPError)
async def unicorn_exception_handler(request: Request, exc: HTTPError):
    return JSONResponse(
        status_code=exc.response.status_code,
        content={"message": exc.response.text},
    )

app.include_router(router, tags=["api"], prefix="/api")
app.include_router(user_router, tags=["users"], prefix="/user")
app.include_router(message_router, tags=["message"], prefix="/message")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
