from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
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

