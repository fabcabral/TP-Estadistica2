# Ejercicio 5: Análisis de Leptina y Fibulina en Preeclampsia
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm

# 1. Cargar y preparar los datos
ruta_csv = "C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/preclampsia.csv"
datos = pd.read_csv(ruta_csv)

print(datos.info())
print(datos.describe())

# Boxplots para visualización inicial
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
datos.boxplot(column='leptina', by='Grupo', ax=axes[0], patch_artist=True, boxprops=dict(facecolor='lightblue'), medianprops=dict(color='black'))
axes[0].set_title("Expresion de Leptina")
axes[0].set_xlabel("Grupo")
axes[0].set_ylabel("Expresion (UA)")
datos.boxplot(column='fibulina', by='Grupo', ax=axes[1], patch_artist=True, boxprops=dict(facecolor='pink'), medianprops=dict(color='black'))
axes[1].set_title("Expresion de Fibulina 1A")
axes[1].set_xlabel("Grupo")
axes[1].set_ylabel("Expresion (UA)")
plt.suptitle("")
plt.tight_layout()
plt.show()

# 2. Análisis de Leptina
grupo_control = datos[datos['Grupo'] == 'Control']['leptina']
grupo_pe = datos[datos['Grupo'] == 'PE']['leptina']
t_stat_leptina, p_leptina = ttest_ind(grupo_control, grupo_pe, equal_var=False)
print("\nANALISIS DE LEPTINA\n------------------")
print(f"t = {t_stat_leptina:.3f}, p-valor = {p_leptina:.4f}")
if p_leptina < 0.05:
    print("✅ Conclusion: Se RECHAZA H0. La expresion de Leptina es significativamente diferente entre grupos.\n")
else:
    print("🟨 Conclusion: No se rechaza H0. No hay evidencia suficiente de diferencia en la expresion de Leptina.\n")

# 3. Análisis de Fibulina 1A
grupo_control_fib = datos[datos['Grupo'] == 'Control']['fibulina']
grupo_pe_fib = datos[datos['Grupo'] == 'PE']['fibulina']
t_stat_fibulina, p_fibulina = ttest_ind(grupo_control_fib, grupo_pe_fib, equal_var=False)
print("\nANALISIS DE FIBULINA 1A\n----------------------")
print(f"t = {t_stat_fibulina:.3f}, p-valor = {p_fibulina:.4f}")
if p_fibulina < 0.05:
    print("✅ Conclusion: Se RECHAZA H0. La expresion de Fibulina 1A es significativamente diferente entre grupos.\n")
else:
    print("🟨 Conclusion: No se rechaza H0. No hay evidencia suficiente de diferencia en la expresion de Fibulina 1A.\n")

# 4. Análisis de errores tipo I y II
alpha = 0.05
n1 = len(grupo_control)
n2 = len(grupo_pe)
d = 0.5  # tamaño del efecto medio
# Aproximación del poder usando fórmula normal
z_alpha = norm.ppf(1 - alpha/2)
z_beta = (z_alpha - d * np.sqrt((n1 * n2) / (n1 + n2)))
power = 1 - norm.cdf(z_beta)
print("\nANALISIS DE ERRORES\n------------------")
print(f"Error tipo I (α): {alpha}")
print(f"Poder de la prueba para Leptina y Fibulina (aprox., d=0.5): {power:.4f}")

# 5. Visualización gráfica de las distribuciones
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# Leptina
dens_control = grupo_control.plot(kind='density', ax=axes[0], color='blue', label='Control')
grupos_pe = grupo_pe.plot(kind='density', ax=axes[0], color='red', label='PE')
axes[0].set_title("Distribucion de Leptina")
axes[0].set_xlabel("Expresion (UA)")
axes[0].set_ylabel("Densidad")
axes[0].legend(loc="upper right")
# Fibulina
dens_control_fib = grupo_control_fib.plot(kind='density', ax=axes[1], color='blue', label='Control')
grupos_pe_fib = grupo_pe_fib.plot(kind='density', ax=axes[1], color='red', label='PE')
axes[1].set_title("Distribucion de Fibulina 1A")
axes[1].set_xlabel("Expresion (UA)")
axes[1].set_ylabel("Densidad")
axes[1].legend(loc="upper right")
plt.tight_layout()
plt.show() 