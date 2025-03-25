from django.contrib import admin

from .models import Post, Comment


class CommentAdminInLine(admin.StackedInline):
    model = Comment
    fields = ["post", "text"]
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_enable", "publish_date", "created_time"]
    inlines = [CommentAdminInLine,]



# class CommentAdmin(admin.ModelAdmin):
    # list_display = ["id", "post", "created_time", "text"]


# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
