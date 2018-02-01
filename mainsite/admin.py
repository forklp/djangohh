from django.contrib import admin
from .models import Port
from .models import Product
# Register your models here.
class PortAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_time')

admin.site.register(Port,PortAdmin)
admin.site.register(Product)