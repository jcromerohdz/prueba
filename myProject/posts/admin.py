from django.contrib import admin
from posts.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "creado"]#Actualizado
	list_display_links = ["creado"]
	list_filter = ["actualizado", "creado"]
	search_fields = ["titulo", "contenido"]
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)
#admin.site.register(Post)