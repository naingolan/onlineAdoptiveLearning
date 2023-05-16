from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    duration = forms.IntegerField()
    
    title.widget.attrs.update({'class': 'form-control'})
    description.widget.attrs.update({'class': 'form-control'})
    duration.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content']
