from django.contrib import admin
from .models import Course, Enrollment, QuestionPaper

class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'subject', 'course')

admin.site.register(QuestionPaper, QuestionPaperAdmin)
admin.site.register(Course)
admin.site.register(QuestionPaper)