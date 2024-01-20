from abc import ABC, abstractmethod


class Serviceable(ABC):
    """Serviceable class was created as an interface for all classes"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass
