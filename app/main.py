import sys
import os
import db

from fastapi import FastAPI
from . routers import student,course

app = FastAPI()

app.include_router(student.router)
app.include_router(course.router)

@app.get("/")
def read_root():
    return {"Hello": "Student"}
