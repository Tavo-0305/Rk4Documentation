# Método de Runge-Kutta de Cuarto Orden (RK4)

El método de Runge-Kutta de cuarto orden (RK4) es un método numérico ampliamente utilizado para la solución de ecuaciones diferenciales ordinarias (EDO). Es un método explícito que se caracteriza por su precisión y eficiencia en la integración de sistemas dinámicos. La ecuación general del método RK4 es la siguiente:

\[
y_{n+1} = y_{n} + \frac{1}{6}(k_{1} + 2k_{2} + 2k_{3} + k_{4}),
\]

donde los valores de \(k_1\), \(k_2\), \(k_3\) y \(k_4\) se calculan como:

\[
k_{1} = h f(t_{n}, y_{n}),
\]

\[
k_{2} = h f\left(t_{n} + \frac{h}{2}, y_{n} + \frac{k_{1}}{2}\right),
\]

\[
k_{3} = h f\left(t_{n} + \frac{h}{2}, y_{n} + \frac{k_{2}}{2}\right),
\]

\[
k_{4} = h f(t_{n} + h, y_{n} + k_{3}).
\]

Aquí:

- \( h \) es el paso de integración, que define la separación entre los puntos \( t_n \) y \( t_{n+1} \) en el tiempo.
- \( f(t, y) \) es la función que describe la dinámica del sistema, en este caso, \( f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)] \), sin dependencia explícita temporal.
- \( y_n \) es el estado del sistema en el tiempo \( t_n \), mientras que \( y_{n+1} \) es el estado en el tiempo \( t_{n+1} \).

El método RK4 estima el valor de la solución en \( t_{n+1} \) utilizando una combinación ponderada de cuatro incrementos (\( k_1, k_2, k_3, k_4 \)) evaluados en diferentes puntos dentro del intervalo \( [t_n, t_{n+1}] \).

### Descripción de los Incrementos:

- \( k_1 \): Representa la pendiente al inicio del intervalo.
- \( k_2 \) y \( k_3 \): Calculan la pendiente en puntos intermedios utilizando el valor de \( k_1 \) y \( k_2 \) para mejorar la precisión.
- \( k_4 \): Evalúa la pendiente al final del intervalo.

Finalmente, la solución se actualiza combinando estos incrementos para obtener una aproximación precisa del estado del sistema en el siguiente paso de tiempo.

Este método es utilizado debido a su balance entre precisión y eficiencia, haciéndolo adecuado para una amplia variedad de problemas en la simulación de sistemas dinámicos.