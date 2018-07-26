from django.shortcuts import render
from .forms import FormularioContato


def home(request):

    return render(request, 'index.html')

def generic(request):

    return render(request, 'footer.html')
# Create your views here.

def contact(request):
    context = {}
    if request.method == 'POST':
        form = FormularioContato(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()

    context['form'] = FormularioContato()

    template_name = 'contact.html'
    return render(request, template_name, context)

def aviso(request):

    return render(request, 'aviso.html')