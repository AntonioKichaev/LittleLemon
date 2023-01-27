from rest_framework import serializers
from .models import Menu,Booking



class MenuSerialize(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields=['id','title','price','inventory']


class BookingSerialize(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields="__all__"