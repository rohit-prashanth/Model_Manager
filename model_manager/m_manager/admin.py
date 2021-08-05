from django.contrib import admin
from .models import A
# Register your models here.

@admin.register(A)
class Admin_A(admin.ModelAdmin):
    list_display = ['name','age','address']