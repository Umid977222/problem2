from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register(r'center', views.GroupViewSet, basename='group')
router.register(r'attendance', views.AttendanceViewSet, basename='attendance')
router.register(r'payments', views.PaymentViewSet, basename='payments')
router.register(r'rooms', views.ClassRoomViewSet, basename='rooms')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    ]
