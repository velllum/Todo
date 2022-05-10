from django.db import models
from django.contrib.auth import get_user_model

from .note import Note


User = get_user_model()


class Comment(models.Model):
    """- Комментарии """

    text = models.TextField(verbose_name="Содержание")
    note = models.ForeignKey(Note, related_name="comments", on_delete=models.CASCADE, verbose_name="Заметка")
    user = models.ForeignKey(User, related_name="commentators", on_delete=models.CASCADE, verbose_name="Пользователь")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ['pk']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
