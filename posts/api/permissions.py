from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = 'you are not the owner of the post'

    def has_permission(self, request, view):
        my_safe_method = ['GET','PUT']
        if request.method in my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user