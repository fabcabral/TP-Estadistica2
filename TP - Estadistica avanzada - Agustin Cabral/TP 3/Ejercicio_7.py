import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Unidad experimental y tamaño muestral
# Unidad experimental: cada placa de Petri (con 4 plántulas)
# Tamaño muestral: 5 placas por condición (pH 6 y pH 8), total 10 mediciones

# 2. Datos
ph6 = np.array([25, 25, 27, 44, 30])
ph8 = np.array([27, 29, 37, 56, 46])

# 3. Planteo de hipótesis
# H0: mu_dif = 0 (no hay diferencia en la expresión de HSP entre pH 6 y pH 8)
# H1: mu_dif < 0 (la expresión de HSP es mayor a pH 8 que a pH 6)
# Prueba: t-test para muestras pareadas

alfa = 0.05

# 4. Chequeo de supuestos
# Normalidad de las diferencias
dif = ph8 - ph6
shapiro = stats.shapiro(dif)
print(f'Shapiro-Wilk para las diferencias: p = {shapiro.pvalue:.4f}')

# 5. Test t para muestras pareadas
# alternative="greater" porque se espera mayor expresión a pH 8
result = stats.ttest_rel(ph8, ph6, alternative='greater')
print(f'Test t pareado: estadístico t = {result.statistic:.4f}, p-valor = {result.pvalue:.4f}')
if result.pvalue < alfa:
    print('Conclusión: Se rechaza H0. El pH alto incrementa la expresión de HSP.')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de sobreexpresión de HSP a pH alto.')

# 6. Visualización
plt.figure(figsize=(7,5))
plt.boxplot([ph6, ph8], patch_artist=True)
plt.xticks([1, 2], ['pH 6', 'pH 8'])
plt.ylabel('HSP (ng/100g)')
plt.title('Expresión de HSP bajo diferentes pH')
# Conectar pares
for i in range(len(ph6)):
    plt.plot([1, 2], [ph6[i], ph8[i]], color='gray', marker='o')
plt.show() 