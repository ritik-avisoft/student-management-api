import sys
import os
import db

from fastapi import FastAPI
from . routers import student

app = FastAPI()

app.include_router(student.router)


@app.get("/")
def read_root():
    return {"Hello": "Student"}
