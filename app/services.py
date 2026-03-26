from django_app.models import Student, Course

def get_all_students():
    students = Student.objects.all().values(
        'id', 'student_name', 'student_email', 'student_age'
    )
    return {"data": list(students)}

def get_student_by_id(id):
    student = Student.objects.filter(id=id).values(
        'id', 'student_name', 'student_email', 'student_age'
    )
    return {"data": list(student)}  

def create_student(data):
    student = Student.objects.create(**data.dict())
    return {
        "student_id": student.id,
        "student_name": student.student_name,
        "student_email": student.student_email,
        "student_age": student.student_age,
    }

def add_course(data):
    course = Course.objects.create(**data.dict())
    return {
        "course_id": course.course_id,
        "course_name": course.course_name,
        "course_instructor": course.course_instructor,
    }

def get_all_courses():
    courses = Course.objects.all().values(
       'course_name', 'course_instructor', 'course_id'
    )
    if not courses.exists():
        return None
    return {"data": list(courses)}

def get_course_by_id(id):
    course = Course.objects.filter(course_id=id).values(
        'course_name', 'course_instructor', 'course_id'
    )
    if not course.exists():
        return None
    return {"data": list(course)}