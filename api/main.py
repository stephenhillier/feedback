"""
Main application entrypoint
"""

import databases
from fastapi import FastAPI, HTTPException
from starlette.responses import Response
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request

from app.config import DATABASE_URI

from app.feedback.models import RatingRequest
from app.feedback.repo import add_rating as repo_add_rating

database = databases.Database(DATABASE_URI)

app = FastAPI(title="Feedback", openapi_url="/api/v1/openapi.json")

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware)


@app.on_event("startup")
async def startup():
    """ run on app startup - get database connection """
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """ run on shutdown """
    await database.disconnect()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/rating")
async def add_rating(rating: RatingRequest, req: Request):

    # if the url was not provided, try to get it from the request header.
    if not rating.url:
        rating.url = req.headers['referer']

    await repo_add_rating(database, rating)
    return {"status": "ok"}
