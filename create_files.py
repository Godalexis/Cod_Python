class TxtRepository:
    def __init__(self, archivo: str = "data.txt"):
        self.archivo = archivo 

    def save_data (self, data: dict) -> bool:
        try:
            linea = "#".join([f"{k}:{v}" for k, v in data.items()])
            with open(self.archivo, "a") as archivo:
                archivo.write(linea + "\n")
            return True
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            return False
        
repo = TxtRepository()

datos = {
    "nombre": "Lucas",
    "edad": 25,
    "ciudad": "Corrientes"
}

exito = repo.save_data(datos)
if exito:
    print("Datos guardados correctamente.")
else:
    print("No se pudieron guardar los datos.")
