class App:
    def execute(self):
        while True:
            print("\n MENÚ PRINCIPAL")
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
        print(">> Función para crear un ingreso")

    def crear_egreso(self):
        print(">> Función para crear un egreso")


