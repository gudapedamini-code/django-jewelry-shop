from django.contrib import admin
from .models import Address, Blog, Category, Product, Cart, Order, OrderItem, Coupon, Review
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .utils import send_delivery_email
from django.utils.html import format_html
from allauth.socialaccount.models import SocialAccount, SocialToken


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state', 'pincode')
    list_filter = ('city', 'state')
    list_per_page = 10
    search_fields = ('address', 'city', 'state', 'pincode')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title", )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'product_image', 'is_active', 'is_featured', 'updated_at')
    list_editable = ('slug', 'category', 'is_active', 'is_featured')
    list_filter = ('category', 'is_active', 'is_featured')
    list_per_page = 10
    search_fields = ('title', 'category', 'short_description')
    prepopulated_fields = {"slug": ("title", )}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_editable = ('quantity',)
    list_filter = ('created_at',)
    list_per_page = 20
    search_fields = ('user', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'ordered_date')
    list_editable = ('quantity', 'status')
    list_filter = ('status', 'ordered_date')
    list_per_page = 20
    search_fields = ('user', 'product')
    
    def save_model(self, request, obj, form, change):
        if change:
            previous = Order.objects.get(pk=obj.pk)
            if previous.status != obj.status and obj.status == 'Delivered':
                send_delivery_email(obj.user.email, obj.product.title ,obj.id)
        super().save_model(request, obj, form, change)


class CustomUserAdmin(UserAdmin):
    def profile_picture(self, obj):
        if hasattr(obj, 'profile') and obj.profile.image:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%; object-fit:cover;" />',
                obj.profile.image.url
            )
        return "No Image"
    profile_picture.short_description = "Profile Picture"

    def verified_status(self, obj):
        return "✅ Verified" if obj.is_active else "❌ Not Verified"
    verified_status.short_description = "Verification Status"

    def delete_model(self, request, obj):
        SocialAccount.objects.filter(user=obj).delete()
        SocialToken.objects.filter(account__user=obj).delete()
        obj.delete()
    
    list_display = ( 'username', 'profile_picture', 'email', 'verified_status', 'date_joined')
    list_filter = ['is_active']
    search_fields = ('username', 'email')
    

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'discount_value', 'usage_limit', 'used_count', 'is_active']
    list_filter = ['is_active', 'discount_type']
    search_fields = ['code']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'comment']



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Blog)
admin.site.register(Review,ReviewAdmin)

