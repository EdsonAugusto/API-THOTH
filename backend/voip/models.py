from django.db import models
from encrypted_model_fields.fields import EncryptedCharField

from inventory.models import Equipment, IPAddress


class Softswitch_VSC(Equipment):

    SOFTSWITCH_CHOICES = (
        ('SERVER', 'SERVER'),
        ('DATABASE', 'DATABASE'),
    )
    id_vsc = models.IntegerField('ID VSC', blank=True, null=True)
    server_type = models.CharField('Servidor', max_length=8, choices=SOFTSWITCH_CHOICES)
    server_port_count = models.PositiveIntegerField('Qtd Portas Server')
    portability_server = models.ForeignKey('voip.Server_Portability', on_delete=models.RESTRICT, verbose_name='Servidor de Portabilidade')
    server_password = EncryptedCharField('Server Password', max_length=128)
    name_database = models.CharField('Nome Database', max_length=128, blank=True, null=True)
    user_database = EncryptedCharField('Usuário Database', max_length=128, blank=True, null=True)
    password_database = EncryptedCharField('Senha Database', max_length=128, blank=True, null=True)
    url_server = models.URLField('Server URL', max_length=255, blank=True, null=True)
    idrac = models.OneToOneField(
        IPAddress,
        on_delete=models.SET_NULL,
        verbose_name='IP IDRAC',
        related_name='associated_equipment_idrac',
        blank=True,
        null=True,
    )

    @property
    def additional_parameters(self):
        if self.server_type == 'DATABASE':
            return {
                'name_database': self.name_database,
                'user_database': self.user_database,
                'password_database': self.password_database
            }
        elif self.server_type == 'SERVER':
            return {
                'url_server': self.url_server
            }
        else:
            return {}

    class Meta:
        verbose_name = 'Softswitch VSC'
        verbose_name_plural = 'Softswitches VSC'
        ordering = ['identification']

    def __str__(self):
        return f'{self.identification} - {self.server_type}'


class Server_Gateway(Equipment):

    GATEWAY_CHOICES = (
        ('TSBC', 'TSBC'),
        ('GATEWAY', 'GATEWAY'),
        ('VM', 'GATEWAY VIRTUAL MACHINE'),
        ('CLIENT', 'CLIENTE'),
    )
    CONECTIONS_METODS_CHOICES = (
        ('L2L', 'Lan2Lan'),
        ('ETHERNET', 'ETHERNET'),
    )

    server_type = models.CharField('Tipo de Gateway', max_length=7, choices=GATEWAY_CHOICES)
    server_password = EncryptedCharField('Senha Gateway', max_length=128)
    server_xserver = models.ForeignKey('voip.Server_XenServer', on_delete=models.RESTRICT, verbose_name='VM XenServer', blank=True, null=True)
    connection_metod = models.CharField('Servidor', max_length=8, choices=CONECTIONS_METODS_CHOICES, blank=True, null=True)

    @property
    def additional_parameters(self):
        if self.server_type == 'VM':
            return {
                'server_xserver': self.server_xserver,
            }
        elif self.server_type == 'SERVER':
            return {
                'connection_metod': self.connection_metod
            }
        else:
            return {}

    class Meta:
        verbose_name = 'Gateway Server'
        verbose_name_plural = "Gateway's Servers"
        ordering = ['identification', 'server_type']

    def __str__(self):
        return f'{self.identification} - {self.server_type}'


class Server_PABx(Equipment):

    GATEWAY_CHOICES = (
        ('INTERNO', 'Interno'),
        ('CENTREX', 'Centrex'),
    )
    server_type = models.CharField('Tipo de PABx', max_length=7, choices=GATEWAY_CHOICES)
    server_password = EncryptedCharField('Senha PABx', max_length=128)

    class Meta:
        verbose_name = 'Server PABx'
        verbose_name_plural = "Servers PABxs"
        ordering = ['identification']

    def __str__(self):
        return f'{self.identification} - {self.server_type}'


class Server_Portability(Equipment):

    server_password = EncryptedCharField('Senha Servidor', max_length=128)

    class Meta:
        verbose_name = 'Portabilidade Server'
        verbose_name_plural = 'Portabilidade Servers'
        ordering = ['identification']

    def __str__(self):
        return self.identification    
    

class Server_XenServer(Equipment):

    server_password = EncryptedCharField('Senha Servidor', max_length=128)
    idrac = models.OneToOneField(
        IPAddress,
        on_delete=models.SET_NULL,
        verbose_name='IP IDRAC',
        related_name='associated_xserver_idrac',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Xen Server'
        verbose_name_plural = 'Xen Servers'
        ordering = ['identification']

    def __str__(self):
        return self.identification