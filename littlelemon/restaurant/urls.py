#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',views.MenuView.as_view(),name='menu-list'),
    path('menu/<int:pk>',views.SingleMenuView.as_view()),
    path('api-token-auth/',obtain_auth_token),
]
