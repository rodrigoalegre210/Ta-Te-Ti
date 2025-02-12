class Juego:

    def __init__(self):

        self.tablero = [' ' for _ in range(9)]

    def hacer_movimiento(self, posicion, jugador):

        if self.es_movimiento_valido(posicion):
            self.tablero[posicion] = jugador

    def es_movimiento_valido(self, posicion):

        return self.tablero[posicion] == ' '
    
    def comprobar_ganador(self):

        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]             # Diagonales
        ]

        for combinacion in combinaciones_ganadoras:
            a, b, c = combinacion
            if self.tablero[a] == self.tablero[b] == self.tablero[c] and self.tablero[a] != ' ':
                return self.tablero[a]
            
        return None
    
    def comprobar_empate(self):
        return ' ' not in self.tablero