# models.py → makemigrations → migrate → table create karta hai pgs me
# python -m django makemigrations django_app --settings=django_app.settings
# python -m django migrate --settings=django_app.settings


from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=100)
    student_address = models.TextField()
    def __str__(self):
        return self.student_name

class Course(models.Model):
    course_id = models.IntegerField(max_length=100)
    course_name = models.CharField(max_length=100)
    course_instructor = models.CharField(max_length=100)
