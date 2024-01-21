from django.db import models
import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return f"{self.nombre} {self.marca} {self.precio}"

# Clase Zapatillas que hereda de Producto
class Zapatilla(Producto):
    talle = models.CharField(max_length=10)
    pais_fabricante = models.CharField(max_length=30)

# Clase Gorras que hereda de Producto
class Gorra(Producto):
    talle = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    pais_fabricante= models.CharField(max_length=30)

# Clase Jeans que hereda de Producto
class Jean(Producto):
    talle = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    material = models.CharField(max_length=20)

# Clase Camperas que hereda de Producto
class Campera(Producto):
    talle = models.CharField(max_length=10)
    material = models.CharField(max_length=20)
    pais_fabricante = models.CharField(max_length=30)



###MODELOS PARA LOS CLIENTES y VENDEDORES###

class Usuario (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"



class Vendedor(Usuario):
    identificacion = models.DecimalField(max_digits=10, decimal_places=2)

class Cliente(Usuario):
    descripcion = models.CharField(max_length=50)



class Venta(models.Model):
    
    fecha = models.DateTimeField(default=datetime.datetime.now)
    articulo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.fecha} ({self.articulo}) - {self.comprador}"
