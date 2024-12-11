from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline): 
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

# Custom User admin
class UserAdmin(BaseUserAdmin):  # Extend from BaseUserAdmin
    inlines = [ProfileInline]

# Unregister the original User model and re-register with the custom UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


