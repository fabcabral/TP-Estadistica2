import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# Datos
n1, n2 = 115, 120
x1, x2 = 8, 12

# Hipótesis
# H0: p1 = p2
# H1: p1 < p2 (menos diarrea con bifidobacteria)

alfa = 0.05
count = np.array([x1, x2])
nobs = np.array([n1, n2])
stat, pval = proportions_ztest(count, nobs, alternative='smaller')

print('Test de proporciones:')
print(f'Estadístico z = {stat:.4f}, p-valor = {pval:.4f}')
if pval < alfa:
    print('Conclusión: Se rechaza H0. El yogur con bifidobacterias reduce la diarrea.')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de reducción.')

# Magnitud del efecto
tasa1, tasa2 = x1/n1, x2/n2
diff = tasa2 - tasa1
ic = proportion_confint([x1, x2], [n1, n2], alpha=0.05, method='wilson')
print(f'Tasa bifido: {tasa1:.3f}, Tasa control: {tasa2:.3f}, Diferencia: {diff:.3f}')
print(f'IC 95% bifido: [{ic[0][0]:.3f}, {ic[0][1]:.3f}], IC 95% control: [{ic[1][0]:.3f}, {ic[1][1]:.3f}]')

# Visualización
groups = ['Bifidobacteria', 'Control']
rates = [tasa1, tasa2]
plt.bar(groups, rates, color=['green', 'gray'])
plt.ylabel('Proporción de diarrea')
plt.title('Incidencia de diarrea infantil')
for i, rate in enumerate(rates):
    plt.text(i, rate+0.01, f'{rate:.2f}', ha='center')
plt.show() 