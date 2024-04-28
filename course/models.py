from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    TECH_COURSE = 'Tech Courses'
    CBSE_COURSE = 'CBSE Courses'
    CATEGORY_CHOICES = [
        (TECH_COURSE, 'Tech Courses'),
        (CBSE_COURSE, 'CBSE Courses'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=TECH_COURSE)
    grade = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='staticfiles/course_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
    
class QuestionPaper(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='question_papers/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title