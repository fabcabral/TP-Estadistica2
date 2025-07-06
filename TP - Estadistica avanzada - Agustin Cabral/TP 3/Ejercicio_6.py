import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Datos
colesterol_dieta1 = np.array([10.4, 14.2, 20.5, 19.6, 18.5, 24.0, 23.4, 13.6])
colesterol_dieta2 = np.array([7.5, 7.2, 6.7, 7.6, 11.2, 9.6, 6.8, 8.5])

# 2. Planteo de hipótesis
# H0: mu1 - mu2 = 0 (no hay diferencia)
# H1: mu1 - mu2 > 0 (Dieta 1 tiene mayor colesterol que Dieta 2)
# Prueba: t-test para muestras independientes

alfa = 0.05

# 3. Chequeo de supuestos
# Normalidad
shapiro1 = stats.shapiro(colesterol_dieta1)
shapiro2 = stats.shapiro(colesterol_dieta2)
# Igualdad de varianzas
levene = stats.levene(colesterol_dieta1, colesterol_dieta2)

print('Chequeo de supuestos:')
print(f'Shapiro Dieta 1: p = {shapiro1.pvalue:.4f}')
print(f'Shapiro Dieta 2: p = {shapiro2.pvalue:.4f}')
print(f'Levene (varianzas iguales): p = {levene.pvalue:.4f}\n')

# 4. Test t para medias independientes
# Usar var.equal=True si p>0.05 en Levene
equal_var = levene.pvalue > 0.05
test = stats.ttest_ind(colesterol_dieta1, colesterol_dieta2, equal_var=equal_var, alternative='greater')

print('Test t para medias independientes:')
print(f'Estadístico t = {test.statistic:.4f}')
print(f'p-valor = {test.pvalue:.4f}')
if test.pvalue < alfa:
    print('Conclusión: Se rechaza H0. La Dieta 2 reduce el colesterol respecto a la Dieta 1.\n')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de reducción de colesterol.\n')

# 5. Errores tipo I y II
print('Errores tipo I y II:')
print('- Error tipo I: Concluir que la Dieta 2 reduce el colesterol cuando no lo hace (falso positivo).')
print('- Error tipo II: No detectar una reducción real de colesterol por la Dieta 2 (falso negativo).')
if test.pvalue < alfa:
    print('En este caso, si se rechaza H0, el riesgo es cometer error tipo I.\n')
else:
    print('Si no se rechaza H0, el riesgo es error tipo II.\n')

# 6. Intervalo de confianza del 95% para la diferencia de medias
from scipy.stats import t
n1, n2 = len(colesterol_dieta1), len(colesterol_dieta2)
mean1, mean2 = np.mean(colesterol_dieta1), np.mean(colesterol_dieta2)
var1, var2 = np.var(colesterol_dieta1, ddof=1), np.var(colesterol_dieta2, ddof=1)
se_diff = np.sqrt(var1/n1 + var2/n2)
dof = ((var1/n1 + var2/n2)**2) / ((var1**2)/((n1**2)*(n1-1)) + (var2**2)/((n2**2)*(n2-1)))
t_crit = t.ppf(1 - alfa/2, dof)
diff_means = mean1 - mean2
ci_low = diff_means - t_crit * se_diff
ci_high = diff_means + t_crit * se_diff
print('Intervalo de confianza del 95% para la reducción esperada (Dieta 1 - Dieta 2):')
print(f'[{ci_low:.2f}, {ci_high:.2f}] mg/g')
print('La inferencia se limita a conejos similares bajo las mismas condiciones experimentales.\n')

# 7. Informe del ensayo
print('Informe del ensayo:')
print('Se realizó un experimento en conejos para evaluar el efecto de la suplementación con HDL-VHDL sobre el contenido de colesterol en aorta.')
print('Se observó una reducción significativa del colesterol en el grupo que recibió HDL-VHDL (Dieta 2) respecto al grupo control (Dieta 1),')
print('según el test t para muestras independientes (p-valor reportado arriba). El intervalo de confianza del 95% para la reducción media se reporta también.')
print('Se discuten los riesgos de errores tipo I y II y el alcance de la inferencia.')

# 8. Visualización
plt.figure(figsize=(7,5))
plt.boxplot([colesterol_dieta1, colesterol_dieta2], patch_artist=True)
plt.xticks([1, 2], ['Dieta 1', 'Dieta 2'])
plt.ylabel('Colesterol en aorta (mg/g)')
plt.title('Contenido de colesterol en aorta por grupo de dieta')
plt.show() 