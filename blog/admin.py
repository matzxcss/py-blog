from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Commentary, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    search_fields = ("title", "owner__username")
    list_filter = ("created_time",)


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    search_fields = ("user", "post__title")
    list_filter = ("created_time",)


admin.site.unregister(Group)
