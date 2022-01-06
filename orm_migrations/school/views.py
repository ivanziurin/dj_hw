from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student = Student.objects.order_by('group')
    context = {'object_list': student}
    return render(request, template, context)
