from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
class IsUserOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.id==obj.id:
            return True
        

     
     
                