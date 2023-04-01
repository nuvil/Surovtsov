from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.
# class HobbiesInline(admin.TabularInline):
#     model = Hobbies
#
#
# admin.site.register(Hobbies, HobbiesInline)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'address')
    list_display_links = ('first_name', 'last_name')
    list_editable = ('age', 'address')
    list_filter = ('age',)
    search_fields = ('last_name',)


admin.site.register(Users, UserAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'address', 'place_phone')


admin.site.register(Place, PlaceAdmin)


class BarAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'free_table', 'average_paycheck')


admin.site.register(Bar, BarAdmin)