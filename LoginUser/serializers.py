from rest_framework import serializers
from django.contrib.auth.models import User

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #generamos una lista de campos que se van a usar para el registro de usuario
        fields = ['username','email','password','first_name','last_name']
        #el extra_kwargs sirve para indicar que el campo password es de solo escritura, es decir, no se va a mostrar en las respuestas de la API
        extra_kwargs ={'password': {'write_only': True}}
        
    def create(self, validated_date):
        #usamos create_user para que la contraseña se guarde encriptada en la BD
        user = User.objects.create_user(
            username=validated_date['username'],
            email=validated_date['email'],
            password=validated_date['password'],
            first_name=validated_date['first_name'],
            last_name=validated_date['last_name']   
        )
        return user