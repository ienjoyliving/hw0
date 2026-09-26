# Guess Number — ООП-версия

## Описание
Текстовая игра «Угадай число», переписанная с процедурного кода на ООП.

## Установка
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск
```bash
python main.py
```

## Тесты
```bash
pytest -v
```

## Архитектура
- `Game` — управление игровым циклом.
- `Player` — состояние игрока и ввод.
- `UI` — абстракция ввода/вывода (подменяется в тестах).

## Диаграмма классов
См. `docs/diagram.md`.

## Решения
- [ADR-001: Разделение Game и UI](docs/adr_001_ui.md)

## Структура
```
guess_number/
├── src/       # исходный код
├── tests/     # тесты
├── docs/      # документация
└── main.py    # точка входа
```
