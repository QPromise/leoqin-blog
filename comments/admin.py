from django.contrib import admin
from comments.models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name', 'email', 'text', 'created_time']
admin.site.register(Comment, CommentAdmin)



