
from django.shortcuts import render
from Blog.models import Blog
from Projects.models import Projects, Skills

def index(request):
    blogs = Blog.objects.all()
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    data = {'skills' : skills, 'projects' : projects, 'insights' : blogs}
    return render(request,'index.html', data)