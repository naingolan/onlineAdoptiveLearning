from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns...
    path('<int:course_id>/add_lesson/', views.add_lesson, name='add_lesson'),
    path('lesson', views.add_lesson, name="add_lesson"),
    path('course', views.add_course, name="add_course"),
]




