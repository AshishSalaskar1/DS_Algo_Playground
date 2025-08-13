# Singleton (Creational)

Ref: https://refactoring.guru/design-patterns/singleton

Overview
- Ensures a class has only one instance and provides a global access point to it.

When to use
- Exactly one shared resource across the app (e.g., config, logging, cache) and you want controlled access.

How to identify
- A class that restricts instantiation and exposes a static accessor to the instance.

Pros
- Single instance controlled access.
- Lazy initialization is possible.

Cons
- Hidden dependency/global state; harder to test.
- Can introduce tight coupling; misuse leads to anti-pattern.

Common confusions
- vs module-level singletons: In Python, a module is effectively a singleton. Prefer modules or DI where possible.

Python example (thread-safe metaclass)
```python
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:  # double-checked locking
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppConfig(metaclass=SingletonMeta):
    def __init__(self, env: str = "prod") -> None:
        self.env = env

if __name__ == "__main__":
    a = AppConfig("dev")
    b = AppConfig("stage")
    print(a is b, a.env, b.env)  # True dev dev
```

Quick glance
- Prefer dependency injection over global singletons for testability.
- In Python, modules or caches can serve similar roles with fewer drawbacks.
