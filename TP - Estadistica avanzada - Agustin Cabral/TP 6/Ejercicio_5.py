import pandas as pd
import numpy as np
from scipy.stats import linregress, t

# Datos de lignina y volumen perdido en frutilla
frutilla_data = '''
8.01 12.46
7.85 11.91
12.56 9.71
13.33 8.15
8.22 10.99
9.53 10.27
9.63 9.84
12.48 9.19
9.50 10.51
12.47 8.49
10.22 9.84
8.53 10.69
15.40 7.57
7.88 11.55
9.36 10.96
9.35 10.69
10.74 10.03
6.62 13
11.90 8.85
12.30 9.78'''

from io import StringIO
frutilla = pd.read_csv(StringIO(frutilla_data), sep=' ', names=['lignina', 'volumen'])

# Modelo lineal y correlación
res = linregress(frutilla['lignina'], frutilla['volumen'])
print("Modelo lineal (scipy.stats.linregress):")
print(f"Pendiente: {res.slope:.4f}")
print(f"Intercepto: {res.intercept:.4f}")
print(f"R: {res.rvalue:.4f}")
print(f"R²: {res.rvalue**2:.4f}")
print(f"p-valor: {res.pvalue:.4g}")
print(f"Error estándar de la pendiente: {res.stderr:.4f}")
print(f"\n✅ Coeficiente de correlación: {res.rvalue:.3f}")

# Prueba t de significancia para la correlación
n = len(frutilla)
t_obs = res.rvalue * np.sqrt((n - 2) / (1 - res.rvalue**2))
p_value = 2 * t.cdf(-abs(t_obs), df=n-2)
print(f"\n🔎 p-valor para H0: rho = 0 → {p_value:.4f}") 