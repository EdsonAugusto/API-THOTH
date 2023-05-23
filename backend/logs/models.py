from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class LogEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Usuário', related_name='logentry_logs_user_set')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='logentry_logs_content_type_set')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    action = models.CharField('Ação', max_length=50)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)

    class Meta:
        verbose_name = 'Log de Alterações'
        verbose_name_plural = 'Logs de Alterações'
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user} {self.action} {self.content_object} at {self.timestamp}'