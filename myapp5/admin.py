from django.contrib import admin
from .models import Product, Category

# Register your models here.

@admin.action(description='Сбросить количество в 0')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['category']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описание продукта'
    actions = [reset_quantity]

    #fields = ['name', 'description', 'category', 'date_added', 'price', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'classes': ['collapse'],
                'fields': ['price', 'quantity'],
            },
        ),
        (
            'Рейтинг и прочее',
            {
                'classes': ['collapse'],
                'description': 'Рейтинг сформирован автоматическ',
                'fields': ['rating', 'date_added'],
            },
        ),
    ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)