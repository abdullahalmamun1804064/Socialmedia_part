from django.contrib import messages
from django.shortcuts import render
from .models import profile
from .forms import profile_forms
# Create your views here.

def my_profile_view(request):
    myprofile=profile.objects.get(user=request.user)
    profilform=profile_forms(request.POST or None, request.FILES or None ,instance= myprofile )
    
    if request.method =="POST":
        if profilform.is_valid():
           profilform.save()
           messages.success(request,'Cogertulation!! your profile successfully update')

    dic={
        'myprofile':myprofile,
        'profilform':profilform,
    }
    return render(request,'profiles/myprofile.html',dic)