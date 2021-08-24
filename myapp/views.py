from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
context = {
    'name': 'Daniel',
    'age': 20,
    'nat': 'Colombian'

}


def showName(request):
    return render(request, 'name.html', context)


def showAge(request):
    return render(request, 'age.html', context)


def showNat(request):
    return render(request, 'nat.html', context)


def showForm(request):
    return render(request, 'form.html')


def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amoutWords': amount_of_words})


def welcome(request):

    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password2 == password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=userName).exists():
                messages.info(request,'Username Already Used')
                return  redirect('register')
            else:
                user=User.objects.create_user(username=userName, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')







    return render(request, 'register.html')

