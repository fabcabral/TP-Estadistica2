import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Datos
antes = np.array([64, 84, 92, 64, 66, 72, 64, 66, 69, 72])
despues = np.array([62, 72, 75, 66, 60, 65, 56, 57, 61, 59])
dif = antes - despues

# 2. Planteo de hipótesis
# H0: El entrenamiento no disminuye la frecuencia cardíaca en reposo (media dif = 0)
# H1: El entrenamiento disminuye la frecuencia cardíaca en reposo (media dif > 0)
# Prueba: t-test pareado

alfa = 0.05

# 3. Análisis de normalidad de las diferencias
shapiro = stats.shapiro(dif)
print(f'Shapiro-Wilk para las diferencias: p = {shapiro.pvalue:.4f}')

# 4. Test t pareado
result = stats.ttest_rel(antes, despues, alternative='greater')
print(f'Test t pareado: t = {result.statistic:.4f}, p-valor = {result.pvalue:.4f}')
if result.pvalue < alfa:
    print('Conclusión: Se rechaza H0. El entrenamiento disminuye la frecuencia cardíaca en reposo.')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de disminución.')

# 5. Visualización
plt.figure(figsize=(7,5))
plt.boxplot([antes, despues], patch_artist=True)
plt.xticks([1,2], ['Antes', 'Después'])
plt.ylabel('Frecuencia cardíaca (lpm)')
plt.title('Frecuencia cardíaca antes y después del entrenamiento')
for i in range(len(antes)):
    plt.plot([1,2], [antes[i], despues[i]], color='gray', marker='o')
plt.show() 