# Ejercicio 2: Test t para lotes de calcio (A234 y G120)
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, t as t_dist

# 1. Configuración inicial y datos del lote A234
alfa = 0.01
media_esperada = 250

calcio_A234 = np.array([
    252.49, 248.16, 251.65, 249.04, 246.85,
    251.16, 247.98, 248.29, 246.86, 253.11,
    250.84, 252.74, 252.26, 250.16, 250.98,
    247.63, 250.93, 250.53, 250.44, 249.22
])

# Test t para LOTE A234
t_stat_A234 = ttest_1samp(calcio_A234, popmean=media_esperada)[0]
p_value_A234 = ttest_1samp(calcio_A234, popmean=media_esperada)[1]
n_A234 = len(calcio_A234)
gl_A234 = n_A234 - 1
media_A234 = np.mean(calcio_A234)
desv_A234 = np.std(calcio_A234, ddof=1)
error_A234 = desv_A234 / np.sqrt(n_A234)
t_obs_A234 = (media_A234 - media_esperada) / error_A234
t_crit_A234 = t_dist.ppf(1 - alfa/2, df=gl_A234)

print("---- LOTE A234 ----")
print(f"Media: {media_A234:.2f}, Desv. Est.: {desv_A234:.2f}, n: {n_A234}")
print(f"t observado: {t_obs_A234:.3f}, t crítico: ±{t_crit_A234:.3f}")
print(f"p-valor (dos colas): {p_value_A234:.4f}")
if p_value_A234 < alfa:
    print(f" Se RECHAZA H0: DETENER el proceso. (p = {p_value_A234:.4f})\n")
else:
    print(f" No se rechaza H0: CONTINUAR el proceso. (p = {p_value_A234:.4f})\n")

# 2. Datos y análisis del lote G120
calcio_G120 = np.array([
    248.48, 249.88, 250.94, 245.61, 247.33,
    247.32, 253.52, 247.87, 248.03, 248.27,
    244.68, 247.34, 250.51, 246.46, 250.06,
    245.49, 247.15, 254.03, 246.36, 249.29
])

t_stat_G120 = ttest_1samp(calcio_G120, popmean=media_esperada)[0]
p_value_G120 = ttest_1samp(calcio_G120, popmean=media_esperada)[1]
n_G120 = len(calcio_G120)
gl_G120 = n_G120 - 1
media_G120 = np.mean(calcio_G120)
desv_G120 = np.std(calcio_G120, ddof=1)
error_G120 = desv_G120 / np.sqrt(n_G120)
t_obs_G120 = (media_G120 - media_esperada) / error_G120
t_crit_G120 = t_dist.ppf(1 - alfa/2, df=gl_G120)

print("---- LOTE G120 ----")
print(f"Media: {media_G120:.2f}, Desv. Est.: {desv_G120:.2f}, n: {n_G120}")
print(f"t observado: {t_obs_G120:.3f}, t crítico: ±{t_crit_G120:.3f}")
print(f"p-valor (dos colas): {p_value_G120:.4f}")
if p_value_G120 < alfa:
    print(f" Se RECHAZA H0: DETENER el proceso. (p = {p_value_G120:.4f})\n")
else:
    print(f" No se rechaza H0: CONTINUAR el proceso. (p = {p_value_G120:.4f})\n")

# 3. Análisis de errores
def imprimir_errores():
    print("---- ERRORES TIPO I Y II ----")
    print("• Error tipo I: Detener el proceso aunque esté dentro del valor esperado (falsa alarma).\n  Consecuencia: Se pierde tiempo y dinero innecesariamente.\n")
    print("• Error tipo II: No detener el proceso aunque el contenido de calcio este mal (pasa un lote defectuoso).\n  Consecuencia: Se comercializa un producto fuera de especificacion, afectando la calidad o salud.\n")
    print("Según los resultados anteriores, es más probable que estemos en riesgo de cometer un error tipo I\nsi rechazamos H0 sin que realmente haya un problema con el contenido de calcio.\n")
imprimir_errores()

# 4. Visualización para lote A234
x = np.arange(-4, 4, 0.01)
y = t_dist.pdf(x, df=gl_A234)
plt.figure(figsize=(8, 5))
plt.plot(x, y, lw=2, color="blue", label="Distribución t")
plt.axvline(float(-t_crit_A234), color="red", linestyle="--", lw=2, label="Límites críticos")
plt.axvline(float(t_crit_A234), color="red", linestyle="--", lw=2)
plt.axvline(float(t_obs_A234), color="darkgreen", lw=2, label="t observado")
plt.xlabel("t")
plt.ylabel("Densidad")
plt.title("Distribución t - Región de rechazo (Lote A234, α = 0.01)")
plt.legend(loc="upper right")
plt.show()

# 5. Visualización para lote G120
x = np.arange(-4, 4, 0.01)
y = t_dist.pdf(x, df=gl_G120)
plt.figure(figsize=(8, 5))
plt.plot(x, y, lw=2, color="blue", label="Distribución t")
plt.axvline(float(-t_crit_G120), color="red", linestyle="--", lw=2, label="Límites críticos")
plt.axvline(float(t_crit_G120), color="red", linestyle="--", lw=2)
plt.axvline(float(t_obs_G120), color="darkgreen", lw=2, label="t observado")
plt.xlabel("t")
plt.ylabel("Densidad")
plt.title("Distribución t - Región de rechazo (Lote G120, α = 0.01)")
plt.legend(loc="upper right")
plt.show()

# 6. Función de interpretación y análisis final
def interpretacion_test(pvalor, alfa, nombre_lote):
    print(f"---- Analisis para lote {nombre_lote} ----\n")
    if pvalor < alfa:
        print("Decision: Se RECHAZA H0. DETENER el proceso.\n")
        print("Dado que se rechazo H0, existe riesgo de cometer un error tipo I (falsa alarma).\n")
    else:
        print("Decision: No se rechaza H0. CONTINUAR el proceso.\n")
        print("Dado que no se rechazo H0, existe riesgo de cometer un error tipo II (dejar pasar lote defectuoso).\n")
    print("Error tipo I (α): Detener el proceso aunque el contenido de calcio este dentro del valor esperado (falsa alarma).\n  Consecuencia: Perdida de tiempo y recursos innecesarios.\n")
    print("Error tipo II (β): No detener el proceso aunque el contenido de calcio este fuera de especificacion.\n  Consecuencia: Comercializar producto fuera de norma, afectando calidad o salud.\n")

interpretacion_test(p_value_A234, alfa, "A234")
interpretacion_test(p_value_G120, alfa, "G120") 