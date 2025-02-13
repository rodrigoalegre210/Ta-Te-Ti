<h1 align = "center"> Ta-Te-Ti con Q-learning</h1>

> **Versión 1.1** - Última actualización: 13/02/2025

---

## Descripción del Proyecto.

Este proyecto consta del juego **Ta-Te-Ti** con una **API en Flask** y un **bot basado en Q-learning**
que mejora su desempeño con cada partida jugada.

### Funcionalidades principales:
* **Interfaz web** con html, css y JavaScript para jugar contra el bot.
* **API en Flask** para gestionar la lógica del juego.
* **Bot entrenado con Q-learing**, que aprende de sus partidas y ajusta su estrategia.
* **Persistencia de aprendizaje**, almacenando la tabla Q en un archivo JSON.

> [!TIP]
> Hay que jugar varias veces contra el bot para ver cómo mejora su estrategia con el tiempo.

---

## Tecnologías usadas.

| Tecnología | Descripción |
|------------|-------------|
| **Python** | Lenguaje principal del proyecto |
| **Flas** | Framework para la API REST |
| **JavaScript** | Manejo de eventos y comunicación con la API |
| **HTML y CSS** | Estructura y estilos de la interfaz gráfica |
| **Q-learning** | Algoritmo de aprendizaje por refuerzo para el bot |
| **JSON** | Almacenamiento de la tabla Q |

---

## Explicación del modelo de aprendizaje (Q-learning).

El bot implementa **Q-learning**, un algoritmo de **aprendizaje por refuerzo** basado en la
ecuación de Bellman. Se representa el estado del juego como una cadena de caracteres y se usa
una tabla **Q** para almacenar los valores de recompensa de cada acción posible.

### Características principales del modelo:
- **Exploración vs Explotación**: El bot usa una estrategia **epsilon-greedy**, en donde elige 
acciones aleatorias con probabilidad *ε* y elige la mejor acción conocida con probabilidad
*(1 - ε)*.
- **Actualización de valores Q**: Se usa la fórmula:
  
  $$ Q(s,a) = Q(s,a) + \alpha (r + \gamma \max Q(s', a') - Q(s,a)) $$

    - **Q(s,a)** es el valor actual del estado *s* y acción *a*
    - *α* es la tasa de aprendizaje.
    - *γ* es el factor de descuento.
    - *r* es la recompensa.
    - *s'* es el nuevo estado después de tomar la ación *a*.

- **Recompensas**:

    - 🏆 **+1** si el bot gana.
    - ❌ **-1** si el bot pierde.
    - ⚖️ **0** en caso de empate o estado intermedio.

> [!IMPORTANT]
> Cuanto más juega el bot, más precisa se vuelve su estrategia, aprendiendo de sus errores.

---

## ¿Cómo se juega?

1. El juego empieza con el turno del usuario (símbolo **X**).
2. Hacer clic en una celda para hacer el movimiento.
3. El bot (símbolo **O**) responderá automáticamente con su jugada.
4. Seguir jugando hasta que haya un ganador o un empate entre ambos.
5. Podes reiniciar el juego haciendo clic en "Jugar otra vez".

> [!TIP]
> Intentá jugar varias veces contra el bot para ver cómo cambia su estrategia.

*Hay que tener en cuenta que el bot necesitaría muchas partidas para aprender a jugar mejor.*

---

<h3 align="center">🚀 Proyecto con IA N°1 🚀</h3>