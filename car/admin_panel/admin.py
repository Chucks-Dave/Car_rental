from django.contrib import admin
from .models import AboutUs, Branch, Brand, NewCar, Vehicle, VehicleComment


# Register Brand Model
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


# Register Branch Model
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


# Register Vehicle Model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


# Register Vehicle Comment Model
@admin.register(VehicleComment)
class VehicleCommentAdmin(admin.ModelAdmin):
    pass


# Register New Car Model
@admin.register(NewCar)
class NewCarAdmin(admin.ModelAdmin):
    pass


# Register About Us Model
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    pass
