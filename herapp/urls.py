from django.contrib import admin
from django.urls import path

from herapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('f/', views.home),
]
