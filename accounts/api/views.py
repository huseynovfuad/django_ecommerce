from rest_framework import generics
from rest_framework.response import Response
from .serializers import LoginSerializer, RegistrationSerializer, VerifySerializer
from django.contrib.auth import get_user_model, login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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

        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response({"email": email, "tokens": tokens}, status=201)



class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # login(request, user)
        return Response(serializer.data, status=201)


class VerifyView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = VerifySerializer
    lookup_field = "slug"

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(data=request.data, instance=obj)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        login(request, user)
        return Response({}, status=201)