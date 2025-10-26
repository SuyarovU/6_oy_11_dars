from django.contrib import admin
from .models import Xodim
# Register your models here.
@admin.register(Xodim)
class XodimAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'position', 'salary', 'join_date', 'city', 'department']