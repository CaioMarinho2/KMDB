from rest_framework import permissions
from rest_framework.views import Request, View


class MoviesRotesPermition(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        return (request.method=="GET" or request.user.is_authenticated and request.user.is_superuser)