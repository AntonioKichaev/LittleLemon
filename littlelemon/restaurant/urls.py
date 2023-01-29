from django.contrib import admin
from django.urls import path,include
from .views import (
    HomeView,
    MenuItemView,
    SingleMenuItemView,
    BookingViewSet,
    BookView,
    MenuView
)
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables',BookingViewSet,basename='booking')

urlpatterns = [
    path("", HomeView.as_view(),name='home'),
    path("menu/",MenuView.as_view(),name="menu"),
    path("menu-items", MenuItemView.as_view()),
    path("menu-items/<int:pk>", SingleMenuItemView.as_view()),
    path('book',BookView.as_view(),name='book'),

    path("booking/",include(router.urls)),
    path('api-token-auth/',obtain_auth_token),
    

]