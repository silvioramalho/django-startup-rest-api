import jwt
from calendar import timegm
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework_jwt.compat import Serializer
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

User = get_user_model()
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class VerificationBaseSerializer(Serializer):
    """
    Abstract serializer used for verifying and refreshing JWTs.
    """
    token = serializers.CharField()

    def validate(self, attrs):
        msg = 'Please define a validate method.'
        raise NotImplementedError(msg)

    def _check_payload(self, token, isRefresh=False):
        # Check payload valid (based off of JSONWebTokenAuthentication,
        # may want to refactor)
        try:
            payload = jwt_decode_handler(token, isRefresh)
        except jwt.ExpiredSignature:
            msg = ('Signature has expired.')
            raise serializers.ValidationError(msg)
        except jwt.DecodeError:
            msg = ('Error decoding signature.')
            raise serializers.ValidationError(msg)

        return payload

    def _check_user(self, payload):
        username = jwt_get_username_from_payload(payload)

        if not username:
            msg = ('Invalid payload.')
            raise serializers.ValidationError(msg)

        # Make sure user exists
        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = ("User doesn't exist.")
            raise serializers.ValidationError(msg)

        if not user.is_active:
            msg = ('User account is disabled.')
            raise serializers.ValidationError(msg)

        return user

class VerifyJSONWebTokenSerializer(VerificationBaseSerializer):
    """
    Check the veracity of an access token.
    """

    def validate(self, attrs):
        token = attrs['token']

        payload = self._check_payload(token=token)
        user = self._check_user(payload=payload)

        return {
            'token': token,
            'user': user
        }

class RefreshJSONWebTokenSerializer(VerificationBaseSerializer):
    """
    Refresh an access token.
    """

    def validate(self, attrs):
        token = attrs['token']
        payload = self._check_payload(token=token, isRefresh=True)
        user = self._check_user(payload=payload)
        
        # Get and check 'orig_iat'
        orig_iat = payload.get('orig_iat')
        if orig_iat:
            # Verify expiration
            refresh_limit = api_settings.JWT_REFRESH_EXPIRATION_DELTA

            if isinstance(refresh_limit, timedelta):
                refresh_limit = (refresh_limit.days * 24 * 3600 +
                                 refresh_limit.seconds)

            expiration_timestamp = orig_iat + int(refresh_limit)
            now_timestamp = timegm(datetime.utcnow().utctimetuple())

            if now_timestamp > expiration_timestamp:
                msg = ('Refresh has expired.')
                raise serializers.ValidationError(msg)
        else:
            msg = ('orig_iat field is required.')
            raise serializers.ValidationError(msg)

        new_payload = jwt_payload_handler(user)
        new_payload['orig_iat'] = orig_iat

        return {
            'token': jwt_encode_handler(new_payload),
            'user': user
        }