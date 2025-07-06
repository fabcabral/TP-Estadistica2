import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# 1. Identificación de elementos del estudio
# Unidad experimental: cada oveja Merino
# Muestras: Grupo 1 (70 sin tratamiento), Grupo 2 (40 con sincronización)
# Poblaciones: todas las ovejas Merino bajo cada tratamiento
# Variable aleatoria: preñada (1) o no preñada (0)

# 2. Datos
n1, n2 = 70, 40
x1, x2 = 56, 35

# 3. Planteo de hipótesis
# H0: p1 = p2 (tasa de preñez igual)
# H1: p1 < p2 (tasa de preñez mayor con sincronización)
# Prueba: z-test para dos proporciones

alfa = 0.05
count = np.array([x1, x2])
nobs = np.array([n1, n2])
stat, pval = proportions_ztest(count, nobs, alternative='smaller')

print('Test de proporciones:')
print(f'Estadístico z = {stat:.4f}, p-valor = {pval:.4f}')
if pval < alfa:
    print('Conclusión: Se rechaza H0. La sincronización hormonal mejora la tasa de preñez.')
    print('Riesgo: error tipo I (falso positivo).')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de mejora con sincronización hormonal.')
    print('Riesgo: error tipo II (falso negativo).')

# 4. Intervalo de confianza del 95% para la tasa de preñez (grupo tratado)
confint = proportion_confint(x2, n2, alpha=0.05, method='wilson')
print(f'IC 95% para la tasa de preñez (sincronización): [{confint[0]:.2f}, {confint[1]:.2f}]')

# 5. Informe técnico y visualización
groups = ['Sin tratamiento', 'Con sincronización']
rates = [x1/n1, x2/n2]
plt.figure(figsize=(6,4))
plt.bar(groups, rates, color=['skyblue', 'orange'])
plt.ylim(0,1)
plt.ylabel('Tasa de preñez')
plt.title('Tasa de preñez en ovejas Merino')
for i, rate in enumerate(rates):
    plt.text(i, rate+0.03, f'{rate:.2f}', ha='center')
plt.show() 