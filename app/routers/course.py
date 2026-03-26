from fastapi import APIRouter, status
from .. import schemas, services
from fastapi import HTTPException

router= APIRouter(
    prefix="/course",
    tags=['Course']
)

@router.get("/list")
def course_list():
    courses = services.get_all_courses()
    if not courses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Not any course added yet")
    return courses

@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_course(course:schemas.CourseCreate):
    return services.add_course(course)

@router.get("/{id}")
def get_course(id: int):
    course = services.get_course_by_id(id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Course with id {id} not found")
    return course