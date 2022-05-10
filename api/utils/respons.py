from typing import Dict

from rest_framework import status
from rest_framework.response import Response


class Message:
    """- Ответы сообщения """

    @classmethod
    def success(cls, kwargs: Dict, status_code: status = status.HTTP_200_OK) -> Response:
        """- передача положительного ответа """
        kw = {"success": True, "data": kwargs}
        return Response(data=kw, status=status_code)

    @classmethod
    def errors(cls, kwargs: Dict, status_code: status = status.HTTP_400_BAD_REQUEST) -> Response:
        """- передача отрицательного ответа """
        kw = {"success": False, "status": status_code, "error": kwargs}
        return Response(data=kw, status=status_code)
