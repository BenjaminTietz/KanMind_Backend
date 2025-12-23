from django.db.models import Count, Q
from kanban_app.models import Board
from auth_app.models import CustomUser
from django.db import transaction

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

@transaction.atomic
def create_board(owner, title, member_ids=None):
    board = Board.objects.create(
        title=title,
        owner=owner,
    )

    members = []

    if member_ids:
        members = list(CustomUser.objects.filter(id__in=member_ids))

    # Owner darf optional Member sein – aber nicht doppelt
    if owner not in members:
        members.append(owner)

    board.members.set(members)
    board.member_count = len(members)
    board.save()

    return board