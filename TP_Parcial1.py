#Servicio de construccion de casas
#Agregar casa a construir
#Datos: Nombre Cliente: XXXX, Direccion: XYZ123, Año a realizar construccion: XXXX, Estado:
# NO COMPLETADO, Cantidad Trabajadores Necesarios: XX, Precio: XXXXXX
print("*** CONSTRUCCIÓN DE CASAS R&E S.A ***")
def agregar(construccion):
    print("     Agrega una nueva construccion a la linea de espera.")
    cliente = input("Nombre y Apellido del cliente: ")
    direccion = input("Direccion del cliente: ")
    fecha = input("Fecha de construccion (DD/MM/AAAA): ")
    estado = "NO COMPLETADO"
    empleado = int(input("Cantidad de empleados necesarios: "))
    precio = float(input("Precio de construccion: "))
    con = {
        "cliente": cliente,
        "direccion": direccion,
        "fecha": fecha,
        "estado": estado,
        "empleado": empleado,
        "precio": precio,
    }
    construccion.append(con)
    print("Construccion agregada con éxito.")

#Listar Construcciones (Completados y no completados, Año a realizar de mayor a menor)
def listar(construccion):
    print("     Lista todas las construcciones, ordenadas por fecha de menor a mayor.")
    if not construccion:
        print("No hay construcciones en la linea de espera.")
        return
    lista_ordenada = sorted(construccion, key=lambda con: con["fecha"])
    print("Listado:")
    for con in lista_ordenada:
        print(f"- Cliente: {con['cliente']}, Direccion: {con['direccion']}, Fecha: {con['fecha']}, Estado: {con['estado']}, empleado: {con['empleado']}, precio: {con['precio']:,}")

#Buscar Construcciones (Dirección)
def buscar(construccion):
    """Buscar construccion por fecha."""
    if not construccion:
        print("No hay construcciones en la linea de espera.")
        return
    busqueda = input("Ingrese la direccion o fecha de la/s casa/s a construir: ")
    resultado = [con for con in construccion if busqueda.lower() in con["direccion"].lower() or busqueda.lower() in con["fecha"].lower()]
    if resultado:
        print("Productos encontrados:")
        for con in resultado:
            print(f"- Cliente: {con['cliente']}, Direccion: {con['direccion']}, Fecha: {con['fecha']}, Estado: {con['estado']}, empleado: {con['empleado']}, precio: {con['precio']:,}")
    else:
        print("No se encontraron productos.")

#Actualizar Construcciones (Actualizar de NO COMPLETADO/EN PROCESO/COMPLETADO)
def actualizar(construccion):
    print("     Actualiza el estado de una construccion específica.")
    if not construccion:
        print("No hay productos en el inventario.")
        return
    direccion = input("Direccion de la construccion a actualizar: ")
    con = next((con for con in construccion if con["direccion"].lower() == direccion.lower()), None)
    if con:
        nuevo_estado = input("Nueva estado de la construccion (NO COMPLETADO, EN PROCESO, COMPLETADO): ")
        con["estado"] = nuevo_estado
        print("Estado actualizado con éxito.")
    else:
        print("Construccion no encontrada.")

#Calcular    
def ganancia(construccion):
    print("     Calcula y muestra el valor total de la ganancia.")
#Calcular costo total (XXXX Salario * Trabajadores (digamos que un trabajador cobra 3M de salario
#a lo largo de la construccion de cada casa) y digamos que no hay costo de materiales, ya que el cliente los provee.)
    costo_total = sum(con["empleado"] * 3000000 for con in construccion)
    print(f"Costo total de las construcciones: {costo_total:,}")
#Calcular Ingreso total (Precio * Construcciones)
    ingreso_total = sum(con["precio"] for con in construccion)
    print(f"Ingreso total de las construcciones, IVA incluido: {ingreso_total:,}")
#Calcular Ganancias (   (Ingreso – Costo) – [(ingreso - costo) * 0.10  ]   )
    valor_total = ingreso_total - costo_total
    print(f"Total ganancias: {valor_total:,}")

#Menu de navegación
construccion = []
while True:
    print("\nGestión de linea de espera de construcciones")
    print("1. Agregar construccion")
    print("2. Listar construcciones")
    print("3. Buscar consruccion")
    print("4. Actualizar estado de construccion")
    print("5. Calcular costo, ingreso y ganancias totales")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar(construccion)
    elif opcion == "2":
        listar(construccion)
    elif opcion == "3":
        buscar(construccion)
    elif opcion == "4":
        actualizar(construccion)
    elif opcion == "5":
        ganancia(construccion)
    elif opcion == "6":
        break
    else:
        print("Opción inválida.")