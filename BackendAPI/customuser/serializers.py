from djoser.serializers import ActivationSerializer
from rest_framework import exceptions, serializers
from rest_framework.serializers import ModelSerializer
from djoser.conf import settings

from rest_framework_jwt.serializers import JSONWebTokenSerializer
from drf_jwt.serializers import RefreshJSONWebTokenSerializer

from .models import CustomUser

class CustomSerializer(ActivationSerializer):

    default_error_messages = {
        "stale_token": settings.CONSTANTS.messages.STALE_TOKEN_ERROR,
        "blocked": settings.CONSTANTS.messages.BLOCKED_ERROR
    }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.user.is_blocked:
            return attrs
        raise exceptions.PermissionDenied(self.error_messages["blocked"])

class CustomTokenSerializer(JSONWebTokenSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs.get('user')
        if not user.is_blocked:
            return attrs
        else:
            raise serializers.ValidationError('Seu usuário encontra-se bloqueado no sistema. Entre em contato com o administrador do sistema.')


class CustomRefreshTokenSerializer(RefreshJSONWebTokenSerializer):

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs.get('user')
        if not user.is_blocked:
            return attrs
        else:
            raise serializers.ValidationError('Seu usuário encontra-se bloqueado no sistema. Entre em contato com o administrador do sistema.')

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phone')


class CustomUserPhotoSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'photo')