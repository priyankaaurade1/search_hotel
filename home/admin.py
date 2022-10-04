from django.contrib import admin

# Register your models here.
from .models import *

class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','hotel_price','hotel_description']

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImage)


