from django.contrib import admin
from material.models import Material



@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome','fabricante','descrição','lote','data_registro','preco_de_compra','preco','quantidade']
    
