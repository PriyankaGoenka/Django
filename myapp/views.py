from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def signup(request):
    return render(request,'myapp/signup.html')
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return HttpResponse("This is about us page")
def contact(request):
    return HttpResponse("Contact us here")
 