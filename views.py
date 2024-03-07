from django.http import JsonResponse
from django.shortcuts import render

from myapplication.models import Employees
from myapplication.serializers import EmployeeSerializer


# Create your views here.
def employee_list(request):
    employees = Employees.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse({'employees', serializer.data})