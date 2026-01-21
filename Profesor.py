# CLASE PROFESOR
# La clase Profesor se encarga de almacenar la información de los profesores y del vehículo que utilizan.
# Atributos:
    # nombre: string.
    # primer_apellido: string.
    # segundo_apellido: string.
    # vehiculo: string (matrícula).
    # tipo_vehiculo: string (tipo de vehículo)
    # itv: string (fecha de caducidad de la ITV).
    # gastos_combustible: dict (clave: fecha, valor: coste del gasto).
# Métodos:
    # __init__: Inicializa los atributos.
    # registrar_gasto_combustible(fecha, costo): Agrega un gasto de combustible al historial.
    # mostrar_gastos_combustible(): Muestra los gastos de combustible acumulados.
    # mostrar_info_profesor(): Muestra la información del profesor y el vehículo.


class Profesor:
    def __init__(self,nombre: str,primer_apellido: str,segundo_apellido: str,vehiculo: str,tipo_vehiculo: str,itv: str,gastos_combustible: dict = None ): #type: ignore
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.vehiculo = vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.itv = itv
        self.gastos_combustible = gastos_combustible or {}
        
    # registrar_gasto_combustible(fecha, costo): Agrega un gasto de combustible al historial.
    def registrar_gasto_combustible(self, fecha: str, costo: float):
        self.gastos_combustible[fecha] = costo
        
    # mostrar_gastos_combustible(): Muestra los gastos de combustible acumulados.
    def mostrar_gastos_combustible(self):
        if not self.gastos_combustible:
            return "No hay gastos de combustible registrados."
        resultado = "Gastos de combustible:\n"
        for fecha, costo in self.gastos_combustible.items():
            resultado += f"- {fecha}: {costo} €\n"
        return resultado
    
    # mostrar_info_profesor(): Muestra la información del profesor y el vehículo.
    def mostrar_info_profesor(self):
        return (
            f"Nombre: {self.nombre} {self.primer_apellido} {self.segundo_apellido}\n"
            f"Vehículo: {self.vehiculo}\n"
            f"Tipo de vehículo: {self.tipo_vehiculo}\n"
            f"ITV (caducidad): {self.itv}"
        )


if __name__ == "__main__":
    
    prof = Profesor(
        nombre="Carlos",
        primer_apellido="Ruiz",
        segundo_apellido="López",
        vehiculo="1234ABC",
        tipo_vehiculo="Turismo",
        itv="30-06-2025",
    )
    print("\nProfesor antes de registrar gasto de combustible\n")
    print(prof.mostrar_info_profesor())
    print(prof.mostrar_gastos_combustible())
    prof.registrar_gasto_combustible("10-02-2024", 45.60)
    print("\nProfesor tras registrar gasto de combustible\n")
    print(prof.mostrar_info_profesor())
    print(prof.mostrar_gastos_combustible())
