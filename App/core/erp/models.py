from django.db import models
from datetime import datetime 

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name="Tipo",unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = 'erp_type'
        ordering = ['name']
        
class Category(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=150, verbose_name="Categoría")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        db_table = 'erp_category'
        ordering = ['name']
        
class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Tipo")
    id = models.AutoField(primary_key=True, verbose_name="ID") 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dni = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(default=datetime.now,verbose_name="Fecha de Registro")
    age = models.IntegerField(default=18,verbose_name="Edad")
    phone = models.CharField(max_length=15,verbose_name="Teléfono")
    address = models.CharField(max_length=100,verbose_name="Dirección")
    position = models.CharField(max_length=50,verbose_name="Cargo")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salario")
    avatar = models.ImageField(upload_to='avatars/',null= True, blank=True, verbose_name="Avatar")
    cvitae = models.FileField(upload_to='cvitas/',null= True, blank=True, verbose_name="Curriculum Vitae")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados" 
        db_table = 'erp_employee'
        ordering = ['id']
