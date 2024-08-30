from Clase_creadora import DeportistaCreator
from Productos_concretos import Futbolista, Tenista, Basquetbolista, Voleybolista
from Producto import IDeportista

# Creadores concretos
class FutbolistaCreator(DeportistaCreator):
    def crear_deportista(self) -> IDeportista:
        return Futbolista()

class TenistaCreator(DeportistaCreator):
    def crear_deportista(self) -> IDeportista:
        return Tenista()

class BasquetbolistaCreator(DeportistaCreator):
    def crear_deportista(self) -> IDeportista:
        return Basquetbolista()

class VoleybolistaCreator(DeportistaCreator):
    def crear_deportista(self) -> IDeportista:
        return Voleybolista()