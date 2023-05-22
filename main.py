from fastapi import FastAPI
from app.api import projects_images_coonection
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Test Task Api",
    description="""Test Task API""",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "*",
    "https://8000-upendrasing-dzinlyfront-6e5arjxjwya.ws-us95.gitpod.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects_images_coonection.router)