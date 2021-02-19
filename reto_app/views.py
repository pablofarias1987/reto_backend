from django.shortcuts import render

from rest_framework import generics

from reto_app.models import Credito

from reto_app.serializers import CreditoSerializer

class CreditoList(generics.ListAPIView):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer

class CreditoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credito.objects.all()
    serializer_class = CreditoSerializer