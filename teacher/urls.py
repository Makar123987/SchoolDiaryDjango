from django.urls import path

from . import views

urlpatterns = [
    path("", views.teacher_dashboard, name="index"),
    path("lessons/<int:lesson_id>", views.lesson_details, name="index"),
    path("lessons/<int:lesson_id>/set_grade", views.set_grade, name="index")
]