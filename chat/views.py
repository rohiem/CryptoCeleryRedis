from django.shortcuts import render
import requests
from .models import Position
# Create your views here.
def home(request):
    data=Position.objects.all()
    
    return render(request,'index.html',context={"data":data})
