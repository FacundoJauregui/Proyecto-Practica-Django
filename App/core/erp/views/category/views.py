from django.shortcuts import render

from core.erp.models import Category  # Import your Category model

def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all().order_by('category_id')  # Assuming you have a Category model defined
        
    }
    
    return render(request, 'category/list.html', data)

