# Aqui crearemos nuestros formularios
# Importamos
from django import forms

from .models import Post 

class PostCreateForm(forms.ModelForm):
    # Clase meta - Aqui declaramos el modelo que queremos editar en este caso el Post
    class Meta:
        model=Post 
        fields=('title', 'content')


