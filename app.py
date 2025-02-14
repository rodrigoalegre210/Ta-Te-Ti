from flask import Flask, render_template, request, jsonify
from logica import Juego
from modelo import Bot

app = Flask(__name__, template_folder = 'templates')

# Instancias del juego y del bot.
juego = Juego()
bot = Bot()
bot.cargar_q_table() # Cargamos la tabla Q al iniciar.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jugar', methods = ['POST'])
def jugar():
    datos = request.get_json()
    movimiento_usuario = int(datos.get('movimiento')) # Movimiento del usuario.

    # Verificamos si el movimiento es válido.
    if not juego.es_movimiento_valido(movimiento_usuario):
        return jsonify({'error': 'Movimiento inválido'}), 400
    
    # Movimiento del jugador.
    juego.hacer_movimiento(movimiento_usuario, 'X')

    # Verificamos si el jugador ganó.
    ganador = juego.comprobar_ganador()

    if ganador:
        if bot.estado_anterior is not None and bot.accion_anterior is not None:
            bot.actualizar_q(bot.estado_anterior, bot.accion_anterior, -1, bot.obtener_estado(juego.tablero))

        bot.guardar_q_table()

        return jsonify({
            'movimiento_bot': None,
            'estado_juego': juego.tablero,
            'ganador': ganador
        })
    
    # Movimiento del bot.
    estado_anterior = bot.obtener_estado(juego.tablero)
    movimientos_validos = [i for i, celda in enumerate(juego.tablero) if celda == ' ']

    if not movimientos_validos:
        bot.actualizar_q(bot.estado_anterior, bot.accion_anterior, 0, bot.obtener_estado(juego.tablero))
        bot.guardar_q_table()
        return jsonify({'movimiento_bot': None,
                        'estado_juego': juego.tablero,
                        'ganador': 'empate'})
    
    movimiento_bot = bot.hacer_movimiento(juego.tablero)
    juego.hacer_movimiento(movimiento_bot, 'O')

    bot.estado_anterior = estado_anterior
    bot.accion_anterior = movimiento_bot

    # Verificamos si el bot ganó.
    ganador = juego.comprobar_ganador()

    if ganador:
        bot.actualizar_q(bot.estado_anterior, bot.accion_anterior, 1, bot.obtener_estado(juego.tablero)) # Recompensar al bot.
        bot.guardar_q_table() # Guardamos la tabla Q.
        return jsonify({
            'movimiento_bot': movimiento_bot,
            'estado_juego': juego.tablero,
            'ganador': ganador
        })

    # Verificamos empate.
    if juego.comprobar_empate():
        bot.actualizar_q(0, bot.obtener_estado(juego.tablero)) # Recompensa neutral.
        bot.guardar_q_table() # Guardar tabla Q.
        return jsonify({
            'movimiento_bot': movimiento_bot,
            'estado_juego': juego.tablero,
            'ganador': ganador
        })
    
    # Actualizar Q para estado intermedio.
    bot.actualizar_q(bot.estado_anterior, bot.accion_anterior, 0, bot.obtener_estado(juego.tablero))

    return jsonify({
        'movimiento_bot': movimiento_bot,
        'estado_juego': juego.tablero,
        'ganador': None
    })

@app.route('/reiniciar', methods = ['POST'])
def reiniciar():
    global juego
    juego = Juego()
    bot.estado_anterior = None
    bot.accion_anterior = None
    return jsonify({'mensaje': 'Juego reiniciado'})

if __name__ == "__main__":
    app.run(debug = True)