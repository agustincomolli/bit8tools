"""
Módulo que contiene las funciones para imprimir texto con colores.

Contenido
---------
- Clase Output: contiene las funciones para imprimir texto con colores.
"""
import locale
import os
import time
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

    @staticmethod
    def clear() -> None:
        """Limpia la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_console_size() -> tuple[int, int]:
        """Obtiene el tamaño de la consola.

        Returns:
            tuple[int, int]: Tamaño de la consola.
        """
        return os.get_terminal_size()

    @staticmethod
    def press_enter_to_continue() -> None:
        """Pide al usuario que presione Enter para continuar."""
        input(
            f"Presione {Colors.colorize('ENTER', Colors.YELLOW)} para continuar...")

    @staticmethod
    def show_error(message: str) -> None:
        """Muestra un mensaje de error.

        Args:
            message (str): Mensaje de error.
        """
        Output.print(message, Colors.RED)

    @staticmethod
    def show_warning(message: str) -> bool:
        """Muestra un mensaje de advertencia.

        Args:
            message (str): Mensaje de advertencia.

        Returns:
            bool: True si el usuario responde afirmativamente, False en caso contrario.
        """
        while True:
            response = input(f"{Colors.colorize(message, Colors.YELLOW)}\n" +
                             "¿Desea continuar? (s/n) ").lower()
            if response in ("s", "y"):
                return True
            return False

    @staticmethod
    def confirm(message: str) -> bool:
        """Muestra un mensaje de confirmación al usuario y solicita una respuesta 
        afirmativa o negativa.

        Args:
            message (str): Mensaje de confirmación a mostrar.

        Returns:    
            bool: True si el usuario responde afirmativamente, False en caso contrario.

        """
        while True:
            response = input(f"{message} (s/n) ").lower()
            if response in ("s", "y"):
                return True
            return False

    @staticmethod
    def typewriter_effect(text: str) -> None:
        """Imprime los caracteres de la cadena de texto uno por uno en un intervalo de 
        tiempo determinado para simular el efecto de que se está escribiendo en tiempo 
        real.

        Args:
            text (str): La cadena de texto que se quiere imprimir con efecto de tipeo.
        """
        # Itera a través de cada carácter en la cadena de texto
        for char in text:
            # Imprime el carácter sin un salto de línea al final, y hace flush del
            # flujo de salida inmediatamente
            print(char, end='', flush=True)
            # Espera un breve intervalo de tiempo antes de imprimir el siguiente carácter
            time.sleep(0.05)
        # Imprime un salto de línea al final para separar esta salida de la próxima en la consola
        print("\n")

    @staticmethod
    def set_locale(region: str) -> None:
        """Establece la localidad regional de la consola.

        Args:
            region (str): Localidad regional a establecer.
        """
        locale.setlocale(locale.LC_ALL, region)

    @staticmethod
    def format_int(value: int) -> str:
        """Formatea un número entero con separadores de miles y decimales.

        Args:
            value (int): Número entero a formatear.

        Returns:
            str: Número entero formateado con separadores de miles y decimales.
        """
        return locale.format_string("%d", value, grouping=True)

    @staticmethod
    def format_float(value: float) -> str:
        """Formatea un número decimal con separadores de miles y decimales.

        Args:
            value (float): Número decimal a formatear.

        Returns:
            str: Número decimal formateado con separadores de miles y decimales.
        """
        return locale.format_string("%.2f", value, grouping=True)

    @staticmethod
    def format_currency(value: float) -> str:
        """Formatea un número como una cantidad de dinero con separadores de miles y decimales.

        Args:
            value (float): Número a formatear como una cantidad de dinero.

        Returns:
            str: Número formateado como una cantidad de dinero con separadores de miles y decimales.
        """
        # locale.setlocale(locale.LC_ALL, locale.getlocale()[0])
        return locale.currency(value, grouping=True)

    @staticmethod
    def format_percentage(value: float) -> str:
        """Formatea un número como un porcentaje con separadores de miles y decimales.

        Args:
            value (float): Número a formatear como un porcentaje.

        Returns:
            str: Número formateado como un porcentaje con separadores de miles y decimales.
        """
        return locale.format_string("%.2f%%", value, grouping=True)

    @staticmethod
    def format_date(date: str) -> str:
        """Formatea una fecha en el formato AAAA-MM-DD.

        Args:
            date (str): Fecha a formatear en el formato AAAA-MM-DD.

        Returns:
            str: Fecha formateada en el formato del locale configurado en la computadora.
        """
        return locale.format_string("%Y-%m-%d", date, grouping=True) + "\n"
