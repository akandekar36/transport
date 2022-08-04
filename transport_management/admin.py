from django.contrib import admin
from django.views.generic import ListView
from .models import Client, Vehicle, VehicleMaintanance, Driver, Product, Booking, Expense
# Register your models here.


# from .models import (
#     Booking,
#     Supplier,
#     Buyer,
#     Season,
#     Drop,
#     Product,
#     Order,
#     Delivery,
#     Vehical,
#     Driver,
#     Goods,
#     VehicleMaintanance,
#     Booking
# )


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address', 'created_date']

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['registration_no', 'owner_name', 'manufacture_company', 'insurance_valid_till', 'permit_tax_valid_till', 'fitness_valid_till']

class VehicleMaintananceAdmin(admin.ModelAdmin):
    list_display = ['vehicle_no', 'date_of_initialization', 'odometer_reading', 'oil_changed', 'spare_parts_replaced', 'total_cost_of_maintenance']

class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number','aadhar_card_no', 'liscence_no', 'liscence_expiry_date', 'joining_date', 'remarks']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight_in_kg','rate']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['client','vehicle','product','no_of_product','driver','loading_date','weight_in_tons','location_from','location_to','freight_amount']

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['booking_no','diesel','fastag','driver_expense','uncertainty','miscellaneous']

admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleMaintanance, VehicleMaintananceAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Expense, ExpenseAdmin)
