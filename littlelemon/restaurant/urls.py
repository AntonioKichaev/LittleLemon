from django.contrib import admin
from django.urls import path,include
from .views import HomeView,MenuItemView,SingleMenuItemView,BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables',BookingViewSet)

urlpatterns = [
    path("", HomeView.as_view(),name='home'),
    path("menu", MenuItemView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    path("booking/",include(router.urls))

]