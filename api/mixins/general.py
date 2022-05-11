from rest_framework import views, response, exceptions, versioning


class RefineResponseMixin(views.APIView):
    """- разрешение позволяющее только владельцам объекта редактировать """

    def finalize_response(self, request, response, *args, **kwargs):
        """- переопределить метод отвечающий за ответ - Response """
        if not response.exception:
            response.data = {'success': True, 'data': response.data}
        return super().finalize_response(request, response, *args, **kwargs)

    def get_exception_handler(self):
        """- переопределить метод ответа исключения. """
        default_handler = super().get_exception_handler()

        def handle_exception(exc, context):
            if not isinstance(exc, (exceptions.APIException,)):
                # неизвестное исключение
                return default_handler(exc, context)
            return response.Response({'success': False, 'error': {'code': exc.status_code, 'message': exc.detail}})

        return handle_exception
