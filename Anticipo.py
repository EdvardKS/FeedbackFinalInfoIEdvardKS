# CLASE ANTICIPO
# La clase Anticipo almacenará y gestionará los pagos anticipados de los alumnos.
# Atributos:
    # alumno: string (DNI del alumno).
    # fecha: string.
    # concepto: string.
    # cantidad: float.
# Métodos:
    # __init__: Inicializa los atributos.
    # mostrar_info_anticipo(): Muestra la información completa del anticipo realizado.
    
    
class Anticipo:
    
    def __init__(self, alumno: str, fecha: str, concepto: str, cantidad: float):
        self.alumno = alumno
        self.fecha = fecha
        self.concepto = concepto
        self.cantidad = cantidad

    # Función para mostrar la información del anticipo
    def mostrar_info_anticipo(self):
        return (
            f"Alumno (DNI): {self.alumno}\n"
            f"Fecha: {self.fecha}\n"
            f"Concepto: {self.concepto}\n"
            f"Cantidad: {self.cantidad} €"
        )


anticipo1 = Anticipo(
    alumno="12345678A",
    fecha="05-03-2024",
    concepto="Primer pago matrícula",
    cantidad=150.0
)

print(anticipo1.mostrar_info_anticipo())
