# Conversores de objetos <-> diccionarios para persistencia en JSON.
# Para explicar bien esto -> Son las funciones que Desserializan a POO y Serializan a JSON
from Alumno import Alumno
from Profesor import Profesor
from Clase import Clase
from Permiso import Permiso
from Factura import Factura
from Anticipo import Anticipo
def alumno_desde_dict(d: dict) -> Alumno:
    return Alumno(
        num_registro=d.get("num_registro", ""),
        nombre=d.get("nombre", ""),
        primer_apellido=d.get("primer_apellido", ""),
        segundo_apellido=d.get("segundo_apellido", ""),
        dni=d.get("dni", ""),
        fecha_nacimiento=d.get("fecha_nacimiento", ""),
        fecha_registro=d.get("fecha_registro", ""),
        permiso_opta=d.get("permiso_opta", ""),
        domicilio=d.get("domicilio", ""),
        municipio=d.get("municipio", ""),
        provincia=d.get("provincia", ""),
        telefono1=d.get("telefono1", ""),
        correo=d.get("correo", ""),
        num_clases=int(d.get("num_clases", 0)),
        profesor=d.get("profesor", ""),
        telefono2=d.get("telefono2", ""),
        examenes_teoricos=d.get("examenes_teoricos") or d.get("examen_teorico") or [],
        examenes_circulacion=d.get("examenes_circulacion") or d.get("examen_circulacion") or [],
        total_anticipos=float(d.get("total_anticipos", 0.0)),
    )
def alumno_a_dict(a: Alumno) -> dict:
    return {
        "num_registro": a.num_registro,
        "nombre": a.nombre,
        "primer_apellido": a.primer_apellido,
        "segundo_apellido": a.segundo_apellido,
        "dni": a.dni,
        "fecha_nacimiento": a.fecha_nacimiento,
        "fecha_registro": a.fecha_registro,
        "permiso_opta": a.permiso_opta,
        "domicilio": a.domicilio,
        "municipio": a.municipio,
        "provincia": a.provincia,
        "telefono1": a.telefono1,
        "telefono2": a.telefono2,
        "correo": a.correo,
        "num_clases": a.num_clases,
        "profesor": a.profesor,
        "examenes_teoricos": a.examenes_teoricos,
        "examenes_circulacion": a.examenes_circulacion,
        "total_anticipos": a.total_anticipos,
    }
def profesor_desde_dict(d: dict) -> Profesor:
    gastos = d.get("gastos_combustible", {})
    return Profesor(
        nombre=d.get("nombre", ""),
        primer_apellido=d.get("primer_apellido", ""),
        segundo_apellido=d.get("segundo_apellido", ""),
        vehiculo=d.get("vehiculo", ""),
        tipo_vehiculo=d.get("tipo_vehiculo", ""),
        itv=d.get("itv", ""),
        gastos_combustible=gastos,
    )
def profesor_a_dict(p: Profesor) -> dict:
    return {
        "nombre": p.nombre,
        "primer_apellido": p.primer_apellido,
        "segundo_apellido": p.segundo_apellido,
        "vehiculo": p.vehiculo,
        "tipo_vehiculo": p.tipo_vehiculo,
        "itv": p.itv,
        "gastos_combustible": p.gastos_combustible,
    }
def clase_desde_dict(d: dict) -> Clase:
    return Clase(
        alumno=d.get("alumno", ""),
        profesor=d.get("profesor", ""),
        matricula_vehiculo=d.get("matricula_vehiculo", ""),
        fecha_hora=d.get("fecha_hora", ""),
    )
def clase_a_dict(c: Clase) -> dict:
    return {
        "alumno": c.alumno,
        "profesor": c.profesor,
        "matricula_vehiculo": c.matricula_vehiculo,
        "fecha_hora": c.fecha_hora,
    }
def anticipo_desde_dict(d: dict) -> Anticipo:
    return Anticipo(
        alumno=d.get("alumno", ""),
        fecha=d.get("fecha", ""),
        concepto=d.get("concepto", ""),
        cantidad=float(d.get("cantidad", 0)),
    )
def anticipo_a_dict(a: Anticipo) -> dict:
    return {
        "alumno": a.alumno,
        "fecha": a.fecha,
        "concepto": a.concepto,
        "cantidad": a.cantidad,
    }
def permiso_desde_dict(d: dict) -> Permiso:
    return Permiso(
        tipo_permiso=d.get("tipo_permiso", ""),
        precio_matricula=float(d.get("precio_matricula", 0)),
        clases_incluidas=int(d.get("clases_incluidas", 0)),
        precio_por_clase=float(d.get("precio_por_clase", 0)),
        precio_examen=float(d.get("precio_examen", 0)),
        precio_renovacion=float(d.get("precio_renovacion", 0)),
    )
def permiso_a_dict(p: Permiso) -> dict:
    return {
        "tipo_permiso": p.tipo_permiso,
        "precio_matricula": p.precio_matricula,
        "clases_incluidas": p.clases_incluidas,
        "precio_por_clase": p.precio_por_clase,
        "precio_examen": p.precio_examen,
        "precio_renovacion": p.precio_renovacion,
    }
def factura_desde_dict(d: dict) -> Factura:
    return Factura(
        alumno=d.get("alumno", ""),
        precio_matricula=float(d.get("precio_matricula", 0)),
        num_clases_incluidas=int(d.get("num_clases_incluidas", 0)),
        num_clases_dadas=int(d.get("num_clases_dadas", 0)),
        precio_clase=float(d.get("precio_clase", 0)),
        num_examenes=int(d.get("num_examenes", 0)),
        precio_examen=float(d.get("precio_examen", 0)),
        num_renovaciones=int(d.get("num_renovaciones", 0)),
        precio_renovacion=float(d.get("precio_renovacion", 0)),
        anticipos=float(d.get("anticipos", 0)),
    )
def factura_a_dict(f: Factura) -> dict:
    return {
        "alumno": f.alumno,
        "precio_matricula": f.precio_matricula,
        "num_clases_incluidas": f.num_clases_incluidas,
        "num_clases_dadas": f.num_clases_dadas,
        "precio_clase": f.precio_clase,
        "num_examenes": f.num_examenes,
        "precio_examen": f.precio_examen,
        "num_renovaciones": f.num_renovaciones,
        "precio_renovacion": f.precio_renovacion,
        "anticipos": f.anticipos,
    }