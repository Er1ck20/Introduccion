from django.db import models

# Create your models here.

# Model del post
class Post(models.Model):
    title = models.CharField(("Titulo"), max_length=50)
    content = models.TextField(("Contenido"), max_length=50)

    # Hacemos referencia a lo que queremos visualizar en el admin.
    def __str__(self):
        return self.title
