# config.py
# Конфигурация парсера Wildberries

# === Задержки между запросами (секунды) ===
DELAY_MIN = 5.0
DELAY_MAX = 10.0

# === Настройки парсинга ===
MAX_PAGES = 5
PRODUCTS_PER_PAGE = 100

# === Настройки сохранения ===
OUTPUT_DIR = "output"
DEFAULT_FILENAME = "wb_products_{timestamp}.xlsx"

# === Таймауты ===
REQUEST_TIMEOUT = 30

SECRET_KEY = "YarMasterTOP1"