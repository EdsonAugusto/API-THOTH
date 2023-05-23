from django.db import models
from encrypted_model_fields.fields import EncryptedCharField
from django.conf import settings
from autoslug import AutoSlugField


class Command(models.Model):
    EQUIPMENT_CHOICES = (
      ('BDVSC', 'Database VSC'),
      ('WINDOWS', 'BAT'),
      ('Gateway', 'Servidor Gateway'),
      ('PABx', 'Servidor PABx'),
      ('Portability', 'Servidor Portabilidade'),
      ('XenServer', 'Servidor XenServer'),
    )
    COMMAND_CHOICES = (
      ('QUERY', 'Query'),
      ('UPDATE', 'Update'),
    )
    title = models.CharField('Titulo', max_length=200)
    status = models.BooleanField('Status', default=False)
    note = models.TextField('Observações', blank=False, null=False)
    command = models.TextField('Comando', blank=False, null=False)
    server_type = models.CharField('Tipo do Equipamento', max_length=20,
    choices=EQUIPMENT_CHOICES)
    command_type = models.CharField('Tipo de Comando', max_length=10,
    choices=COMMAND_CHOICES)
    slug = AutoSlugField('Identificador', populate_from='title')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Criado por', blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True, related_name='+')

    class Meta:
      verbose_name = 'Comando'
      verbose_name_plural = 'Comandos'
    def __str__(self):
      return f'{self.title} - {self.server_type}'