import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Datos
# Filas: Disturbio (Sí, No), Columnas: Mosqueta (Presente, Ausente)
tabla = np.array([[15, 8], [10, 7]])

# Hipótesis
# H0: No hay asociación entre disturbio y presencia de rosa mosqueta
# H1: Hay asociación

alfa = 0.05
chi2, pval, dof, expected = chi2_contingency(tabla, correction=False)

print('Test chi-cuadrado:')
print(f'Estadístico chi2 = {chi2:.4f}, p-valor = {pval:.4f}')
if pval < alfa:
    print('Conclusión: Se rechaza H0. Hay asociación entre disturbio y rosa mosqueta.')
else:
    print('Conclusión: No se rechaza H0. No hay evidencia de asociación.')

# Visualización
groups = ['Disturbio Sí', 'Disturbio No']
present = [15, 10]
absent = [8, 7]
bar_width = 0.35
x = np.arange(len(groups))
plt.bar(x, present, bar_width, label='Presente', color='green')
plt.bar(x, absent, bar_width, bottom=present, label='Ausente', color='gray')
plt.xticks(x, groups)
plt.ylabel('Número de parcelas')
plt.title('Presencia de rosa mosqueta según disturbio')
plt.legend()
plt.show() 