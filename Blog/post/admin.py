from django.contrib import admin
from .models import Post, Comment  # Agrega un espacio después de 'from'


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fechaDepublicacion', 'autor')  # Verifica que estos campos existan en tu modelo
    search_fields = ('titulo',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date')  # Asegúrate de que estos campos existan también
    search_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)