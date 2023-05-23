from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
import ipaddress


class Rack(models.Model):

    identification = models.CharField('Nome Rack', max_length=200, unique=True)
    pop_installed = models.ForeignKey('core.DataCenter', on_delete=models.CASCADE, verbose_name='POP Instalado', related_name='+')
    slug =  AutoSlugField('Identificador', populate_from='identification')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    status = models.BooleanField('Status', default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Criado por', blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='+')


    class Meta:
        verbose_name = 'Rack'
        verbose_name_plural = "Rack's"
        ordering = ['identification']

    def __str__(self):
        return self.identification


class Equipment(models.Model):

    SECTOR_CHOICES = (
        ('networks', 'Redes'),
        ('voip', 'VoIP'),
    )
    identification = models.CharField('Nome Equipamento', max_length=200, unique=True)
    rack_installed = models.ForeignKey('inventory.Rack', on_delete=models.RESTRICT, verbose_name='Rack Instalado', related_name='+')
    responsible_sector = models.CharField('Setor Responsável', max_length=10, choices=SECTOR_CHOICES, default='voip')
    ip_address = models.OneToOneField(
        'IPAddress',
        on_delete=models.SET_NULL,
        verbose_name='Endereço IP',
        related_name='associated_equipment',
        blank=True,
        null=True,
    )
    description_equipment = models.TextField('Descrição', blank=True, null=True)

    slug =  AutoSlugField('Identificador', populate_from='identification')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    status = models.BooleanField('Status', default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Criado por', blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True, related_name='+')

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = "Equipmentos"
        ordering = ['identification']

    def __str__(self):
        return self.identification

    @property
    def pop_installed(self):
        return self.rack_installed.pop_installed

    def save(self, *args, **kwargs):
        super(Equipment, self).save(*args, **kwargs)
        if self.ip_address and self.ip_address.is_available:
            self.ip_address.is_available = False
            self.ip_address.equipment = self
            self.ip_address.save()

    def delete(self, *args, **kwargs):
        super(Equipment, self).delete(*args, **kwargs)
        if self.ip_address:
            self.ip_address.is_available = True
            self.ip_address.equipment = None
            self.ip_address.save()
        

class IPAddress(models.Model):

    IP_TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    ip = models.GenericIPAddressField('Endereço IP', unique=True)
    ip_type = models.CharField('Tipo de IP', max_length=10, choices=IP_TYPE_CHOICES, default='public')
    network = models.CharField('Rede', max_length=20, blank=True, null=True)
    subnet = models.CharField('Sub-rede', max_length=20, blank=True, null=True)
    equipment = models.ForeignKey('inventory.Equipment', on_delete=models.SET_NULL, verbose_name='Equipamento', related_name='ip_addresses', blank=True, null=True)
    is_available = models.BooleanField('Disponível', default=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True, related_name='+')

    class Meta:
        verbose_name = 'Endereço IP'
        verbose_name_plural = 'Endereços IP'
        ordering = ['ip']

    def __str__(self):
        return self.ip


#def create_ip_addresses(network):
#    network = ipaddress.ip_network(network, strict=False)
#    for ip in network.hosts():
#        IPAddress.objects.get_or_create(ip=str(ip), network=network)


#create_ip_addresses('200.162.139.1/24')