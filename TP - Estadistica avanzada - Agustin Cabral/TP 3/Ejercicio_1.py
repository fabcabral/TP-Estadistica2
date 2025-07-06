# Ejercicio 1: Test de hipótesis para el rendimiento de una nueva variedad
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as t_dist

# Datos iniciales
rendimiento_referencia = 3.5  # rendimiento medio de la variedad común (ton/ha)
alfa = 0.05  # nivel de significación

# Datos de la nueva variedad
rendimientos = np.array([3.15, 3.92, 4.26, 3.72, 4.19, 3.42, 4.38, 4.50, 3.36])

# 1. Estadísticos descriptivos
n = len(rendimientos)
media_muestral = np.mean(rendimientos)
desv_est = np.std(rendimientos, ddof=1)
error_est = desv_est / np.sqrt(n)

print("\nESTADISTICOS DESCRIPTIVOS")
print("------------------------")
print(f"- Media muestral: {media_muestral:.3f} ton/ha")
print(f"- Desviacion estandar: {desv_est:.3f} ton/ha")
print(f"- Error estandar: {error_est:.3f} ton/ha")

# 2. Cálculo del estadístico t y valor crítico
t_calc = (media_muestral - rendimiento_referencia) / error_est
t_critico = t_dist.ppf(1 - alfa, df=n-1)

# 3. Cálculo del p-valor
p_valor = 1 - t_dist.cdf(t_calc, df=n-1)

print("\nPRUEBA DE HIPOTESIS")
print("-------------------")
print("H0: μ ≤ 3.5 ton/ha")
print("H1: μ > 3.5 ton/ha")
print(f"\n- Estadistico t calculado: {t_calc:.3f}")
print(f"- Valor critico (t): {t_critico:.3f}")
print(f"- P-valor: {p_valor:.4f}")

# 4. Decisión y conclusión
print("\nDECISION:")
print("---------")
if p_valor < alfa:
    print(f"Se rechaza H0 con un nivel de significacion de {alfa}")
    print("Hay evidencia estadistica para afirmar que el rendimiento promedio")
    print("de la nueva variedad es mayor que 3.5 ton/ha.")
else:
    print(f"No se rechaza H0 con un nivel de significación de {alfa}")
    print("No hay evidencia estadística suficiente para afirmar que el rendimiento")
    print("promedio de la nueva variedad es mayor que 3.5 ton/ha.")

# 5. Análisis de errores
print("\nANALISIS DE ERRORES:")
print("-------------------")
print("- Error Tipo I: Rechazar H0 cuando es verdadera")
print("  (Afirmar que la nueva variedad es mejor cuando no lo es)")
print(f"  Probabilidad = {alfa}")
print("\n- Error Tipo II: No rechazar H0 cuando es falsa")
print("  (No detectar que la nueva variedad es mejor cuando si lo es)")
print("  La probabilidad depende del tamano del efecto real")

# 6. Visualización gráfica
x = np.linspace(-4, 4, 1000)
y = t_dist.pdf(x, df=n-1)

plt.figure(figsize=(8, 5))
plt.plot(x, y, lw=2, color="blue", label="Distribución t")
plt.fill_between(x, 0, y, where=(x >= t_critico), color="red", alpha=0.3, label="Región de rechazo")
plt.axvline(t_critico, color="red", linestyle="--", lw=2, label="Límite crítico")
plt.axvline(t_calc, color="darkgreen", lw=2, label="t observado")
plt.xlabel("Estadístico t")
plt.ylabel("Densidad")
plt.title("Distribución t: Test de cola superior")
plt.legend(loc="upper right")
plt.show() 