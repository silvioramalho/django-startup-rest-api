from django.db import models
import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import datetime

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        '''
        Cria e salva um usuário com o email e a senha fornecidos.
        '''
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        '''
        Cria e salva um superusuário com o email e a senha fornecidos.
        '''
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
class CustomUser(AbstractBaseUser):

    email = models.EmailField(db_column='usu_des_email', verbose_name='e-mail', max_length=255, unique=True)
    is_active = models.BooleanField(db_column='usu_idc_ativo', default=True, verbose_name="ativo")
    is_admin = models.BooleanField(db_column='usu_idc_admin', default=False, verbose_name="admin")
    jwt_secret = models.UUIDField(db_column='usu_uid_jwtsecret', default=uuid.uuid4, verbose_name="JWT Secret")
    is_blocked = models.BooleanField(db_column='usu_idc_bloqueado', default=False, verbose_name="bloqueado")
    is_staff = models.BooleanField(db_column='usu_idc_staff', default=False, verbose_name="is staff")
    phone = phone = models.CharField(db_column='usu_des_telefone', max_length=11, blank=True, null=True, verbose_name="telefone")
    photo = models.ImageField(db_column='usu_img_foto', upload_to='photos', null=True, blank=True, verbose_name="foto")
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'usuário'
        db_table = 'usuario_usu'
    
    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

def jwt_get_secret_key(user_model):
    return user_model.jwt_secret

