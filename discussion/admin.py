from django.contrib import admin
from .models import discussion, Categorys, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(discussion)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('created_on', 'author')
    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


admin.site.register(Categorys)
admin.site.register(Comment)
