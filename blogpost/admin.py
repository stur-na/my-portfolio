from django.contrib import admin
from .models import Post, Comment, Category

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'overview', 'timestamp')
    search_fields = ('title', 'overview')


admin.site.register(Category)


