from django.contrib import admin
from .models import *
admin.site.register (Product)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )