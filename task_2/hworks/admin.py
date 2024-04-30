from django.contrib import admin

from .models import Group, Hwork, Order


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    search_fields = ('title', )
    list_filter = ('title', )
    list_display_links = (
        'title',
        'description',
    )

    empty_value_display = '-пусто-'


class HworkAdmin(admin.ModelAdmin):
    list_editable = ('is_archived', )
    list_display = (
        'id',
        'title',
        'short_text',
        'user',
        'price',
        'group',
        'is_archived'
    )
    list_display_links = (
        'title',
        'short_text',
    )
    search_fields = ('user__username', )
    list_filter = ('is_archived', 'group',)
    empty_value_display = '-пусто-'
    list_per_page = 20

    def short_text(self, obj):
        return f'{obj.description[:50]}...'
    short_text.short_description = 'Описание'


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('customer__username', )
    list_editable = ('is_ready', 'is_finished')
    list_display = (
        'hwork',
        'customer',
        'seller',
        'price',
        'is_ready',
        'is_finished'
    )
    list_filter = ('is_ready', 'is_finished')
    readonly_fields = ('seller', )
    empty_value_display = '-пусто-'
    list_per_page = 20


admin.site.register(Group, GroupAdmin)
admin.site.register(Hwork, HworkAdmin)
admin.site.register(Order, OrderAdmin)
