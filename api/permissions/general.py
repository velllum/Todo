from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """- разрешение позволяющее только владельцам объекта редактировать """

    def has_object_permission(self, request, view, obj):
        """- переопределить метод работающий только с одной записью """
        if request.method in permissions.SAFE_METHODS:
            return True

        # если пользователь объекта равны, то возвращаем True, иначе False
        return obj.author == request.user
