from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from common_data.models import Lesson, StudentClass, Grade, SchoolClass


class Lessons(View):
    def get(self, request, *args, **kwargs):
        all_lessons = Lesson.objects.all()
        all_classes = SchoolClass.objects.all()
        date = datetime.now().strftime("%Y-%m-%d")
        return render(request, 'lessons.html', {
            'all_lessons': all_lessons,
            'all_classes':all_classes,
            "datetime":date
        })

    def post(self, request, *args, **kwargs):
        current_class_id = int(request.POST['sclass_id'])
        current_class = SchoolClass.objects.get(pk=current_class_id)

        current_lesson = Lesson(
            name = request.POST["name"],
            description = request.POST["description"],
            date = request.POST["date"],
            homework = request.POST['homework'],
            room = request.POST['room'],
            sclass = current_class,
            teacher = request.user
        )
        current_lesson.save()

        return redirect(f'/teacher/lessons/#lesson_{current_lesson.id}')



# Create your views here.

def teacher_dashboard(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        classes = SchoolClass.objects.all()
        return render(request, 'teacher_dashboard.html', {
            'lessons': lessons,
            'classes': classes,
        })
    else:
        return redirect('teacher_dashboard')

def lesson_details(request, lesson_id : int):
    if request.method == 'GET':
        current_lesson = Lesson.objects.get(pk=lesson_id)
        grades = Grade.objects.filter(lesson=current_lesson)
        current_class = current_lesson.sclass
        current_students = list(StudentClass.objects.filter(sclass=current_class))
        return render(request, 'lesson.html', {
            'lesson': current_lesson,
            'grades':grades,
            'students':current_students
        })
    else:
        return None

def set_grade(request, lesson_id : int):
    if request.method == 'POST':
        current_student = User.objects.get(pk=int(request.POST['student_id']))
        current_grade = Grade(
            grade = int(request.POST['Grade']),
            student = current_student,
            lesson = Lesson.objects.get(pk=lesson_id)
        )
        current_grade.save()

        return redirect(f'/teacher/lessons/{lesson_id}/')