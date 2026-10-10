from producto import Producto, ProductoAlimento

# Creamos un producto general.
producto1 = Producto("Arroz", 1.25, 20)

# Creamos un alimento que hereda de Producto.
producto2 = ProductoAlimento("Galletas", 0.75, 15, "Marca A")

print("=== PRODUCTO GENERAL ===")
print(producto1.mostrar_info())

print("\n=== PRODUCTO ALIMENTO ===")
print(producto2.mostrar_info())

print("\n=== PRUEBA DE VENTA ===")
producto1.vender(2)

print("\n=== EXISTENCIAS ACTUALIZADAS ===")
print(producto1.mostrar_info())
