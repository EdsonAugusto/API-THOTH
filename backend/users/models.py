from django.contrib.auth.models import AbstractUser
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


class CustomUser(AbstractUser):
    user_vsc = EncryptedCharField('Usuário VSC',max_length=128, blank=True, null=True)
    password_vsc = EncryptedCharField('Senha VSC', max_length=128, blank=True, null=True)
    biography = models.TextField('Biografia', blank=True, null=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']

    def __str__(self):
        return self.username