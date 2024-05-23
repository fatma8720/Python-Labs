from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/list.html', context={'students': students})

def student_details(request, name):
    student = Student.objects.filter(name=name).first()
    return render(request, 'student/details.html', context={'student': student})

def student_add(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        year = request.POST.get('year')
        if name and course and year:
            Student.objects.create(name=name, course=course, year=year)
            return redirect(Student.get_list_url())
        else:
            context['msg'] = 'Please provide name, course, and year'
    return render(request, 'student/add.html', context)

def student_update(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        year = request.POST.get('year')
        if name and course and year:
            student.name = name
            student.course = course
            student.year = year
            student.save()
            return redirect(Student.get_list_url())
    return render(request, 'student/update.html', context={'student': student})

def student_delete(request, id):
    student = Student.objects.filter(id=id).delete()
    return redirect('student_list')

