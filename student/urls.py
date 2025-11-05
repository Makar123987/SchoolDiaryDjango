from django.urls import path
from . import views


urlpatterns = [ path("", views.student_main_page, name="index"),
                path("lessons/", views.lessons_list, name="lessons_list"),
                path("lessons/<int:lesson_id>", views.lesson_details, name="lesson_details"),
                path("my-grades/", views.my_grades, name="my_grades")
                ]