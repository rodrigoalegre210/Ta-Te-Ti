class Juego: # Definimos la clase Juego para manejar la lógica del Ta-Te-Ti

    # Función que inicializa el tablero vació como una lista con 9 espacios en blanco.
    def __init__(self):
        self.tablero = [' ' for _ in range(9)]

    # Función para hacer un movimiento si es válido.
    def hacer_movimiento(self, posicion, jugador):

        if self.es_movimiento_valido(posicion):
            self.tablero[posicion] = jugador

    # Función para comprobar si el movimiento es válido.
    def es_movimiento_valido(self, posicion):

        return self.tablero[posicion] == ' ' # Es válido si la posición está vacía (' ')
    
    # Función para comprobar si hay un ganador.
    def comprobar_ganador(self):

        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8] # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8] # Columnas
            [0, 4, 8], [2, 4, 6] # Diagonales
        ]

        # Recorremos cada combinación posible para ver si hay tres posiciones del mismo jugador en línea.
        for combinacion in combinaciones_ganadoras:
            a, b, c = combinacion # Índices de la combinación.

            # Comprobamos si las tres celdas tienen el mismo símbolo y no están vacías.
            if self.tablero[a] == self.tablero[b] == self.tablero[c] and self.tablero[a] != ' ':
                return self.tablero # Retornamos el símbolo del jugador ganador ('X' o 'O').
            
        return None # Retornamos None si no hay ganador.
    
    # Función para comprobar si el tablero está lleno sin ganador.
    def comprobar_empate(self):

        return ' ' not in self.tablero # Si no hay espacios vacíos es un empate.