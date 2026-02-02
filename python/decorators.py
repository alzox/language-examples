"""
Decorators are mainly used as a way to extend functionality, specifically found in frameworks like flask or fastapi for things like registering routes and such.
"""

from typing import Callable

def example_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print("Decorator extending functionality")
        return func(*args, **kwargs)
    return wrapper

@example_decorator
def some_func():
    return 1
