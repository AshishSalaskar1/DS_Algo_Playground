from abc import ABC, abstractmethod

# Implementor
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool: ...

    @abstractmethod
    def enable(self) -> None: ...

    @abstractmethod
    def disable(self) -> None: ...

    @abstractmethod
    def set_volume(self, value: int) -> None: ...

class TV(Device):
    def __init__(self) -> None:
        self._on = False
        self._volume = 10

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True

    def disable(self) -> None:
        self._on = False

    def set_volume(self, value: int) -> None:
        self._volume = max(0, min(100, value))
        print(f"TV volume: {self._volume}")

# Abstraction
class Remote:
    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self) -> None:
        self.device.set_volume(20)

# Refined Abstraction
class AdvancedRemote(Remote):
    def mute(self) -> None:
        self.device.set_volume(0)

if __name__ == "__main__":
    tv = TV()
    remote = AdvancedRemote(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.mute()
