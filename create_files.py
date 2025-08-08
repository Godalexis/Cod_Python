class TxtRepository:
    def __init__(self, archivo: str = "data.txt"):
        self.archivo = archivo 

    def  save_data (self, data: dict) -> bool:
        try:
            linea = "#".join([f"{k}:{v}" for k, v in data.items()])
            with open(self.archivo, "a") as archivo:
                archivo.write(linea + "\n")
            return True
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            return False   
        
    def busqueda_por_concepto(self, concepto: str) -> str:
        with open(self.archivo, "r") as archivo:
            for linea in archivo:
                if f"concepto:{concepto}" in linea:
                    return linea.strip()
        return "No se encontró el concepto."
    
repo = TxtRepository()

datos = {
    "nombre": "Juan",
    "edad": 28,
    "ciudad": "Jujuy"
    }

exito = repo.save_data(datos)
if exito:
    print("Datos guardados correctamente.")
else:
    print("No se pudieron guardar los datos.")

resultado = repo.busqueda_por_concepto("Gaseosa")
print(resultado)
