# from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def hello(request, username):
    return HttpResponse("Hello %s" % username)


def about(request):
    username = 'delfin'
    return render(request, 'about.html', {
        'username': username
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    c = 0
    for p in projects:
        c += 1
    return render(request, 'projects/projects.html', {
        'projects': projects,
        'c': c
    })


def tasks(request):
    # task = Task.objects.get(title = title)
    tasks = Task.objects.all()
    c_t = 0
    for t in tasks:
        c_t += 1
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks,
        'c_t': c_t
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=request.POST['project'])
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    c_t = 0
    for t in tasks:
        c_t += 1
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks,
        'c_t': c_t
    })


def delete_task(request, id):
    task = Task.objects.filter(id=id)
    task.delete()
    return redirect ('tasks')


def delete_project(request, id):
    project = Project.objects.filter(id=id)
    project.delete()
    return redirect ('projects')


def true_task(request, id):
    task = Task.objects.get(id=id, done=False)
    task.done = True
    Task.id = task.save()
    return redirect ('tasks')
