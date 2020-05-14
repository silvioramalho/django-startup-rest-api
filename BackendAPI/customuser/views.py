import uuid

from rest_framework import views, permissions, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from datetime import datetime, timedelta
from calendar import timegm
from djoser.views import UserViewSet
from djoser import serializers
from rest_framework import permissions

from customuser.models import CustomUser
from customuser import permissions as custom_permissions
from .models import CustomUser
from .serializers import CustomUserPhotoSerializer, CustomUserSerializer

from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken
from .serializers import CustomTokenSerializer, CustomRefreshTokenSerializer
from drf_jwt.utils import jwt_decode_handler


class CustomUserLogoutAllView(views.APIView):
    '''
    Use este endpoint para efetuar logout de todas as sessões para um determinado usuário.
    '''
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        user.jwt_secret = uuid.uuid4()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomUserCreateView(UserViewSet):
    '''
    Uses the default Djoser view, but add custom fields (phone in this case)
    Use this endpoint to create user.
    '''
    model = CustomUser
    serializer_class = serializers.UserCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(pk=response.data.get('id'))
        user.phone = request.data.get('phone')
        user.save()
        return response


class CustomUserView(UserViewSet):
    '''
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to retrieve/update user.
    '''
    model = CustomUser
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, custom_permissions.IsUserBlocked]

    def me(self, request, *args, **kwargs):
        return super().me(request, *args, **kwargs)
 
class CustomUserDeleteView(UserViewSet):
    '''
    Uses the default Djoser view, but add the IsOtpVerified permission.
    Use this endpoint to remove actually authenticated user.
    '''
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserLogin(ObtainJSONWebToken):
    
    serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        response = super(CustomUserLogin, self).post(request, *args, **kwargs)
        try:
            user_id = jwt_decode_handler(response.data.get('token')).get('user_id')
            user = CustomUser.objects.get(pk=user_id)
            if user.photo:
                response.data['photo'] = request.META['wsgi.url_scheme'] + '://' + request.META['HTTP_HOST'] + user.photo.url
        except:
            pass        
        return response

class CustomRefreshToken(RefreshJSONWebToken):
    
    serializer_class = CustomRefreshTokenSerializer

class CustomUserPhotoViewSet(ModelViewSet):
    serializer_class = CustomUserPhotoSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.user.id # self.request.query_params.get('id', None)
        queryset = None

        if id:
            queryset = CustomUser.objects.filter(pk=id)
        else:
            queryset = CustomUser.objects.all()

        return queryset

    def retrieve(self, request, *args, **kwargs):
        return super(CustomUserPhotoViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(CustomUserPhotoViewSet, self).partial_update(request, *args, **kwargs)

class CustomUserViewSet(ModelViewSet):

    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.user.id # self.request.query_params.get('id', None)
        queryset = None

        if id:
            queryset = CustomUser.objects.filter(pk=id)
        else:
            queryset = CustomUser.objects.all()

        return queryset

    def retrieve(self, request, *args, **kwargs): 
        return super(CustomUserViewSet, self).retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return super(CustomUserViewSet, self).partial_update(request, *args, **kwargs)
    