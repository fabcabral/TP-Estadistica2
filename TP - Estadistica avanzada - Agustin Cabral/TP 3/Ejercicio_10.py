import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

# Datos
g1, g2 = 200, 200
c1, c2 = 136, 91

# Hipótesis
# H0: p1 = p2
# H1: p1 > p2 (más complicaciones con midazolam)

alfa = 0.05
count = np.array([c1, c2])
nobs = np.array([g1, g2])
stat, pval = proportions_ztest(count, nobs, alternative='larger')

print('Test de proporciones:')
print(f'Estadístico z = {stat:.4f}, p-valor = {pval:.4f}')
if pval < alfa:
    print('Conclusión: Se rechaza H0. Midazolam tiene mayor proporción de complicaciones.')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de diferencia.')

# Visualización
groups = ['Midazolam', 'Dexmedetomidina']
rates = [c1/g1, c2/g2]
plt.bar(groups, rates, color=['blue', 'purple'])
plt.ylabel('Proporción de complicaciones')
plt.title('Complicaciones por sedante en terapia intensiva')
for i, rate in enumerate(rates):
    plt.text(i, rate+0.01, f'{rate:.2f}', ha='center')
plt.show() 