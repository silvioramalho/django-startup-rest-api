from django.urls import re_path
from django.urls import path
from djoser import views as djoser_views
from drf_jwt import views as jwt_views
from .views import CustomUserView, CustomUserDeleteView, CustomUserLogin, CustomRefreshToken, CustomUserCreateView

from customuser import views

urlpatterns = [
    # As VIEWS são definidas no Dojser, mas estamos atribuindo caminhos personalizados.
    re_path(r'^user/view/$', views.CustomUserView.as_view({'get': 'me'}), name='user-view'),
    re_path(r'^user/delete/$', views.CustomUserDeleteView.as_view({'delete': 'destroy'}), name='user-delete'),
    re_path(r'^user/logout/all/$', views.CustomUserLogoutAllView.as_view(), name='user-logout-all'),
    #re_path(r'^user/create/$', djoser_views.UserViewSet.as_view({'post': 'create'}), name='user-create'),
    re_path(r'^user/create/$', CustomUserCreateView.as_view({'post': 'create'}), name='user-create'),
    re_path(r'^user/activation/$', djoser_views.UserViewSet.as_view({'post': 'activation'}), name='user-activation'),
    re_path(r'^user/forget-password/$', djoser_views.UserViewSet.as_view({'post': 'reset_password'}), name='reset-password'),
    re_path(r'^user/reset-password-confirm/$', djoser_views.UserViewSet.as_view({'post': 'reset_password_confirm'}), name='reset-password-confirm'),
    re_path(r'^user/set-password/$', djoser_views.UserViewSet.as_view({'post': 'set_password'}), name='set-password'),
    
    # As VIEWS são definidas no DRF-JWT, mas estamos atribuindo caminhos personalizados.
    re_path(r'^user/login/$', views.CustomUserLogin.as_view(), name='user-login'),
    re_path(r'^user/login/refresh/$', views.CustomRefreshToken.as_view(), name='user-login-refresh'),
    re_path(r'^user/login/verify/$', jwt_views.verify_jwt_token, name='user-token-verify'),

    # As VIEWS customizadas de usuário
    path('user/photo/<int:id>/', views.CustomUserPhotoViewSet.as_view({'post': 'partial_update', 'get': 'retrieve'}), name='update-user-photo'),
    path('user/data/<int:id>/', views.CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'partial_update'}), name='user-data'),
]