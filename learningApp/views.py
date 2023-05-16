from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def add_lesson(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form, 'course': course})
