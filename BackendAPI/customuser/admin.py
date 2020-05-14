from django.contrib import admin
from django.contrib.admin.actions import delete_selected

from .models import CustomUser
from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.conf import settings

def make_activate(modeladmin, request, queryset):
    queryset.update(is_active=True)

def block_user(modeladmin, request, queryset):
    queryset.update(is_blocked=True)

def send_confirmation_email(modeladmin, request, queryset):
    
    for user in queryset:
        if settings.SEND_CONFIRMATION_EMAIL:
            context = {"user": user}
            to = [get_user_email(user)]
            settings.EMAIL.confirmation(request, context).send(to)

def send_resend_activation_email(modeladmin, request, queryset):
    
    for user in queryset:
        if settings.SEND_CONFIRMATION_EMAIL:
            context = {"user": user}
            to = [get_user_email(user)]
            settings.EMAIL.activation(request, context).send(to)


def send_reset_password_email(modeladmin, request, queryset):
    
    for user in queryset:
        if settings.SEND_CONFIRMATION_EMAIL:
            context = {"user": user}
            to = [get_user_email(user)]
            settings.EMAIL.password_reset(request, context).send(to)


make_activate.short_description = "Ativar Usuarios"
send_confirmation_email.short_description = "Enviar Email de Confirmacao"
send_resend_activation_email.short_description = "Reenviar Email de Ativação"
send_reset_password_email.short_description = "Enviar link para Troca de Senha"
block_user.short_description = "Bloquear Usuário"

# Exclui globalmente a ação de apagar selecionados
# É necessário adicionar apenas nos que quiser conforme abaixo
admin.site.disable_action('delete_selected')
delete_selected.short_description = "Apagar Selecionados"

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_blocked', 'is_admin', 'is_staff')
    fields = [('email', 'is_active', 'is_blocked', 'is_admin', 'is_staff')]
    list_filter = ['is_active', 'is_blocked', 'is_admin', 'is_staff']
    search_fields = ['email']
    actions = [
        make_activate, send_confirmation_email, block_user,
        send_resend_activation_email, send_reset_password_email,
        'delete_selected']

admin.site.site_header = 'Titulo do Topo'
admin.site.index_title = 'Titulo do Index'
admin.site.site_title = 'Titulo do Site(HTML)'

admin.site.register(CustomUser, CustomUserAdmin)
