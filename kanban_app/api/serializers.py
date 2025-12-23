from rest_framework import serializers
from kanban_app.models import Board
from auth_app.models import CustomUser


class BoardCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    members = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )

    def validate_members(self, value):
        users = CustomUser.objects.filter(id__in=value)
        if users.count() != len(set(value)):
            raise serializers.ValidationError("One or more users do not exist.")
        return value
    


class BoardListSerializer(serializers.ModelSerializer):
    member_count = serializers.IntegerField(read_only=True)
    ticket_count = serializers.IntegerField(read_only=True)
    tasks_to_do_count = serializers.IntegerField(read_only=True)
    tasks_high_prio_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Board
        fields = [
            "id",
            "title",
            "member_count",
            "ticket_count",
            "tasks_to_do_count",
            "tasks_high_prio_count",
            "owner_id",
        ]