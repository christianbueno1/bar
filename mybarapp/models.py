from django.db import models

class Restaurante(models.Model):
    ruc_res_id = models.BigIntegerField(primary_key=True)
    restaurante = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)
    horario_ini = models.TimeField()
    horario_fin = models.TimeField()

class Usuario(models.Model):
    nombre_real = models.CharField(max_length=30)
    correo = models.EmailField()
    usuario = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=30)

class Platillo(models.Model):
    platillo = models.CharField(max_length=30)
    calorias = models.DecimalField(max_digits=8, decimal_places=2)
    grasa = models.DecimalField(max_digits=8, decimal_places=2)
    carbohidratos = models.DecimalField(max_digits=8, decimal_places=2)
    proteinas = models.DecimalField(max_digits=8, decimal_places=2)

class Precio(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    precio = models.FloatField()

class Typos_usuarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=25)

class Calificacion(models.Model):
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
    calificacion = models.PositiveSmallIntegerField()
    comentario = models.TextField()

class Venta(models.Model):
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)
    hora_reserva = models.DateTimeField()
