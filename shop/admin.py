from django.contrib import admin

# Register your models here.
from shop.models import *
from django.db.models import QuerySet


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']
    list_per_page = 5
    search_fields = ['description', 'title']


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_display_links = list_display
    list_per_page = 20
    search_fields = list_display


class ItemOrderAdmin(admin.TabularInline):
    model = ItemOrders
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemOrderAdmin]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_category', 'category', 'gender', 'cur', 'amount',
                    'article', 'old_price', 'is_popular', 'pub_date']
    list_display_links = ['title', 'article']
    search_fields = ['title', 'sub_category', 'category', 'article']
    list_filter = ['gender',
                   'is_popular']
    list_per_page = 15
    list_editable = ['amount', 'cur']
    date_hierarchy = 'pub_date'

    actions = ['set_dollar', 'set_rub', 'add_one']

    @admin.action(description='Изменит волюта на доллар')
    def set_dollar(self, request, qs: QuerySet):
        qs.update(cur=Product.USD)

    @admin.action(description='Изменит волюта на рубль')
    def set_rub(self, request, qs: QuerySet):
        qs.update(cur=Product.RUB)

    @admin.action(description='Добавить 1 на количество')
    def add_one(self, request, qs: QuerySet):
        for i in qs:
            i.amount += 1
            i.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'owner', 'is_published']
    list_display_links = ['product', 'owner']
    save_on_top = True
    list_per_page = 20


admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
