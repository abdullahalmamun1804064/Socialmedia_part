from django.contrib import admin
from .models import profile,Relationship

@admin.register(profile)
class profile_admin(admin.ModelAdmin):
    list_display=['id','frist_name','last_name','user','bio','email','country','avatar','slug','updated','created']

@admin.register(Relationship)
class profile_admin(admin.ModelAdmin):
    list_display=['id','sender','recever','status','updated','created']

