from rest_framework import serializers
from api.models import Nome, CPF, RG


class NomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nome
        fields = ("nome", )


class NomeComFiliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nome
        fields = ("nome", "mae", "pai")


class CPFSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPF
        fields = ("cpf", )


class RGSerializer(serializers.ModelSerializer):

    class Meta:
        model = RG
        fields = ("rg", )
