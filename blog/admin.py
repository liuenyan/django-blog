from django.contrib import admin
from blog.models import Post, Comment, Tag, Category, Link

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('body_html',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Link)
