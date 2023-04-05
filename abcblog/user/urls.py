from django.urls import path
from user import views


urlpatterns = [
    path('login/', views.login),
    path('add/', views.SignUpViews.as_view(), name='register')

]