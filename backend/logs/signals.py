from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import LogEntry
from core.models import Company, Sector, Extensions, DataCenter, AccessRelease
from inventory.models import Equipment, IPAddress, Rack
from networks.models import Switch, SwitchPort
from voip.models import Server_Gateway, Server_Portability, Server_XenServer, Softswitch_VSC
from intranet.models import (Category, Article, FAQ, Procedure, TechnicalDictionary, ShiftHandover, Notice,
                             GeneralProblem, Announcement, SystemMaintenance, TeamMeeting, BestPractice,
                             Reminder, GeneralNotes)



models_to_track = [
                    Company, Sector, Extensions, DataCenter, AccessRelease,
                    Equipment, IPAddress, Rack,
                    Switch, SwitchPort, 
                    Softswitch_VSC, Server_Gateway, Server_Portability, Server_XenServer,
                    Category, Article, FAQ, Procedure, TechnicalDictionary, ShiftHandover, Notice,GeneralProblem, Announcement, SystemMaintenance, TeamMeeting, BestPractice, Reminder, GeneralNotes,
                   ]

def create_log_entry(sender, instance, action, **kwargs):
    if not issubclass(sender, LogEntry):
        content_type = ContentType.objects.get_for_model(instance)
        LogEntry.objects.create(
            content_type=content_type,
            object_id=instance.id,
            action=action,
            user=instance.updated_by
        )

def handle_post_save(sender, instance, **kwargs):
    create_log_entry(sender, instance, action="Update", **kwargs)

def handle_post_delete(sender, instance, **kwargs):
    create_log_entry(sender, instance, action="Delete", **kwargs)

for model in models_to_track:
    post_save.connect(handle_post_save, sender=model)
    post_delete.connect(handle_post_delete, sender=model)