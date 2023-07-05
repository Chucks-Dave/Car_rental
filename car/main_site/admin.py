from django.contrib import admin

from .models import FAQ, Booking, CustomerQuery, CustomerReview

# Register your models here.


# Register Booking Model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


# Register Customer Review Model
@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    pass


# Register Customer Query Model
@admin.register(CustomerQuery)
class CustomerQueryAdmin(admin.ModelAdmin):
    pass


# Register FAQ Model
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass
