from django.shortcuts import render
from django.views import View
from django.contrib import messages

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'Home/home.html')

class About(View):
    def get(self, request):
        return render(request, 'Home/about.html')

class Contact(View):
    def get(self, request):
        return render(request, 'Home/contact.html')

    def post(self, request):
        name = request.POST['name']
        image = request.POST['image']
        contact = request.POST['contact']
        message = request.POST['message']

        cont = ContactUs(
            name=name,
            image=image,
            contact = contact,
            message = message
        )
        cont.save()
        messages.success(request, 'You message has been sent!')
        return render(request, 'Home/contact.html')


class Projects(View):
    def get(self, request):
        return render(request, 'Home/projects.html')

class Service(View):
    def get(self, request):
        return render(request, 'Home/service.html')

class Team(View):
    def get(self, request):
        return render(request, 'Home/team.html')
