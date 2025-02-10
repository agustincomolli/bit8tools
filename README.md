# bit8tools

Biblioteca Python moderna para crear interfaces CLI elegantes con colores, validación de entrada y componentes estilizados, inspirada en la era de los 8 bits 🎮✨

## 🚀 Características

### Input
Clase para manejo de entrada de datos con validación:
- `text()`: Entrada de texto
- `int_number()`: Entrada y validación de números enteros
- `float_number()`: Entrada y validación de números decimales
- `yes_no()`: Entrada de opciones sí/no

### Output
Clase para mostrar información formateada:
- `print()`: Impresión con colores
- `show_warning()`: Muestra mensajes de advertencia
- `show_error()`: Muestra mensajes de error
- `confirm()`: Muestra mensajes de confirmación
- `clear()`: Limpia la pantalla
- `press_enter_to_continue()`: Pausa hasta que se presione Enter
- `set_locale()`: Configura la localización
- `format_currency()`: Formatea números como moneda

### Colors
Clase base para manejo de colores en terminal:
- Códigos de color para texto
- Códigos de color para fondos
- Utilidades de formateo

## 📦 Instalación

```bash
pip install bit8tools
```

## 🎮 Ejemplo de Uso

```python
from bit8tools import Input, Output, Colors

# Entrada de datos
nombre = Input.text("Ingrese su nombre:", Colors.GREEN, Colors.BLUE)
edad = Input.int_number("Ingrese su edad:", Colors.GREEN, Colors.BLUE, 0, 120)
peso = Input.float_number("Ingrese su peso:", Colors.GREEN, Colors.BLUE, 50, 150)
continuar = Input.yes_no("¿Deseas continuar? (si/no):", Colors.GREEN, Colors.BLUE)

# Salida formateada
Output.print(nombre, Colors.WHITE)
Output.print(edad, Colors.WHITE)
Output.print(peso, Colors.WHITE)
Output.print(continuar, Colors.WHITE)

Output.show_warning("Esto es un mensaje de advertencia.")
Output.show_error("Esto es un mensaje de error.")
Output.confirm("Esto es un mensaje de confirmación.")
Output.clear()
Output.print("Esto es un mensaje de limpieza.", Colors.RED)
Output.set_locale("es_AR")
Output.print(f"Mi sueldo es de {Output.format_currency(367000)}", Colors.GREEN)
```

## 🛠️ Requisitos
- Python 3.8 o superior

## 📜 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuir
Las contribuciones son bienvenidas. Por favor, siéntete libre de:
- Reportar bugs
- Sugerir nuevas funcionalidades
- Enviar pull requests

## ✨ Próximas Funcionalidades
- Validación personalizada de entrada
- Más opciones de formato para tablas
- Barras de progreso
- Menús interactivos
