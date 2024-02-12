import jwt
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_get_secret_key

def jwt_decode_handler(token, isRefresh=False):
    options = {
        'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
    }
    if isRefresh: 
        options = {
            'verify_exp': False,
        }

    unverified_payload = jwt.decode(token, options={"verify_signature": False})
    secret_key = jwt_get_secret_key(unverified_payload)
    return jwt.decode(
        token,
        key=api_settings.JWT_PUBLIC_KEY or secret_key,
        verify=api_settings.JWT_VERIFY,
        options=options,
        leeway=api_settings.JWT_LEEWAY,
        audience=api_settings.JWT_AUDIENCE,
        issuer=api_settings.JWT_ISSUER,
        algorithms=[api_settings.JWT_ALGORITHM]
    )