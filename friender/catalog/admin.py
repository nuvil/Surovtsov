from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# # Register your models here.
# class HobbiesInline(admin.TabularInline):
#     model = Hobbies
#
#
# admin.site.register(Hobbies, HobbiesInline)

class HobbiesInline(admin.ModelAdmin):
    model = Hobbies


admin.site.register(Hobbies, HobbiesInline)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'address')
    list_display_links = ('first_name', 'last_name')
    list_editable = ('age', 'address')
    list_filter = ('age',)
    search_fields = ('last_name',)


admin.site.register(Users, UserAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'address', 'place_phone', 'get_html_photo')
    list_display_links = ('place_name',)

    def get_html_photo(self, object):
        if object.place_photo:
            return mark_safe(f"<img width=100 src={object.place_photo.url}/>")

    get_html_photo.short_description = 'фото'


admin.site.register(Place, PlaceAdmin)


class BarAdmin(admin.ModelAdmin):
    list_display = ('place_name',)


admin.site.register(Bar, BarAdmin)


class CafeAdmin(admin.ModelAdmin):
    list_display = ('place_name',)


admin.site.register(Cafe, CafeAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('place_name',)


admin.site.register(Restaurant, RestaurantAdmin)


class MeetingsAdmin(admin.ModelAdmin):
    list_display = ['meeting_name', ]


admin.site.register(Meetings, MeetingsAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['user_rating', 'comment']


admin.site.register(Rating, RatingAdmin)
