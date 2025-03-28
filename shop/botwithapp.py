from django.contrib import admin

from .models import Users, Category, TeaItems, Cards, OrderItems, Orders, Announcements


class OrdersTabAdmin(admin.TabularInline):
    model = Orders
    fields = ['id', 'status']
    readonly_fields = ['created_dt']
    extra = 1


class CardTabAdmin(admin.TabularInline):
    model = Cards
    fields = ['tea_item', 'quantity']
    search_fields = ['tea_item']
    extra = 1


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'tg_id', 'tg_name']
    search_fields = ['item_name__']

    inlines = [CardTabAdmin, OrdersTabAdmin]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(TeaItems)
class TeaItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_desc', 'item_price', 'item_weight']
    ordering = ["item_name"]


class OrderItemsTabAdmin(admin.TabularInline):
    model = OrderItems
    fields = ['tea_item', 'price', 'quantity']
    search_fields = ['tea_item']
    extra = 0


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'created_dt', 'last_updated_dt', 'status']
     search_fields = ['id']
     list_filter = ["status"]
     inlines = [OrderItemsTabAdmin]


@admin.register(Announcements)
class OrdersAdmin(admin.ModelAdmin):
     list_display = ['announcement_desc']