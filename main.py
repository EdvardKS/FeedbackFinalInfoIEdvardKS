import os
from Funciones import (
    registrar_alumno,
    registrar_profesor,
    registrar_clase,
    registrar_anticipo,
    mostrar_guardar_factura,
    menu_ver_datos,
    mostrar_menu,
    cargar_datos,
    guardar_datos
)

# =========================
# PROGRAMA PRINCIPAL
# =========================

def main():  
    # Crear carpetas donde voy a guardar los datos o facturas que generé
    os.makedirs("datos", exist_ok=True)
    os.makedirs("facturas", exist_ok=True)

    # Cargo todos los datos como objetos y los desempaco en variables
    datasets = dict(cargar_datos())
    alumnos = datasets.get("alumnos", [])
    profesores = datasets.get("profesores", [])
    clases = datasets.get("clases", [])
    anticipos = datasets.get("anticipos", [])
    facturas = datasets.get("facturas", [])
    permisos = datasets.get("permisos", [])

    # Lógica del menú principal        
    opcion = -1
    while opcion != 0:
        os.system("cls")
        mostrar_menu()
        
        # Después de mostrar el error controlo que el user meta un número válido (del 0 al 6)
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe introducir un número")
            continue

        # Esto es el switch-case en Python -> en vez de usar if-elif-else
        match opcion:            
            case 1:
                registrar_alumno(alumnos)
            case 2:
                registrar_profesor(profesores)
            case 3:
                registrar_clase(clases, alumnos, profesores)
            case 4:
                registrar_anticipo(anticipos)
            case 5:
                mostrar_guardar_factura(facturas, alumnos, clases, anticipos, permisos)
            case 6:
                menu_ver_datos(alumnos, profesores, clases, anticipos, facturas)
            case 0:
                print("Saliendo del programa...")
            case _:
                print("Opción no válida")
        

    # Si se selecciona 0, entonces guardamos la información de la sesión en los archivos JSON
    guardar_datos([("alumnos", alumnos),("profesores", profesores),("clases", clases),("anticipos", anticipos),("facturas", facturas),("permisos", permisos),]) 


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    main()
