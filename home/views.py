from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False,'name':'Chirag'} 
    if request.method == "POST":
        task = request.POST['task']
        desc = request.POST['desc']
        print('Data addded')
        ins = Task(taskTitle= task,taskDesc = desc)
        ins.save()
        context = {'success': True } 

    return render(request,'index.html',context)

def task(request):
    alltask = Task.objects.all()
    #for item in alltask:
       # print(item.taskTitle)
    context={'tasks':alltask}
    return render(request,'task.html',context)    
