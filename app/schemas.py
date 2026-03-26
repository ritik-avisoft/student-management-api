from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    student_name: str
    student_email: EmailStr
    student_age:int

class StudentResponse(BaseModel):
    student_id:int
    student_name:str
    student_email:EmailStr
    student_age:int

