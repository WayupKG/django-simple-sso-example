from django.urls import path, include

from .views import index, system_logout

urlpatterns = [
    path('', index, name='index'),
    path('logout/', system_logout, name='logout')
]
