from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"})


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError({"Sifre ve ya email yalnisdir"})

        if len(password) < 6:
            raise serializers.ValidationError({"Sifre en azi 6 simvoldan ibaret olmalidir"})

        return attrs



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "name", "surname", "password")
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        email_qs = User.objects.filter(email=email).exists()

        if email_qs:
            raise serializers.ValidationError({"Bu email ile artiq qeydiyyatdan kecilib"})

        if len(password) < 6:
            raise serializers.ValidationError({"Sifre en azi 6 simvoldan ibaret olmalidir"})

        return attrs

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop("password")
        user = User(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user