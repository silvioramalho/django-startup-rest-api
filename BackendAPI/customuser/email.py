from django.conf import settings
from djoser.email import PasswordResetEmail, ConfirmationEmail, ActivationEmail, PasswordChangedConfirmationEmail


class CustomActivationEmail(ActivationEmail):
    template_name = "email/activation.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["frontend"] = settings.FRONTEND_URL
        return context

class CustomConfirmationEmail(ConfirmationEmail):
    template_name = "email/confirmation.html"

class CustomPasswordChangedConfirmationEmail(PasswordChangedConfirmationEmail):
    template_name = "email/password_changed_confirmation.html"

class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["frontend"] = settings.FRONTEND_URL
        return context