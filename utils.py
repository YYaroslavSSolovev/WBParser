# utils.py
# Вспомогательные функции для парсера

import os
import time
import random
from datetime import datetime

from rich.console import Console
from rich.panel import Panel

from config import DELAY_MIN, DELAY_MAX, OUTPUT_DIR

# Создаём консоль для красивого вывода
console = Console()


def log(message: str, style: str = "white") -> None:
    """Логирование сообщения в консоль с цветом"""
    console.print(f"[{style}]{message}[/{style}]")


def log_success(message: str) -> None:
    """Логирование успешного действия (зелёный)"""
    console.print(f"[bold green]✓[/bold green] {message}")


def log_error(message: str) -> None:
    """Логирование ошибки (красный)"""
    console.print(f"[bold red]✗[/bold red] {message}")


def log_warning(message: str) -> None:
    """Логирование предупреждения (жёлтый)"""
    console.print(f"[bold yellow]![/bold yellow] {message}")


def log_info(message: str) -> None:
    """Логирование информации (синий)"""
    console.print(f"[bold blue]ℹ[/bold blue] {message}")


def random_delay() -> None:
    """Случайная задержка между запросами"""
    delay = random.uniform(DELAY_MIN, DELAY_MAX)
    log(f"Задержка {delay:.1f} сек...", "dim")
    time.sleep(delay)


def create_output_dir() -> str:
    """Создаёт папку для сохранения результатов"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        log_success(f"Создана папка: {OUTPUT_DIR}")
    return OUTPUT_DIR


def generate_filename(query: str) -> str:
    """Генерирует имя файла с запросом и временем"""
    # Очищаем запрос от спецсимволов
    safe_query = "".join(c for c in query if c.isalnum() or c in (' ', '-', '_'))
    safe_query = safe_query.strip().replace(' ', '_')[:30]

    # Добавляем timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"wb_{safe_query}_{timestamp}.xlsx"
    return filename


def show_banner() -> None:
    """Показывает красивый баннер при запуске"""

    logo = """
[bold cyan]
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ██╗    ██╗ ██████╗     ██████╗  █████╗ ██████╗ ███████╗███████╗ ║
║   ██║    ██║ ██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝ ║
║   ██║ █╗ ██║ ██████╔╝    ██████╔╝███████║██████╔╝███████╗█████╗   ║
║   ██║███╗██║ ██╔══██╗    ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝   ║
║   ╚███╔███╔╝ ██████╔╝    ██║     ██║  ██║██║  ██║███████║███████╗ ║
║    ╚══╝╚══╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
[/bold cyan]
[bold white]                    WILDBERRIES PARSER v1.0[/bold white]
[dim]              Парсер товаров с защитой от блокировок[/dim]
"""

    console.print(logo)
    console.print()


def show_stats(total: int, success: int, errors: int) -> None:
    """Показывает красивую статистику парсинга"""
    from rich.table import Table
    from rich import box

    table = Table(
        title="📊 Статистика парсинга",
        box=box.DOUBLE_EDGE,
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Параметр", style="cyan", justify="left")
    table.add_column("Значение", style="bold green", justify="right")

    table.add_row("Всего товаров", str(total))
    table.add_row("Успешно обработано", str(success))
    table.add_row("Ошибок", str(errors), style="bold red" if errors > 0 else "bold green")

    # Процент успеха
    success_rate = (success / total * 100) if total > 0 else 0
    table.add_row("Успешность", f"{success_rate:.1f}%")

    console.print(table)