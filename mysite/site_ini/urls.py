from django.urls import path
from .views import home, generic, contact

urlpatterns =[
    path('',home),
    path('index.html',home),
    path('generic.html',generic),
    path('contact.html',contact),
]