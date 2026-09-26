"""Игра «Угадай число»."""

import random
from .ui import UI
from .player import Player


class Game:
    """Управляет игровым циклом «Угадай число».

    Отвечает за:
    - генерацию секретного числа;
    - создание игрока;
    - проверку попыток;
    - завершение игры.
    """

    def __init__(self, max_attempts: int = 10, ui: UI | None = None):
        self._max_attempts = max_attempts
        self._secret = 0
        self._ui = ui if ui is not None else UI()

    def run(self) -> None:
        """Запустить игровой цикл."""
        self._secret = random.randint(1, 100)
        self._ui.show_message(
            f"Я загадал число от 1 до 100. У вас {self._max_attempts} попыток."
        )
        player = Player("Игрок", self._ui)
        while player.attempts < self._max_attempts:
            guess = player.make_guess()
            player.increment_attempts()
            result = self.check_guess(guess)
            self._ui.show_message(result)
            if guess == self._secret:
                return
        self._ui.show_message(
            f"Попытки закончились. Было загадано: {self._secret}"
        )

    def check_guess(self, guess: int) -> str:
        """Вернуть сообщение-подсказку для попытки."""
        if guess < self._secret:
            return "Больше!"
        elif guess > self._secret:
            return "Меньше!"
        return "Угадали!"

    @property
    def secret(self) -> int:
        """Секретное число (только чтение; используется в тестах)."""
        return self._secret