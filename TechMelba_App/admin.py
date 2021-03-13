from django.contrib import admin
from .models import *
import admin_thumbnails

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(Projects)
admin.site.register(ProjectImages)
admin.site.register(TeamMember)
admin.site.register(Services)
admin.site.register(SuccessStory)
admin.site.register(Clients)
admin.site.register(ContactUs)
admin.site.register(Counter)