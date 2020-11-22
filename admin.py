from django.contrib import admin
from .models import Facility,Category,Room,Booking,contact
class BookingAdmin(admin.ModelAdmin):
    def get_readonly_fields(self,request,obj=None):
        if obj:
            return ['userid','name','emailid','Idetitity','BookingDate','ArrivalDate','DepartureDate','gender','address','bookingnumber','roomid']
        else:
            return []
# Register your models here.
admin.site.register(Facility)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Booking,BookingAdmin)
admin.site.register(contact)