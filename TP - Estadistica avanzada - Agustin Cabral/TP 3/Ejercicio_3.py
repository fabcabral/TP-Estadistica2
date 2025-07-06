# Ejercicio 3: Test de hipótesis para proporción de contaminadas
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Datos iniciales
n = 300
n_libre = 165
n_contaminadas = n - n_libre  # contaminadas = 135
p0 = 0.40  # proporción bajo H0
alfa = 0.05
conf_level = 0.90

# Cálculo de la proporción muestral
p_hat = n_contaminadas / n

# 1. Test de hipótesis para proporción (prueba de una cola)
z_obs = (p_hat - p0) / np.sqrt(p0 * (1 - p0) / n)
z_crit = norm.ppf(1 - alfa)

print("Test de hipótesis para proporción contaminada:")
print(f"Proporción muestral = {p_hat:.4f}")
print(f"Estadístico z observado = {z_obs:.4f}")
print(f"Valor crítico z = {z_crit:.4f}")

if z_obs > z_crit:
    print("Decisión: RECHAZAMOS H0 - Se considera que hay emergencia sanitaria.\n")
else:
    print("Decisión: No se rechaza H0 - No hay suficientes evidencias para declarar emergencia sanitaria.\n")

# 2. Intervalo de confianza para la proporción
z_ic = norm.ppf(1 - (1 - conf_level)/2)
se_p = np.sqrt(p_hat * (1 - p_hat) / n)
ic_inf = p_hat - z_ic * se_p
ic_sup = p_hat + z_ic * se_p

print(f"Intervalo de confianza al {int(conf_level*100)}% para la proporción contaminada:")
print(f"[{ic_inf:.4f}, {ic_sup:.4f}]\n")

# 3. Cálculo del p-valor
p_value = 1 - norm.cdf(z_obs)
print("Resultados del p-valor:")
print(f"Estadístico z observado: {z_obs:.4f}")
print(f"p-valor (cola superior): {p_value:.6f}")
if p_value < alfa:
    print("Rechazamos H0: hay evidencia para declarar emergencia sanitaria.")
else:
    print("No se rechaza H0: no hay evidencia suficiente para declarar emergencia sanitaria.")

# 4. Visualización gráfica
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, lw=2, color="blue", label="Distribución normal estándar")
plt.fill_between(x, 0, y, where=(x >= z_crit).tolist(), color="red", alpha=0.3, label="Región de rechazo")
plt.axvline(float(z_crit), color="red", linestyle="--", lw=2, label="Límite crítico")
plt.axvline(float(z_obs), color="darkgreen", lw=2, label="Z observado")
plt.xlabel("Estadístico z")
plt.ylabel("Densidad")
plt.title("Distribución normal estándar: test de cola superior")
plt.legend(loc="upper right")
plt.show() 