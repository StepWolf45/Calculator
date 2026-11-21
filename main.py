"""Точка входа калькулятора."""

import tkinter as tk

from gui import CalculatorApp


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()