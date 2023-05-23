from django.db import models
from inventory.models import Equipment, IPAddress



class Switch(Equipment):

    manufacturer = models.CharField('Fabricante', max_length=200)
    model = models.CharField('Modelo', max_length=200)
    is_manageable = models.BooleanField('Gerenciável', default=False)
    installation_date = models.DateField('Data de Instalação', blank=True, null=True)
    warranty_period = models.PositiveIntegerField('Período de Garantia (meses)', blank=True, null=True)
    number_of_ports = models.PositiveIntegerField('Número de Portas')
    port_speed = models.CharField('Velocidade das Portas', max_length=20)

    class Meta:
        verbose_name = 'Switch'
        verbose_name_plural = 'Switches'

    def __str__(self):
        return f'{self.identification} - {self.number_of_ports} ports'
    

class SwitchPort(models.Model):

    SWITCH_PROTOCOL_CHOICES = (
        ('trunk', 'Trunk'),
        ('access', 'Access'),
    )

    switch = models.ForeignKey(Switch, on_delete=models.RESTRICT, verbose_name='Switch', related_name='ports')
    port_number = models.PositiveIntegerField('Número da Porta')
    vlan = models.PositiveIntegerField('VLAN')
    protocol = models.CharField('Protocolo', max_length=10, choices=SWITCH_PROTOCOL_CHOICES)
    speed = models.CharField('Velocidade da Porta', max_length=20)
    equipment = models.OneToOneField(
        Equipment,
        on_delete=models.SET_NULL,
        verbose_name='Equipamento Linkado',
        related_name='switch_port',
        blank=True,
        null=True,
    )
    description = models.TextField('Descrição', blank=True, null=True)

    class Meta:
        verbose_name = 'Porta do Switch'
        verbose_name_plural = 'Portas do Switch'
        unique_together = ('switch', 'port_number')
        ordering = ['switch', 'port_number']

    def __str__(self):
        return f'{self.switch.identification} - Porta {self.port_number}'
