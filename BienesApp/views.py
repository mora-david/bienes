from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializer import CustomUserSerializer, BienesSerializer
from .models import CustomUSer, Bienes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CustomUserModelViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUSer.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserSerializer

class BienesModelViewSet(ModelViewSet):
    serializer_class = BienesSerializer
    queryset = Bienes.objects.all()
    permission_classes = [IsAuthenticated]

class GetBulkBienesViewSet(ModelViewSet):
    """
    Este Endpoint regresa los ids que se quieran consultar
    recibe por url dichos ids separados por '&', por ejemplo

    /BienesBulk/123&234&890

    regresará los bienes con los ids 123, 234 y 890 en caso de que existan
    """
    queryset = Bienes.objects.none()
    serializer_class = BienesSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def list(self, request, ids):
        queryset = Bienes.objects.filter(id__in=list(ids.split("&")))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
        
    