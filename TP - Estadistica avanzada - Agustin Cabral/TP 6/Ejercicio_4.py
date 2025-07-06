import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar datos
aedes = pd.read_csv(r'C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/aedes.csv')

# Modelo lineal y correlación
res = linregress(aedes['temperatura'], aedes['tiempo_desarr'])
print("Modelo lineal (scipy.stats.linregress):")
print(f"Pendiente: {res.slope:.4f}")
print(f"Intercepto: {res.intercept:.4f}")
print(f"R: {res.rvalue:.4f}")
print(f"R²: {res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4g}")
print(f"Error estándar de la pendiente: {res.stderr:.4f}")

# Interpretación
print("\n✅ Pendiente negativa: A mayor temperatura, menor tiempo de desarrollo.")
print(f"✅ R²: {res.rvalue**2:.3f}\n")

# Visualización
plt.figure(figsize=(7,5))
plt.scatter(aedes['temperatura'], aedes['tiempo_desarr'], c='black')
plt.title('Temperatura vs Tiempo de desarrollo')
plt.xlabel('Temperatura')
plt.ylabel('Tiempo de desarrollo')
x_vals = np.linspace(aedes['temperatura'].min(), aedes['temperatura'].max(), 100)
y_vals = res.intercept + res.slope * x_vals
plt.plot(x_vals, y_vals, color='red')
plt.show() 