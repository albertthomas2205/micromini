from django.urls import path

from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)

from .views import UserViewSet,UserRegistrationView,LoginView

urlpatterns = [
    path('account',UserViewSet.as_view({
        'post':'create',
        'get':'list'
        })),
   path('/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('register/', UserRegistrationView.as_view(), name='user-registration'),
   path('login/', LoginView.as_view(), name='login'),
    
]