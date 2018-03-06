from rest_framework import serializers

from .models import app_1

class app_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = app_1
        fields = '__all__'