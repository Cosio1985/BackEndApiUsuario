from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistroUsuarioSerializer

# creamos un endpoint publico para registrar un usuario.
@api_view(['POST'])
@permission_classes([AllowAny]) #se indica que cualquier usuario puede acceder a este endpoint, incluso si no está autenticado
def registrar_usuario(request):
    serializer = RegistroUsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"mensaje": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#2 Endpoint protegido, servirá para obtener el perfil del usuario autenticado
@api_view(['GET'])
@permission_classes([IsAuthenticated]) #solo accesible con token valido
def perfil_usuario(request):
    usuario = request.user
    return Response({
        "id": usuario.id,
        "username": usuario.username,
        "email": usuario.email,
        "nombre_completo": f"{usuario.first_name} {usuario.last_name}"
    }, status=status.HTTP_200_OK) #esta linea indica que la respuesta es exitosa y se devuelve un código de estado 200 OK
