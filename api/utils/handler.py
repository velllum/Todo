from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """- Обработчик статусов"""

    response = exception_handler(exc, context)

    if response is None:
        return response

    if not response.status_code:
        return response

    if not response.data:
        return response

    return Response({'success': False, 'error': {'code': response.status_code, 'message': response.data}})
