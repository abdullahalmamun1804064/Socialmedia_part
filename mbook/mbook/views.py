from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
         user= request.user
    else:
        user=''
    return render(request,'main/home.html',{'usr':user})