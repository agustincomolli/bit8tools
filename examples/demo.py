"""
Ejemplo de uso de la clase Input en el módulo bit8tools.

Para ejecutar el ejemplo, ejecutar python -m examples.demo.
"""
from src.bit8tools import Input, Output, Colors

def main() -> None:
    """ Función principal del módulo. """
    text = Input.text("Ingresa tu nombre: ", Colors.RED, Colors.YELLOW)
    Output.print(text, Colors.CYAN)
    text = Input.text("Ingresa tu edad: ", Colors.GREEN, Colors.BLUE)
    Output.print(text, Colors.WHITE)


if __name__ == "__main__":
    main()
