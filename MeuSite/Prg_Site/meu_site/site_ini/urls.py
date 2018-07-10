from django.urls import path
from .views import home, generic, elements

urlpatterns =[
    path('',home),
    path('index.html',home),
    path('generic.html',generic),
    path('elements.html',elements),
]