from django.shortcuts import render
from rest_framework import generics
from .models import Menu,Booking
from .serializers import UserSerializer,MenuSerializer

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer




class SingleMenuView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer

