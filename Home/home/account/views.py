from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from .serializer import UserRegisterSerializer,MyTokenObtainPairSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView

from rest_framework.exceptions import AuthenticationFailed,ParseError
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView


from .producer import publish


class RegisterView(APIView):
    
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE,)  
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        
        content ={'Message':'User Registered Successfully'}
        return Response(content,status=status.HTTP_201_CREATED,)
    


class LoginView(APIView):
    user = User.objects.all()
    print(user)
    def post(self,request):
        try:
            email = request.data['email']
            password =request.data['password']
        
        except KeyError:
            raise ParseError('All Fields Are Required')
        
        if not User.objects.filter(email=email).exists():
            raise AuthenticationFailed('Invalid Email Address')
        
        
        print(email,password)
        user = authenticate(username=email,password=password)
        if user is None:
            raise AuthenticationFailed('Invalid Password')
        
        refresh = RefreshToken.for_user(user)
        refresh["first_name"] = str(user.first_name)
       
        content = {
                     'refresh': str(refresh),
                     'access': str(refresh.access_token),
                    #  'isAdmin':user.is_superuser,
                }
        
        return Response(content,status=status.HTTP_200_OK)
    

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        userEmail = User.objects.get(id=request.user.id).email
        content = {
            'user-email':userEmail,
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    
class ProductView(APIView):    
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        publish("list_products",{})
        
        return Response({"haiii"})
        
    
    