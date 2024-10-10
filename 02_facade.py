# Subsistemas complejos que representan diferentes fases del proceso de IA

class PreprocesadorDeDatos:
    def limpiar_datos(self):
        print("Limpieza de datos completada")

    def escalar_datos(self):
        print("Escalado de datos completado")

class EntrenamientoDeModelo:
    def entrenar_modelo(self):
        print("Modelo entrenado con éxito")

    def ajustar_parametros(self):
        print("Parámetros del modelo ajustados")

class EvaluacionDeModelo:
    def evaluar_modelo(self):
        print("Evaluación del modelo completada")
        
    def generar_reporte(self):
        print("Reporte de evaluación generado")


# Facade para simplificar la interacción con el sistema

class ProcesoIAFacade:
    def __init__(self):
        self.preprocesador = PreprocesadorDeDatos()
        self.entrenamiento = EntrenamientoDeModelo()
        self.evaluacion = EvaluacionDeModelo()

    def ejecutar_proceso_completo(self):
        # El Facade llama a los métodos en el orden correcto
        print("Iniciando el proceso completo de IA...\n")
        self.preprocesador.limpiar_datos()
        self.preprocesador.escalar_datos()
        self.entrenamiento.ajustar_parametros()
        self.entrenamiento.entrenar_modelo()
        self.evaluacion.evaluar_modelo()
        self.evaluacion.generar_reporte()
        print("\nProceso completo de IA finalizado.")

# Prueba del Facade
if __name__ == '__main__':
    # En lugar de interactuar con cada subsistema individualmente, usamos el Facade
    proceso_ia = ProcesoIAFacade()
    proceso_ia.ejecutar_proceso_completo()

#NOTA > Las variables están en español, pero es una buena práctica escribirlas en inglés.