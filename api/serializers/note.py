from rest_framework import serializers

from . import GetCommentSerializer
from .. import models


class GetNoteSerializer(serializers.ModelSerializer):
    """- Получить """
    author = serializers.SerializerMethodField(method_name='get_full_name')
    status = serializers.CharField(source='status.name')
    comments = GetCommentSerializer(many=True)

    class Meta:
        model = models.Note
        fields = '__all__'

    @classmethod
    def get_full_name(cls, obj):
        """- Получить полное имя """
        if obj.author.first_name or obj.author.last_name:
            return f'{obj.author.first_name} {obj.author.last_name} ({obj.author.username})'.strip()
        return obj.author.username

    def to_representation(self, instance):
        """- переопределить метод с данными """
        representation = super().to_representation(instance)
        # определить поле comments в конец
        representation.move_to_end('comments', last=True)
        return representation


class CreateNoteSerializer(serializers.ModelSerializer):
    """- Создать """
    STATUS_DEFAULT = 1  # статус по умолчанию 'Активно'

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status_id = serializers.HiddenField(default=STATUS_DEFAULT)

    class Meta:
        model = models.Note
        fields = ['title', 'description', 'content', 'author', 'status_id']

    def validate(self, data):
        """- Проверка на валидности """
        # Проверка заголовка на уникальность, так как от него зависит поле slug
        if self.Meta.model.objects.filter(title=data.get("title")).exists():
            raise serializers.ValidationError({"title": "Такой заголовок уже существует."})
        return data


class UpdateNoteSerializer(serializers.ModelSerializer):
    """- Обновить """

    class Meta:
        model = models.Note
        fields = ['title', 'description', 'content', 'is_relevant', 'is_public', 'status']

    def validate(self, data):
        """- Проверка на валидности """
        # Проверка заголовка на уникальность, за исключением текущего, так как от него зависит поле slug
        if self.Meta.model.objects.exclude(pk=self.instance.id).filter(title=data.get("title")).exists():
            raise serializers.ValidationError(
                {"title": "Такой заголовок (title) уже существует. Для формирования slug, измените его."}
            )
        return data
