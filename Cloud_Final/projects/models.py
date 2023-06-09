import email
import uuid
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from. import dic



class usuario(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Ubcacion = models.CharField(max_length=200)
    Direccion = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    tipo_doc = models.IntegerField(choices=dic.TIPO_DOC,blank=False)
    N_doc = models.IntegerField()
    N_cel = models.IntegerField()
    Medio_trans = models.CharField(max_length=200)
    Fecha_exp = models.DateTimeField(auto_now_add=True)

    def _str_(self) -> str:
        return self.Nombre + ' (#' + self.contraseña+ ')'



    



