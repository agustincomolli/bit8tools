"""
Ejemplo de uso de la clase Input en el módulo bit8tools.

Para ejecutar el ejemplo, ejecutar python -m examples.demo.
"""
from src.bit8tools import Input, Output, Colors


def main() -> None:
    """ Función principal del módulo. """
    name = Input.text("Ingresa tu nombre: ", Colors.GREEN, Colors.BLUE)
    Output.print(name, Colors.WHITE)

    age = Input.int_number("Ingresa tu edad: ",
                           Colors.GREEN, Colors.BLUE, 1, 99)
    Output.print(age, Colors.WHITE)

    weight = Input.float_number(
        "Ingresa tu peso: ", Colors.GREEN, Colors.BLUE, 50, 150)
    Output.print(weight, Colors.WHITE)

    next_step = Input.yes_no(
        "¿Deseas continuar? (si/no): ", Colors.GREEN, Colors.BLUE)
    Output.print(next_step, Colors.WHITE)

    Output.press_enter_to_continue()

    Output.show_warning("Esto es un mensaje de advertencia.")

    Output.press_enter_to_continue()

    Output.show_error("Esto es un mensaje de error.")

    Output.press_enter_to_continue()

    Output.confirm("Esto es un mensaje de confirmación.")

    Output.press_enter_to_continue()

    Output.clear()
    Output.print("Esto es un mensaje de limpieza.", Colors.RED)

    Output.print(
        f"Hola {name}, tienes {age} años y pesas {weight} kg.", Colors.WHITE)

    Output.set_locale("es_AR")
    Output.print(f"Mi sueldo es de {Output.format_currency(367000)}",
                 Colors.GREEN)


if __name__ == "__main__":
    main()
