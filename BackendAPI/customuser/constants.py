from djoser.constants import Messages


class CustomMessages(Messages):
    INVALID_CREDENTIALS_ERROR = ("Não foi possível efetuar login com credenciais fornecidas.")
    INACTIVE_ACCOUNT_ERROR = ("A conta de usuário está desativada.")
    INVALID_TOKEN_ERROR = ("Token inválido para este usuário.")
    INVALID_UID_ERROR = ("ID de usuário inválido ou usuário não existe.")
    STALE_TOKEN_ERROR = ("Token expirado para este usuário.")
    PASSWORD_MISMATCH_ERROR = ("Os dois campos de senha não coincidem.")
    USERNAME_MISMATCH_ERROR = ("Os dois campos {0} não coincidem.")
    INVALID_PASSWORD_ERROR = ("Senha inválida.")
    EMAIL_NOT_FOUND = ("Este usuário não existe.")
    CANNOT_CREATE_USER_ERROR = ("Não foi possível criar a conta.")
    BLOCKED_ERROR = ("Usuário bloqueado.")