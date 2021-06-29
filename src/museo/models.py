
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class NombreAbstract(models.Model):
    nombre = models.CharField(
        _('Nombre'),
        help_text=_('Nombre descriptivo'),
        max_length=200,
        # unique=True,
    )

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        abstract = True

class Sede(NombreAbstract):
    
    cantMaxVisitantes = models.BigIntegerField(
        _('Cantidad maxima de visitantes'),
       # max_digits=15,
        help_text=_('Cantidad maxima de visitantes'),
        default=0,
        null=False,
        blank=True
    )

    cantMaxPorGuia = models.BigIntegerField(
        _('Cantidad maxima de visitantes por guia'),
       # max_digits=15,
        help_text=_('Cantidad maxima de visitantes por guia'),
        default=0,
        null=False,
        blank=True
    )


class Planta(NombreAbstract):
    
    numero = models.BigIntegerField(
        _('Numero de planta'),
       # max_digits=15,
        help_text=_('Numero de planta'),
        default=0,
        null=False,
        blank=True
    )

    sede =  models.ForeignKey(
        Sede,
        help_text=_('Sede'),
        verbose_name='Sede',
        related_name='%(app_label)s_%(class)s',
        related_query_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class Sala(NombreAbstract):
    
    superficie = models.DecimalField(
        _('Superficie'),
        max_digits=15,
        decimal_places=2,
        help_text=_('Superficie en m2'),
        default=0,
        null=False,
        blank=True
    )

    planta = models.ForeignKey(
        Planta,
        help_text=_('Planta de la sede'),
        verbose_name='Planta',
        related_name='%(app_label)s_%(class)s',
        related_query_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

   
  



class Pared(NombreAbstract):

    alto = models.DecimalField(
        _('Alto'),
        max_digits=15,
        decimal_places=2,
        help_text=_('Alto de pared'),
        default=0,
        null=False,
        blank=True
    )

    ancho = models.DecimalField(
        _('Ancho'),
        max_digits=15,
        decimal_places=2,
        help_text=_('Ancho de pared'),
        default=0,
        null=False,
        blank=True
    )

    sala = models.ForeignKey(
        Sala,
        help_text=_('Sala de la planta'),
        verbose_name='Sala',
        related_name='%(app_label)s_%(class)s',
        related_query_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )   

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Pared'
        verbose_name_plural = 'Paredes'





class Empleado(NombreAbstract):

    apellido = models.CharField(
        _('Apellido'),
        help_text = _('Apellido del Empleado'),
        max_length=200,
        blank=True,
        null=False
    )

    codigoValidacion = models.BigIntegerField(
         _('Codigo Validacion'),
        blank=True,
        null=True
    )

    cuit = models.BigIntegerField(
         _('Cuit'),
        help_text=_(
            'Cuit del Empleado'),
        blank=True,
        null=True
    )

    dni = models.BigIntegerField(
        _('DNI'),
        help_text=_('Documento del Empleado'),
        blank=True,
        null=False
    )

    domicilio = models.CharField(
        _('Dirección'),
        help_text=_('Dirección del empleado'),
        max_length=200,
        blank=True,
        null=True
    )

    fecha_ingreso = models.DateField(
        _('Fecha de Ingreso'),
        help_text= ('Fecha de ingreso del empleado'),
        blank=True,
        null=False
    )

    fecha_nacimiento = models.DateField(
        _('Fecha de Nacimiento'),
        help_text= ('Fecha de nacimiento del empleado'),
        blank=True,
        null=False
    )

    email = models.EmailField(
        _('Email'),
        help_text=_('Email del empleado'),
        null=True,
        blank=True,
    )
    masculino = 'Masculino'
    femenino = 'Femenino'
    noInfo = 'No Info'
    opciones = [
        (masculino, "Masculino"),
        (femenino, "Femenino"),
        (noInfo, "No Info")
    ]


    sexo = models.CharField(
        max_length=10,
        choices=opciones,
        default=noInfo
    )
    
    telefono = models.BigIntegerField(
        _('Teléfono'),
        help_text=_('teléfono del empleado'),
        blank=True,
        null=True
    )

    sede =  models.ForeignKey(
        Sede,
        help_text=_('Sede'),
        verbose_name='Sede',
        related_name='%(app_label)s_%(class)s',
        related_query_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['nombre']
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'

class Usuario(NombreAbstract):

    caducidad = models.DateField(
        _('Caducidad'),
        help_text=('Fecha de caducidad del Usuario'),
        blank=True
    )

    constraseña = models.CharField(
        _('Contraseña'),
        max_length=30,
        help_text=('Contraseña del usuario'),
        blank=True,
        null=False
    )

    empleado = models.ForeignKey(
        Empleado,
        help_text=_('Empleado'),
        verbose_name='Empleado',
        related_name='%(app_label)s_%(class)s',
        related_query_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )


    class meta:
        ordering = ['nombre']
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

class Sesion(models.Model):

   
    def __str__(self):
        return '{}'.format(self.usuario.nombre)

    fecha_fin = models.DateField(
        _('Fecha fin'),
        help_text=('Fecha fin de la Sesión'),
        blank=True
    )

    fecha_inicio = models.DateField(
        _('Fecha inicio'),
        help_text=('Fecha inicio de la Sesión'),
        blank=True
    )

    hora_inicio = models.TimeField(
        _('Hora de inicio'),
        help_text=('Hora de inicio de la Sesion'),
        blank=True,
    )

    hora_fin = models.TimeField(
        _('Hora de fin'),
        help_text=('Hora de fin de la Sesion'),
        blank=True,
    )

    usuario = models.ForeignKey(
        Usuario,
        help_text=_('Usuario'),
        verbose_name='Usuario',
        related_name='%(app_label)s_%(class)s',
        related_query_name='%(app_label)s_%(class)s',
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )

    class Meta:
        ordering = ['usuario']
        verbose_name = 'Sesion'
        verbose_name_plural = 'Sesiones'
