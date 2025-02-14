import random
import json

class Bot:

    def __init__(self, alpha = 0.1, gamma = 0.9, epsilon = 0.1):

        self.q_table = {} # Diccionario para almacenar valores Q.
        self.alpha = alpha # Tasa de aprendizaje.
        self.gamma = gamma # Factor de descuento.
        self.epsilon = epsilon # Probabilidad de explorar.
        self.epsilon_decay = 0.995 # Reducción progresiva de epsilon.
        self.estado_anterior = None
        self.accion_anterior = None
        self.cargar_q_table()

    # Convierte el tablero en una representación única para usar como clave.
    def obtener_estado(self, tablero):
        return tuple(tablero)

    # Guarda la tabla Q en un archivo JSON, serealizando las claves.
    def guardar_q_table(self):

        with open("q_table.json", "w") as f:
            json.dump({str(k): v for k, v in self.q_table.items()}, f)

    # Carga la tabla Q desde un archivo JSON, deserializando las claves.
    def cargar_q_table(self):

        try:
            with open("q_table.json", "r") as f:
                data = json.load(f)
                self.q_table = {eval(k): v for k, v in data.items()}
            
        except (FileNotFoundError, json.JSONDecodeError):
            self.q_table = {}
    
    # Selecciona una acción usando la política epsilon-greedy.
    """def elegir_accion(self, estado, movimientos_validos):
        if random.random() < self.epsilon:
            return random.choice(movimientos_validos) # Exploración: elige una acción aleatoria.
        
        else:
            return max(
                movimientos_validos,
                # Explotación: elige la mejor acción según la tabla Q.
                key = lambda accion: self.q_table.get((estado, accion), 0) 
            )
       """ 
    # Actualiza los valores Q usando la ecuación de Bellman.
    def actualizar_q(self, estado_anterior, accion_anterior, recompensa, estado_actual):

        estado_accion_anterior = (estado_anterior, accion_anterior)
        valor_actual = self.q_table.get(estado_accion_anterior, 0)

        estado_actual_q = [self.q_table.get((estado_actual, a), 0)
                           for a in range(9) if (estado_actual, a) in self.q_table]
        
        mejor_q = max(estado_actual_q) if estado_actual_q else 0

        nuevo_valor_q = valor_actual + self.alpha * (recompensa + self.gamma * mejor_q - valor_actual)

        if nuevo_valor_q != valor_actual:
            self.q_table[estado_accion_anterior] = nuevo_valor_q
            self.guardar_q_table()

        self.epsilon = max(0.01, self.epsilon * self.epsilon_decay)

    # Realiza un movimiento basado en Q-learning.
    def hacer_movimiento(self, tablero):
        estado = self.obtener_estado(tablero)
        movimientos_validos = [i for i, celda in enumerate(tablero) if celda == ' ']
        
        if not movimientos_validos:
            return None
        
        elif random.uniform(0, 1) < self.epsilon:
            return random.choice(movimientos_validos) # Exploración
        
        else:
            q_val = {a: self.q_table.get((estado, a), 0) for a in movimientos_validos}
        
            return max(q_val, key = q_val.get)