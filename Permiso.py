# CLASE PERMISO
# La clase Permiso gestionará la información de los tipos de licencias disponibles en la autoescuela.
# Atributos:
    # tipo_permiso: string (ej. "B", "A").
    # precio_matricula: float.
    # clases_incluidas: int.
    # precio_por_clase: float.
    # precio_examen: float.
    # precio_renovacion: float.
# Métodos:
    # __init__: Inicializa los atributos del permiso.
    # mostrar_info_permiso(): Muestra la información completa del permiso.
    
class Permiso:
    def __init__( self, tipo_permiso: str, precio_matricula: float, clases_incluidas: int, precio_por_clase: float, precio_examen: float, precio_renovacion: float = 0.0):
        self.tipo_permiso = tipo_permiso
        self.precio_matricula = precio_matricula
        self.clases_incluidas = clases_incluidas
        self.precio_por_clase = precio_por_clase
        self.precio_examen = precio_examen
        self.precio_renovacion = precio_renovacion


    # Función para mostrar información del permiso
    def mostrar_info_permiso(self):
        return (
            f"Tipo de permiso: {self.tipo_permiso}\n"
            f"Precio matrícula: {self.precio_matricula} €\n"
            f"Clases incluidas: {self.clases_incluidas}\n"
            f"Precio por clase: {self.precio_por_clase} €\n"
            f"Precio de examen: {self.precio_examen} €\n"
            f"Precio de renovación: {self.precio_renovacion} €"
        )

if __name__ == "__main__":
    # Ejemplo de uso
    permiso_b = Permiso(
        tipo_permiso="B",
        precio_matricula=350.0,
        clases_incluidas=10,
        precio_por_clase=30.0,
        precio_examen=120.0,
        precio_renovacion=80.0
    )

    print(permiso_b.mostrar_info_permiso())
