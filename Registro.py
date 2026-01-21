# CLASE REGISTRO
# La clase Registro se encargará de almacenar y gestionar la información básica de los alumnos.
# Atributos:
    # num_registro: string (formato "Año/Numero").
    # nombre: string.
    # primer_apellido: string.
    # segundo_apellido: string.
    # dni: string.
    # fecha_nacimiento: string (formato "DD-MM-AAAA").
    # fecha_registro: string (formato "DD-MM-AAAA").
    # permiso_opta: string (ej. "B", "A").
# Métodos:
    # __init__: Para inicializar los atributos.
    # mostrar_datos(): Para mostrar la información del alumno en formato legible.


class Registro:
    def __init__(self, num_registro: str, nombre: str, primer_apellido: str, segundo_apellido: str, dni: str, fecha_nacimiento: str, fecha_registro: str, permiso_opta: str):
        self.num_registro = num_registro
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_registro = fecha_registro
        self.permiso_opta = permiso_opta

    # mostrar_datos(): Para mostrar la información del alumno en formato legible.
    def mostrar_datos(self):
        return (
            f"Num. Registro: {self.num_registro}\n"
            f"Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\n"
            f"DNI: {self.dni}\n"
            f"Fecha Nacimiento: {self.fecha_nacimiento}\n"
            f"Fecha Registro: {self.fecha_registro}\n"
            f"Permiso OPTA: {self.permiso_opta}"
        )
  
if __name__ == "__main__":
    # Ejemplo de uso: creamos un registro y mostramos sus datos SOLO SE EJECUTARA SI HACES PY REGISTRO.PY
    registro1 = Registro(
        num_registro="2025/001",
        nombre="Juan",
        primer_apellido="Pérez",
        segundo_apellido="García",
        dni="12345678A",
        fecha_nacimiento="01-01-1990",
        fecha_registro="15-05-2023",
        permiso_opta="B"
    )
    print(registro1.mostrar_datos())
