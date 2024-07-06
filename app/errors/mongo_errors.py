from functools import wraps
from pymongo import errors
from typing import Callable

def error_handler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except errors.DuplicateKeyError:
            print(f"Erro: Chave duplicada detectada ao executar {func.__name__}")
            return {"error": "Duplicate key error"}
        except errors.ExecutionTimeout as e:
            print(f"Timeout ao executar {func.__name__}: {str(e)}")
            return {"error": str(e)}
        except errors.PyMongoError as e:
            print(f"Erro no PyMongo ao executar {func.__name__}: {str(e)}")
            return {"error": str(e)}
        except Exception as e:
            print(f"Erro de lógica ao executar {func.__name__}: {str(e)}")
            return {"error": str(e)}
    return wrapper