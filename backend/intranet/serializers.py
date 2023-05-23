
from rest_framework import serializers
from .models import (Category, Article, FAQ, Procedure, TechnicalDictionary, ShiftHandover, Notice,
                     GeneralProblem, Announcement, SystemMaintenance, TeamMeeting, BestPractice,
                     Reminder, GeneralNotes)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class KnowledgeBaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class TechnicalDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalDictionary
        fields = '__all__'

class ShiftHandoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftHandover
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class GeneralProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralProblem
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class SystemMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemMaintenance
        fields = '__all__'

class TeamMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMeeting
        fields = '__all__'

class BestPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestPractice
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class GeneralNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralNotes
        fields = '__all__'