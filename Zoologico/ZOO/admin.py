from django.contrib import admin
from .models import Zoologico, Animal, Cliente, GuiaTuristico, Veterinaria, Administracion, CompraBoleto, RegistroMedico, Habitat, Jaula


@admin.register(Zoologico)
class ZoologicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'idAnimal')
    search_fields = ('nombre', 'idAnimal')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('tipoCliente',)

@admin.register(GuiaTuristico)
class GuiaTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'idioma')
    search_fields = ('nombre', 'idioma')

@admin.register(Veterinaria)
class VeterinariaAdmin(admin.ModelAdmin):
    list_display = ('nombreVeterianario', 'especialidad')
    search_fields = ('nombreVeterianario', 'especialidad')

@admin.register(Administracion)
class AdministracionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo')
    search_fields = ('nombre', 'cargo')

@admin.register(CompraBoleto)
class CompraBoletoAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'fecha', 'montoTotal', 'cantidad', 'metodoPago', 'tipo')
    search_fields = ('identificador', 'tipo')

@admin.register(RegistroMedico)
class RegistroMedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'peso', 'diagnostico')
    search_fields = ('id', 'diagnostico')

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('tipoDeHabitat', 'temperatura', 'humedad')
    search_fields = ('tipoDeHabitat',)

@admin.register(Jaula)
class JaulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ubicacion', 'dimensiones', 'estado')
    search_fields = ('id', 'estado')
