def realizar_pedido():
    global recaudacion_total, contador_pedidos
    global cant_hamburguesas, cant_pizzas, cant_bebidas
    
    mostrar_categorias()
    
    # =========================================================================
    # 1. VALIDACIÓN DE CATEGORÍA (Estructura de control iterativa + Excepciones)
    # =========================================================================
    while True:
        try:
            cat = int(input("Seleccione una categoría (1-3): "))
            if 1 <= cat <= 3:
                break  # Rompe el bucle si el número está dentro del rango válido
            print("⚠️ Opción inválida. El número debe estar entre 1 y 3.")
        except ValueError:
            # Captura el error si el operador ingresa letras, símbolos o vacíos
            print("⚠️ Error crítico: Entrada no válida. Debe ingresar obligatoriamente un número entero.")
            
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
        
    # =========================================================================
    # 2. VALIDACIÓN DE OPCIÓN DE PRODUCTO (opcion_producto)
    # =========================================================================
    while True:
        try:
            opcion_prod = int(input("Seleccione el producto deseado (1-2): "))
            if 1 <= opcion_prod <= 2:
                break  # Dato correcto, salimos del ciclo de validación
            print("⚠️ Opción fuera de rango. Por favor, seleccione 1 o 2.")
        except ValueError:
            print("⚠️ Error crítico: No se permiten letras ni espacios. Ingrese un número (1 o 2).")

    # =========================================================================
    # 3. VALIDACIÓN DE CANTIDAD (Debe ser entero mayor a cero)
    # =========================================================================
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de unidades: "))
            if cantidad > 0:
                break  # Cantidad lógica para un pedido gastronómico
            print("⚠️ Operación inválida. La cantidad física debe ser un número positivo mayor a 0.")
        except ValueError:
            print("⚠️ Error crítico: La cantidad debe ser un número entero (ej: 1, 2, 5). No se acepta texto.")

    # =========================================================================
    # PROCESAMIENTO LOGÍSITICO (Lógica de negocio una vez que los datos son seguros)
    # =========================================================================
    nombre_producto, precio_unitario = obtener_datos_producto(cat, opcion_prod)
    subtotal = precio_unitario * cantidad
    
    print(f"\n📝 Detalle: {cantidad}x {nombre_producto} (Precio Unit: ${precio_unitario})")
    print(f"Subtotal Inicial: ${subtotal}")
    
    # Descuento por superar monto base
    if subtotal > 12000:
        descuento_promo = subtotal * 0.10
        subtotal -= descuento_promo
        print(f"🎉 ¡Descuento por Súper Compra (10%) aplicado!: -${descuento_promo}")

    # Selección y validación del medio de pago
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
            print("⚠️ Error crítico: Debe ingresar un número entero.")
            
    if medio_pago == 1:
        descuento_pago = subtotal * 0.10
        subtotal -= descuento_pago
        print(f"💵 Descuento por pago en Efectivo (10%): -${descuento_pago}")

    print(f"💰 IMPORTE TOTAL A PAGAR: ${subtotal:.2f}")
    
    confirmar = input("\n¿Confirma el pedido? (S/N): ").upper()
    if confirmar == 'S':
        recaudacion_total += subtotal
        contador_pedidos += 1
        
        if cat == 1:
            cant_hamburguesas += cantidad
        elif cat == 2:
            cant_pizzas += cantidad
        elif cat == 3:
            cant_bebidas += cantidad
            
        print("✅ ¡Pedido registrado con éxito!")
    else:
        print("❌ Pedido cancelado por el operador.")