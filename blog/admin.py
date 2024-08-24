from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title', 'counted_views', 'reading_time', 'status', 'published_date', 'created_date']
    list_filter = ['status']
    search_fields = ['title', 'content']


admin.site.register(Category)
admin.site.register(Post, PostAdmin)