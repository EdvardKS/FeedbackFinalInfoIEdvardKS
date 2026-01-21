# Funcionalidades Adicionales:
# 1. Menú Interactivo: Se encuentra en main.py
# 2. Persistencia de Datos:
    # Utilice archivos JSON o CSV para almacenar la información de los alumnos, profesores, clases, permisos y facturas, 
    # de modo que los datos se puedan cargar al iniciar el programa y se guarden al finalizar.
# 3. Manejo de Errores:
    # Incluya manejo de excepciones para evitar errores en la entrada de datos 
    # (ej. fechas mal formateadas, valores incorrectos, etc.).
# 4. Formato de Salida:
    # Asegúrese de que las facturas y otros informes se muestren de manera clara en la consola y se puedan guardar en un archivo .txt o .pdf.
#region ########## Imports ##########
import json
import os
from datetime import datetime
from typing import List, Tuple
from Alumno import Alumno
from Profesor import Profesor
from Clase import Clase
from Permiso import Permiso
from Factura import Factura
from Anticipo import Anticipo
from ConvertidorPOO import (
    alumno_desde_dict,
    alumno_a_dict,
    profesor_desde_dict,
    profesor_a_dict,
    clase_desde_dict,
    clase_a_dict,
    anticipo_desde_dict,
    anticipo_a_dict,
    permiso_desde_dict,
    permiso_a_dict,
    factura_desde_dict,
    factura_a_dict,
)
#endregion
#region ########## Carga y guardado global ##########
def _cargar_lista_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def cargar_datos() -> List[Tuple[str, list]]:
    
    # Lee todos los JSON conocidos, crea objetos y devuelve una lista de tuplas:
    # [
    #     ("alumnos", [Alumno, ...]),
    #     ("profesores", [Profesor, ...]),
    #     ("clases", [Clase, ...]),
    #     ("anticipos", [Anticipo, ...]),
    #     ("facturas", [Factura, ...]),
    #     ("permisos", [Permiso, ...]),
    # ]
    # IMPORTANTE es que deveuelve tuplas, pero las listas internas si son editables
    base = "datos"
    alumnos = [alumno_desde_dict(d) for d in _cargar_lista_json(os.path.join(base, "alumnos.json"))]
    profesores = [profesor_desde_dict(d) for d in _cargar_lista_json(os.path.join(base, "profesores.json"))]
    clases = [clase_desde_dict(d) for d in _cargar_lista_json(os.path.join(base, "clases.json"))]
    anticipos = [anticipo_desde_dict(d) for d in _cargar_lista_json(os.path.join(base, "anticipos.json"))]
    facturas = [factura_desde_dict(d) for d in _cargar_lista_json(os.path.join(base, "facturas.json"))]
    permisos = [permiso_desde_dict(d) for d in _cargar_lista_json(os.path.join(base, "permisos.json"))]
    return [
        ("alumnos", alumnos),
        ("profesores", profesores),
        ("clases", clases),
        ("anticipos", anticipos),
        ("facturas", facturas),
        ("permisos", permisos),
    ]
def guardar_datos(dataset: List[Tuple[str, list]]):
    # Recibe la lista de tuplas (nombre, lista_de_objetos) y vuelca cada lista a su JSON.
    base = "datos"
    mapping = {
        "alumnos": ("alumnos.json", alumno_a_dict),
        "profesores": ("profesores.json", profesor_a_dict),
        "clases": ("clases.json", clase_a_dict),
        "anticipos": ("anticipos.json", anticipo_a_dict),
        "facturas": ("facturas.json", factura_a_dict),
        "permisos": ("permisos.json", permiso_a_dict),
    }
    for nombre, objetos in dataset:
        if nombre not in mapping:
            continue
        archivo, a_dict = mapping[nombre]
        datos = [a_dict(obj) for obj in objetos]
        ruta = os.path.join(base, archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
#endregion
#region ########## Operaciones de negocio ##########
def registrar_alumno(alumnos: list):
    try:
        current_year = datetime.now().year
        existing_nums = [int(a.num_registro.split("/")[1]) for a in alumnos if a.num_registro.startswith(f"{current_year}/")]
        next_num = max(existing_nums) + 1 if existing_nums else 1
        num_registro = f"{current_year}/{next_num:03d}"

        nombre = input("Nombre: ")
        primer_apellido = input("Primer apellido: ")
        segundo_apellido = input("Segundo apellido: ")
        dni = input("DNI: ")
        fecha_nacimiento = input("Fecha nacimiento (DD-MM-AAAA): ")
        fecha_registro = input("Fecha registro (DD-MM-AAAA): ")
        # Validación mínima de fechas y número de clases
        datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        datetime.strptime(fecha_registro, "%d-%m-%Y")
        permiso_opta = input("Permiso (A/B): ")
        domicilio = input("Domicilio: ")
        municipio = input("Municipio: ")
        provincia = input("Provincia: ")
        telefono1 = input("Teléfono 1: ")
        correo = input("Correo: ")
        num_clases = int(input("Número de clases: "))
        profesor = input("Profesor asignado: ")

        alumno = Alumno(
            num_registro=num_registro,
            nombre=nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            dni=dni,
            fecha_nacimiento=fecha_nacimiento,
            fecha_registro=fecha_registro,
            permiso_opta=permiso_opta,
            domicilio=domicilio,
            municipio=municipio,
            provincia=provincia,
            telefono1=telefono1,
            correo=correo,
            num_clases=num_clases,
            profesor=profesor,
        )
        alumnos.append(alumno)
        print("Alumno registrado correctamente")
    except ValueError:
        print("Error en los datos introducidos (revisa fechas o números)")
def registrar_profesor(profesores: list):
    try:
        nombre = input("Nombre: ")
        primer_apellido = input("Primer apellido: ")
        segundo_apellido = input("Segundo apellido: ")
        vehiculo = input("Matrícula del vehículo: ")
        tipo_vehiculo = input("Tipo de vehículo: ")
        itv = input("ITV (DD-MM-AAAA): ")
        datetime.strptime(itv, "%d-%m-%Y")

        profesor = Profesor(
            nombre=nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            vehiculo=vehiculo,
            tipo_vehiculo=tipo_vehiculo,
            itv=itv,
        )
        profesores.append(profesor)
        print("Profesor registrado correctamente")
    except ValueError as e:
        print(f"Error: {e}") 
def registrar_clase(clases: list, alumnos: list, profesores: list):
    try:
        dni_alumno = input("DNI alumno: ")
        dni_profesor = input("DNI profesor: ")
        fecha_hora = input("Fecha y hora (DD-MM-AAAA HH:MM): ")
        try:
            datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M")
        except ValueError:
            print("Fecha y hora con formato incorrecto")
            return

        alumno_existe = any(getattr(a, "dni", "") == dni_alumno for a in alumnos)
        if not alumno_existe:
            print("Error: El alumno no existe en el registro.")
            return

        profesor_existe = any(getattr(p, "dni", "") == dni_profesor for p in profesores) or bool(profesores)
        if not profesor_existe:
            print("Error: El profesor no existe en el registro.")
            return

        clase = Clase(
            alumno=dni_alumno,
            profesor=dni_profesor,
            matricula_vehiculo=input("Matrícula vehículo: "),
            fecha_hora=fecha_hora,
        )
        clases.append(clase)
        print("Clase registrada correctamente")
    except ValueError as e:
        print(f"Error: {e}") 
def registrar_anticipo(anticipos: list):
    try:
        fecha = input("Fecha (DD-MM-AAAA): ")
        datetime.strptime(fecha, "%d-%m-%Y")
        cantidad = float(input("Cantidad: "))
        anticipo = Anticipo(
            alumno=input("DNI alumno: "),
            fecha=fecha,
            concepto=input("Concepto: "),
            cantidad=cantidad,
        )
        anticipos.append(anticipo)
        print("Anticipo registrado correctamente")
    except ValueError:
        print("Cantidad incorrecta")
def mostrar_guardar_factura(facturas: list, alumnos: list, clases: list, anticipos: list, permisos: list):
    try:
        if not alumnos:
            print("No hay alumnos para facturar.")
            return

        print("\n=== ALUMNOS DISPONIBLES PARA FACTURA ===")
        for i, alumno in enumerate(alumnos, 1):
            print(f"{i}. {alumno.dni} - {alumno.nombre} {alumno.primer_apellido} {alumno.segundo_apellido}")

        idx = int(input("Elige el número de alumno: "))
        if idx < 1 or idx > len(alumnos):
            print("Opción fuera de rango")
            return

        alumno = alumnos[idx - 1]
        dni_alumno = alumno.dni

        permiso = next((p for p in permisos if p.tipo_permiso == getattr(alumno, "permiso_opta", "")), None)
        if not permiso:
            print("Error: Permiso no encontrado para ese alumno.")
            return

        num_clases_dadas = len([c for c in clases if getattr(c, "alumno", "") == dni_alumno])
        total_anticipos = sum(getattr(a, "cantidad", 0) for a in anticipos if getattr(a, "alumno", "") == dni_alumno)

        # Tomo exámenes de las listas del alumno para que no tenga que meterlos a mano
        num_examenes = len(getattr(alumno, "examenes_teoricos", []) or []) + len(getattr(alumno, "examenes_circulacion", []) or [])
        # Las renovaciones no se almacenan en ningún sitio, así que si algún día se añaden en el objeto se usan, si no 0
        num_renovaciones = getattr(alumno, "num_renovaciones", 0)

        factura = Factura(
            alumno=dni_alumno,
            precio_matricula=permiso.precio_matricula,
            num_clases_incluidas=permiso.clases_incluidas,
            num_clases_dadas=num_clases_dadas,
            precio_clase=permiso.precio_por_clase,
            num_examenes=num_examenes,
            precio_examen=permiso.precio_examen,
            num_renovaciones=num_renovaciones,
            precio_renovacion=permiso.precio_renovacion,
            anticipos=total_anticipos,
        )
        facturas.append(factura)

        contenido = factura.generar_factura()
        os.makedirs("facturas", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"./facturas/factura_{factura.alumno}_{timestamp}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(contenido)
        os.system("cls")
        print("Factura generada correctamente:")
        print(contenido)
        print(f"Guardada en {nombre_archivo}")
        input("\nPulse Enter para continuar...")
    except ValueError:
        print("Error en los datos de la factura")
        input("\nPulse Enter para continuar...")
#endregion
#region ########## Listados y menús ##########
def mostrar_alumnos(alumnos: list):
    if not alumnos:
        print("\nNo hay alumnos registrados")
        return
    print("\n=== ALUMNOS REGISTRADOS ===")
    for i, alumno in enumerate(alumnos, 1):
        print(f"{i}. {alumno.nombre} {alumno.primer_apellido} - DNI: {alumno.dni}")
    print()
def mostrar_profesores(profesores: list):
    if not profesores:
        print("\nNo hay profesores registrados")
        return
    print("\n=== PROFESORES REGISTRADOS ===")
    for i, profesor in enumerate(profesores, 1):
        print(f"{i}. {profesor.nombre} {profesor.primer_apellido} - Vehículo: {profesor.vehiculo}")
def mostrar_clases(clases: list):
    if not clases:
        print("\nNo hay clases registradas")
        return
    print("\n=== CLASES REGISTRADAS ===")
    for i, clase in enumerate(clases, 1):
        print(f"{i}. Alumno: {clase.alumno} - Profesor: {clase.profesor} - Fecha: {clase.fecha_hora}")
    print()
def mostrar_anticipos(anticipos: list):
    if not anticipos:
        print("\nNo hay anticipos registrados")
        return
    print("\n=== ANTICIPOS REGISTRADOS ===")
    for i, anticipo in enumerate(anticipos, 1):
        print(f"{i}. Alumno: {anticipo.alumno} - Cantidad: {anticipo.cantidad}€ - Fecha: {anticipo.fecha}")
    print()
def mostrar_facturas(facturas: list):
    if not facturas:
        print("\nNo hay facturas generadas")
        return
    print("\n=== FACTURAS GENERADAS ===")
    for i, factura in enumerate(facturas, 1):
        print(f"{i}. Alumno: {factura.alumno} - Total con IVA: {factura.calcular_total_con_iva():.2f}€ - Saldo: {factura.calcular_saldo_pendiente():.2f}€")
    print()
def menu_ver_datos(alumnos, profesores, clases, anticipos, facturas):
    while True:
        print("\n--- MENÚ VER DATOS ---")
        print("1. Ver alumnos")
        print("2. Ver profesores")
        print("3. Ver clases")
        print("4. Ver anticipos")
        print("5. Ver facturas")
        print("0. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe introducir un número")
            continue

        if opcion == 1:
            mostrar_alumnos(alumnos)
        elif opcion == 2:
            mostrar_profesores(profesores)
        elif opcion == 3:
            mostrar_clases(clases)
        elif opcion == 4:
            mostrar_anticipos(anticipos)
        elif opcion == 5:
            mostrar_facturas(facturas)
        elif opcion == 0:
            break
        else:
            print("Opción no válida")
def mostrar_menu():
    print("\n--- MENÚ AUTOESCUELA ---")
    print("1. Registrar alumno")
    print("2. Registrar profesor")
    print("3. Registrar clase")
    print("4. Registrar anticipo")
    print("5. Generar factura")
    print("6. Ver datos")
    print("0. Salir") 
#endregion 