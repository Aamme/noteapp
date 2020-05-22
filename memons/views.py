from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *
from .forms import *
# Create your views here.

class daries(View):
    def get(self, request):
        return render(request, 'memons/index.html', {})


class Notes(View):
    def get(self, request):
        return render(request, 'memons/notes.html', {})

    def post(self, request):
        title = request.POST['title']
        body = request.POST['body']

        note = Diry()
        note.title = title
        note.body = body
        note.save()
        return render(request, 'memons/notes.html', {})


class Register(View):
    signup = RegisterForm()

    def get(self, request):
        context = {'forms': self.signup}
        return render(request, 'memons/register.html', context)

    def post(self, request):
        forms = RegisterForm(request.POST)
        context = {'forms': self.signup}

        if forms.is_valid():
            username = forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            fname = forms.cleaned_data['firstname']
            lname = forms.cleaned_data['lastname']
            address = forms.cleaned_data['address']
            streetno = forms.cleaned_data['streetno']
            postalcode = forms.cleaned_data['postalcode']
            password = forms.cleaned_data['password']
            conpassword = forms.cleaned_data['conformpassword']
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=fname, last_name=lname)

        else:
            context['errors'] = 'This Form is not valid please try again'

        return render(request, 'memons/register.html', context)