
import json
import os

os.makedirs('datos', exist_ok=True)

# 10 ALUMNOS
alumnos = [
    {
        'num_registro': '2024/001',
        'nombre': 'Juan',
        'primer_apellido': 'Pérez',
        'segundo_apellido': 'García',
        'dni': '12345678A',
        'fecha_nacimiento': '01-01-1995',
        'fecha_registro': '10-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Calle Mayor 10',
        'municipio': 'Madrid',
        'provincia': 'Madrid',
        'telefono1': '600123456',
        'telefono2': None,
        'correo': 'juan.perez@email.com',
        'num_clases': 10,
        'profesor': 'Carlos Ruiz',
        'examenes_teoricos': ['15-03-2024 10:00'],
        'examenes_circulacion': ['22-03-2024 09:30']
    },
    {
        'num_registro': '2024/002',
        'nombre': 'María',
        'primer_apellido': 'López',
        'segundo_apellido': 'Martínez',
        'dni': '23456789B',
        'fecha_nacimiento': '15-05-1996',
        'fecha_registro': '12-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Avenida Paseo 25',
        'municipio': 'Barcelona',
        'provincia': 'Barcelona',
        'telefono1': '600234567',
        'telefono2': None,
        'correo': 'maria.lopez@email.com',
        'num_clases': 8,
        'profesor': 'Ana Fernández',
        'examenes_teoricos': [],
        'examenes_circulacion': []
    },
    {
        'num_registro': '2024/003',
        'nombre': 'Carlos',
        'primer_apellido': 'González',
        'segundo_apellido': 'Rodríguez',
        'dni': '34567890C',
        'fecha_nacimiento': '22-03-1997',
        'fecha_registro': '14-02-2024',
        'permiso_opta': 'A',
        'domicilio': 'Plaza del Sol 5',
        'municipio': 'Valencia',
        'provincia': 'Valencia',
        'telefono1': '600345678',
        'telefono2': '600345679',
        'correo': 'carlos.gonzalez@email.com',
        'num_clases': 12,
        'profesor': 'Miguel Torres',
        'examenes_teoricos': ['20-03-2024 11:00'],
        'examenes_circulacion': []
    },
    {
        'num_registro': '2024/004',
        'nombre': 'Laura',
        'primer_apellido': 'Sánchez',
        'segundo_apellido': 'Gómez',
        'dni': '45678901D',
        'fecha_nacimiento': '08-07-1994',
        'fecha_registro': '16-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Calle Real 42',
        'municipio': 'Sevilla',
        'provincia': 'Sevilla',
        'telefono1': '600456789',
        'telefono2': None,
        'correo': 'laura.sanchez@email.com',
        'num_clases': 6,
        'profesor': 'Carlos Ruiz',
        'examenes_teoricos': [],
        'examenes_circulacion': []
    },
    {
        'num_registro': '2024/005',
        'nombre': 'Diego',
        'primer_apellido': 'Ramírez',
        'segundo_apellido': 'López',
        'dni': '56789012E',
        'fecha_nacimiento': '30-11-1998',
        'fecha_registro': '18-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Avenida Central 88',
        'municipio': 'Bilbao',
        'provincia': 'Vizcaya',
        'telefono1': '600567890',
        'telefono2': None,
        'correo': 'diego.ramirez@email.com',
        'num_clases': 9,
        'profesor': 'Ana Fernández',
        'examenes_teoricos': ['25-03-2024 14:00'],
        'examenes_circulacion': ['01-04-2024 10:00']
    },
    {
        'num_registro': '2024/006',
        'nombre': 'Elena',
        'primer_apellido': 'Martín',
        'segundo_apellido': 'Jiménez',
        'dni': '67890123F',
        'fecha_nacimiento': '12-02-1996',
        'fecha_registro': '20-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Camino Verde 15',
        'municipio': 'Malaga',
        'provincia': 'Malaga',
        'telefono1': '600678901',
        'telefono2': None,
        'correo': 'elena.martin@email.com',
        'num_clases': 7,
        'profesor': 'Miguel Torres',
        'examenes_teoricos': [],
        'examenes_circulacion': []
    },
    {
        'num_registro': '2024/007',
        'nombre': 'Fernando',
        'primer_apellido': 'Díaz',
        'segundo_apellido': 'Moreno',
        'dni': '78901234G',
        'fecha_nacimiento': '19-09-1995',
        'fecha_registro': '22-02-2024',
        'permiso_opta': 'A',
        'domicilio': 'Pasaje Nuevo 60',
        'municipio': 'Zaragoza',
        'provincia': 'Zaragoza',
        'telefono1': '600789012',
        'telefono2': None,
        'correo': 'fernando.diaz@email.com',
        'num_clases': 11,
        'profesor': 'Carlos Ruiz',
        'examenes_teoricos': ['28-03-2024 09:00'],
        'examenes_circulacion': []
    },
    {
        'num_registro': '2024/008',
        'nombre': 'Gabriela',
        'primer_apellido': 'Flores',
        'segundo_apellido': 'Santos',
        'dni': '89012345H',
        'fecha_nacimiento': '25-06-1997',
        'fecha_registro': '24-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Avenida Libertad 20',
        'municipio': 'Palma',
        'provincia': 'Baleares',
        'telefono1': '600890123',
        'telefono2': None,
        'correo': 'gabriela.flores@email.com',
        'num_clases': 8,
        'profesor': 'Ana Fernández',
        'examenes_teoricos': [],
        'examenes_circulacion': ['05-04-2024 15:00']
    },
    {
        'num_registro': '2024/009',
        'nombre': 'Héctor',
        'primer_apellido': 'Castro',
        'segundo_apellido': 'Ruiz',
        'dni': '90123456I',
        'fecha_nacimiento': '03-04-1994',
        'fecha_registro': '26-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Calle Paz 35',
        'municipio': 'Córdoba',
        'provincia': 'Córdoba',
        'telefono1': '600901234',
        'telefono2': '600901235',
        'correo': 'hector.castro@email.com',
        'num_clases': 10,
        'profesor': 'Miguel Torres',
        'examenes_teoricos': ['30-03-2024 10:30'],
        'examenes_circulacion': []
    },
    {
        'num_registro': '2024/010',
        'nombre': 'Isabela',
        'primer_apellido': 'Navarro',
        'segundo_apellido': 'Molina',
        'dni': '01234567J',
        'fecha_nacimiento': '14-10-1998',
        'fecha_registro': '28-02-2024',
        'permiso_opta': 'B',
        'domicilio': 'Calle Esperanza 50',
        'municipio': 'Alicante',
        'provincia': 'Alicante',
        'telefono1': '601012345',
        'telefono2': None,
        'correo': 'isabela.navarro@email.com',
        'num_clases': 9,
        'profesor': 'Carlos Ruiz',
        'examenes_teoricos': [],
        'examenes_circulacion': []
    }
]

# 10 PROFESORES
profesores = [
    {
        'nombre': 'Carlos',
        'primer_apellido': 'Ruiz',
        'segundo_apellido': 'López',
        'dni': '87654321B',
        'vehiculo': '1234ABC',
        'tipo_vehiculo': 'Turismo',
        'itv': '30-06-2025',
        'gastos_combustible': {'10-02-2024': 45.60, '18-02-2024': 38.20}
    },
    {
        'nombre': 'Ana',
        'primer_apellido': 'Fernández',
        'segundo_apellido': 'García',
        'dni': '87654322C',
        'vehiculo': '5678DEF',
        'tipo_vehiculo': 'Turismo',
        'itv': '15-08-2025',
        'gastos_combustible': {'12-02-2024': 52.40, '20-02-2024': 41.80}
    },
    {
        'nombre': 'Miguel',
        'primer_apellido': 'Torres',
        'segundo_apellido': 'Sánchez',
        'dni': '87654323D',
        'vehiculo': '9012GHI',
        'tipo_vehiculo': 'Turismo',
        'itv': '22-05-2025',
        'gastos_combustible': {'14-02-2024': 38.50, '21-02-2024': 45.70}
    },
    {
        'nombre': 'Patricia',
        'primer_apellido': 'Moreno',
        'segundo_apellido': 'Díaz',
        'dni': '87654324E',
        'vehiculo': '3456JKL',
        'tipo_vehiculo': 'Turismo',
        'itv': '10-07-2025',
        'gastos_combustible': {'16-02-2024': 50.00, '24-02-2024': 42.30}
    },
    {
        'nombre': 'Javier',
        'primer_apellido': 'Gómez',
        'segundo_apellido': 'Ramírez',
        'dni': '87654325F',
        'vehiculo': '7890MNO',
        'tipo_vehiculo': 'Turismo',
        'itv': '18-09-2025',
        'gastos_combustible': {'17-02-2024': 44.20, '25-02-2024': 39.80}
    },
    {
        'nombre': 'Sandra',
        'primer_apellido': 'Martínez',
        'segundo_apellido': 'López',
        'dni': '87654326G',
        'vehiculo': '2345PQR',
        'tipo_vehiculo': 'Turismo',
        'itv': '05-06-2025',
        'gastos_combustible': {'19-02-2024': 47.60, '26-02-2024': 43.20}
    },
    {
        'nombre': 'Roberto',
        'primer_apellido': 'Jiménez',
        'segundo_apellido': 'García',
        'dni': '87654327H',
        'vehiculo': '6789STU',
        'tipo_vehiculo': 'Turismo',
        'itv': '12-04-2025',
        'gastos_combustible': {'21-02-2024': 51.40, '27-02-2024': 40.60}
    },
    {
        'nombre': 'Valentina',
        'primer_apellido': 'Castro',
        'segundo_apellido': 'Molina',
        'dni': '87654328I',
        'vehiculo': '0123VWX',
        'tipo_vehiculo': 'Turismo',
        'itv': '28-08-2025',
        'gastos_combustible': {'23-02-2024': 46.80, '28-02-2024': 38.40}
    },
    {
        'nombre': 'Andrés',
        'primer_apellido': 'Flores',
        'segundo_apellido': 'Navarro',
        'dni': '87654329J',
        'vehiculo': '4567YZA',
        'tipo_vehiculo': 'Turismo',
        'itv': '20-03-2025',
        'gastos_combustible': {'25-02-2024': 49.20, '29-02-2024': 41.70}
    },
    {
        'nombre': 'Cristina',
        'primer_apellido': 'Ruiz',
        'segundo_apellido': 'Sánchez',
        'dni': '87654330K',
        'vehiculo': '8901BCD',
        'tipo_vehiculo': 'Turismo',
        'itv': '11-07-2025',
        'gastos_combustible': {'27-02-2024': 53.10, '01-03-2024': 44.50}
    }
]

# 10 CLASES
clases = [
    {
        'alumno': '12345678A',
        'profesor': '87654321B',
        'matricula_vehiculo': '1234ABC',
        'fecha_hora': '20-03-2024 10:00'
    },
    {
        'alumno': '23456789B',
        'profesor': '87654322C',
        'matricula_vehiculo': '5678DEF',
        'fecha_hora': '21-03-2024 11:00'
    },
    {
        'alumno': '34567890C',
        'profesor': '87654323D',
        'matricula_vehiculo': '9012GHI',
        'fecha_hora': '22-03-2024 09:30'
    },
    {
        'alumno': '45678901D',
        'profesor': '87654321B',
        'matricula_vehiculo': '1234ABC',
        'fecha_hora': '23-03-2024 14:00'
    },
    {
        'alumno': '56789012E',
        'profesor': '87654322C',
        'matricula_vehiculo': '5678DEF',
        'fecha_hora': '24-03-2024 15:30'
    },
    {
        'alumno': '67890123F',
        'profesor': '87654323D',
        'matricula_vehiculo': '9012GHI',
        'fecha_hora': '25-03-2024 10:00'
    },
    {
        'alumno': '78901234G',
        'profesor': '87654321B',
        'matricula_vehiculo': '1234ABC',
        'fecha_hora': '26-03-2024 11:30'
    },
    {
        'alumno': '89012345H',
        'profesor': '87654324E',
        'matricula_vehiculo': '3456JKL',
        'fecha_hora': '27-03-2024 13:00'
    },
    {
        'alumno': '90123456I',
        'profesor': '87654325F',
        'matricula_vehiculo': '7890MNO',
        'fecha_hora': '28-03-2024 09:00'
    },
    {
        'alumno': '01234567J',
        'profesor': '87654326G',
        'matricula_vehiculo': '2345PQR',
        'fecha_hora': '29-03-2024 16:00'
    }
]

# 10 ANTICIPOS
anticipos = [
    {
        'alumno': '12345678A',
        'fecha': '05-03-2024',
        'concepto': 'Primer pago matrícula',
        'cantidad': 150.0
    },
    {
        'alumno': '23456789B',
        'fecha': '06-03-2024',
        'concepto': 'Pago parcial clases',
        'cantidad': 100.0
    },
    {
        'alumno': '34567890C',
        'fecha': '07-03-2024',
        'concepto': 'Primer pago',
        'cantidad': 200.0
    },
    {
        'alumno': '45678901D',
        'fecha': '08-03-2024',
        'concepto': 'Anticipo general',
        'cantidad': 120.0
    },
    {
        'alumno': '56789012E',
        'fecha': '09-03-2024',
        'concepto': 'Pago inicial',
        'cantidad': 180.0
    },
    {
        'alumno': '67890123F',
        'fecha': '10-03-2024',
        'concepto': 'Primer pago parcial',
        'cantidad': 140.0
    },
    {
        'alumno': '78901234G',
        'fecha': '11-03-2024',
        'concepto': 'Anticipo de matrícula',
        'cantidad': 250.0
    },
    {
        'alumno': '89012345H',
        'fecha': '12-03-2024',
        'concepto': 'Pago de clases',
        'cantidad': 110.0
    },
    {
        'alumno': '90123456I',
        'fecha': '13-03-2024',
        'concepto': 'Matrícula parcial',
        'cantidad': 160.0
    },
    {
        'alumno': '01234567J',
        'fecha': '14-03-2024',
        'concepto': 'Pago inicial matricula',
        'cantidad': 175.0
    }
]

# 10 FACTURAS
facturas = [
    {
        'alumno': '12345678A',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 14,
        'precio_clase': 30.0,
        'num_examenes': 2,
        'precio_examen': 120.0,
        'num_renovaciones': 1,
        'precio_renovacion': 80.0,
        'anticipos': 200.0
    },
    {
        'alumno': '23456789B',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 8,
        'precio_clase': 30.0,
        'num_examenes': 0,
        'precio_examen': 120.0,
        'num_renovaciones': 0,
        'precio_renovacion': 80.0,
        'anticipos': 100.0
    },
    {
        'alumno': '34567890C',
        'precio_matricula': 380.0,
        'num_clases_incluidas': 12,
        'num_clases_dadas': 15,
        'precio_clase': 32.0,
        'num_examenes': 1,
        'precio_examen': 140.0,
        'num_renovaciones': 0,
        'precio_renovacion': 90.0,
        'anticipos': 200.0
    },
    {
        'alumno': '45678901D',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 6,
        'precio_clase': 30.0,
        'num_examenes': 0,
        'precio_examen': 120.0,
        'num_renovaciones': 0,
        'precio_renovacion': 80.0,
        'anticipos': 120.0
    },
    {
        'alumno': '56789012E',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 12,
        'precio_clase': 30.0,
        'num_examenes': 2,
        'precio_examen': 120.0,
        'num_renovaciones': 1,
        'precio_renovacion': 80.0,
        'anticipos': 180.0
    },
    {
        'alumno': '67890123F',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 7,
        'precio_clase': 30.0,
        'num_examenes': 0,
        'precio_examen': 120.0,
        'num_renovaciones': 0,
        'precio_renovacion': 80.0,
        'anticipos': 140.0
    },
    {
        'alumno': '78901234G',
        'precio_matricula': 380.0,
        'num_clases_incluidas': 12,
        'num_clases_dadas': 13,
        'precio_clase': 32.0,
        'num_examenes': 1,
        'precio_examen': 140.0,
        'num_renovaciones': 0,
        'precio_renovacion': 90.0,
        'anticipos': 250.0
    },
    {
        'alumno': '89012345H',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 9,
        'precio_clase': 30.0,
        'num_examenes': 1,
        'precio_examen': 120.0,
        'num_renovaciones': 0,
        'precio_renovacion': 80.0,
        'anticipos': 110.0
    },
    {
        'alumno': '90123456I',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 11,
        'precio_clase': 30.0,
        'num_examenes': 2,
        'precio_examen': 120.0,
        'num_renovaciones': 1,
        'precio_renovacion': 80.0,
        'anticipos': 160.0
    },
    {
        'alumno': '01234567J',
        'precio_matricula': 350.0,
        'num_clases_incluidas': 10,
        'num_clases_dadas': 10,
        'precio_clase': 30.0,
        'num_examenes': 0,
        'precio_examen': 120.0,
        'num_renovaciones': 0,
        'precio_renovacion': 80.0,
        'anticipos': 175.0
    }
]

# Guardar todos los datos
with open('datos/alumnos.json', 'w', encoding='utf-8') as f:
    json.dump(alumnos, f, indent=4, ensure_ascii=False)

with open('datos/profesores.json', 'w', encoding='utf-8') as f:
    json.dump(profesores, f, indent=4, ensure_ascii=False)

with open('datos/clases.json', 'w', encoding='utf-8') as f:
    json.dump(clases, f, indent=4, ensure_ascii=False)

with open('datos/anticipos.json', 'w', encoding='utf-8') as f:
    json.dump(anticipos, f, indent=4, ensure_ascii=False)

with open('datos/facturas.json', 'w', encoding='utf-8') as f:
    json.dump(facturas, f, indent=4, ensure_ascii=False)

with open('datos/permisos.json', 'w', encoding='utf-8') as f:
    json.dump([
        {
            "tipo_permiso": "A",
            "precio_matricula": 500,
            "clases_incluidas": 10,
            "precio_por_clase": 50,
            "precio_examen": 100,
            "precio_renovacion": 200
        },
        {
            "tipo_permiso": "B",
            "precio_matricula": 550,
            "clases_incluidas": 12,
            "precio_por_clase": 52,
            "precio_examen": 105,
            "precio_renovacion": 210
        }
    ], f, indent=4, ensure_ascii=False)

print('[OK] Datos de ejemplo cargados correctamente')
print('- 10 alumnos en alumnos.json')
print('- 10 profesores en profesores.json')
print('- 10 clases en clases.json')
print('- 10 anticipos en anticipos.json')
print('- 10 facturas en facturas.json')
print('- 2 permisos en permisos.json')
