from django.db.models import Count, Q
from kanban_app.models import Board

def get_board_queryset_for_user(user):
    return (
        Board.objects
        .filter(Q(owner=user) | Q(members=user))
        .distinct()
        .annotate(
            member_count=Count("members", distinct=True),
            ticket_count=Count("tasks", distinct=True),
            tasks_to_do_count=Count(
                "tasks",
                filter=Q(tasks__status="to-do"),
                distinct=True,
            ),
            tasks_high_prio_count=Count(
                "tasks",
                filter=Q(tasks__priority="high"),
                distinct=True,
            ),
        )
    )
