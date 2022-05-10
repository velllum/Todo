from django.db import models


class Status(models.Model):
    """- Статусы"""

    name = models.CharField(max_length=250, verbose_name="Наименование")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('pk',)
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
