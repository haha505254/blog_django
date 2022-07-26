from django.contrib import admin
from .models import Post,Comment,Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','publish','status','get_tags')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created','post','active')
    list_filter = ('active', 'created', 'email')
    search_fields = ('username', 'email')

class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Tag,TagAdmin)
