import random
import json

class Bot:

    def __init__(self, alpha = 0.1, gamma = 0.9, epsilon = 0.1):

        self.q_table = {} # Diccionario para almacenar valores Q.
        self.alpha = alpha # Tasa de aprendizaje.
        self.gamma = gamma # Factor de descuento.
        self.epsilon = epsilon # Probabilidad de explorar.
        self.estado_anterior = None # Estado previo del juego.
        self.accion_anterior = None # Acción previa tomada.

    # Guarda la tabla Q en un archivo JSON, serealizando las claves.
    def guardar_q_table(self, archivo = "q_table.json"):

        q_table_serializable = {str(key): valor for key, valor in self.q_table.items()}

        with open(archivo, 'w') as f:
            json.dump(q_table_serializable, f)

    # Carga la tabla Q desde un archivo JSON, deserializando las claves.
    def cargar_q_table(self, archivo = 'q_table.json'):

        try:
            with open(archivo, 'r') as f:
                q_table_serializable = json.load(f)
                self.q_table = {eval(key): valor for key, valor in q_table_serializable.items()}
        
        except (FileNotFoundError, json.JSONDecodeError):
            # Si el archivo no existe o da error, inicializa una tabla vacía.
            self.q_table = {}

    # Convierte el tablero en una representación única para usar como clave.
    def obtener_estado(self, tablero):

        return ''.join(tablero)
    
    # Selecciona una acción usando la política epsilon-greedy.
    def elegir_accion(self, estado, movimientos_validos):
        if random.random() < self.epsilon:
            return random.choice(movimientos_validos) # Exploración: elige una acción aleatoria.
        
        else:
            return max(
                movimientos_validos,
                # Explotación: elige la mejor acción según la tabla Q.
                key = lambda accion: self.q_table.get((estado, accion), 0) 
            )
        
    # Actualiza los valores Q usando la ecuación de Bellman.
    def actualizar_q(self, recompensa, estado_actual):

        if self.estado_anterior is not None and self.accion_anterior is not None:
            estado_accion_anterior = (self.estado_anterior, self.accion_anterior)
            estado_actual_q = [
                self.q_table.get((estado_actual, a), 0)
                for a in range(9) if (estado_actual, a) in self.q_table
            ]

            # Fórmula Q-learning.
            mejor_q = max(estado_actual_q) if estado_actual_q else 0
            valor_actual = self.q_table.get(estado_accion_anterior, 0)
            self.q_table[estado_accion_anterior] = valor_actual + self.alpha * (
                recompensa + self.gamma * mejor_q - valor_actual
            )

        self.estado_anterior = estado_actual

    # Realiza un movimiento basado en Q-learning.
    def hacer_movimiento(self, tablero):
        estado = self.obtener_estado(tablero)
        movimientos_validos = [i for i, celda in enumerate(tablero) if celda == ' ']
        accion = self.elegir_accion(estado, movimientos_validos)
        self.accion_anterior = accion
        
        return accion