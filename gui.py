import tkinter as tk
from operations import add, sub, mul, div, mod, sin, cos, power, sqrt, floor, ceil
from memory import Memory

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expr = tk.StringVar()

        # объект памяти (m+, m-, mc, mr)
        self.mem = Memory()

        # поле ввода
        entry = tk.Entry(
            root,
            textvariable=self.expr,
            justify="right",
            font=("Arial", 16),
            bd=4,
            relief="ridge",
        )
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

        # (текст, строка, столбец)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("^", 5, 2), ("√", 5, 3),
            ("floor", 6, 0), ("ceil", 6, 1), ("%", 6, 2), ("C", 6, 3),
            ("m+", 7, 0), ("m-", 7, 1), ("mc", 7, 2), ("mr", 7, 3),
        ]

        for text, r, c in buttons:
            tk.Button(
                root,
                text=text,
                width=6,
                height=2,
                font=("Arial", 12),
                command=lambda t=text: self.on_button(t),
            ).grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    # ------------------------------------------------------------------
    # обработчики
    # ------------------------------------------------------------------
    def on_button(self, text):
        """Единая точка входа для всех кнопок."""
        if text == "C":
            self.expr.set("")
        elif text == "=":
            self.calculate()
        elif text == "m+":
            self.mem.m_plus(self._current_value())
        elif text == "m-":
            self.mem.m_minus(self._current_value())
        elif text == "mc":
            self.mem.mc()
        elif text == "mr":
            self.expr.set(str(self.mem.mr()))
        else:
            # цифры, точка, операторы, sin, cos, ^, √, floor, ceil, %
            self.expr.set(self.expr.get() + text)

    def _current_value(self):
        """Текущее число из поля ввода (0.0, если пусто/мусор)."""
        try:
            return float(self.expr.get())
        except ValueError:
            return 0.0

    def calculate(self):
        """Вычислить выражение и показать результат."""
        raw = self.expr.get().strip()
        if not raw:
            return
        try:
            # бинарные операции: a op b
            for op in ("+", "-", "*", "/", "%", "^"):
                if op in raw:
                    a_str, b_str = raw.split(op, 1)
                    a, b = float(a_str), float(b_str)
                    result = {
                        "+": add,
                        "-": sub,
                        "*": mul,
                        "/": div,
                        "%": mod,
                        "^": power,
                    }[op](a, b)
                    self.expr.set(self._fmt(result))
                    return

            # унарные операции: префикс + число
            if raw.startswith("sin"):
                self.expr.set(self._fmt(sin(float(raw[3:])))); return
            if raw.startswith("cos"):
                self.expr.set(self._fmt(cos(float(raw[3:])))); return
            if raw.startswith("√"):
                self.expr.set(self._fmt(sqrt(float(raw[1:])))); return
            if raw.startswith("floor"):
                self.expr.set(self._fmt(floor(float(raw[5:])))); return
            if raw.startswith("ceil"):
                self.expr.set(self._fmt(ceil(float(raw[4:])))); return

            # просто число — оставляем как есть (нормализованное)
            self.expr.set(self._fmt(float(raw)))

        except ZeroDivisionError:
            self.expr.set("Error: division by zero")
        except ValueError:
            self.expr.set("Error")
        except Exception:
            self.expr.set("Error")

    @staticmethod
    def _fmt(x):
        """Красивый вывод: 5.0 -> '5', 0.5 -> '0.5'."""
        if isinstance(x, float) and x.is_integer():
            return str(int(x))
        return str(x)