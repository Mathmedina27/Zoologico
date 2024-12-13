from django.db import models

class Zoologico(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    idAnimal = models.AutoField(primary_key=True)
    zoologico = models.ForeignKey(Zoologico, on_delete=models.CASCADE, related_name='animales')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    tipoCliente = models.CharField(max_length=50)

    def __str__(self):
        return self.tipoCliente

class GuiaTuristico(models.Model):
    nombre = models.CharField(max_length=100)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Veterinaria(models.Model):
    nombreVeterianario = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreVeterianario

class Administracion(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class CompraBoleto(models.Model):
    identificador = models.AutoField(primary_key=True)
    fecha = models.DateField()
    montoTotal = models.FloatField()
    cantidad = models.IntegerField()
    metodoPago = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"Compra {self.identificador}"

class RegistroMedico(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    peso = models.FloatField()
    diagnostico = models.TextField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='registros_medicos')

    def __str__(self):
        return f"Registro {self.id}"

class Habitat(models.Model):
    tipoDeHabitat = models.CharField(max_length=100)
    temperatura = models.FloatField()
    humedad = models.FloatField()

    def __str__(self):
        return self.tipoDeHabitat

class Jaula(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=200)
    dimensiones = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, related_name='jaulas')

    def __str__(self):
        return f"Jaula {self.id}"
