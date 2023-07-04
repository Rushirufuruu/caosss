from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)

    def __str__(self) -> str:
        return self.nombre


class Noticia(models.Model):
    idNoticia = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 200)
    descripcion = models.TextField()
    fecha = models.DateField()
    foto = models.ImageField(upload_to='foto', null = True)
    publicar = models.BooleanField(default = False)
    comentario = models.TextField(default='s/c')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Noticia"+" "+str(self.idNoticia)
    

class producto(models.Model):
    idProducto = models.AutoField(primary_key = True)
    nombreProducto = models.CharField(max_length= 200)
    foto = models.ImageField(upload_to='foto', null = True)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return self.nombreProducto


class Galeria(models.Model):
    idGaleria = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='foto')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "N "+str(self.idGaleria)+" / "+self.noticia.titulo


#crear tabla cliente --> rut --> nombre --> apellido --> id_compra----------> 
#asociarla a tabla compras --> id_compra --> valor_total -->metodo_pago

 

