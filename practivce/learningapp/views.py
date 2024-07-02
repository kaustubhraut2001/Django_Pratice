from django.shortcuts import render
# from django import response 
# Create your views here.


def index(request):
    return render(request, 'index.html' , {'content':'Kaustubh'}  )

def register(request):
    return render(request, 'register.html' )
