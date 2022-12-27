# Importamos
from django.urls import path 
from .views import BlogListView, FormListView, BlogCreateView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),

    path('create/', BlogCreateView.as_view(), name='create'),

    # int:pk - int = Numero entero. pk = primary key
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    


    # Formulario ejemplo
    path('form/', FormListView.as_view(), name='form'),
]
# 1:40