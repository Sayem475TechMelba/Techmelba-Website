from django.contrib import admin
from .models import *
import admin_thumbnails
from django_summernote.admin import SummernoteModelAdmin


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(Services)
admin.site.register(Counter)

@admin_thumbnails.thumbnail('image')
class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    readonly_fields = ('id',)
    extra = 5


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ['project_title', 'slug', 'project_country', 'image_tag']
    prepopulated_fields={'slug':('project_title',)}
    inlines = [ProjectImagesInline]
admin.site.register(Projects, ProjectAdmin)

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name','image_tag' ]

@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'message' ]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'member_designation', 'image_tag' ]
    search_fields = ['member_name'] 

class SuccessStoryAdmin(SummernoteModelAdmin):
    list_display = ['story_client_name', 'story_client_desig', 'story_client_message', 'image_tag'] 
    search_fields = ['story_client_name']  
admin.site.register(SuccessStory, SuccessStoryAdmin)

