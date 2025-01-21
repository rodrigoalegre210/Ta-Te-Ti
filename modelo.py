import random
import json

class Bot: # # Definimos la clase Bot.

    # Función que inicializa el bot con parámetros para el algoritmo Q-learning.
    def __init__(self, alpha = 0.1, gamma = 0.9, epsilon = 0.1):

        self.q_table = {} # Diccionario para almacenar valores Q (estado - acción).
        self.alpha = alpha # Tasa de aprendizaje: Controla cuánto se actualizan los valores Q.
        self.gamma = gamma # Factor de descuento: Vaora más las recompensas a corto plazo.
        self.epsilon = epsilon # Probabilidad de explorar (seleccionar una acción aleatoria)
        self.estado_anterior = None # Estado previo del juego.
        self.accion_anterior = None # Acción previa tomada por el bot.

    # Función que guarda la tabla Q en un archivo JSON, serializando las claves.
    def guardar_q_table(self, archivo = "q_table.json"):

        # Convertimos las claves del diccionario en cadenas para poder almacenarlas en JSON.
        q_table_serializable = {str(key): value for key, value in self.q_table.items()}
        with open(archivo, "w") as f:
            json.dump(q_table_serializable, f) # Guardamos la tabla Q en el archivo.