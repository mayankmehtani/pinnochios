from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    password_confirm = forms.CharField(max_length=30)