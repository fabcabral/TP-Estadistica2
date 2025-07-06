import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, ttest_rel

# Datos
prot = pd.DataFrame({
    'quimico': [14.3, 4, 15.9, 14.3, 14.3, 13.6, 8, 13.3, 5.2, 10.8],
    'NIRS':    [11.4, 4.9, 15.3, 14.2, 10.3, 10, 8.4, 13.5, 5, 10.3]
})

# Modelo lineal con linregress
res = linregress(prot['quimico'], prot['NIRS'])
print('Modelo lineal (scipy.stats.linregress):')
print(f"Pendiente: {res.slope:.4f}")
print(f"Intercepto: {res.intercept:.4f}")
print(f"R: {res.rvalue:.4f}")
print(f"R²: {res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4g}")
print(f"Error estándar de la pendiente: {res.stderr:.4f}")
correl = prot['quimico'].corr(prot['NIRS'])
print(f"\n✅ Correlación: {correl:.3f}\n")

# Prueba de diferencia entre métodos (t-test pareado)
test = ttest_rel(prot['quimico'], prot['NIRS'])
print(test)
if test.pvalue < 0.05:
    print("\n✅ Si p < 0.05, hay diferencia significativa entre métodos.")
else:
    print("\n✅ No hay diferencia significativa entre métodos.")

# Visualización
plt.figure(figsize=(7,5))
plt.scatter(prot['quimico'], prot['NIRS'], c='black')
plt.title('Comparación Químico vs NIRS')
plt.xlabel('Químico')
plt.ylabel('NIRS')
# Línea de regresión
x_vals = np.linspace(prot['quimico'].min(), prot['quimico'].max(), 100)
y_vals = res.intercept + res.slope * x_vals
plt.plot(x_vals, y_vals, color='red')
plt.show() 