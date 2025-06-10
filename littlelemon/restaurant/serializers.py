from rest_framework import serializers
from .models import Menu,Booking
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['url','username','email','groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    booking_date= serializers.DateTimeField(format='%Y-%m-%d %H', input_formats=['%Y-%m-%d %H'])
    class Meta:
        model=Booking
        fields=['name','no_of_guests','booking_date']


