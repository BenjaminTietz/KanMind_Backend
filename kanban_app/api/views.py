from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import BoardListSerializer, BoardCreateSerializer
from .services.board_service import (
    get_board_queryset_for_user,
    create_board,
)


class BoardViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return get_board_queryset_for_user(self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return BoardCreateSerializer
        return BoardListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        board = create_board(
            owner=request.user,
            title=serializer.validated_data["title"],
            member_ids=serializer.validated_data.get("members", []),
        )

        response_serializer = BoardListSerializer(board)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)