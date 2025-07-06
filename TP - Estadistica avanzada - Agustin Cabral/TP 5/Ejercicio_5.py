# Ejercicio 5
# Problema: Cálculo de tamaño muestral para detectar diferencia mínima relevante
import numpy as np
from scipy.stats import norm

delta = 0.5     # Diferencia mínima relevante
sigma = 1       # Desvío estándar común
alpha = 0.05    # Nivel de significación
power = 0.80    # Potencia

z_alpha = norm.ppf(1 - alpha / 2)
z_beta = norm.ppf(power)

n = ((z_alpha + z_beta)**2 * 2 * sigma**2) / delta**2
n_redondeado = int(np.ceil(n))
print(f"🔹 Tamaño muestral necesario (sin pérdidas): {n_redondeado} pacientes por grupo")

# Supongamos una pérdida del 20%
tasa_perdida = 0.20
n_ajustado = int(np.ceil(n_redondeado / (1 - tasa_perdida)))
print(f"🔹 Tamaño muestral ajustado por pérdidas del 20%: {n_ajustado} pacientes por grupo")

print(f"📝 El tamaño muestral fue calculado para detectar una diferencia mínima clínicamente relevante de 0.5 log₁₀ copias/ml en la carga viral entre grupos de tratamiento, "
      f"asumiendo una desviación estándar común de 1, un nivel de significación bilateral del 5% y una potencia estadística del 80%. "
      f"Bajo estas condiciones, se estimó que se requerían {n_redondeado} pacientes por grupo. "
      f"Considerando una tasa de pérdida del 20%, se ajustó el tamaño muestral a {n_ajustado} pacientes por grupo.") 