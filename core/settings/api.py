
REST_FRAMEWORK = {
    # общий доступ по умолчанию
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    # Авторизация, аутентификация
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # проверка статусов ошибок
    'EXCEPTION_HANDLER': 'api.utils.custom_exception_handler',
    # пагинация
    'DEFAULT_PAGINATION_CLASS': 'api.utils.StandardResultsSetPagination',
}
