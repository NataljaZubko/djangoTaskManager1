from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Позволяет редактировать объект только его владельцу.
    """

    def has_object_permission(self, request, view, obj):
        # Все пользователи могут просматривать (GET, HEAD, OPTIONS)
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Только владелец может изменять объект
        return obj.owner == request.user