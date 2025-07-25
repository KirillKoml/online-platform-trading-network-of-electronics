from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """Класс для определения, что пользователь авторизован и его статус активный"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active