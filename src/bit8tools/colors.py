"""
Mòdulo que contiene las clases y funciones para darle estilo y color a la
salida de la consola.

Contenido
---------
- Clase Colors: contiene los códigos ANSI para colorear el texto en la consola.
- Clase TextStyles: contiene los códigos ANSI para darle estilo al texto en la consola.

"""


class Colors:
    """
    Clase que contiene los códigos ANSI para colorear el texto en la consola.

    Atributos:
        RED (str): Código ANSI para texto en rojo.
        GREEN (str): Código ANSI para texto en verde.
        YELLOW (str): Código ANSI para texto en amarillo.
        BLUE (str): Código ANSI para texto en azul.
        MAGENTA (str): Código ANSI para texto en magenta.
        CYAN (str): Código ANSI para texto en cian.
        WHITE (str): Código ANSI para texto en blanco.
        DEFAULT (str): Código ANSI para resetear el color del texto.
    """
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    DEFAULT = "\033[0m"

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def colorize(text: str, color: str) -> str:
        """
        Aplica un color al texto y lo resetea al final.
        Valida que el color sea uno de los predefinidos.
        """

        valid_colors = [
            Colors.RED,
            Colors.GREEN,
            Colors.YELLOW,
            Colors.BLUE,
            Colors.MAGENTA,
            Colors.CYAN,
            Colors.WHITE,
            Colors.DEFAULT
        ]

        if color not in valid_colors:
            raise ValueError(
                "Color inválido. Usa los colores predefinidos en la clase Colors.")

        return f"{color}{text}{Colors.DEFAULT}"

    @staticmethod
    def bold(text: str) -> str:
        """Aplica negrita al texto."""
        return f"{Colors.BOLD}{text}{Colors.DEFAULT}"

    @staticmethod
    def underline(text: str) -> str:
        """Aplica subrayado al texto."""
        return f"{Colors.UNDERLINE}{text}{Colors.DEFAULT}"


def main():
    """
    Ejemplo de uso de la clase Colors.

    Imprime los textos "Hello, world!" con diferentes estilos y colores.
    """

    print(Colors.colorize("Hello, world!", Colors.RED))
    print(Colors.bold("Hello, world!"))
    print(Colors.underline("Hello, world!"))
    print(Colors.colorize(Colors.underline("Hello, world!"), Colors.YELLOW))
    print(Colors.colorize(Colors.bold("Hello, world!"), Colors.BLUE))


if __name__ == "__main__":
    main()
