from django.shortcuts import render


def home(request):

    return render(request, 'index.html',{'usuario':'Jose Carlos'})

def generic(request):

    return render(request, 'generic.html')
# Create your views here.

def elements(request):

    return render(request, 'elements.html')