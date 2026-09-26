"""Тесты класса Game."""

from src.game import Game


class TestGame:
    """Проверяем логику проверки попытки."""

    def test_check_guess_too_low(self):
        """Если попытка меньше секрета — «Больше!»."""
        g = Game()
        g._secret = 50
        assert g.check_guess(30) == "Больше!"

    def test_check_guess_too_high(self):
        """Если попытка больше секрета — «Меньше!»."""
        g = Game()
        g._secret = 50
        assert g.check_guess(70) == "Меньше!"

    def test_check_guess_correct(self):
        """Если попытка равна секрету — «Угадали!»."""
        g = Game()
        g._secret = 50
        assert g.check_guess(50) == "Угадали!"

    def test_secret_property(self):
        """Свойство secret возвращает целое число."""
        g = Game()
        assert isinstance(g.secret, int)