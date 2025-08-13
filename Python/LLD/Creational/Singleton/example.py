import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppConfig(metaclass=SingletonMeta):
    def __init__(self, env: str = "prod") -> None:
        self.env = env

if __name__ == "__main__":
    a = AppConfig("dev")
    b = AppConfig("stage")
    print(a is b, a.env, b.env)
