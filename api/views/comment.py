from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from .. import models, mixins, serializers


class CommentViewSet(mixins.RefineResponseMixin, viewsets.ModelViewSet):
    """- Создать, получить комментарии """
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    http_method_names = ["get", "post"]
    filterset_fields = ['note', 'user']
    search_fields = ['title']
    ordering_fields = ['-updated_date', 'note', 'user']
    ordering = ['-id']

    def get_serializer_class(self):
        """- переопределить метод получения serializer """
        if self.action == 'create':
            return serializers.CreateCommentSerializer
        if self.action == 'list':
            return serializers.GetListCommentSerializer
        return serializers.GetCommentSerializer
