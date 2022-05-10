from rest_framework import viewsets, permissions

from .. import models, mixins, serializers


class StatusViewSet(mixins.RefineResponseMixin, viewsets.ModelViewSet):
    """- Создать, получить статусы """
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAdminUser]
