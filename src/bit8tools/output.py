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
    def print(text: str, color: str) -> None:
        """Imprime un texto con un color.

        Args:
            text (str): Texto a imprimir.
            color (str): Color a aplicar al texto.
        """
        # Validar el color
        if not Colors.is_valid_color(color):
            color = Colors.DEFAULT

        text = Colors.colorize(text, color)

        print(text)
