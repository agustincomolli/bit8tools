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
        color_prompt = Colors.validate_color(color_prompt)
        color_input = Colors.validate_color(color_input)

        # Colorear el mensaje.
        message_colored = f"{color_prompt}{prompt}{color_input}"

        # Solicitar el input al usuario.
        user_input = input(message_colored)
        print(Colors.DEFAULT, end="")

        # Devolver la respuesta del usuario con el color por defecto.
        return f"{user_input}"

    @staticmethod
    def int(prompt: str, color_prompt: str, color_input: str,
            min_value: int = None, max_value: int = None) -> int:
        """
        Solicita un número entero al usuario mostrando el mensaje en un color y la respuesta en 
        otro color.

        Args:
            prompt (str): El mensaje a mostrar al usuario.
            color_prompt: El color en el que se mostrará el mensaje.
            color_input: El color en el que se mostrará la respuesta del usuario.

        Returns: 
            int: La respuesta del usuario.
        """

        # Validar el color
        color_prompt = Colors.validate_color(color_prompt)
        color_input = Colors.validate_color(color_input)

        # Colorear el mensaje.
        message_colored = f"{color_prompt}{prompt}{color_input}"

        # Validar el input.
        while True:
            # Solicitar el input al usuario.
            user_input = input(message_colored)
            print(Colors.DEFAULT, end="")
            # Validar el input.
            if user_input.isdigit():
                if not min_value is None and not max_value is None:
                    if int(user_input) < min_value or int(user_input) > max_value:
                        print(f"El valor debe estar entre {
                              min_value} y {max_value}.")
                        continue
                break
            print("El valor debe ser un número entero.")

        # Devolver la respuesta del usuario con el color por defecto.
        return int(user_input)

    @staticmethod
    def float(prompt: str, color_prompt: str, color_input: str,
              min_value: int = None, max_value: int = None) -> float:
        """
        Solicita un float al usuario mostrando el mensaje en un color y la respuesta en 
        otro color.

        Args:
            prompt (str): El mensaje a mostrar al usuario.
            color_prompt: El color en el que se mostrará el mensaje.
            color_input: El color en el que se mostrará la respuesta del usuario.

        Returns: 
            float: La respuesta del usuario.
        """

        # Validar el color
        color_prompt = Colors.validate_color(color_prompt)
        color_input = Colors.validate_color(color_input)

        # Colorear el mensaje.
        message_colored = f"{color_prompt}{prompt}{color_input}"

        # Validar el input.
        while True:
            # Solicitar el input al usuario.
            user_input = input(message_colored)
            print(Colors.DEFAULT, end="")
            # Validar el input.
            if user_input.isdigit():
                if not min_value is None and not max_value is None:
                    if float(user_input) < min_value or float(user_input) > max_value:
                        print(f"El valor debe estar entre {
                              min_value} y {max_value}.")
                        continue
                break
            print("El valor debe ser un número entero.")

        # Devolver la respuesta del usuario con el color por defecto.
        return float(user_input)

    @staticmethod
    def bool(prompt: str, color_prompt: str, color_input: str) -> bool:
        """
        Solicita un booleano al usuario mostrando el mensaje en un color y la respuesta en 
        otro color.

        Args:
            prompt (str): El mensaje a mostrar al usuario.
            color_prompt: El color en el que se mostrará el mensaje.
            color_input: El color en el que se mostrará la respuesta del usuario.

        Returns: 
            bool: La respuesta del usuario.
        """

        # Validar el color
        color_prompt = Colors.validate_color(color_prompt)
        color_input = Colors.validate_color(color_input)

        # Colorear el mensaje.
        message_colored = f"{color_prompt}{prompt}{color_input}"

        while True:
            # Solicitar el input al usuario.
            user_input = input(message_colored).lower()
            print(Colors.DEFAULT, end="")

            # Validar el input.
            if user_input.lower() in ["s", "n", "y"]:
                if user_input.lower().startswith("s") or user_input.lower().startswith("y"):
                    return True
                return False
            print("Por favor ingrese 's', 'n' o 'y'.")
