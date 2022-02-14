from django.contrib import admin
from .models import discussion
from django_summernote.admin import SummernoteModelAdmin


@admin.register(discussion)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on', 'author')
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
