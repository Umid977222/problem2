from .models import Group, ClassRoom, Attendance, Payments
from rest_framework import serializers


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'VALUE_TYPE', 'VALUE_TYPE2', 'name', 'room', 'teacher', 'student_size', 'students',
                  'start_time', 'days', 'status', 'text']


class RoomSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'student_size']


class AttendanceSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'VALUE_TYPE', 'group_id', 'student_id', 'data', 'attendance']


class PaymentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payments
        fields = ['id', 'VALUE_TYPE', 'student', 'data', 'amount', 'amount_type']
