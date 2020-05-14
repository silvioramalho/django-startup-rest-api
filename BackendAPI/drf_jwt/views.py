from django.shortcuts import render
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from .serializers import VerifyJSONWebTokenSerializer, RefreshJSONWebTokenSerializer

class ObtainJSONWebToken(JSONWebTokenAPIView):

    serializer_class = JSONWebTokenSerializer

class VerifyJSONWebToken(JSONWebTokenAPIView):

    serializer_class = VerifyJSONWebTokenSerializer

class RefreshJSONWebToken(JSONWebTokenAPIView):

    serializer_class = RefreshJSONWebTokenSerializer

obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()