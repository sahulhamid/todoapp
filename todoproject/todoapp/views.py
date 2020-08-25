from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import TaskForm
from .forms import Task_Todo_Form

def home(request):
    tasks = TaskForm.objects.all()
    form = Task_Todo_Form()

    if request.method == 'POST':
        form = Task_Todo_Form(request.POST)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('/')

    context ={'tasks':tasks, 'form':form}
    return render(request,'todoapp/home.html',context)


def update(request,pk):
    sel_task = TaskForm.objects.get(id=pk)

    form = Task_Todo_Form(instance=sel_task)

    if request.method == 'POST':
        form = Task_Todo_Form(request.POST,instance=sel_task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'todoapp/update.html', {'form':form})


def delete(request,pk):
    del_task = TaskForm.objects.get(id=pk)
    print(del_task)

    if request.method == 'POST':
        del_tast.delet()
        return redirect('/')

    return render(request, 'todoapp/delete.html')
