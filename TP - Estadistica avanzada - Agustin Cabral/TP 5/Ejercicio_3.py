# Ejercicio 3
# Problema: Niveles de HDL por genotipo con IC del 95%
import pandas as pd
import numpy as np
from scipy.stats import t

# Cambia la ruta si es necesario
datos = pd.read_csv("C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/PECT.csv")
print("Columnas originales:", datos.columns.tolist())
# Ajustar nombres según cantidad de columnas
if len(datos.columns) == 2:
    datos.columns = ["genotipo", "HDL"]
elif len(datos.columns) == 3:
    datos.columns = ["genotipo", "HDL", "col3"]  # Ajusta el nombre de la tercera columna si es necesario
# Si hay más columnas, puedes ajustar aquí

datos["HDL"] = pd.to_numeric(datos["HDL"], errors="coerce")

def ic_95(x):
    n = len(x)
    m = np.mean(x)
    se = np.std(x, ddof=1) / np.sqrt(n)
    error = t.ppf(0.975, df=n-1) * se
    return pd.Series({"Media": m, "IC_inf": m - error, "IC_sup": m + error, "SD": np.std(x, ddof=1), "N": n})

resumen = datos.groupby("genotipo")["HDL"].apply(ic_95).unstack()
resumen = resumen.round(2)
resumen = resumen.reset_index()
print("Tabla 1. Niveles de HDL por genotipo con IC del 95%:")
print(resumen) 