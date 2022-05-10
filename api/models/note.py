from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from .status import Status


User = get_user_model()


class Note(models.Model):
    """- Заметка"""

    title = models.CharField(max_length=250, verbose_name="Заголовок")
    description = models.CharField(max_length=250, verbose_name="Краткое описания")
    content = models.TextField(verbose_name="Описания")
    is_relevant = models.BooleanField(default=False, verbose_name="Важное")
    is_public = models.BooleanField(default=True, verbose_name="Публичное")
    status = models.ForeignKey(Status, related_name="statuses", on_delete=models.CASCADE, verbose_name="Статус")

    author = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE, verbose_name="Автор")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="ЧПУ")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        """- переопределяем свойства slug"""
        if self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['pk']
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
