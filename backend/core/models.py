from django.db import models
from django.conf import settings
from django.utils.text import slugify
from encrypted_model_fields.fields import EncryptedCharField

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField
from django_cpf_cnpj.fields import CNPJField, CPFField


class Company(models.Model):

    id_trb = models.CharField('ID TRB', max_length=30, unique=True)
    name = models.CharField('Empresa', max_length=200, unique=True)
    cnpj = CNPJField('CNPJ', unique=True)
    phone = PhoneNumberField("Telefone", unique=True)
    site = models.URLField('Site', unique=True)
    address = models.TextField('Endereço', max_length=1000)
    note = models.TextField('Observações', blank=True, null=True, max_length=1000)
    slug = AutoSlugField('Identificador', populate_from='name', unique=True)
    is_active = models.BooleanField('Status', default=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Criado por', blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='+')


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['name']

    def __str__(self):
        return self.name


class GeneralInformation(models.Model):

    class Meta:
        abstract = True

    class ActingSector(models.TextChoices):
        CNGR = 'CNGR', ('CNGR')
        COMERCIAL = 'Comercial', ('Comercial')
        CONTABILIDADE = 'Contabilidade', ('Contabilidade')
        DFO = 'DFO', ('DFO')
        DRF = 'DRF', ('DRF')
        SAC = 'Sac', ('Sac')
        VOIP = 'VoIP', ('VoIP')
        REDES = 'Redes', ('Redes')
        NGN = 'NGN', ('NGN')
        TI = 'TI', ('TI')
        FINANCEIRO = 'Financeiro', ('Financeiro')
        RH = 'RH', ('RH')
        JURIDICO = 'JURIDICO', ('Jurídico')
        MARKETING = 'Marketing', ('Marketing')

    
    acting_sector = models.CharField( max_length=15, choices=ActingSector.choices, verbose_name='Setor Responsável')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Criado por', blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='+')
    status = models.BooleanField('Status',  default=True)


class Sector(GeneralInformation):

    name = models.CharField('Setor', blank=False, null=False, max_length=50, unique=True)
    email = models.EmailField('E-mail Setor', blank=False, null=False, unique=True)
    flag_company = models.ForeignKey('core.Company', on_delete=models.RESTRICT, verbose_name='Bandeira', related_name='+')
    slug =  AutoSlugField('Identificador', populate_from='name')

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    @property
    def phone_sector(self):
        return self.company.phone


class Extensions(GeneralInformation):

    employee = models.CharField('Funcionario', blank=False, null=False, max_length=30, unique=True)
    employee_email = models.EmailField('E-mail Funcionario', blank=False, null=False, unique=True)
    employee_phone = PhoneNumberField("Telefone Pessoal", blank=True, null=True, unique=True)
    branch_line = models.IntegerField('Ramal', blank=False, null=False)
    service_group = models.IntegerField('Grupo de Atendimento', blank=False, null=False)
    floor_installed = models.IntegerField('Andar Instalado', blank=False, null=False)
    mac_phone = models.CharField('Mac PhoneIP', blank=False, null=False, max_length=32, unique=True)
    on_call = models.BooleanField('Plantonista', default=False)
    slug = AutoSlugField('Identificador', populate_from='employee')

    class Meta:
        verbose_name = 'Ramal'
        verbose_name_plural = 'Ramais'
        ordering = ['employee', 'branch_line']

    def __str__(self):
        return self.employee


class DataCenter(GeneralInformation):

    name = models.CharField('Nome POP', blank=False, null=False, max_length=30, unique=True)
    responsible_company = models.ForeignKey('core.Company', on_delete=models.RESTRICT, verbose_name='Empresa Responsável')
    phone_number = PhoneNumberField("Telefone POP", blank=False, null=False, unique=True)
    cell_number =  PhoneNumberField("Celular POP", blank=True, null=True, unique=True)
    email = models.EmailField('E-mail POP', blank=False, null=False, unique=True)
    adress = models.TextField('Endereço', blank=True, null=True, max_length=1000)
    note = models.TextField('Observações', blank=True, null=True, max_length=1000)
    site = models.URLField('Site POP', blank=True, null=True, unique=True)
    slug =  AutoSlugField('Identificador', populate_from='name')

    class Meta:
        verbose_name = 'Data Center'
        verbose_name_plural = 'POPs'
        ordering = ['name']

    def __str__(self):
        return self.name

 
class AccessRelease(GeneralInformation):

    employee_name = models.CharField('Nome Funcionario', blank=False, null=False, max_length=40, unique=True)
    employees_CPF = CPFField(masked=True, verbose_name='CPF', blank=False, null=False, unique=True)
    employees_RG = models.IntegerField('RG', blank=False, null=False, unique=True)
    slug =  AutoSlugField('Identificador', populate_from='employee_name')

    class Meta:
        verbose_name = 'Dados de Tecnico'
        verbose_name_plural = 'Dados dos Tecnicos'
        ordering = ['employee_name']

    def __str__(self):
        return self.employee_name


class ImportantAccesses(GeneralInformation):
    
	user = models.CharField('Usuario', max_length=200)
	password_acesses = EncryptedCharField('Senha Database', max_length=128,
	blank=True, null=True)
	access_url = models.URLField('URL de Acesso', blank=False, null=False)
	note = models.TextField('Observações', blank=True, null=True)
	slug = AutoSlugField('Identificador', populate_from='user', unique=True)

	class Meta:
		verbose_name = 'Acesso'
		verbose_name_plural = 'Acessos'
		ordering = ['user']
	
	def __str__(self):
		return self.user


class ProActiveContacts(GeneralInformation):
    
	responsible_company = models.ForeignKey('core.Company', on_delete=models.CASCADE, related_name='responsible_client', verbose_name='Empresa Responsável')
	name_client = models.CharField('Nome do Contato', max_length=200)
	phone = PhoneNumberField("Telefone", unique=True)
	email = models.EmailField('E-mail', unique=True)
	note = models.TextField('Observações', blank=True, null=True)
	slug = AutoSlugField('Identificador', populate_from='name_client',unique=True)
	
	class Meta:
		verbose_name = 'Contato Proativo'
		verbose_name_plural = 'Contatos Proativos'
		ordering = ['name_client']
	
	def __str__(self):
		return self.name_client


class ProviderContacts(GeneralInformation):
    
	responsible_company = models.ForeignKey('core.Company',
	on_delete=models.CASCADE, related_name='responsible_providers', verbose_name='Empresa Responsável')
	name_provider = models.CharField('Nome do Cliente', max_length=200)
	phone = PhoneNumberField("Telefone", unique=True)
	email = models.EmailField('E-mail', unique=True)
	note = models.TextField('Observações', blank=True, null=True)
	slug = AutoSlugField('Identificador', populate_from='name_provider', unique=True)

	class Meta:
		verbose_name = 'Contato de Provedor'
		verbose_name_plural = 'Contatos de Provedores'
		ordering = ['name_provider']

	def __str__(self):
		return self.name_provider