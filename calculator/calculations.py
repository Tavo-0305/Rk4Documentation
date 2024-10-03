"""
Proporciona funciones para simular sistemas dinámicos.

Este módulo permite al usuario realizar simulaciones numéricas de sistemas dinámicos
utilizando operadores personalizados y estados iniciales.

El módulo contiene las siguientes funciones:

- `dyn_generator(oper, state)` - Genera la dinámica del sistema utilizando el operador y estado dados.
- `rk4(func, oper, state, h)` - Aplica el método de Runge-Kutta (RK4) para la integración numérica de la evolución del sistema.
"""

import numpy as np
import matplotlib.pyplot as plt 

def dyn_generator(oper, state) -> Tuple[np.ndarray, np.ndarray]:
    """
    Produce una función encargada de generar y simular la dinámica del problema.

    Examples:
        >>> import numpy as np
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> print(oOper)
        [[0 1]
         [1 0]]
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> print(yInit)
        [[1 0]
         [0 0]]
        >>> test = dyn_generator(oOper, yInit)
        >>> print(test)
        [[0.-0.j 0.+1.j]
         [0.-1.j 0.-0.j]]

    Args:
        oper (tuple): numpy.ndarray El operador que representa la dinámica.
        state (tuple): numpy.ndarray El estado inicial de la simulación.

    Returns:
        (tuple): El resultado de la operación (-1.0j) * (oper * state - state * oper).
    """
    return (-1.0j)*(np.dot(oper,state)-np.dot(state,oper))
    
def rk4(func, oper, state, h) -> Tuple[np.ndarray, np.ndarray]:
    """
    Aplica el método de Runge-Kutta de cuarto orden (RK4) para la integración numérica de un sistema de ecuaciones diferenciales.

    Examples:
        >>> import numpy as np
        >>> times = np.linspace(0.0, 10.0, 1011)
        >>> print(times)
        [0.00000000e+00 9.90099010e-03 1.98019802e-02 ... 9.98019802e+00
         9.99009901e+00 1.00000000e+01]
        >>> h = times[1] - times[0]
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> result = rk4(dyn_generator, oOper, yInit, h)
        >>> print(result)
        [[9.99901974e-01+0.j         0.00000000e+00+0.00990034j]
         [0.00000000e+00-0.00990034j 9.80264017e-05+0.j        ]]

    Args:
        func (callable): Función que describe la dinámica del sistema. Debe aceptar `oper` y `state` como parámetros y devolver una matriz numpy.
        oper (tuple): numpy.ndarray El operador que representa la dinámica del sistema.
        state (tuple): numpy.ndarray El estado actual del sistema.
        h (float): Paso de integración.

    Returns:
        (tuple): El estado del sistema después de un paso de integración usando el método RK4.
    """
    k_1 = h * func(oper , state)
    k_2 = h * func(oper , state + (k_1)/(2))
    k_3 = h * func(oper , state + (k_2)/(2))
    k_4 = h * func(oper , state + k_3)
    return state + 1/(6) * (k_1 + 2 * k_2 + 2* k_3 + k_4)