from django.urls import path
from rest_framework.authtoken import views

from .views import RegisterCreateApiView,logout

urlpatterns = [
    path('register/',RegisterCreateApiView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', logout),
]


