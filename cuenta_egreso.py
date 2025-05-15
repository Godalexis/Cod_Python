class Egreso:
    def __init__(self, concepto: str = "", monto: float = 0, frecuencia: str = "indefinido") -> None:
        self.concepto: str = concepto
        self.monto: float = monto
        self.frecuencia: str = frecuencia

    def guardar_nombre(self, nuevo_concepto: str) -> None:     
        self.concepto = nuevo_concepto

    def guardar_monto(self, nuevo_monto: float) -> None:     
        self.monto = nuevo_monto

    def guardar_frecuencia(self, nueva_frecuencia: str) -> None:   
        frecuencias_validas: list[str] = ["anual", "mensual", "quincenal", "semanal", "diario", "indefinido"]
        if nueva_frecuencia in frecuencias_validas:
            self.frecuencia = nueva_frecuencia
        else:
            raise ValueError("Frecuencia no válida. Debe ser: anual, mensual, quincenal, semanal, diario o indefinido.")

