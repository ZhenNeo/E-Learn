from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Course, Enrollment, QuestionPaper

def enrolled_courses(request):
    user_enrollments = Enrollment.objects.filter(user=request.user)
    enrolled_courses = [enrollment.course for enrollment in user_enrollments]
    return render(request, 'enrolled_courses.html', {'enrolled_courses': enrolled_courses})

def previous_question_papers(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    question_papers = QuestionPaper.objects.filter(course=course)
    data = {
        'selected_course': course.title,
        'question_papers': [{'title': qp.title, 'year': qp.year, 'file_url': qp.file.url} for qp in question_papers]
    }
    return JsonResponse(data)