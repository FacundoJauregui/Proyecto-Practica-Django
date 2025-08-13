from django.urls import path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.erp.views.category.views import category_list

urlpatterns = [
    path('category/list/', category_list, name='category_list'),
]