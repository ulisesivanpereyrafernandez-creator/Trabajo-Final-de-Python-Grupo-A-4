# Variables globales para estadísticas (Acumuladores y Contadores)
recaudacion_total = 0.0
contador_pedidos = 0

def mostrar_menu_principal():
    print("\n--- 🍔 ROTISERÍA UTN - SISTEMA DE PEDIDOS 🍔 ---")
    print("1. Realizar Nuevo Pedido")
    print("2. Ver Estadísticas del Día")
    print("3. Salir")

def mostrar_productos():
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Hamburguesa Completa - $4500")
    print("2. Pizza Mozzarella    - $5000")
    print("3. Gaseosa 500ml       - $1200")

def realizar_pedido():
    global recaudacion_total, contador_pedidos
    
    mostrar_productos()
    opcion_producto = input("Seleccione el producto (1-3): ")
    cantidad = int(input("Ingrese la cantidad: ")) # <- Ojo: Esto puede fallar si meten texto
    
    precio = 0
    nombre_prod = ""
    
    if opcion_producto == "1":
        precio = 4500
        nombre_prod = "Hamburguesa"
    elif opcion_producto == "2":
        precio = 5000
        nombre_prod = "Pizza"
    elif opcion_producto == "3":
        precio = 1200
        nombre_prod = "Gaseosa"
    else:
        print("Producto no válido.")
        return

    subtotal = precio * cantidad
    print(f"\nPedido registrado: {cantidad}x {nombre_prod} - Subtotal: ${subtotal}")
    
    # Aplicar descuento por apertura (Promoción)
    if subtotal > 10000:
        print("¡PROMO! Descuento del 10% aplicado por superar los $10000.")
        subtotal = subtotal * 0.9
        print(f"Nuevo Total con descuento: ${subtotal}")
        
    # Actualizar estadísticas
    recaudacion_total += subtotal
    contador_pedidos += 1
    print("¡Pedido confirmado con éxito!")

def mostrar_estadisticas():
    print("\n=== 📊 ESTADÍSTICAS DIARIAS ===")
    print(f"Cantidad total de pedidos: {contador_pedidos}")
    print(f"Recaudación total: ${recaudacion_total:.2f}")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            realizar_pedido()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            print("Cerrando caja diaria. ¡Hasta mañana!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()S