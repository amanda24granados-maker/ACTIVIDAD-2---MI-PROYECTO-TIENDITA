class Producto:
    """Representa un producto de la tiendita."""

    def _init_(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        """Muestra la información del producto."""
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Cantidad: {self.cantidad}"
        )

    def vender(self, cantidad=1):
        """Vende productos si hay existencias."""
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
        elif cantidad > self.cantidad:
            print("No hay suficiente existencia.")
        else:
            self.cantidad -= cantidad
            print(f"Venta realizada: {cantidad} unidad(es).")


class ProductoAlimento(Producto):
    """Representa un alimento de la tiendita."""

    def _init_(self, nombre, precio, cantidad, marca):
        super()._init_(nombre, precio, cantidad)
        self.marca = marca

    def mostrar_info(self):
        # Polimorfismo: sobrescribe el método de Producto.
        return (
            f"Alimento: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Cantidad: {self.cantidad}"
        )
