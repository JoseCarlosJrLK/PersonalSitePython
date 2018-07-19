from django.urls import path
from .views import home, generic, contact, aviso

urlpatterns =[
    path('',home),
    path('index.html',home),
    path('aviso.html',aviso),
    path('generic.html',generic),
    path('contact.html',contact),
]