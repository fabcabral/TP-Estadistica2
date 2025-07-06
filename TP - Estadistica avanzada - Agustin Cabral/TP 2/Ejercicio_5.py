# Ejercicio 1
# - Proporcion de nacimientos prematuros -> estimador: p-hat
# - Peso medio de nacidos a termino -> estimador: x-barra
# - Poblacion: nacimientos de madres adolescentes en la maternidad

# Ejercicio 2
import numpy as np
from scipy.stats import norm
z_crit = norm.ppf(0.975)

# Para proporcion (suponiendo p aprox 0.5 para maxima variabilidad)
margen_error_prop = 0.05
n_prop = (z_crit**2 * 0.5 * 0.5) / (margen_error_prop**2)

# Para media (con sd aprox 500 g por ejemplo)
margen_error_media = 250
sd_media = 500
n_media = (z_crit * sd_media / margen_error_media)**2

print('Tamaño muestral para proporcion:', np.ceil(n_prop))
print('Tamaño muestral para media:', np.ceil(n_media)) 