from django.contrib import admin

# Register your models here.
from .models import *

# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'quantity', 'scheme','rate','discountPercent','discount','gst',
#                     'value','date_created','product_image')
# admin.site.register(Purchase, PurchaseAdmin)




class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'scheme','discountPercent','discount','gst',
                    'value','date_created','user','date')

admin.site.register(Purchase, PurchaseAdmin)


# class salesItemInline(admin.TabularInline):
#     model =Product
#
#
# class salesAdmin(admin.ModelAdmin):
#     list_display = ('quantity', 'scheme','discountPercent','discount','gst',
#                     'value','date_created','user','date')
#     list_filter = [ 'date_created']
#     inlines = [salesItemInline]
# class saleAdmin(admin.ModelAdmin):
#    list_display = ('quantity', 'scheme','discountPercent','discount','gst',
#                    'value','date_created','user','date')
# #
# admin.site.register(sale, saleAdmin)
#
class employeeAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'email', 'HomeAdress','Salary','user')

admin.site.register(Employee, employeeAdmin)

class routesAdmin(admin.ModelAdmin):
    list_display = ('AreaName','AreaDistance','user')

admin.site.register(Routes, routesAdmin)

admin.site.register(Company)
admin.site.register(Product)
admin.site.register(SaleProduct)



class saleAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'scheme','discountPercent','discount','gst',
                    'value','date_created','user','date')
    model = sale

admin.site.register(sale, saleAdmin)
admin.site.register(OrderItem)