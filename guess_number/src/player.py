"""Игрок."""

from .ui import UI


class Player:
    """Игрок: имя, счётчик попыток, взаимодействие с UI.

    Атрибуты:
        _name (str): имя игрока (инкапсулировано).
        _attempts (int): количество сделанных попыток.
        _ui (UI): зависимость, инжектируется через конструктор.
    """

    def __init__(self, name: str, ui: UI):
        self._name = name
        self._attempts = 0
        self._ui = ui

    @property
    def name(self) -> str:
        return self._name

    @property
    def attempts(self) -> int:
        return self._attempts

    def make_guess(self) -> int:
        """Запросить у игрока целое число.

        Повторяет запрос при неверном вводе.
        """
        while True:
            try:
                return int(self._ui.get_input("Ваш вариант: "))
            except ValueError:
                self._ui.show_message("Введите целое число!")

    def increment_attempts(self) -> None:
        """Увеличить счётчик попыток на 1."""
        self._attempts += 1