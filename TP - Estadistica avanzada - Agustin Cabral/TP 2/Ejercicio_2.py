# Ejercicio 1
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
fosfolipidos = np.random.normal(loc=0.38, scale=0.05, size=30)
plt.hist(fosfolipidos, bins=20, color="lightblue")
plt.title("Fosfolipidos en Aceite de Girasol")
plt.xlabel("g/100g")
plt.show()

# Ejercicio 2
media = np.mean(fosfolipidos)
n = len(fosfolipidos)
s = np.std(fosfolipidos, ddof=1)
from scipy.stats import t
alpha = 0.05
t_crit = t.ppf(1 - alpha/2, df=n-1)
error = t_crit * s / np.sqrt(n)
IC95 = [media - error, media + error]
print('IC 95%:', IC95)

# Ejercicio 3
alpha = 0.01
t_crit = t.ppf(1 - alpha/2, df=n-1)
error = t_crit * s / np.sqrt(n)
IC99 = [media - error, media + error]
print('IC 99%:', IC99)

# Ejercicio 4
amplitud = IC95[1] - IC95[0]
amplitud_deseada = amplitud / 2
t_crit_100 = t.ppf(1 - 0.05/2, df=100)
n_nuevo = (t_crit_100 * s / (amplitud_deseada/2))**2
print('Nuevo tamaño muestral:', np.ceil(n_nuevo))

# Ejercicio 5
inferiores = fosfolipidos < 0.35
p_hat = np.mean(inferiores)
se = np.sqrt(p_hat * (1 - p_hat) / n)
from scipy.stats import norm
z_crit = norm.ppf(0.975)
IC_prop = [p_hat - z_crit * se, p_hat + z_crit * se]
print('IC 95% para proporcion:', IC_prop)

# Ejercicio 6
# - Muestra aleatoria y representativa.
# - Observaciones independientes.
# - Normalidad (o aplicacion del TCL para muestras grandes).

# Ejercicio 7
# Se estimaron:
# - La media poblacional de concentracion de fosfolipidos.
# - La proporcion poblacional de aliquotas con calidad inferior.
# Conclusion: Las inferencias aplican a la poblacion de aliquotas de aceite crudo de girasol. 