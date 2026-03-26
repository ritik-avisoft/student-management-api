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

@router.get("/{id}")
def get_student(id: int):
    student = services.get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Student with id {id} not found")
    return student
