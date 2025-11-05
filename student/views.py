from datetime import datetime
from django.shortcuts import render, redirect
from common_data.models import Lesson, StudentClass, Grade, SchoolClass
# Create your views here.

def student_main_page(request):
    all_sclass_ids = StudentClass.objects.filter(student=request.user).values_list('sclass_id', flat=True)
    all_lessons = Lesson.objects.filter(sclass_id__in=all_sclass_ids).order_by('-date')
    return render(request, 'student_dashboard.html', {
        'lessons': all_lessons
    })


def lessons_list(request):
    if request.method == 'GET':
        all_lessons = Lesson.objects.all()
        all_classes = SchoolClass.objects.all()
        date = datetime.now().strftime("%Y-%m-%d")
        return render(request, 'lessons.html', {
            'all_lessons': all_lessons,
            'all_classes': all_classes,
            "datetime": date,
            'student': 'student'
        })

def lesson_details(request, lesson_id : int):
    if request.method == 'GET':
        current_lesson = Lesson.objects.get(pk=lesson_id)
        grades = list(Grade.objects.filter(lesson=current_lesson, student=request.user))
        current_class = current_lesson.sclass
        current_students = list(StudentClass.objects.filter(sclass=current_class))
        return render(request, 'lesson.html', {
            'lesson': current_lesson,
            'grades': grades,
            'students': current_students,
            'student':'student'
        })
    else:
        return None

def my_grades(request):
    if request.method == 'GET':
        grades = list(Grade.objects.filter(student=request.user))
        return render(request, 'Student_grades.html', {
            'grades': grades,
        })
    else:
        return None
