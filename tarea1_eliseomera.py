#%%

import numpy as np
import matplotlib.pyplot as plt
import math

# valores de x de 0 a 10
x = np.linspace(0, 10, 200)

# número máximo de términos de la serie
N = 10  

# inicializamos con ceros
taylor_sum = np.zeros_like(x)

# vamos sumando los términos de la serie de Taylor de xsin(x)
for n in range(N+1):
    term = ((-1)**n) * (x**(2*n+2)) / float(math.factorial(2*n+1))
    taylor_sum += term

# graficamos
plt.plot(x, x*np.sin(x), label="xsin(x)", color="black")
plt.plot(x, taylor_sum, label=f"Serie de Taylor hasta n={N}", linestyle="--")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Aproximación de xsin(x) con serie de Taylor")
plt.grid(True)
plt.show()

# %%
# Nota: 7.0