"""
Ejemplo de uso de la clase Input en el módulo bit8tools.

Para ejecutar el ejemplo, ejecutar python -m examples.demo.
"""
from src.bit8tools import Input, Output, Colors

def main() -> None:
    """ Función principal del módulo. """
    text = Input.text("Ingresa tu nombre: ", Colors.GREEN, Colors.BLUE)
    Output.print(text, Colors.WHITE)
    text = Input.int("Ingresa tu edad: ", Colors.GREEN, Colors.BLUE, 1, 99)
    Output.print(text, Colors.WHITE)
    text = Input.float("Ingresa tu peso: ", Colors.GREEN, Colors.BLUE, 50, 150)
    Output.print(text, Colors.WHITE)
    text = Input.bool("¿Deseas continuar? (si/no): ", Colors.GREEN, Colors.BLUE)
    Output.print(text, Colors.WHITE)

if __name__ == "__main__":
    main()
