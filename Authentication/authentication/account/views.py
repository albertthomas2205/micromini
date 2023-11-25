from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
import logging

logger = logging.getLogger(__name__)

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    
    def list(self, request):
        users = User.objects.filter(is_admin = True)
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
      

        return Response(serializer.data, status=200)

    def create(self, request):
        print("haiiii")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
           
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)