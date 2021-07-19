from django.contrib.auth.models import User
from user.serializers import UserSerializer
from rest_framework import generics


class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer