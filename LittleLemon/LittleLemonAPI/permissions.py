from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAdminUser
)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Manager").exists()


class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Delivery Crew").exists()


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        # return (request.method in SAFE_METHODS) and request.user.is_authenticated
        return request.method in SAFE_METHODS


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # The IsAdminUser permission class will deny permission to any user, unless user.is_staff is True in which case permission will be allowed
        return request.user.is_authenticated and IsAdminUser
