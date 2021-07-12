from .models import CustomUSer, Bienes
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken



class CustomUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUSer
        fields = ('usuario','nombre','password','token')
        read_only_fields = ('token',)
        extra_kwargs = {'password': {'write_only': True,
        'style':{'input_type': 'password', 'placeholder': 'Password'}}}

    def get_token(self, user):
        tkn = RefreshToken.for_user(user)
        return {'access':str(tkn.access_token)}

    def validate_password(self, value: str) -> str:
        return make_password(value)

class CustomUserReadOnly(serializers.ModelSerializer):
    class Meta:
        model = CustomUSer
        fields = ('id','usuario','nombre')


class BienesSerializer(serializers.ModelSerializer):
    usuario = CustomUserReadOnly(source="usuario_id", read_only=True)

    class Meta:
        model = Bienes
        fields = ('id','usuario', 'articulo','descripcion','created_at','updated_at','usuario_id')
        read_only_fields = ('usuario','id')
        extra_kwargs = {'usuario_id': {'write_only': True}}