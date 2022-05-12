from django import views
from django.core.serializers.json import DjangoJSONEncoder
from django.test import Client
from django.shortcuts import render


class BaseView(views.View):
    """- Базовое представление """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = Client(json_encoder=DjangoJSONEncoder, HTTP_USER_AGENT='Mozilla/5.0')


class ListView(BaseView):
    """- Вывод списком """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.context = {}

    def get(self, request):
        dictionary = self.client.get('/api/v1/notes/').json()

        if dictionary.get('success'):
            self.context['list_dicts'] = dictionary['data']['results']

        return render(request, template_name='index.html', context=self.context)


class DetailView(views.View):
    """- Детальный вывод """

    def get(self, request, *args, **kwargs):
        ...


class CreateView(views.View):
    """- Создать """

    def post(self, request, *args, **kwargs):
        ...


class EditView(views.View):
    """- Редактировать """

    def put(self, request, *args, **kwargs):
        ...


class DeleteView(views.View):
    """- Удалить """

    def delete(self, request, *args, **kwargs):
        ...

