# Ejercicio 1
# Problema: Efectividad de Droga Analgésica
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, bartlett, f_oneway, kruskal, t
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Crear los datos
neuralgia = pd.DataFrame({
    'Paciente': np.arange(1, 31),
    'tratamiento': ['Placebo']*10 + ['Aspirina']*10 + ['Droga']*10,
    'tiempo_sin_dolor': [2.5, 2.5, 2.3, 2.4, 2.7, 2.7, 2.6, 2.4, 2.3, 2.3,
                        2.9, 2.5, 3.0, 2.5, 2.7, 2.8, 2.7, 3.0, 2.9, 2.8,
                        3.1, 3.1, 2.9, 3.3, 3.1, 3.0, 3.1, 3.2, 2.9, 3.1],
    'complic': [0, 3, 2, 3, 4, 2, 2, 3, 1, 1,
                1, 4, 3, 0, 2, 3, 4, 5, 2, 3,
                4, 5, 4, 2, 3, 4, 1, 5, 3, 0]
})

# Estadísticas descriptivas
print("\nEstadísticas descriptivas por tratamiento:")
print(neuralgia.groupby('tratamiento')['tiempo_sin_dolor'].agg(['count', 'mean', 'std', 'min', 'max']))

# Boxplot y histogramas
plt.figure(figsize=(10, 6))
neuralgia.boxplot(column='tiempo_sin_dolor', by='tratamiento', grid=False, patch_artist=True,
                  boxprops=dict(facecolor='lightblue'), medianprops=dict(color='black'))
plt.title('Tiempo sin dolor por tratamiento')
plt.suptitle('')
plt.xlabel('Tratamiento')
plt.ylabel('Tiempo sin dolor (horas)')
plt.show()

for grupo, color in zip(['Placebo', 'Aspirina', 'Droga'], ['lightblue', 'lightgreen', 'lightcoral']):
    plt.hist(neuralgia[neuralgia['tratamiento'] == grupo]['tiempo_sin_dolor'],
             bins=5, alpha=0.7, color=color, label=grupo, range=(2, 3.5))
    plt.title(f'Histograma: {grupo}')
    plt.xlabel('Tiempo sin dolor')
    plt.ylabel('Frecuencia')
    plt.show()

# Gráfico de medias con IC 95%
groups = ['Placebo', 'Aspirina', 'Droga']
means = np.array(neuralgia.groupby('tratamiento')['tiempo_sin_dolor'].mean())
sds = np.array(neuralgia.groupby('tratamiento')['tiempo_sin_dolor'].std())
n_per_group = 10
se = sds / np.sqrt(n_per_group)
ci_lower = means - 1.96 * se
ci_upper = means + 1.96 * se
plt.errorbar(range(1, 4), means, yerr=1.96*se, fmt='o', color='black', capsize=5)
plt.xticks([1, 2, 3], groups)
plt.xlabel('Tratamiento')
plt.ylabel('Tiempo sin dolor promedio (horas)')
plt.title('Medias por tratamiento con IC 95%')
plt.ylim(2, 3.5)
plt.show()

# Supuestos: Normalidad y homocedasticidad
print("\nTest de Shapiro-Wilk por grupo:")
for grupo in groups:
    stat, p = shapiro(neuralgia[neuralgia['tratamiento'] == grupo]['tiempo_sin_dolor'])
    print(f"{grupo}: W = {stat:.4f}, p = {p:.4f}")

# Test de Bartlett
stat_bartlett, p_bartlett = bartlett(
    neuralgia[neuralgia['tratamiento'] == 'Placebo']['tiempo_sin_dolor'],
    neuralgia[neuralgia['tratamiento'] == 'Aspirina']['tiempo_sin_dolor'],
    neuralgia[neuralgia['tratamiento'] == 'Droga']['tiempo_sin_dolor'])
print(f"\nTest de Bartlett: K = {stat_bartlett:.4f}, p = {p_bartlett:.4f}")

# ANOVA
f_stat, p_anova = f_oneway(
    neuralgia[neuralgia['tratamiento'] == 'Placebo']['tiempo_sin_dolor'],
    neuralgia[neuralgia['tratamiento'] == 'Aspirina']['tiempo_sin_dolor'],
    neuralgia[neuralgia['tratamiento'] == 'Droga']['tiempo_sin_dolor'])
print(f"\nANOVA: F = {f_stat:.2f}, p = {p_anova:.4f}")

# Comparaciones múltiples: Tukey (requiere statsmodels)
tukey = pairwise_tukeyhsd(neuralgia['tiempo_sin_dolor'], neuralgia['tratamiento'])
print("\nTest de Tukey:")
print(tukey)
tukey.plot_simultaneous()
plt.show()

# Efectos colaterales gástricos (Kruskal-Wallis)
print("\nAnálisis de efectos colaterales gástricos:")
print(neuralgia.groupby('tratamiento')['complic'].agg(['count', 'mean', 'std', 'median', 'min', 'max']))
stat_kruskal, p_kruskal = kruskal(
    neuralgia[neuralgia['tratamiento'] == 'Placebo']['complic'],
    neuralgia[neuralgia['tratamiento'] == 'Aspirina']['complic'],
    neuralgia[neuralgia['tratamiento'] == 'Droga']['complic'])
print(f"\nTest de Kruskal-Wallis: H = {stat_kruskal:.2f}, p = {p_kruskal:.4f}")

plt.figure(figsize=(8, 4))
neuralgia.boxplot(column='complic', by='tratamiento', grid=False, patch_artist=True,
                  boxprops=dict(facecolor='lightblue'), medianprops=dict(color='black'))
plt.title('Efectos colaterales por tratamiento')
plt.suptitle('')
plt.xlabel('Tratamiento')
plt.ylabel('Frecuencia de efectos colaterales (0-5)')
plt.show()

# Gráfico de barras de frecuencias
table_complic = pd.crosstab(neuralgia['tratamiento'], neuralgia['complic'])
table_complic.plot(kind='bar', stacked=False, color=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Distribución de efectos colaterales')
plt.xlabel('Tratamiento')
plt.ylabel('Número de pacientes')
plt.legend(title='Frecuencia (0-5)')
plt.show() 