class ConfiguracionModelo:
    _instancia_unica = None  # Variable de clase para almacenar la instancia única

    def __new__(cls):
        if cls._instancia_unica is None:  # Si no existe una instancia
            cls._instancia_unica = super(ConfiguracionModelo, cls).__new__(cls)  # Crea una nueva instancia
            cls._instancia_unica.parametros = {}  # Inicializa un diccionario para los parámetros
        return cls._instancia_unica  # Retorna la misma instancia cada vez

    def establecer_parametro(self, clave, valor):
        self.parametros[clave] = valor  # Establece un valor para el parámetro

    def obtener_parametro(self, clave):
        return self.parametros.get(clave, None)  # Obtiene un valor del parámetro


# Prueba del Singleton
if __name__ == '__main__':
    config_entrenamiento1 = ConfiguracionModelo()
    config_entrenamiento1.establecer_parametro("tasa_aprendizaje", 0.01)
    config_entrenamiento1.establecer_parametro("batch_size", 32)

    config_entrenamiento2 = ConfiguracionModelo()
    print(config_entrenamiento2.obtener_parametro("tasa_aprendizaje"))  # 0.01
    print(config_entrenamiento2.obtener_parametro("batch_size"))         # 32

    print(f"config_entrenamiento1 es igual a config_entrenamiento2: {config_entrenamiento1 is config_entrenamiento2}")  # True

#NOTA > Las variables están en español, pero es una buena práctica escribirlas en inglés.