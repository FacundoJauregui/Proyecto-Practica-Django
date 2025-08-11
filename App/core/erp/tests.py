import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Ahora puedes hacer:
from Config import wsgi
# ...resto del código...
from core.erp.models import Type

'''# SELECT * FROM erp_type

query = Type.objects.all()

#INSERT INTO erp_type (name) VALUES ('Test Type')

t = Type()
t.name = "Test Type2"
t.save()  # Guardar el objeto en la base de datos

#UPDATE erp_type SET name = 'Updated Type' WHERE id = 1
try :
    t = Type.objects.get(id=10)
    t.name = "Updated Type"
    t.save()  # Guardar los cambios en la base de datos
except Exception as e:
    print(f"Error: {e}")
    
  
#DELETE FROM erp_type WHERE id = 1
try :
    t = Type.objects.get(id=10)
    t.delete()  # Eliminar el objeto de la base de datos
except Exception as e:
    print(f"Error: {e}")'''
    
'''obj1 = Type.objects.filter(name="Test Type2")
print(obj1)
obj2 = Type.objects.filter(name__contains="Test")
print(obj2)
obj2 = Type.objects.filter(name__icontains="test")
print(obj2)'''
