from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Project

@login_required
def home(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, "home.html", {"projects": projects})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        url = request.POST.get('url')
        project = Project.objects.create(title=title, description=description, image=image, url=url, owner=request.user)
        return redirect('home')
    return render(request, 'create_project.html')