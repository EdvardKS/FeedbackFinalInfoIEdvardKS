# CLASE ALUMNO
# La clase Alumno hereda de la clase Registro y contiene información adicional relacionada con el alumno.
# Atributos:
    # domicilio: string.
    # municipio: string.
    # provincia: string.
    # telefono1: string.
    # telefono2: string (opcional).
    # correo: string.
    # num_clases: int.
    # profesor: string.
    # examenes_teoricos: list (fecha y hora de los exámenes teóricos).
    # examenes_circulacion: list (fecha y hora de los exámenes de circulación).
    # total_anticipos: float.
# • Métodos:
    # __init__: Inicializa con los atributos del alumno.
    # agregar_examen_teorico(): Permite añadir nuevas fechas para los exámenesteóricos.
    # agregar_examen_circulacion(): Permite añadir nuevas fechas para los exámenes de circulación.
    # agregar_clases(num): Añade el número de clases realizadas.
    # mostrar_info_completa(): Muestra toda la información completa del alumno.

from Registro import Registro


class Alumno(Registro):
    def __init__( self, num_registro: str, nombre: str, primer_apellido: str, segundo_apellido: str, dni: str, fecha_nacimiento: str, fecha_registro: str, permiso_opta: str, domicilio: str, municipio: str, provincia: str, telefono1: str, correo: str, num_clases: int, profesor: str, telefono2: str = None,  examenes_teoricos: list = None, examenes_circulacion: list = None, total_anticipos: float = 0.0, ):# type: ignore
        
        # Construimos la parte de Registro
        super().__init__( num_registro=num_registro, nombre=nombre, primer_apellido=primer_apellido, segundo_apellido=segundo_apellido, dni=dni, fecha_nacimiento=fecha_nacimiento, fecha_registro=fecha_registro, permiso_opta=permiso_opta, )
       
        # Ahora añadimos los atributos específicos de Alumno
        self.domicilio = domicilio
        self.municipio = municipio
        self.provincia = provincia
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.correo = correo
        self.num_clases = num_clases
        self.profesor = profesor
        self.examenes_teoricos = examenes_teoricos or []
        self.examenes_circulacion = examenes_circulacion or []
        self.total_anticipos = total_anticipos

    # agregar_examen_teorico(): Permite añadir nuevas fechas para los exámenes teóricos.
    def agregar_examen_teorico(self, fecha_hora: str):
        self.examenes_teoricos.append(fecha_hora)

    # agregar_examen_circulacion(): Permite añadir nuevas fechas para los exámenes de circulación.
    def agregar_examen_circulacion(self, fecha_hora: str):
        self.examenes_circulacion.append(fecha_hora)

    # agregar_clases(num): Añade el número de clases realizadas.
    def agregar_clases(self, num: int):
        self.num_clases += num
    
    # mostrar_info_completa(): Muestra toda la información completa del alumno.
    def mostrar_info_completa(self):
        # Primero saco la info básica del padre y luego añado los datos extra del alumno
        info_base = super().mostrar_datos()
        info_extra = (
            f"\n\nDomicilio: {self.domicilio}\n"
            f"Municipio: {self.municipio}\n"
            f"Provincia: {self.provincia}\n"
            f"Teléfono 1: {self.telefono1}\n"
            f"Teléfono 2: {self.telefono2}\n"
            f"Correo: {self.correo}\n"
            f"Profesor: {self.profesor}\n"
            f"Número de clases: {self.num_clases}\n"
            f"Exámenes teóricos: {self.examenes_teoricos}\n"
            f"Exámenes circulación: {self.examenes_circulacion}\n"
            f"Total anticipos: {self.total_anticipos} €"
        )
        return info_base + info_extra


if __name__ == "__main__":
    # Ejemplo de uso sencillo EJECUTAR conn py alumno.py
    alumno1 = Alumno(
        num_registro="2025/002",
        nombre="Ana",
        primer_apellido="Lopez",
        segundo_apellido="Diaz",
        dni="12345678A",
        fecha_nacimiento="01-01-1990",
        fecha_registro="02-02-2025",
        permiso_opta="B",
        domicilio="Calle Mayor 1",
        municipio="Madrid",
        provincia="Madrid",
        telefono1="600000000",
        correo="ana@test.com",
        num_clases=5,
        profesor="Profe Uno",
    )
    
    print("Información inicial del alumno:\n")
    print(alumno1.mostrar_info_completa())
    
    
    alumno1.agregar_examen_teorico("10-02-2025 09:00")
    alumno1.agregar_clases(2)
    
    print("\nInformación del alumno tras añadir examen teórico y clases:\n")
    print(alumno1.mostrar_info_completa())
