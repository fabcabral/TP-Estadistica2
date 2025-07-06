# Ejercicio 1
import pandas as pd
import numpy as np
from scipy.stats import norm
# Cambia la ruta si es necesario
datos = pd.read_csv(r'C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/RYR1.csv')

tabla = datos['Genotipo'].value_counts()
total = tabla.sum()
prop = tabla / total

z = norm.ppf(0.975)
LI = prop - z * np.sqrt(prop * (1 - prop) / total)
LS = prop + z * np.sqrt(prop * (1 - prop) / total)

print(np.round(pd.concat([prop, LI, LS], axis=1) * 100, 2))

# Ejercicio 2
amplitud = LS - LI
print('Amplitud:', np.round(amplitud, 4))

e = 0.01
p = 0.5
n_necesario = np.ceil((z**2 * p * (1 - p)) / e**2)
print('Tamaño muestral necesario para ±1% de error:', n_necesario)

# Ejercicio 3
def ic_media(x):
    n = len(x)
    media = np.mean(x)
    sd = np.std(x, ddof=1)
    se = sd / np.sqrt(n)
    from scipy.stats import t
    t_crit = t.ppf(0.975, df=n-1)
    li = media - t_crit * se
    ls = media + t_crit * se
    return pd.Series({'n': n, 'media': media, 'LI': li, 'LS': ls})

resultados = datos.groupby('Genotipo')['pH'].apply(ic_media)
# Convertir a DataFrame para acceder por columna
resultados_df = resultados.unstack()
print(np.round(resultados_df, 2))

amplitud_pH = resultados_df['LS'] - resultados_df['LI']
print('Amplitud de los IC de pH:', np.round(amplitud_pH, 4))

n_actual = resultados_df['n']
n_necesario_dup = np.ceil(n_actual * 4)
print(pd.DataFrame({'n_actual': n_actual, 'n_necesario_dup': n_necesario_dup}))

# Ejercicio 4
# 1. Proporciones poblacionales de genotipos (estimador: p-hat)
# 4. Medias poblacionales de pH por genotipo (estimador: x-barra) 