from django.contrib import admin
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.erp.models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Sale_Detail)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
