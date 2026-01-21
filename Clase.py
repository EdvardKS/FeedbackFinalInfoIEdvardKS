# CLASE CLASE
# La clase Clase gestionará las sesiones entre el alumno y el profesor.
# Atributos:
    # alumno: string (DNI del alumno).
    # profesor: string (DNI del profesor).
    # matricula_vehiculo: string.
    # fecha_hora: string.
# Métodos:
    # __init__: Inicializa la clase con los datos requeridos.
    # mostrar_info_clase(): Muestra la información de la clase realizada

class Clase:
    def __init__( self, alumno: str, profesor: str, matricula_vehiculo: str, fecha_hora: str ):
        self.alumno = alumno
        self.profesor = profesor
        self.matricula_vehiculo = matricula_vehiculo
        self.fecha_hora = fecha_hora

    # Función para mostrar la información de la clase
    def mostrar_info_clase(self):
        return (
            f"Alumno (DNI): {self.alumno}\n"
            f"Profesor (DNI): {self.profesor}\n"
            f"Matrícula del vehículo: {self.matricula_vehiculo}\n"
            f"Fecha y hora: {self.fecha_hora}"
        )

# Ejemplo de uso: USAR PY clase.py
if __name__ == "__main__":
    clase_ejemplo = Clase("12345678A", "87654321B", "ABC1234", "2024-06-15 10:00")
    print(clase_ejemplo.mostrar_info_clase())
