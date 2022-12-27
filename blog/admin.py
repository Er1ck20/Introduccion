from django.contrib import admin

# Importamos desde models
from .models import Post
# Registramos los modelos en el admin.
admin.site.register(Post)