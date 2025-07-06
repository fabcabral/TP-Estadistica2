import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, t

# Cargar datos y limpiar
ruta = r'C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/ratones_etanol.csv'
etanol = pd.read_csv(ruta)
etanol = etanol.dropna()
etanol['etanol'] = pd.to_numeric(etanol['etanol'], errors='coerce')
etanol['vol'] = pd.to_numeric(etanol['vol'], errors='coerce')

# Modelo lineal y correlación
res = linregress(etanol['etanol'], etanol['vol'])
print("Modelo lineal (scipy.stats.linregress):")
print(f"Pendiente: {res.slope:.4f}")
print(f"Intercepto: {res.intercept:.4f}")
print(f"R: {res.rvalue:.4f}")
print(f"R²: {res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4g}")
print(f"Error estándar de la pendiente: {res.stderr:.4f}")

# Diagnóstico de residuos (residuos vs ajustados)
residuos = etanol['vol'] - (res.intercept + res.slope * etanol['etanol'])
plt.figure(figsize=(7,5))
plt.scatter(res.intercept + res.slope * etanol['etanol'], residuos)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Valores ajustados')
plt.ylabel('Residuos')
plt.title('Residuos vs Ajustados')
plt.show()

# Interpretación
print("\n✅ Pendiente negativa: a mayor etanol, menor volumen cerebral.")
print(f"✅ R²: {res.rvalue**2:.3f}\n")

# Predicción con intervalos de confianza manuales
X = etanol['etanol']
Y = etanol['vol']
n = len(X)
mean_x = np.mean(X)
se = res.stderr
s_yx = np.sqrt(np.sum((Y - (res.intercept + res.slope * X))**2) / (n-2))
t_crit = t.ppf(0.975, df=n-2)
for x0 in [1.5, 2, 5]:
    y0 = res.intercept + res.slope * x0
    se_pred = s_yx * np.sqrt(1/n + (x0 - mean_x)**2 / np.sum((X - mean_x)**2))
    ci_lower = y0 - t_crit * se_pred
    ci_upper = y0 + t_crit * se_pred
    print(f"Predicción para etanol={x0}: {y0:.2f} (IC 95%: {ci_lower:.2f}, {ci_upper:.2f})")

# Intervalos de confianza para los coeficientes
print("\nIntervalos de confianza para la pendiente:")
ci_slope = (res.slope - t_crit * res.stderr, res.slope + t_crit * res.stderr)
print(f"Pendiente: {ci_slope}") 