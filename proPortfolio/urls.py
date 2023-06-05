from django.contrib import admin
from django.urls import path
from mainDashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.baseView, name='base'),
]
