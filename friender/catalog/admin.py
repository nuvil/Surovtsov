from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.
class HobbiesInline(admin.TabularInline):
    model = Hobbies


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'address')
    list_display_links = ('first_name', 'last_name')


admin.site.register(Users, UserAdmin)
