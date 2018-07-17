from django import forms



class FormularioContato(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    mensage = forms.CharField(label='Mensagem', widget=forms.Textarea)