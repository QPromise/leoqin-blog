from django.contrib import admin
from .models import Post, Category, Tag, Poll


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','excerpt','image','created_time', 'modified_time', 'category', 'author']
class PollAdmin(admin.ModelAdmin):
    list_display = ['post','ip']
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Poll,PollAdmin)