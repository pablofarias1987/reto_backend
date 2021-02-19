from rest_framework import serializers

from reto_app.models import Credito

class CreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credito
        fields = ('id', 'codigo','deuda', 'monto', 'cliente', 'puntaje')
