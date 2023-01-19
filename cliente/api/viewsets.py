from rest_framework import viewsets
from cliente.api import serializers
from cliente import models
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = models.Cliente.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]