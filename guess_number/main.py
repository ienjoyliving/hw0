"""Точка входа в игру."""

from src.game import Game


def main() -> None:
    Game(max_attempts=10).run()


if __name__ == "__main__":
    main()