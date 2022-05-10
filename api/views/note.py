from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .. import models, permissions, mixins, serializers


class NoteViewSet(mixins.RefineResponseMixin, viewsets.ModelViewSet):
    """- Создать, получить, удалить заметки """
    permission_classes = [permissions.IsUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_relevant', 'is_public', 'status', 'author']
    search_fields = ['title', 'description', 'content']
    ordering_fields = ['-updated_date', 'is_relevant']
    ordering = ['-id']

    def get_serializer_class(self):
        """- переопределить метод получения serializer """
        if self.action == 'create':
            return serializers.CreateNoteSerializer
        elif self.action == 'update':
            return serializers.UpdateNoteSerializer
        return serializers.GetNoteSerializer

    def get_queryset(self):
        """- переопределить запрос """
        # показать все записи, только зарегистрированному пользователю.
        if self.request.auth:
            return models.Note.objects.all()
        return models.Note.objects.filter(is_public=True).all()
