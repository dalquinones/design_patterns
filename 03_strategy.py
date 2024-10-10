# Estrategias de optimización (cada clase representa una estrategia diferente)

class EstrategiaSGD:
    def entrenar(self, datos):
        print("Entrenando con Descenso de Gradiente Estocástico (SGD)")

class EstrategiaAdam:
    def entrenar(self, datos):
        print("Entrenando con Adam")

class EstrategiaRMSprop:
    def entrenar(self, datos):
        print("Entrenando con RMSprop")


# Contexto que usará las estrategias

class ModeloEntrenamiento:
    def __init__(self, estrategia):
        self.estrategia = estrategia  # La estrategia se inyecta al crear la instancia

    def cambiar_estrategia(self, nueva_estrategia):
        self.estrategia = nueva_estrategia  # Cambia la estrategia en tiempo de ejecución

    def entrenar_modelo(self, datos):
        self.estrategia.entrenar(datos)  # Usa la estrategia actual para entrenar

# Prueba del strategy
if __name__ == '__main__':
    datos_entrenamiento = "Datos de entrenamiento"

    # Inicialmente usamos la estrategia SGD
    modelo = ModeloEntrenamiento(EstrategiaSGD())
    modelo.entrenar_modelo(datos_entrenamiento)

    # Cambiamos a la estrategia Adam en tiempo de ejecución
    modelo.cambiar_estrategia(EstrategiaAdam())
    modelo.entrenar_modelo(datos_entrenamiento)

    # Finalmente, cambiamos a la estrategia RMSprop
    modelo.cambiar_estrategia(EstrategiaRMSprop())
    modelo.entrenar_modelo(datos_entrenamiento)
