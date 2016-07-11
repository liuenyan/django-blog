from django.contrib import admin
from .models import Post, Comment, Tag, Link

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('body_html',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Link)
