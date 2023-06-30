from django.db import models


class Nome(models.Model):
    nome = models.CharField(max_length=255)
    mae = models.CharField(max_length=255)
    pai = models.CharField(max_length=255)


class CPF(models.Model):
    cpf = models.CharField(max_length=11)


class RG(models.Model):
    rg = models.CharField(max_length=9)
