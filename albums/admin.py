from django.contrib import admin
from .models import Album


class CustomAlbumAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "user", "id"]


admin.site.register(Album, CustomAlbumAdmin)
