from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,Userr
import logging
from rest_framework.exceptions import AuthenticationFailed,ParseError
from rest_framework_simplejwt.tokens import RefreshToken

logger = logging.getLogger(__name__)

from .serializers import UserSerializer,UserRegistrationSerializer

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
    



from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    
class LoginView(APIView):
    def post(self,request):
        try:
            email = request.data['email']
            password =request.data['password']
        
        except KeyError:
            raise ParseError('All Fields Are Required')
        
        if not Userr.objects.filter(email=email).exists():
            raise AuthenticationFailed('Invalid Email Address')
        
        
        if not Userr.objects.filter(email=email,is_active=True).exists():
            raise AuthenticationFailed('You are blocked by admin ! Please contact admin')
        
        user = authenticate(username=email,password=password)
        if user is None:
            raise AuthenticationFailed('Invalid Password')
        print("haiiii")
        refresh = RefreshToken.for_user(user)
        refresh["first_name"] = str(user.first_name)
       
        content = {
                     'refresh': str(refresh),
                     'access': str(refresh.access_token),
                     'isAdmin':user.is_admin,
                }
        
        return Response(content,status=status.HTTP_200_OK)
        
        
class UserRegistrationView(APIView):
    def post(self, request):
        print("haiii")
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
