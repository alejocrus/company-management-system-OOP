# Sistema de Gestión Organizacional — POO en Python

Proyecto desarrollado como parte del aprendizaje de **Programación Orientada a Objetos (POO)** en Python. Simula el sistema interno de una organización llamada **ALECRU**, permitiendo gestionar empleados, directivos y clientes desde consola.

---

## Descripción

El sistema cuenta con dos áreas principales:

- **Área Administrativa** (protegida por contraseña): gestión de empleados y directivos.
- **Área de Clientes**: registro y gestión de clientes de la organización.

Cada área permite **agregar, listar, buscar, modificar y eliminar** registros.

---

## Conceptos de POO aplicados

- **Herencia**: `empleado` y `directivo` heredan de la clase padre `persona`.
- **Encapsulamiento**: atributos privados con métodos `get` y `set`.
- **Abstracción**: cada clase tiene métodos propios con responsabilidades definidas.
- **Instanciación de objetos**: cada registro crea un objeto de su clase correspondiente.

---

## Estructura del proyecto

```
sistema-gestion-empresa-poo/
│
├── README.md
├── main.py              # Lógica principal y menús de navegación
└── MODELO/
    ├── Log_persona.py   # Clase padre: Persona
    ├── Log_empleado.py  # Clase hija: Empleado (hereda de Persona)
    ├── Log_directivo.py # Clase hija: Directivo (hereda de Empleado)
    ├── Log_cliente.py   # Clase: Cliente
    └── Log_empresa.py   # Clase contenedora: Empresa
```

---

## Funcionalidades

### Empleados
- Registrar nombre, edad y sueldo bruto
- Cálculo automático de **salario neto** (descuento del 4% salud + 4% pensión)
- Listar, buscar, modificar y eliminar

### Directivos
- Mismas funcionalidades que empleados
- Campo adicional: **nivel de categoría** (Alto / Medio / Bajo)

### Clientes
- Registrar nombre, edad, empresa de contacto y teléfono
- Listar, buscar, modificar y eliminar

---

## Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/sistema-gestion-empresa-poo.git
   ```

2. Entra a la carpeta:
   ```bash
   cd sistema-gestion-empresa-poo
   ```

3. Ejecuta el programa:
   ```bash
   python main.py
   ```

>  Requiere Python 3.x. No necesita librerías externas.  
>  Diseñado para ejecutarse en consola de Windows (`os.system("cls")` y `"pause"`).

---

## Contexto académico

Proyecto desarrollado para el **Parcial del 3er corte** de la materia de Programación Orientada a Objetos. El objetivo fue aplicar los pilares de POO en un sistema funcional de consola.

---

## 👤 Autor

**Alejandro Cruz Castañeda**  
Estudiante de Ingenieria de sistemas — MInuto de Dios

