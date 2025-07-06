import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, ttest_ind

# Cargar datos
data_path = r'C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/Ru.id.csv'
ru = pd.read_csv(data_path)

# Gráfico de dispersión
plt.figure(figsize=(7,5))
plt.scatter(ru['RU'], ru['ID'], c='black')
plt.title('Concentración RU vs Daño ADN')
plt.xlabel('RU')
plt.ylabel('Índice de Daño')
plt.show()

# Modelo numérico (lineal)
res = linregress(ru['RU'], ru['ID'])
print('--- Modelo numérico (scipy.stats.linregress) ---')
print(f"Pendiente: {res.slope:.4f}")
print(f"Intercepto: {res.intercept:.4f}")
print(f"R: {res.rvalue:.4f}")
print(f"R²: {res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4g}")
print(f"Error estándar de la pendiente: {res.stderr:.4f}")

# Modelo categórico (ANOVA simplificado)
ru['RU_factor'] = ru['RU'].astype('category')
group_means = ru.groupby('RU_factor')['ID'].mean()
print('\n--- Modelo categórico (medias por grupo) ---')
print(group_means)

# Comparación de R²
print(f"\nR² modelo numérico: {res.rvalue**2:.3f}\n")

# Interpretación
print("\n✅ Si RU se mide como numérico, asumimos relación lineal. Si como factor, se analiza diferencia de medias.\n")

# Predicciones
for val in [1500, 2200]:
    pred = res.intercept + res.slope * val
    print(f"Predicción para RU={val}: {pred:.2f}") 