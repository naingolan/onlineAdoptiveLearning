from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20, unique=True)
    # Other staff-related fields

    def __str__(self):
        return self.staff_id


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    #enrollments = models.ManyToManyField('Enrollment', through='StudentEnrollment')
    # Other student-related fields

    def __str__(self):
        return self.student_id


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # in minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    duration = models.PositiveIntegerField()  # in minutes
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# class Quiz(models.Model):
#     title = models.CharField(max_length=255)
#     duration = models.PositiveIntegerField()  # in minutes
#     pass_mark = models.PositiveIntegerField()
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# class Question(models.Model):
#     text = models.CharField(max_length=255)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text


# class AnswerOption(models.Model):
#     text = models.CharField(max_length=255)
#     is_correct = models.BooleanField()
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text


# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     enrolled_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(null=True, blank=True)
#     is_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.student} enrolled in {self.course}'


# class StudentEnrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.student} enrolled in {self.enrollment}'


# class StudentLesson(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     started_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(null=True, blank=True)
#     is_completed = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.student} started lesson {self.lesson}'


# class StudentQuiz(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     started_at = models.DateTimeField(auto_now_add=True)
#     completed_at = models.DateTimeField(null=True, blank=True)
#     is_completed = models.BooleanField(default=False)
#     score = models.PositiveIntegerField(default=0)
#     selected_answers = models.ManyToManyField(AnswerOption, blank=True)

#     def __str__(self):
#         return f"{self.student} - {self.quiz}"