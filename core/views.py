# Importamos
from django.views.generic import View
from django.shortcuts import render

# Vista de clase 
class HomeView(View):
    # Funcion Get - Sirve para llamar

    # Fundamentos web:
        # GetRequest - Es lo que pide la informacion para ver. Es lo que vemos.
        # PostRequest - Es lo que envias al servidor para mostrar.
    def get(self, request, *args, **kwargs):
        # args y kwargs - Hacen referencia a cualquier variable/parametro que nuestro request pueda tener.

        # Diccionario - Contexto
        context = {

        }

        # Retornamos lo que renderizaremos.
        return render(request, 'index.html', context)


# Ejemplo
class Prueba(View):
    def get(self, request):
        return render (request, 'prueba.html')