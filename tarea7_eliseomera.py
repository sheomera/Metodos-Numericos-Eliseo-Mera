import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def f(x):
    return 1/(np.sqrt(x**2+16))

def trapecio(a, b, n):
    h = (b - a)/n
    x = np.linspace(a+h, b-h, n-1, endpoint=True)
    return (h/2)*(f(a) + 2*sum(f(x)) + f(b)) , h

integracion = integrate.quad(lambda x: f(x), 0, 4)

trapecio_array = np.array([trapecio(0, 4, i+1) for i in range(100)])
error = integracion[0] - trapecio_array[:,0]

plt.plot(trapecio_array[:,1], error)
plt.xlabel('h')
plt.ylabel('error')
plt.show()

# Nota 5.0
# Faltó comparar con el método de Simpson
# Se pedía comparar con la solución exacta. 
# En cambio se comparó con una aproximación
# numérica obtenida con scipy.
