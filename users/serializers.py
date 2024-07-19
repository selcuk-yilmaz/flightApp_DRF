from rest_framework import serializers, validators
from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


# User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}

    )

    password1 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password1'
        )

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError(
                {"password": "Password didn't match..... "}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")  #gelen datadan password ü laıyorum çünkü onu olduğu gibi kaydetmiyeceğim hashleme yapacağım.
        validated_data.pop('password1')  #gelen datanın içinden sadece bir adet password ü kullancağım için siliyorum.
        user = User.objects.create(**validated_data) #gelen validate olmuş datayı create ediyorum.Ama password yok dikkat.
        user.set_password(password)    #set_password metodu ile password ü hash liyor.
        user.save()                    #user modelini kaydediyor
        return user   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = (
            'key',
            'user'
        )