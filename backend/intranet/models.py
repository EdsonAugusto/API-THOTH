from django.db import models
from autoslug import AutoSlugField
from django.conf import settings


# Common base model for all models
class BaseModel(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, null=True, related_name='+')

    class Meta:
        abstract = True

# Models related to knowledge base
class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug =  AutoSlugField('Slug', populate_from='name')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class KnowledgeBaseItem(BaseModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Article(KnowledgeBaseItem):
    content = models.TextField()

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'

class FAQ(KnowledgeBaseItem):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class Procedure(KnowledgeBaseItem):
    steps = models.TextField()

    class Meta:
        verbose_name = 'Procedimento Técnico'
        verbose_name_plural = 'Procedimentos Técnicos'

class TechnicalDictionary(BaseModel):
    term = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return self.term
    
    class Meta:
        verbose_name = 'Nomenclatura Técnica'
        verbose_name_plural = 'Nomenclaturas Técnicas'

# Model for shift handovers
class ShiftHandover(BaseModel):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='shift_handovers_created')
    handed_over_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='shift_handovers_received')

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
    
    class Meta:
        verbose_name = 'Passagem de Plantão'
        verbose_name_plural = 'Passagens de Plantões'

# Model for notices
class Notice(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Aviso Importante'
        verbose_name_plural = 'Avisos Importantes'

# Model for general problem handling
class GeneralProblem(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    solution = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Problema Geral'
        verbose_name_plural = 'Problemas Gerais'
    
# Model for announcements
class Announcement(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Anúncio'
        verbose_name_plural = 'Anúncios'

# Model for system maintenance
class SystemMaintenance(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Manutenção Programada'
        verbose_name_plural = 'Manutenções Programadas'

# Model for team meetings
class TeamMeeting(BaseModel):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    agenda = models.TextField()
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Conferência'
        verbose_name_plural = 'Conferências'

# Model for best practices
class BestPractice(KnowledgeBaseItem):
    content = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Boa Pratica'
        verbose_name_plural = 'Boas Praticas'
    
# Model for reminders, "to-do" items, and notes
class Reminder(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='reminders')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lembrete'
        verbose_name_plural = 'Lembretes'

# Model for general problem handling
class GeneralNotes(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Nota Geral'
        verbose_name_plural = 'Notas Gerais'