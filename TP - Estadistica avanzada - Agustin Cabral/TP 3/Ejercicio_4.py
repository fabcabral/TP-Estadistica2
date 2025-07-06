# Ejercicio 4: Análisis de pH y proporciones en RYR1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, norm

# 1. Análisis del pH para individuos TT y CT
# Cargar datos
ruta_csv = "C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/RYR1.csv"
datos = pd.read_csv(ruta_csv)

# Filtrar individuos TT y CT
tt_ct = datos[datos['Genotipo'].isin(['TT', 'CT'])]

# Prueba t unilateral: ¿pH significativamente menor a 6.2?
t_stat, p_value = ttest_1samp(tt_ct['pH'], popmean=6.2, alternative='less')
print("Resultados test t (pH TT y CT vs 6.2):")
print(f"t = {t_stat:.3f}, p-valor = {p_value:.4f}")
if p_value < 0.05:
    print("✅ Conclusión: Se RECHAZA H0. El pH de TT y CT es significativamente menor a 6.2 (anormal).\n")
else:
    print("🟨 Conclusión: No se rechaza H0. No hay evidencia suficiente para decir que el pH es menor a 6.2.\n")

# 2. Análisis de prevalencia de individuos CC
n = len(datos)
cc = np.sum(datos['Genotipo'] == 'CC')
phat = cc / n
p0 = 0.05
z = (phat - p0) / np.sqrt(p0 * (1 - p0) / n)
z_crit = norm.ppf(1 - 0.05)
p_val = 1 - norm.cdf(z)
print(f"Proporción muestral de CC: {phat:.4f}")
print(f"Estadístico Z: {z:.3f}")
print(f"Valor crítico Z: {z_crit:.3f}")
print(f"p-valor: {p_val:.4f}")
if z > z_crit:
    print("✅ Conclusión: Se RECHAZA H0. Hay evidencia de que la proporción de CC supera el 5%.\n")
else:
    print("🟨 Conclusión: No se rechaza H0. No hay evidencia suficiente para afirmar que supera el 5%.\n")

# 3. Visualización gráfica de la distribución Z
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, color="blue", lw=2, label="Distribución normal estándar")
plt.fill_between(x, 0, y, where=(x > z_crit), color="red", alpha=0.4, label="Región de rechazo")
plt.axvline(z, color="black", lw=1, label=f"z observado = {z:.3f}")
plt.axvline(z_crit, color="red", linestyle="--", lw=1, label=f"z crítico = {z_crit:.3f}")
plt.title("Distribución Z – Proporción de individuos CC\nZona roja = región de rechazo (α = 0.05)")
plt.xlabel("Valor Z")
plt.ylabel("Densidad")
plt.legend(loc="upper right")
plt.show()

# 4. Análisis de errores tipo I y II
n = 300
p0 = 0.10         # hipótesis nula
alpha = 0.05
p_real = 0.13     # hipótesis alternativa para estimar beta
z_crit = norm.ppf(1 - alpha)
umbral_p = p0 + z_crit * np.sqrt(p0 * (1 - p0) / n)
z_beta = (umbral_p - p_real) / np.sqrt(p_real * (1 - p_real) / n)
beta = norm.cdf(z_beta)
print(f"🔺 Error tipo I (α): {alpha}")
print(f"🔻 Error tipo II (β) estimado si p real = 0.13: {beta:.4f}") 