from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('showName/', views.showName, name='showName'),
    path('showAge/', views.showAge, name='showAge'),
    path('showNat/', views.showNat, name='showNat'),
    path('showForm/', views.showForm, name='showForm'),
    path('showForm/counter', views.counter, name='counter')
]