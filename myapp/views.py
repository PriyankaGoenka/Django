from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.
def signup(request):
    return render(request,'myapp/signup.html')
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return HttpResponse("This is about us page")
def contact(request):
    return HttpResponse("Contact us here")
 
def form_view(request):
    form=forms.Signupform
    return render(request,'myapp/register.html',{'form':form})