from rest_framework import viewsets, permissions
from .serializers import GroupSerializers, AttendanceSerializers, PaymentSerializers, RoomSerializers
from .models import Group, Attendance, ClassRoom, Payments

# Create your views here.


class GroupViewSet(viewsets.ModelViewSet):
    """Group
    ViewSet
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AttendanceViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Attendance.objects.all().order_by('id')
    serializer_class = AttendanceSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClassRoomViewSet(viewsets.ModelViewSet):
    """"""
    queryset = ClassRoom.objects.all().order_by('id')
    serializer_class = RoomSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PaymentViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Payments.objects.all().order_by('id')
    serializer_class = PaymentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
