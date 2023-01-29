from django.shortcuts import render
from django.views import View
from rest_framework import generics
from .models import Menu,Booking
from .serializers import MenuSerialize,BookingSerialize
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class HomeView(View):


    def get(self,request):

        return render(request=request,template_name='index.html',context={})


class BookView(View):

    def get(self,request):
        return render(request=request,template_name='book.html',context={})

class MenuView(View):

    def get(self,request):
        return render(request=request,template_name='menu.html',context={})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialize
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialize

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerialize
    permission_classes = [IsAuthenticated]
