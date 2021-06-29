from django.contrib import admin
from museo.models import *

@admin.register(Sesion)
class sesionAdmin(admin.ModelAdmin):
    list_display = ('usuario','hora_inicio','hora_fin')
    list_display_links = ('usuario',)



class SalaInline(admin.TabularInline):
    model = Sala
    extra = 0


@admin.register(Planta)
class plantaAdmin(admin.ModelAdmin):
    list_display = ('nombre','sede')
    list_display_links = ('nombre',)
    inlines = [
        SalaInline,
    ]
    ordering = ['nombre']  # -nombre descendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )



class PlantaInline(admin.TabularInline):
    model = Planta
    extra = 0 

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    inlines = [
        PlantaInline,
    ]
    list_display = ('nombre','cantMaxVisitantes','cantMaxPorGuia')
    list_display_links = ('nombre',)
    ordering = ['nombre']  # -nombre descendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

    


class ParedInline(admin.TabularInline):
    model =  Pared
    extra = 0

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    
    inlines = [
        ParedInline,
    ]
    ordering = ['nombre']  # -nombre descendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )
    list_display = ('nombre','planta','superficie')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','caducidad')
    list_display_links = ('nombre',)
    list_filter = ('caducidad',)

class UsuarioInline(admin.TabularInline):
    model = Usuario
    extra = 0

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','email','sede','fecha_ingreso',)
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    inlines = [
        UsuarioInline,
    ]
    ordering = ['nombre']  # -nombre descendente, nombre ascendente
    search_fields = ['nombre']

@admin.register(Pared)
class ParedAdmin(admin.ModelAdmin):
    list_display = ('nombre','sala','alto','ancho')
    list_display_links = ('nombre',)
