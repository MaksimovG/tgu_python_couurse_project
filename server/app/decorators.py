# decorators.py

import logging
from functools import wraps
from fastapi import HTTPException

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_execution(func):
    """Декоратор для логирования начала и конца выполнения функции"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logger.info(f"Начало выполнения функции: {func.__name__}")
        result = await func(*args, **kwargs)
        logger.info(f"Конец выполнения функции: {func.__name__}")
        return result
    return wrapper

def observe_errors(func):
    """Декоратор для отслеживания ошибок и логирования их"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Ошибка при выполнении функции {func.__name__}: {e}")
            raise HTTPException(status_code=500, detail="Произошла ошибка сервера")
    return wrapper