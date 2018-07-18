from django.shortcuts import render


def home(request):

    return render(request, 'index.html')

def generic(request):

    return render(request, 'footer.html')
# Create your views here.

def contact(request):

    return render(request, 'contact.html')