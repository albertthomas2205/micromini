from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('account',UserViewSet.as_view({
        'post':'create',
        'get':'list'
        }))
    
]