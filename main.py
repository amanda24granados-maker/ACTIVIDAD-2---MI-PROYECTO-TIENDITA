from producto import Categoria, ProductoAlimento, Inventario


# Creamos una categoría.
categoria = Categoria("Alimentos")

# Creamos productos para la tiendita.
arroz = ProductoAlimento("Arroz", 1.25, 20, categoria, "Marca A")
galletas = ProductoAlimento("Galletas", 0.75, 15, categoria, "Marca B")

# Agrupamos los productos en un inventario.
inventario = Inventario()
inventario.agregar_producto(arroz)
inventario.agregar_producto(galletas)

print("=== INVENTARIO DE LA TIENDITA ===")
inventario.mostrar_inventario()

print("\n=== PRUEBA DE VENTA ===")
arroz.vender(2)

print("\n=== INVENTARIO ACTUALIZADO ===")
inventario.mostrar_inventario()

print("\n=== ACTUALIZACIÓN DE PRECIO ===")
galletas.actualizar_precio(descuento=10)
print(galletas.mostrar_info())
