from django_app.models import Student

def get_all_students():
    students = Student.objects.all().values(
        'id', 'student_name', 'student_email', 'student_age'
    )
    return {"data": list(students)}

def create_student(data):
    student = Student.objects.create(**data.dict())
    return {
        "student_id": student.id,
        "student_name": student.student_name,
        "student_email": student.student_email,
        "student_age": student.student_age,
    }