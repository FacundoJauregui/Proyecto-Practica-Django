from django.db import models
from datetime import datetime 

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.name} {self.last_name} - {self.dni}"
    
    class Meta:
        db_table = 'erp_client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['dni']
        
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(default=datetime.now, blank=True)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Sale {self.sale_id} - {self.client.name} {self.client.last_name}"
    
    class Meta:
        db_table = 'erp_sale'
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        ordering = ['sale_date']
        
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'erp_product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
        
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'erp_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Sale_Detail(models.Model):
    sale_detail_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Detail {self.sale_detail_id} - Sale {self.sale.sale_id} - Product {self.product.name}"
    
    class Meta:
        db_table = 'erp_sale_detail'
        verbose_name = 'Sale Detail'
        verbose_name_plural = 'Sale Details'
        ordering = ['sale_detail_id']