from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    Image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Projects(models.Model):
    project_title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, null=True)
    project_image = models.ImageField(upload_to='images', null=True)
    project_country = models.CharField(max_length=80, null=True, blank=True)
    project_desc = models.TextField()

    def __str__(self):
        return self.project_title

    def image_tag(self):
        if self.project_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.project_image.url))
        else:
            return ""
    def get_absolute_url(self):
        return reverse('project_detail', args=[self.id, self.slug])

class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class TeamMember(models.Model):
    member_name = models.CharField(max_length=120, null=True)
    member_image = models.ImageField(upload_to='images/', null=True)
    member_designation = models.CharField(max_length=120, null=True, blank=True)
    member_twitter = models.CharField(max_length=120, null=True, blank=True)
    member_facebook = models.CharField(max_length=120, null=True, blank=True)
    member_linkedin = models.CharField(max_length=120, null=True, blank=True)
    member_github = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return self.member_name

    def image_tag(self):
        if self.member_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.member_image.url))
        else:
            return ""

class Services(models.Model):
    service_title = models.CharField(max_length=120, null=True)
    service_image = models.ImageField(upload_to='images/', null=True)
    service_desc = models.TextField(null=True)

    def __str__(self):
        return self.service_title

    def image_tag(self):
        if self.service_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.service_image.url))
        else:
            return ""

class ServiceImages(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

class SuccessStory(models.Model):
    story_client_name = models.CharField(max_length=120, null=True)
    story_client_image = models.ImageField(upload_to='images', null=True)
    story_client_desig = models.CharField(max_length=120, null=True)
    story_client_message = models.TextField()

    def __str__(self):
        return self.story_client_name
    
    def image_tag(self):
        if self.story_client_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.story_client_image.url))
        else:
            return ""

class Clients(models.Model):
    client_name = models.CharField(max_length=120, null=True)
    client_image = models.ImageField(upload_to='images/', null=True)
    client_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.client_name

    def image_tag(self):
        if self.client_image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.client_image.url))
        else:
            return ""


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class Counter(models.Model):
    clients = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    countries = models.PositiveIntegerField()
    members = models.PositiveIntegerField()

    def __str__(self):
        return "Click here to edit the counter"


