from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post

# Lista del blog
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        # Llamaremos todos los objetos post de la base de datos
        posts = Post.objects.all()
        context = {
            'posts': posts
        }

        # Retornamos
        return render(request, 'Blog_list.html', context)

# Ejemplo 
class FormListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog_form.html') 

class BlogCreateView(View):


    def get(self, request, *args, **kwargs):
        form=PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)
    
    # Crear un formulario post correctamente
    def post(self, request, *args, **kwargs):
        # Preguntamos si la respuesta es un metodo post
        if request.method=='POST':
            # Si es igual a post, obtendremos denuevo el formulario, y pasamos la informacion dentro de post con el request.POST
            form = PostCreateForm(request.POST)

            # Si es valido obtenedremos la informacion de nuestro formulario que serian (titulo y contenido)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                # p de post y creamos el post, llamamos el post del Model
                p, created = Post.objects.get_or_create(title=title, content=content)
                # Guardamos todo
                p.save()

                # Nos redirigira
                return redirect('blog:home')
        context = {
            'form': form
            

        }
        return render(request, 'blog_create.html', context)

# Clase para mostrar los detalles de los blog
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        # Get_object_or_404 - Llama al model y obtiene el objeto de este.
        post = get_object_or_404(Post, pk=pk)
        context={
            'post': post
        }
        return render(request, 'blog_detail.html', context)