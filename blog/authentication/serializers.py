from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import validators


class RegisterSerilaizer(serializers.ModelSerializer):
    email=serializers.EmailField(validators=[validators.UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model=User
        fields=('id','username','email','password')

        def create(self, validated_data):  # Doğru yer
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'username', 'email')

