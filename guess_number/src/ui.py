"""Интерфейс пользователя."""


class UI:
    """Абстракция над вводом/выводом.

    Инкапсулирует ввод и вывод, чтобы:
    1. Не засорять игровую логику вызовами print/input.
    2. Позволить подменять UI в тестах (Mock) и демонстрациях (FakeUI).
    """

    def show_message(self, message: str) -> None:
        """Показать сообщение пользователю."""
        print(message)

    def get_input(self, prompt: str) -> str:
        """Получить ввод от пользователя."""
        return input(prompt)