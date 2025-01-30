# bit8tools

Biblioteca Python moderna para crear interfaces CLI elegantes con colores, validación de entrada y componentes estilizados, inspirada en la era de los 8 bits 🎮✨

## 🚀 Características

### Input
Clase para manejo de entrada de datos con validación:
- `number()`: Entrada y validación de números
- `text()`: Entrada de texto
- `date()`: Entrada y validación de fechas
- `options()`: Selección entre opciones predefinidas
- `email()`: Entrada y validación de correos electrónicos
- `password()`: Entrada segura de contraseñas

### Output
Clase para mostrar información formateada:
- `print()`: Impresión con colores
- `tabulate()`: Muestra datos en formato tabla
- `title()`: Muestra títulos estilizados

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
nombre = Input.text("Ingrese su nombre:")
edad = Input.number("Ingrese su edad:", min_value=0, max_value=120)
correo = Input.email("Ingrese su correo:")

# Salida formateada
output = Output()
output.title("Información del Usuario")

# Mostrar datos en tabla
datos = [
    ["Campo", "Valor"],
    ["Nombre", nombre],
    ["Edad", edad],
    ["Correo", correo]
]
output.tabulate(datos)
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
