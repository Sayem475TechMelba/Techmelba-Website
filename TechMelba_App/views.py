from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
# Create your views here.

class Home(View):
    def get(self, request):
        client = Clients.objects.all()
        success = SuccessStory.objects.all()
        all_projects = Projects.objects.all()
        count = Counter.objects.all()
        context = {
            'client':client,
            'success':success,
            'all_projects': all_projects,
            'count':count
        }
        return render(request, 'Home/home.html', context)

class About(View):
    def get(self, request):
        return render(request, 'Home/about.html')

class Contact(View):
    def get(self, request):
        return render(request, 'Home/contact.html')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        message = request.POST['message']

        cont = ContactUs(
            name=name,
            email=email,
            contact = contact,
            message = message
        )
        cont.save()
        messages.success(request, 'You message has been sent!')
        return render(request, 'Home/contact.html')


class OurProject(View):
    def get(self, request):
        all_project = Projects.objects.all()
        context = {
            'all_project': all_project
        }
        return render(request, 'Home/projects.html', context)

class ProjectDetail(View):
    def get(self, request, id, slug):
        project = get_object_or_404(Projects, id=id, slug=slug)
        images = ProjectImages.objects.filter(project_id=id)
        
        context = {

			'project': project,
            'images' : images
		}
        return render(request, 'Home/project_detail.html', context)

class Service(View):
    def get(self, request):
        return render(request, 'Home/service.html')

class Team(View):
    def get(self, request):
        members = TeamMember.objects.all()
        context = {
            'members':members
        }
        return render(request, 'Home/team.html', context)
