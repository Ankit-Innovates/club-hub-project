from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'ADMIN'

class IsEventAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'EVENT_ADMIN'

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'STUDENT' 