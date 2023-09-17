from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User

class LBBOPermissionRequiredMixin(PermissionRequiredMixin):
    raise_exception=True
    call_all_permission=None
    get_permission=None
    post_permission=None
    put_permission=None
    patch_permission=None
    delete_permission=None

    def  has_permission(self) :
        if self.call_all_permission is not None and self.request.user.has_perm(self.call_all_permission):
            return True
        if self.request.method == 'GET':
            if self.get_permission is not None and self.request.user.has_perm(self.get_permission):
                return True
        if self.request.method == 'POST':
            if self.post_permission is not None and self.request.user.has_perm(self.post_permission):
                return True
        if self.request.method == 'PUT':
            if self.put_permission is not None and self.request.user.has_perm(self.put_permission):
                return True
        if self.request.method == 'PATCH':
            if self.patch_permission is not None and self.request.user.has_perm(self.patch_permission):
                return True
        if self.request.method == 'DELETE':
            if self.delete_permission is not None and self.request.user.has_perm(self.delete_permission):
                return True
        
        return False


class TipoUser(models.Model):
    ADMIN=0

    tipo_usuario = models.CharField(max_length=100)
    class Meta:
        db_table = "REPZ_TIPO_USER"
        verbose_name = "Tipo Usuario"
        verbose_name_plural = "Tipos Usuario"

    def __str__(self) -> str:
        return self.tipo_usuario
    
class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey(TipoUser, verbose_name='Tipo de Usuario', on_delete=models.CASCADE)
    class Meta:
        db_table = "REPZ_USER_PROFILE"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("user__username",)

    def __str__(self) -> str:
        return f"{self.user.username} ({self.tipo_usuario})"
    @property
    def is_admin(self):
        return self.tipo_usuario_id == TipoUser.ADMIN


class LoginLog(models.Model):
    """Log dos logins dos utilizadores da REPZ"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    login_ip = models.GenericIPAddressField()
    class Meta:
        db_table = 'REPZ_LOGIN_LOG'

class InvalidLoginLog(models.Model):
    username = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    login_ip = models.GenericIPAddressField()

    class Meta:
        db_table = 'REPZ_LOGIN_INVALID_LOG'