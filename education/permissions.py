from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists()


class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_moderator = request.user.groups.filter(name='moderator').exists()

        return obj.user == request.user or is_moderator
