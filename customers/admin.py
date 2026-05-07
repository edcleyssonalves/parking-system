from django.contrib import admin
from customers.models import Customer


@admin.register(Customer)
class CustumerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'cpf')
    search_fields = ('user', 'name', 'cpf')
