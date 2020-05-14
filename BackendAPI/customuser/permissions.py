from rest_framework import permissions

class IsUserBlocked(permissions.BasePermission):
    '''
    Se o usuário estiver bloqueado.
    '''
    message = "Seu usuário está bloqueado. Entre em contato com o administrador do sistema."

    def has_permission(self, request, view):
        print('Permission User: ', request.user.is_blocked)
        if request.user:
            return not request.user.is_blocked
        else:
            return False
