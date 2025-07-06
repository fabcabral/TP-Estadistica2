import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar datos y preparar
ruta = r'C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/curva_calib_AF.csv'
calib = pd.read_csv(ruta)
calib['dosis_mg'] = calib['dosisAF'] / 1000

# Dispersión y recta de regresión
plt.figure(figsize=(7,5))
plt.scatter(calib['dosis_mg'], calib['lectura'], color='black')
res = linregress(calib['dosis_mg'], calib['lectura'])
x_vals = np.linspace(calib['dosis_mg'].min(), calib['dosis_mg'].max(), 100)
y_vals = res.intercept + res.slope * x_vals
plt.plot(x_vals, y_vals, color='red', lw=2)
plt.title('Curva de calibración')
plt.xlabel('Dosis (mg)')
plt.ylabel('Lectura')
plt.show()

# Resumen del modelo
print('Modelo lineal (scipy.stats.linregress):')
print(f"Pendiente: {res.slope:.4f}")
print(f"Intercepto: {res.intercept:.4f}")
print(f"R: {res.rvalue:.4f}")
print(f"R²: {res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4g}")
print(f"Error estándar de la pendiente: {res.stderr:.4f}")

# Diagnóstico de residuos (residuos vs ajustados)
residuos = calib['lectura'] - (res.intercept + res.slope * calib['dosis_mg'])
plt.figure(figsize=(7,5))
plt.scatter(res.intercept + res.slope * calib['dosis_mg'], residuos)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Valores ajustados')
plt.ylabel('Residuos')
plt.title('Residuos vs Ajustados')
plt.show()

# Interpretaciones
print("\n✅ Pendiente: indica cuánto aumenta la lectura por mg de ácido fólico.")
print("✅ Intercepto: valor estimado de lectura sin ácido fólico (0 mg).")
print(f"✅ R²: {res.rvalue**2:.3f} → Porcentaje de variabilidad explicada.")

# Predicciones
for d in [15, 350]:
    pred = res.intercept + res.slope * d
    print(f"Predicción para dosis {d} mg: {pred:.2f}")

# Inversa para lectura 265 mg
dosis_para_265 = (265 - res.intercept) / res.slope
print(f"\n🔁 Inversa para lectura 265 mg: {dosis_para_265:.2f} mg") 