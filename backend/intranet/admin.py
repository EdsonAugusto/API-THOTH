from django.contrib import admin
from .models import (Category, Article, FAQ, Procedure, TechnicalDictionary, ShiftHandover, Notice,
                     GeneralProblem, Announcement, SystemMaintenance, TeamMeeting, BestPractice,
                     Reminder, GeneralNotes)

class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

class CategoryAdmin(BaseModelAdmin):
    list_display = ['name', 'created', 'updated_by']
    search_fields = ['name']
    list_filter = ['created', 'updated_by']

class KnowledgeBaseItemAdmin(BaseModelAdmin):
    list_display = ['title', 'category', 'created_by', 'created', 'updated_by']
    search_fields = ['title', 'category__name']
    list_filter = ['category', 'created_by', 'created', 'updated_by']

class TechnicalDictionaryAdmin(BaseModelAdmin):
    list_display = ['term', 'created_by', 'created', 'updated_by']
    search_fields = ['term']
    list_filter = ['created_by', 'created', 'updated_by']

class ShiftHandoverAdmin(BaseModelAdmin):
    list_display = ['start_time', 'end_time', 'created_by', 'handed_over_to', 'created', 'updated_by']
    search_fields = ['start_time', 'end_time', 'created_by__username', 'handed_over_to__username']
    list_filter = ['created_by', 'handed_over_to', 'created', 'updated_by']

class NoticeAdmin(BaseModelAdmin):
    list_display = ['title', 'author', 'created', 'updated_by']
    search_fields = ['title', 'author__username']
    list_filter = ['author', 'created', 'updated_by']

class GeneralProblemAdmin(BaseModelAdmin):
    list_display = ['title', 'created_by', 'resolved', 'created', 'updated_by']
    search_fields = ['title', 'created_by__username']
    list_filter = ['created_by', 'resolved', 'created', 'updated_by']

class AnnouncementAdmin(BaseModelAdmin):
    list_display = ['title', 'author', 'start_date', 'end_date', 'created', 'updated_by']
    search_fields = ['title', 'author__username']
    list_filter = ['author', 'start_date', 'end_date', 'created', 'updated_by']

class SystemMaintenanceAdmin(BaseModelAdmin):
    list_display = ['title', 'created_by', 'start_time', 'end_time', 'completed', 'created', 'updated_by']
    search_fields = ['title', 'created_by__username']
    list_filter = ['created_by', 'start_time', 'end_time', 'completed', 'created', 'updated_by']

class TeamMeetingAdmin(BaseModelAdmin):
    list_display = ['title', 'created_by', 'date', 'time', 'location', 'created', 'updated_by']
    search_fields = ['title', 'created_by__username', 'location']
    list_filter = ['created_by', 'date', 'time', 'location', 'created', 'updated_by']

class BestPracticeAdmin(KnowledgeBaseItemAdmin):
    pass

class ReminderAdmin(BaseModelAdmin):
    list_display = ['title', 'assigned_to', 'due_date', 'completed', 'created', 'updated_by']
    search_fields = ['title', 'assigned_to__username']
    list_filter = ['assigned_to', 'due_date', 'completed', 'created', 'updated_by']

class GeneralNotesAdmin(BaseModelAdmin):
    list_display = ['title', 'created_by', 'resolved', 'created', 'updated_by']
    search_fields = ['title', 'created_by__username']
    list_filter = ['created_by', 'resolved', 'created', 'updated_by']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, KnowledgeBaseItemAdmin)
admin.site.register(FAQ, KnowledgeBaseItemAdmin)
admin.site.register(Procedure, KnowledgeBaseItemAdmin)
admin.site.register(TechnicalDictionary, TechnicalDictionaryAdmin)
admin.site.register(ShiftHandover, ShiftHandoverAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(GeneralProblem, GeneralProblemAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(SystemMaintenance, SystemMaintenanceAdmin)
admin.site.register(TeamMeeting, TeamMeetingAdmin)
admin.site.register(BestPractice, BestPracticeAdmin)
admin.site.register(Reminder, ReminderAdmin)
admin.site.register(GeneralNotes, GeneralNotesAdmin)