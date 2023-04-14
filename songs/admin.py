from django.contrib import admin
from .models import Song


class CustomSongAdmin(admin.ModelAdmin):
    list_display = ["title", "duration", "album", "id"]


admin.site.register(Song, CustomSongAdmin)
