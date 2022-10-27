from rest_framework import generics
from rest_framework.response import Response
from .serializers import LoginSerializer, RegistrationSerializer
from django.contrib.auth import get_user_model, login, authenticate

User = get_user_model()

class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data.get("email")
        password = serializer.data.get("password")

        user = authenticate(email=email, password=password)
        print(user)
        login(request, user)

        return Response({"email": email}, status=201)



class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        login(request, user)
        return Response(serializer.data, status=201)