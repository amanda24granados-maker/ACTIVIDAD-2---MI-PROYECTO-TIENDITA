from abc import ABC, abstractmethod


class Categoria:
    """Representa la categoría de un producto."""

    def _init_(self, nombre):
        self.nombre = nombre


class Producto(ABC):
    """Clase abstracta para los productos de la tiendita."""

    def _init_(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self._precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = nuevo_precio

    @abstractmethod
    def mostrar_info(self):
        """Cada producto define cómo mostrar su información."""
        pass

    def vender(self, cantidad=1):
        """El argumento por defecto permite vender una unidad."""
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
        elif cantidad > self.cantidad:
            print("No hay suficiente existencia.")
        else:
            self.cantidad -= cantidad
            print(f"Venta realizada: {cantidad} unidad(es).")

    def actualizar_precio(self, nuevo_precio=None, descuento=0):
        # Simula sobrecarga con argumentos opcionales.
        if nuevo_precio is not None:
            self.precio = nuevo_precio
        elif descuento > 0 and descuento < 100:
            self.precio *= (1 - descuento / 100)
        else:
            print("Indique un precio o un descuento válido.")


class ProductoAlimento(Producto):
    """Producto alimenticio que hereda de Producto."""

    def _init_(self, nombre, precio, cantidad, categoria, marca):
        super()._init_(nombre, precio, cantidad, categoria)
        self.marca = marca

    def mostrar_info(self):
        # Polimorfismo: sobrescribe el método abstracto.
        return (
            f"Alimento: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Categoría: {self.categoria.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Cantidad: {self.cantidad}"
        )


class Inventario:
    """Agrupa varios productos de la tiendita."""

    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto.mostrar_info())
            print("-" * 25)
