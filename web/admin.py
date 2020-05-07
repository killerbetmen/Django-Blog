from django.contrib import admin
from .models import Publication, Comment
from django.contrib.auth.models import User

admin.site.unregister(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',)
    list_filter = ('last_login', 'date_joined')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('publication_title', 'user', 'publication_date')
    list_filter = ('user', 'publication_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'publication', 'comment_date')
    list_filter = ('user', 'publication', 'comment_date')

