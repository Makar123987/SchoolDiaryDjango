from django.urls import path
from . import views

urlpatterns = [ path("", views.student_main_page, name="index"),
                path("lessons/", views.lessons_list, name="index"),
                path("lessons/<int:lesson_id>", views.lesson_details, name="index"),
                path("my-grades/", views.my_grades, name="index")
                ]