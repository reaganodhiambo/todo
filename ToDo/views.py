from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    todo_list = ToDo.objects.order_by('id')

    context = { 'todo_list': todo_list }
    
    return render(request, 'ToDo/index.html', context)