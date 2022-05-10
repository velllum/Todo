from rest_framework import serializers

from .. import models


class CreateCommentSerializer(serializers.ModelSerializer):
    """- создать """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Comment
        fields = ['text', 'note', 'user']


class GetCommentSerializer(serializers.ModelSerializer):
    """- Получить """
    user = serializers.SerializerMethodField(method_name='get_full_name')

    class Meta:
        model = models.Comment
        fields = ['id', 'user', 'text', 'created_date']

    @classmethod
    def get_full_name(cls, obj):
        """- Получить полное имя """
        if obj.user.first_name or obj.user.last_name:
            return f'{obj.user.first_name} {obj.user.last_name} ({obj.user.username})'.strip()
        return obj.user.username


class GetListCommentSerializer(GetCommentSerializer):
    """- Получить список """
    class Meta(GetCommentSerializer.Meta):
        fields = '__all__'
