from django.urls import path

from core.erp.views import myfirst_view

urlpatterns = [
    path('erp/', myfirst_view, name='myfirst_view'),
]