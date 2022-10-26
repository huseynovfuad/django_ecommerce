from django.contrib import admin
from .models import Category, Subcategory, Brand, Product, ProductImage, Basket

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    list_display = ("name", "slug", "created_at", "updated_at")


admin.site.register(Category, CategoryAdmin)


class SubcategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Subcategory

    list_display = ("name", "category", "slug", "created_at", "updated_at")


admin.site.register(Subcategory, SubcategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    class Meta:
        model = Brand

    list_display = ("name", "slug", "created_at", "updated_at")


admin.site.register(Brand, BrandAdmin)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_display = (
        "name",
        "slug",
        "subcategory",
        "brand",
        "price",
        "tax_price",
        "discount_price",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)


admin.site.register(Basket)