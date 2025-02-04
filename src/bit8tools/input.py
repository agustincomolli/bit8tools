"""
Módulo que contiene las funciones para solicitar input al usuario con colores.

Contenido
---------
- Clase Input: contiene las funciones para solicitar input al usuario con colores.
"""
from .colors import Colors


class Input:
    """
    Clase que contiene las funciones para solicitar input al usuario con colores.
    """
    @staticmethod
    def text(prompt: str, color_prompt: str, color_input: str) -> str:
        """
        Solicita un input al usuario mostrando el mensaje en un color y la respuesta en otro color.

        Args:
            prompt (str): El mensaje a mostrar al usuario.
            color_prompt: El color en el que se mostrará el mensaje.
            color_input: El color en el que se mostrará la respuesta del usuario.

        Returns: 
            str: La respuesta del usuario.
        """
        
        # Validar el color
        if not Colors.is_valid_color(color_prompt):
            color_prompt = Colors.DEFAULT

        if not Colors.is_valid_color(color_input):
            color_input = Colors.DEFAULT

        # Coloreamos el mensaje.
        message_colored = f"{color_prompt}{prompt}{color_input}"

        # Solicitamos el input al usuario.
        user_input = input(message_colored)
        print(Colors.DEFAULT, end="")

        # Devolvemos la respuesta del usuario con el color por defecto.
        return f"{user_input}"
