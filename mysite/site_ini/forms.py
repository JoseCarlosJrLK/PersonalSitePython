from django import forms
from django.core.mail import send_mail
from django.conf import settings


class FormularioContato(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    mensage = forms.CharField(label='Message', widget=forms.Textarea)

    def send_mail(self):
        subject = 'Contato pelo Site'

        n = self.cleaned_data['name'],
        e = self.cleaned_data['email'],
        m = self.cleaned_data['mensage']

        message = 'Nome: %s; \n\nE-mail: %s; \n\n%s' % (n, e, m)

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
