def add(a: float, b: float) -> float:
    """Сложение: a + b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание: a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение: a * b."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Деление: a / b.

    Исключение ZeroDivisionError: если b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def modulo(a: float, b: float) -> float:
    """
    Остаток от деления: a % b.

    Исключение ZeroDivisionError: если b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("Остаток от деления на ноль невозможен")
    return a % b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
}


def calculate(a: float, b: float, operator: str) -> float:
    """
    Универсальная точка входа для калькулятора.
    Принимает два числа и символ операции, возвращает результат.

    Исключение ValueError: если оператор не поддерживается.
    Исключение ZeroDivisionError: если деление на ноль.
    """
    if operator not in OPERATIONS:
        raise ValueError(f"Неподдерживаемая операция: {operator}")
    return OPERATIONS[operator](a, b)