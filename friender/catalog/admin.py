from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


# Register your models here.
class HobbiesAdmin(admin.ModelAdmin):
    model = Hobbies


admin.site.register(Hobbies, HobbiesAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'address', 'get_html_photo')
    list_display_links = ('first_name', 'last_name')
    list_editable = ('age', 'address')
    list_filter = ('age',)
    search_fields = ('last_name',)

    def get_html_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img width=100 src={objects.photo.url}/>")

    get_html_photo.short_description = 'фото'


admin.site.register(Users, UserAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'address', 'place_phone', 'get_html_photo')
    list_display_links = ('place_name',)
    list_editable = ('place_phone', 'address')
    search_fields = ('place_name',)

    def get_html_photo(self, objects):
        if objects.place_photo:
            return mark_safe(f"<img width=100 src={objects.place_photo.url}/>")

    get_html_photo.short_description = 'фото'


admin.site.register(Place, PlaceAdmin)


class BarAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'address', 'place_phone', 'get_html_photo', 'average_paycheck', 'description')
    list_display_links = ('place_name', 'get_html_photo')
    list_editable = ('place_phone', 'address', 'average_paycheck')
    search_fields = ('place_name',)

    def get_html_photo(self, objects):
        if objects.place_photo:
            return mark_safe(f"<img width=100 src={objects.place_photo.url}/>")

    get_html_photo.short_description = 'фото'


admin.site.register(Bar, BarAdmin)


class CafeAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'address', 'place_phone', 'get_html_photo', 'average_paycheck', 'description')
    list_display_links = ('place_name', 'get_html_photo')
    list_editable = ('place_phone', 'address', 'average_paycheck')
    search_fields = ('place_name',)

    def get_html_photo(self, objects):
        if objects.place_photo:
            return mark_safe(f"<img width=100 src={objects.place_photo.url}/>")

    get_html_photo.short_description = 'фото'


admin.site.register(Cafe, CafeAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'address', 'place_phone', 'get_html_photo', 'average_paycheck', 'description')
    list_display_links = ('place_name', 'get_html_photo')
    list_editable = ('place_phone', 'address', 'average_paycheck')
    search_fields = ('place_name',)

    def get_html_photo(self, objects):
        if objects.place_photo:
            return mark_safe(f"<img width=100 src={objects.place_photo.url}/>")

    get_html_photo.short_description = 'фото'


admin.site.register(Restaurant, RestaurantAdmin)


class MeetingsAdmin(admin.ModelAdmin):
    list_display = ['meeting_name', 'date_meeting', 'time_meeting', 'place']
    list_display_links = ['meeting_name', ]
    list_filter = ['date_meeting', 'time_meeting']
    list_editable = ['date_meeting', 'time_meeting']
    search_fields = ['meeting_name', ]


admin.site.register(Meetings, MeetingsAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ['meetings', 'place', 'meetings_rating', 'comment']
    list_display_links = ['meetings', ]
    list_editable = ['comment', ]
    search_fields = ('meetings',)


admin.site.register(Rating, RatingAdmin)
