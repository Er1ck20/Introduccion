# Es el url.py principal

from django.contrib import admin
from django.urls import path, include
from .views import HomeView, Prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', HomeView.as_view(), name = 'home'),

    
    path('prueba/', Prueba.as_view(), name = "prueba"),

    # URL de mis app
    path('blog/', include('blog.urls', namespace='blog')),

]
