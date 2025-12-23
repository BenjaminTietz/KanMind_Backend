from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import BoardListSerializer
from .services.board_service import get_board_queryset_for_user
from .permissions import IsBoardMemberOrOwner

class BoardViewSet(ModelViewSet):
    serializer_class = BoardListSerializer
    permission_classes = [IsAuthenticated, IsBoardMemberOrOwner]

    def get_queryset(self):
        print("USER:", self.request.user)
        print("AUTH:", self.request.auth)
        return get_board_queryset_for_user(self.request.user)

