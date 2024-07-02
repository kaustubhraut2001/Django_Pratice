from django.shortcuts import render
from .models import Test
# from django import response 
# Create your views here.


def index(request):
    return render(request, 'index.html' , {'content':'Kaustubh'}  )

def register(request):
    return render(request, 'register.html' )

def getdatafromDb(request):
    print(Test.objects.all() , "data in the db")
    return render(request , 'dbdata.html' , {'dbdata':Test.objects.all()} );
