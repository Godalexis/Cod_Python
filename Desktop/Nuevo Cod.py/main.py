from ingreso import pedir_datos_ingreso, Ingreso

class App:
    def __init__(self):
        self.ingresos: list[Ingreso] = []

    def execute(self):
        while True:
            print("\nMENÚ PRINCIPAL")
            print("1. Crear ingreso")
            print("2. Crear egreso")
            print("3. Salir")

            opcion = input("Seleccioná una opción: ")

            if opcion == "1":
                self.crear_ingreso()
            elif opcion == "2":
                self.crear_egreso()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intentá de nuevo.")

    def crear_ingreso(self):
        ingreso = pedir_datos_ingreso()
        self.ingresos.append(ingreso)
        print("\nIngreso registrado correctamente:")
        print(f"Concepto: {ingreso.concepto}")
        print(f"Monto: {ingreso.monto}")
        print(f"Frecuencia: {ingreso.frecuencia}")

    def crear_egreso(self):
        print(">> Función para crear un egreso")