from django.db.models import OuterRef
from django.db.models import Q
from django.db.models import Subquery
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.chat.models.chat import ChatRoom
from apps.chat.models.message import Message
from apps.chat.serializers.chat import ChatReceiveSerializer


class ChatsReceiveView(ListModelMixin, GenericViewSet):
    serializer_class = ChatReceiveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.GET.get('first_user')
        last_message_subquery = (
            Message.objects.filter(chat_room=OuterRef('pk')).order_by('created_at').values('created_at')[:1]
        )

        return (
            ChatRoom.objects.filter(Q(first_user=user) | Q(second_user=user))
            .annotate(last_message_time=Subquery(last_message_subquery))
            .order_by('last_message_time')
        )
