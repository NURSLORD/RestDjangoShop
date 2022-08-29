from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.position == 'A' else False


class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.position == 'M' else False


class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.position == 'S' else False


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.position == 'C' else False


class IsSixteen(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.age >= 16 else False


