from Creadores_concretos import FutbolistaCreator, TenistaCreator, BasquetbolistaCreator, VoleybolistaCreator

# Programa principal o main
def client_code(creator):
    print(creator.descripcion_deportista())

if __name__ == "__main__":
    print("Creación de Futbolista:")
    client_code(FutbolistaCreator())

    print("\nCreación de Tenista:")
    client_code(TenistaCreator())

    print("\nCreación de Basquetbolista:")
    client_code(BasquetbolistaCreator())

    print("\nCreación de Voleybolista:")
    client_code(VoleybolistaCreator())
