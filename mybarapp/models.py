from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Restaurante(models.Model):
    ruc_res_id = models.BigIntegerField(primary_key=True)
    restaurante = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)
    horario_ini = models.TimeField()
    horario_fin = models.TimeField()

    def __str__(self):
        return self.restaurante

    def get_absolute_url(self):
        return reverse('mybarapp:restaurante-detail', args=[str(self.ruc_res_id)])

    class Meta:
        ordering = ["restaurante"]

# class Usuario(models.Model):
#     nombre_real = models.CharField(max_length=30)
#     correo = models.EmailField()
#     usuario = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)

class Platillo(models.Model):
    platillo = models.CharField(max_length=30)
    calorias = models.DecimalField(max_digits=8, decimal_places=2)
    grasa = models.DecimalField(max_digits=8, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=8, decimal_places=2)
    proteinas = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='media/platillos/')

    class Meta:
        ordering = ["platillo"]

    def __str__(self):
        return self.platillo

    def get_absolute_url(self):
        return reverse('mybarapp:platillo-detail',args=[self.id])


class Precio(models.Model):

    STAR_CHOICES = (
        (0, 'Cero Estrella'),
        (1, 'Una Estrella'),
        (2, "Dos Estrellas"),
        (3, "Tres Estrellas"),
        (4, "Cuatro Estrellas"),
        (5, "Cinco Estrellas")
    )

    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    calificacion = models.PositiveSmallIntegerField(choices=STAR_CHOICES,default=0)
    precio = models.FloatField()
    comentario = models.TextField()


# class Typos_usuarios(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     tipo = models.CharField(max_length=25)



# class Venta(models.Model):
#     precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
#     hora_reserva = models.DateTimeField()
