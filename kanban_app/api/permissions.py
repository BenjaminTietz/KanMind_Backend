from rest_framework.permissions import BasePermission

class IsBoardMemberOrOwner(BasePermission):
    """
    Board permissions:
    - LIST / CREATE: authenticated users
    - DETAIL: owner or member
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            obj.owner == request.user
            or obj.members.filter(id=request.user.id).exists()
        )