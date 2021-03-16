from django.contrib import admin
from .models import *
import admin_thumbnails

# Register your models here.
admin.site.register(AboutUs)
# admin.site.register(Projects)
# admin.site.register(ProjectImages)
admin.site.register(TeamMember)
admin.site.register(Services)
admin.site.register(SuccessStory)
admin.site.register(Clients)
admin.site.register(ContactUs)
admin.site.register(Counter)

@admin_thumbnails.thumbnail('image')
class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    readonly_fields = ('id',)
    extra = 5

@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('project_title',)}
    inlines = [ProjectImagesInline]