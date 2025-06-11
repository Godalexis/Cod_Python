class Ingreso:
    def __init__(self, concepto: str, monto: float, frecuencia: str) -> None:
        self.guardar_nombre(concepto)
        self.guardar_monto(monto)
        self.guardar_frecuencia(frecuencia)

    def guardar_nombre(self, nuevo_concepto: str) -> None:
        if nuevo_concepto.strip():
            self.concepto: str = nuevo_concepto.strip()
        else:
            raise ValueError("El concepto debe ser un texto no vacío.")

    def guardar_monto(self, nuevo_monto: float) -> None:
        if nuevo_monto >= 0:
            self.monto: float = nuevo_monto
        else:
            raise ValueError("El monto debe ser un número positivo o cero.")

    def guardar_frecuencia(self, nueva_frecuencia: str) -> None:
        frecuencias_validas: list[str] = ["anual", "mensual", "quincenal", "semanal", "diario", "indefinido"]
        if nueva_frecuencia.lower() in frecuencias_validas:
            self.frecuencia: str = nueva_frecuencia.lower()
        else:
            raise ValueError(f"Frecuencia inválida. Opciones válidas: {frecuencias_validas}")


def pedir_datos_ingreso() -> Ingreso:
    while True:
        try:
            concepto: str = input("Ingrese el concepto del ingreso: ")
            monto_input: str = input("Ingrese el monto del ingreso: ")
            monto: float = float(monto_input)
            frecuencia: str = input("Ingrese la frecuencia (anual, mensual, quincenal, semanal, diario, indefinido): ")

            ingreso: Ingreso = Ingreso(concepto, monto, frecuencia)
            return ingreso

        except ValueError as e:
            print(f"Error: {e}")
            print("Por favor, vuelva a ingresar los datos.\n")


ingreso1: Ingreso = pedir_datos_ingreso()
print("\nDatos del ingreso registrado:")
print(f"Concepto: {ingreso1.concepto}")
print(f"Monto: {ingreso1.monto}")
print(f"Frecuencia: {ingreso1.frecuencia}")