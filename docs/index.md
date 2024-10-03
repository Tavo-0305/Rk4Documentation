# Introducción

Este proyecto aborda la resolución de una ecuación diferencial de primer orden de la forma:

\[
\frac{dy}{dt} = f(t, y),
\]

donde la función \( f(t, \mathbf{y}) \) está dada por:

\[
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
\]

con \( \mathbf{O} \) representando un operador y \( \mathbf{y}(t) \) un estado que evoluciona en el tiempo. La ecuación diferencial está sujeta a la siguiente condición inicial:

\[
y(t_0) = y_0.
\]

Es importante destacar que, en este caso, no existe una dependencia explícita temporal en la función \( f(t, \mathbf{y}) \), lo que simplifica el análisis y la integración numérica del sistema.

El objetivo principal de este proyecto es implementar métodos numéricos, como el método de Runge-Kutta de cuarto orden (RK4), para la integración y simulación de esta dinámica, aplicando operadores personalizados y estados iniciales. La función `dyn_generator` es responsable de generar la dinámica del sistema, mientras que la función `rk4` aplica el método RK4 para su evolución en el tiempo.

Puede encontrar el código de esta documentación en: https://github.com/Tavo-0305/Rk4Documentation