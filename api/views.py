from rest_framework import views, viewsets
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from api.serializers import NomeSerializer, NomeComFiliacaoSerializer, CPFSerializer, RGSerializer
from api.models import Nome, CPF, RG
from PyFakeDados.nome import gerar_nome, gerar_nome_completo, gerar_nome_com_filiacao
from PyFakeDados.cpf import gerar_cpf
from PyFakeDados.rg import gerar_rg


class NomeView(views.APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        nome = Nome(nome=gerar_nome())
        serializer = NomeSerializer(nome)
        return Response(serializer.data)


class NomeCompletoView(views.APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        nome = Nome(nome=gerar_nome_completo())
        serializer = NomeSerializer(nome)
        return Response(serializer.data)


class NomeComFiliacaoView(views.APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        nomes = gerar_nome_com_filiacao()
        nome = Nome(
            nome=nomes[0],
            mae=nomes[1],
            pai=nomes[2],
        )
        serializer = NomeComFiliacaoSerializer(nome)
        return Response(serializer.data)


class CPFView(views.APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        cpf = CPF(cpf=gerar_cpf())
        serializer = CPFSerializer(cpf)
        return Response(serializer.data)


class RGView(views.APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        rg = RG(rg=gerar_rg())
        serializer = RGSerializer(rg)
        return Response(serializer.data)
