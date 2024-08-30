from abc import ABC, abstractmethod
from Producto import IDeportista

# Clase creadora
class DeportistaCreator(ABC):
    @abstractmethod
    def crear_deportista(self) -> IDeportista:
        pass

    def descripcion_deportista(self) -> str:
        deportista = self.crear_deportista()
        return f"Descripción: {deportista.descripcion()}"
