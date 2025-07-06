import numpy as np
# Ejercicio 1
n = 755
x = 203
p_hat = x / n
se = np.sqrt(p_hat * (1 - p_hat) / n)
from scipy.stats import norm
z_crit = norm.ppf(0.975)
IC_prop = [p_hat - z_crit * se, p_hat + z_crit * se]
print('IC 95%:', IC_prop)

# Ejercicio 2
amplitud = IC_prop[1] - IC_prop[0]
amplitud_deseada = amplitud / 2
n_nuevo = (z_crit**2 * p_hat * (1 - p_hat)) / (amplitud_deseada/2)**2
print('Nuevo tamaño muestral:', np.ceil(n_nuevo))

# Ejercicio 3
amplitud_obs = (0.2954 - 0.2423) / 2
se_aprox = np.sqrt(p_hat * (1 - p_hat) / n)
z_aprox = amplitud_obs / se_aprox
nivel_confianza_aprox = 2 * norm.cdf(z_aprox) - 1
print('Nivel de confianza aproximado:', nivel_confianza_aprox) 