from abc import ABC, abstractmethod

# Producto
class IDeportista(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass
