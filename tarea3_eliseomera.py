import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

mediciones = [2, 3, 3, 3, 0, 1, 2, 2, 0, 4, 10, 0, 2, 4, 6, 3, 2, 1, 1, 1]

def poisson(n, lamda):
    return lamda**n*np.exp(-lamda)/factorial(n)

datosenorden = []

for i in range(0, 11):
  n = 0
  for j in mediciones:
    if i == j:
      n += 1
  datosenorden.append((i, n))

media = np.mean(mediciones)
sigma = np.std(mediciones)
varianza = np.var(mediciones)

datos_array = np.array(datosenorden)
predicciones = np.array([poisson(n, media)*sum(datos_array[:,1]) for n in range(11)])

plt.bar(range(len(predicciones)), predicciones)
plt.title("Distribución de Probabilidad")
plt.show()

print(media)
print(varianza)

# 1. Compare estos resultados con la distribución de Poisson. 
# No es como una distribución de Poisson, ya que el valor de la varianza no es igual al valor de la media, y ni siquiera se acerca

# 2. Discuta en cuáles intervalos cree usted que se detectó una señal que no es contaminación.
# Yo creo que el que no es contaminación es el intervalo de 10 señales, ya que es anómalo y el ruido sigue una distribución bien definida.