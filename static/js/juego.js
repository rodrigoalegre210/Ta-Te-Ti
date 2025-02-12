// Selección de elementos del DOM
const celdas = document.querySelectorAll('.celda');
const estado = document.getElementById('estado');
const botonReiniciar = document.getElementById('reiniciar');

let juegoTerminado = false; // Estado para controlar si el juego terminó

// Función para actualizar el tablero
function actualizarTablero(estadoJuego) {
    celdas.forEach((celda, indice) => {
        celda.textContent = estadoJuego[indice];
    });
}

// Función para realizar un movimiento
function realizarMovimiento(posicion) {
    if (juegoTerminado) {
        estado.textContent = 'El juego ha terminado. Reinicia para jugar de nuevo.';
        return;
    }

    fetch('/jugar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ movimiento: parseInt(posicion) }),
    })
    .then(response => {
        if (!response.ok) throw new Error(`Error en la solicitud: ${response.statusText}`);
        return response.json();
    })
    .then(datos => {
        actualizarTablero(datos.estado_juego);

        if (datos.ganador) {
            juegoTerminado = true; // Marcar el juego como terminado
            estado.textContent = datos.ganador === 'Empate' 
                ? '¡Es un empate! Reinicia para jugar de nuevo.' 
                : `¡Ganó ${datos.ganador}! Reinicia para jugar otra vez.`;
            return;
        }

        estado.textContent = `El bot movió en la posición ${datos.movimiento_bot}. Tu turno.`;
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
        estado.textContent = 'Error al procesar tu movimiento. Inténtalo de nuevo.';
    });
}

// Añadir evento de clic a las casillas
celdas.forEach(celda => {
    celda.addEventListener('click', () => {
        const posicion = celda.dataset.posicion;
        realizarMovimiento(posicion);
    });
});

// Función para reiniciar el juego
function reiniciarJuego() {
    fetch('/reiniciar', { method: 'POST' })
        .then(response => {
            if (!response.ok) throw new Error(`Error en la solicitud: ${response.statusText}`);
            return response.json();
        })
        .then(() => {
            // Limpiar el tablero y reiniciar estado
            celdas.forEach(celda => (celda.textContent = ''));
            estado.textContent = 'Tu turno';
            juegoTerminado = false; // Permitir nuevos movimientos
        })
        .catch(error => {
            console.error('Error al reiniciar el juego:', error);
            estado.textContent = 'Error al reiniciar el juego. Inténtalo de nuevo.';
        });
}

// Añadir evento al botón de reinicio
botonReiniciar.addEventListener('click', reiniciarJuego);
