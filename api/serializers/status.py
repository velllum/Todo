from rest_framework import serializers

from api import models


class StatusSerializer(serializers.ModelSerializer):
    """- Получить, создать, обновить """

    class Meta:
        model = models.Status
        fields = '__all__'
