from django.shortcuts import render

# Create your views here.
from .models import *
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        en = Portfolio(name = name , email = email , mobile = mobile ,text = message )
        en.save()
        
    return render(request , "index.html")