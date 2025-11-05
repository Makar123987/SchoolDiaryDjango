from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User
# Create your models here.

class SchoolClass(models.Model):
    class_name = models.CharField(max_length=100)

class StudentClass(models.Model):
    student = ForeignKey(User, on_delete=models.CASCADE)
    sclass = ForeignKey(SchoolClass, on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    teacher = ForeignKey(User, on_delete=models.CASCADE)
    sclass = ForeignKey(SchoolClass, on_delete=models.CASCADE)
    homework = models.TextField()
    lesson_type = models.IntegerField(null=True, blank=True)
    room = models.CharField(max_length=100)

class Grade(models.Model):
    student = ForeignKey(User, on_delete=models.CASCADE)
    lesson = ForeignKey(Lesson, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.student.username} — {self.lesson.name}: {self.grade}"

