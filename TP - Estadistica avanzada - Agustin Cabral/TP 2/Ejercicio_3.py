# Ejercicio 1
import numpy as np
apio = np.array([0.58, 0.95, 0.46, 0.84, 0.59, 0.92, 0.52, 0.92, 0.52, 0.55,
          0.40, 0.51, 0.52, 0.52, 0.60, 0.70, 0.35, 0.40, 0.50, 0.41,
          0.53, 0.51, 0.66, 0.60, 0.45, 0.77, 0.39, 0.50, 0.66, 0.85])
n = len(apio)
media = np.mean(apio)
s = np.std(apio, ddof=1)
from scipy.stats import t
alpha = 0.01
t_crit = t.ppf(1 - alpha/2, df=n-1)
error = t_crit * s / np.sqrt(n)
IC99 = [media - error, media + error]
print('IC 99%:', IC99)

# Ejercicio 2
# Si el limite superior del intervalo de confianza supera los 0.50 ppm, el lote podria no ser apto para consumo. En este caso, el IC99 incluye valores mayores a 0.50, por lo tanto no se puede afirmar con un 99% de confianza que el lote sea seguro. 