# CLASE FACTURA
#La clase Factura gestionará la generación de facturas para cada alumno.
# Atributos:
    # alumno: string (DNI del alumno).
    # precio_matricula: float.
    # num_clases_incluidas: int.
    # num_clases_dadas: int.
    # precio_clase: float.
    # num_examenes: int.
    # precio_examen: float.
    # num_renovaciones: int.
    # precio_renovacion: float.
    # anticipos: float.
# Métodos:
    # __init__: Inicializa los atributos.
    # calcular_total(): Calcula el total de la factura (matrícula + clases + exámenes + renovaciones).
    # calcular_iva(): Calcula el 21% de IVA.
    # calcular_total_con_iva(): Calcula el total con IVA incluido.
    # calcular_saldo_pendiente(): Resta los anticipos del total con IVA.
    # generar_factura(): Muestra la factura completa, detallando todos los conceptos.

class Factura:
    def __init__( self, alumno: str, precio_matricula: float, num_clases_incluidas: int, num_clases_dadas: int, precio_clase: float, num_examenes: int, precio_examen: float, num_renovaciones: int, precio_renovacion: float, anticipos: float, ):
        self.alumno = alumno
        self.precio_matricula = precio_matricula
        self.num_clases_incluidas = num_clases_incluidas
        self.num_clases_dadas = num_clases_dadas
        self.precio_clase = precio_clase
        self.num_examenes = num_examenes
        self.precio_examen = precio_examen
        self.num_renovaciones = num_renovaciones
        self.precio_renovacion = precio_renovacion
        self.anticipos = anticipos

    def calcular_total(self):
        # Solo se cobra lo que supera las clases incluidas
        clases_extra = max(0, self.num_clases_dadas - self.num_clases_incluidas)
        total_clases = clases_extra * self.precio_clase
        total_examenes = self.num_examenes * self.precio_examen
        total_renovaciones = self.num_renovaciones * self.precio_renovacion
        return self.precio_matricula + total_clases + total_examenes + total_renovaciones

    def calcular_iva(self):
        return self.calcular_total() * 0.21

    def calcular_total_con_iva(self):
        return self.calcular_total() + self.calcular_iva()

    def calcular_saldo_pendiente(self):
        return self.calcular_total_con_iva() - self.anticipos

    def generar_factura(self):
        total = self.calcular_total()
        iva = self.calcular_iva()
        total_con_iva = self.calcular_total_con_iva()
        saldo = self.calcular_saldo_pendiente()
        clases_extra = max(0, self.num_clases_dadas - self.num_clases_incluidas)
        total_clases = clases_extra * self.precio_clase
        total_examenes = self.num_examenes * self.precio_examen
        total_renovaciones = self.num_renovaciones * self.precio_renovacion

        return (
            f"{'='*50}\n"
            f"{'FACTURA DE AUTOESCUELA':^50}\n"
            f"{'='*50}\n\n"
            f"Alumno (DNI): {self.alumno}\n\n"
            f"DETALLE DE CONCEPTOS:\n"
            f"-{'-'*48}\n"
            f"Matricula:                          {self.precio_matricula:.2f} EUR\n"
            f"\nClases:\n"
            f"  Clases incluidas: {self.num_clases_incluidas}\n"
            f"  Clases dadas: {self.num_clases_dadas}\n"
            f"  Clases extra ({clases_extra}): {clases_extra} x {self.precio_clase:.2f} EUR {total_clases:.2f} EUR\n"
            f"\nExamenes: {self.num_examenes} x {self.precio_examen:.2f} EUR {total_examenes:.2f} EUR\n"
            f"\nRenovaciones: {self.num_renovaciones} x {self.precio_renovacion:.2f} EUR {total_renovaciones:.2f} EUR\n"
            f"-{'-'*48}\n"
            f"Total sin IVA:                      {total:.2f} EUR\n"
            f"IVA (21%):                          {iva:.2f} EUR\n"
            f"TOTAL CON IVA:                      {total_con_iva:.2f} EUR\n"
            f"Menos: Anticipos:                  -{self.anticipos:.2f} EUR\n"
            f"{'='*50}\n"
            f"SALDO PENDIENTE:                    {saldo:.2f} EUR\n"
            f"{'='*50}\n"
        )


if __name__ == "__main__":
    # Ejemplo rápido
    factura1 = Factura(
        alumno="12345678A",
        precio_matricula=350.0,
        num_clases_incluidas=10,
        num_clases_dadas=14,
        precio_clase=30.0,
        num_examenes=2,
        precio_examen=120.0,
        num_renovaciones=1,
        precio_renovacion=80.0,
        anticipos=200.0,
    )
    print(factura1.generar_factura())

