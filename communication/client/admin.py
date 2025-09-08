from django.contrib import admin
from client.models import Order, OrderItem, User









#Registeration

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [ OrderItemInline ] 

admin.site.register(Order, OrderAdmin)
admin.site.register(User)

 