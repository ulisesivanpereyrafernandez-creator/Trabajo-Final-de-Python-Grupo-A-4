# =====================================================================
# TRABAJO FINAL INTEGRADOR - LABORATORIO DE PYTHON
# Algoritmos y Estructuras de Datos - ISI - Ciclo 2026 - UTN FRRE
# Escenario 5: Sistema de Pedidos de Comida
# =====================================================================

# --- VARIABLES GLOBALES (Contadores y Acumuladores de Caja Diaria) ---
recaudacion_total = 0.0
contador_pedidos = 0

# Contadores específicos por categoría para estadísticas avanzadas
cant_hamburguesas = 0
cant_pizzas = 0
cant_bebidas = 0

def mostrar_menu_principal():
    """Muestra las opciones generales del sistema por consola."""
    print("\n" + "="*45)
    print(" 🍔 SYSTEM ROTISERÍA UTN - MENÚ PRINCIPAL 🍔 ")
    print("="*45)
    print("1. Registrar Nuevo Pedido")
    print("2. Ver Estadísticas de Ventas del Día")
    print("3. Cerrar Caja y Salir")
    print("-"*45)

def mostrar_categorias():
    """Muestra las categorías de productos disponibles."""
    print("\n--- CATEGORÍAS DE PRODUCTOS ---")
    print("1. Hamburguesas")
    print("2. Pizzas")
    print("3. Bebidas")

def obtener_datos_producto(categoria, opcion_prod):
    """
    Retorna el nombre y precio del producto según la categoría seleccionada.
    Basado en lógica de condicionales anidados (Módulo 2).
    """
    nombre = ""
    precio = 0
    
    if categoria == 1:  # Hamburguesas
        if opcion_prod == 1:
            nombre = "Hamburguesa Simple"
            precio = 4000
        elif opcion_prod == 2:
            nombre = "Hamburguesa Completa"
            precio = 4800
            
    elif categoria == 2:  # Pizzas
        if opcion_prod == 1:
            nombre = "Pizza Mozzarella"
            precio = 5000
        elif opcion_prod == 2:
            nombre = "Pizza Especial"
            precio = 6200
            
    elif categoria == 3:  # Bebidas
        if opcion_prod == 1:
            nombre = "Gaseosa 500ml"
            precio = 1200
        elif opcion_prod == 2:
            nombre = "Agua Mineral"
            precio = 1000
            
    return nombre, precio

def realizar_pedido():
    """Gestiona el flujo completo de armado de un pedido, promociones y pago."""
    global recaudacion_total, contador_pedidos
    global cant_hamburguesas, cant_pizzas, cant_bebidas
    
    mostrar_categorias()
    
    # --- VALIDACIÓN DE CATEGORÍA ---
    while True:
        try:
            cat = int(input("Seleccione una categoría (1-3): "))
            if 1 <= cat <= 3:
                break
            print("⚠️ Opción inválida. Debe ser entre 1 y 3.")
        except ValueError:
            print("⚠️ Error: Debe ingresar un número entero.")
            
    # --- MOSTRAR SUB-PRODUCTOS ---
    print("\n--- PRODUCTOS DISPONIBLES ---")
    if cat == 1:
        print("1. Hamburguesa Simple   - $4000")
        print("2. Hamburguesa Completa - $4800")
    elif cat == 2:
        print("1. Pizza Mozzarella    - $5000")
        print("2. Pizza Especial      - $6200")
    elif cat == 3:
        print("1. Gaseosa 500ml       - $1200")
        print("2. Agua Mineral        - $1000")
        
    # --- VALIDACIÓN DE PRODUCTO ---
    while True:
        try:
            opcion_prod = int(input("Seleccione el producto deseado (1-2): "))
            if 1 <= opcion_prod <= 2:
                break
            print("⚠️ Opción inválida. Seleccione 1 o 2.")
        except ValueError:
            print("⚠️ Error: Debe ingresar un número entero.")

    # --- VALIDACIÓN DE CANTIDAD ---
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            if cantidad > 0:
                break
            print("⚠️ La cantidad debe ser mayor a 0.")
        except ValueError:
            print("⚠️ Error: Debe ingresar un número entero.")

    # Obtención de datos finales del producto elegido
    nombre_producto, precio_unitario = obtener_datos_producto(cat, opcion_prod)
    subtotal = precio_unitario * cantidad
    
    print(f"\n📝 Detalle: {cantidad}x {nombre_producto} (Precio Unit: ${precio_unitario})")
    print(f"Subtotal Inicial: ${subtotal}")
    
    # --- APLICACIÓN DE PROMOCIÓN ---
    # Si el subtotal supera los $12000 se realiza un 10% de descuento automático
    if subtotal > 12000:
        descuento_promo = subtotal * 0.10
        subtotal -= descuento_promo
        print(f"🎉 ¡Descuento por Súper Compra (10%) aplicado!: -${descuento_promo}")
        print(f"Subtotal con Promoción: ${subtotal}")

    # --- SELECCIÓN Y VALIDACIÓN DEL MEDIO DE PAGO ---
    print("\n--- MEDIOS DE PAGO ---")
    print("1. Efectivo / Transferencia (10% Descuento Adicional)")
    print("2. Tarjeta de Crédito / Débito (Sin modificaciones)")
    
    while True:
        try:
            medio_pago = int(input("Seleccione medio de pago (1-2): "))
            if 1 <= medio_pago <= 2:
                break
            print("⚠️ Opción inválida. Seleccione 1 o 2.")
        except ValueError:
            print("⚠️ Error: Debe ingresar un número entero.")
            
    # Aplicar lógica financiera según el medio de pago
    if medio_pago == 1:
        descuento_pago = subtotal * 0.10
        subtotal -= descuento_pago
        print(f"💵 Descuento por pago en Efectivo (10%): -${descuento_pago}")
    else:
        print("💳 Pago registrado con tarjeta.")

    print(f"💰 IMPORTE TOTAL A PAGAR: ${subtotal:.2f}")
    
    # --- CONFIRMACIÓN FINAL DEL PEDIDO ---
    confirmar = input("\n¿Confirma el pedido? (S/N): ").upper()
    if confirmar == 'S':
        # Actualización de acumuladores y contadores globales con operadores del Modulo 2
        recaudacion_total += subtotal
        contador_pedidos += 1
        
        if cat == 1:
            cant_hamburguesas += cantidad
        elif cat == 2:
            cant_pizzas += cantidad
        elif cat == 3:
            cant_bebidas += cantidad
            
        print("✅ ¡Pedido registrado y enviado a la cocina con éxito!")
    else:
        print("❌ Pedido cancelado por el operador.")

def mostrar_estadisticas():
    """Muestra los indicadores de desempeño acumulados durante la jornada."""
    print("\n" + "="*45)
    print(" 📊 ESTADÍSTICAS DEL SISTEMA DE VENTAS 📊 ")
    print("="*45)
    print(f"• Número total de pedidos completados: {contador_pedidos}")
    print(f"• Recaudación total acumulada en caja: ${recaudacion_total:.2f}")
    print("-"*45)
    print("• Unidades vendidas desglosadas por categoría:")
    print(f"  - Hamburguesas: {cant_hamburguesas} unidades")
    print(f"  - Pizzas:       {cant_pizzas} unidades")
    print(f"  - Bebidas:      {cant_bebidas} unidades")
    print("="*45)

def main():
    """Función de arranque principal que controla el flujo del menú."""
    while True:
        mostrar_menu_principal()
        try:
            opcion = int(input("Seleccione una acción del menú (1-3): "))
            
            if opcion == 1:
                realizar_pedido()
            elif opcion == 2:
                mostrar_estadisticas()
            elif opcion == 3:
                print("\n🔐 Cerrando el sistema gastronómico. ¡Buen descanso equipo!")
                break
            else:
                print("⚠️ Opción fuera de rango. Seleccione un número entre 1 y 3.")
        except ValueError:
            print("⚠️ Error crítico: La opción debe ser un número entero.")

if __name__ == "__main__":
    main()