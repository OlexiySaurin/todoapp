from tasks import models
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SimpleTaskSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = models.SimpleTask
        fields = ['id', 'title', 'completed', 'updated_at', 'due_date', 'email']
        read_only_fields = ['updated_at', 'email']
