from fastapi import APIRouter, status, HTTPException
from .. import schemas, services

router = APIRouter(
    prefix="/student",
    tags=['student']
)

@router.get("/list")
def student_list():
    return services.get_all_students()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate):
    return services.create_student(student)

