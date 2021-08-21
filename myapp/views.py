from django.shortcuts import render
from django.http import HttpResponse
from.models import Feature
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

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast 1'
    feature1.details = 'Our service is very quick'
    feature1.isTrue = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Fast 2'
    feature2.details = 'Our service is very quick'
    feature2.isTrue = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Fast 3'
    feature3.details = 'Our service is very quick'
    feature3.isTrue = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Fast 4'
    feature4.details = 'Our service is very quick'
    feature4.isTrue = True


    features = [feature1,feature2,feature3,feature4]
    return render(request, 'index.html', {'features': features})
