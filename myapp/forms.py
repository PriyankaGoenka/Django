from django import forms

class Signupform(forms.Form):
    first_name=forms.CharField(label="FirstName")
    last_name=forms.CharField(label="LastName")
    email=forms.EmailField(max_length=40)
    password=forms.CharField(widget=forms.PasswordInput)