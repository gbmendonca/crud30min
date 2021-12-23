from django.contrib import admin
from .models import Product
# para gerenciar lista de produtos pelo admin, precisa importar ele (linha 2) e o registrar (linha 6


admin.site.register(Product)
