"""
Módulo que contiene las funciones para imprimir texto con colores.

Contenido
---------
- Clase Output: contiene las funciones para imprimir texto con colores.
"""
from .colors import Colors


class Output:
    """Clase que contiene las funciones para imprimir texto con colores."""
    @staticmethod
    def print(text: object, color: str) -> None:
        """Imprime un texto con un color.

        Args:
            text (object): Texto a imprimir.
            color (str): Color a aplicar al texto.
        """
        # Validar el color
        color = Colors.validate_color(color)

        text = Colors.colorize(str(text), color)

        print(text)
