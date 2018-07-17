from django.db import models

# Create your models here.
class SendEmail(models.Model):

    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    areas = models.TextField('Mensagem')

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    uploaded_at = models.DateTimeField('Atualizado em', auto_now=True)