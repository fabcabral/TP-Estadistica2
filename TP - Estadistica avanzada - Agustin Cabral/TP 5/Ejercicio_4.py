# Ejercicio 4
# Problema: pH post mortem por genotipo RyR1 con IC del 95%
import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Cambia la ruta si es necesario
datos = pd.read_csv("C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/RYR1.csv")
datos["Genotipo"] = datos["Genotipo"].astype(str)
datos["pH"] = pd.to_numeric(datos["pH"], errors="coerce")

def ic_95(x):
    n = len(x)
    m = np.mean(x)
    se = np.std(x, ddof=1) / np.sqrt(n)
    error = t.ppf(0.975, df=n-1) * se
    return pd.Series({"Media": m, "IC_inf": m - error, "IC_sup": m + error, "SD": np.std(x, ddof=1), "N": n})

resumen = datos.groupby("Genotipo")["pH"].apply(ic_95).unstack()
resumen = resumen.round(2)
resumen = resumen.reset_index()
print("Tabla 1. pH post mortem por genotipo RyR1 con IC del 95%:")
print(resumen)

# ANOVA de un factor usando scipy
# Agrupar los valores de pH por genotipo
genotipos = datos['Genotipo'].unique()
grupos_ph = [datos[datos['Genotipo'] == g]['pH'].dropna() for g in genotipos]
f_stat, p_anova = f_oneway(*grupos_ph)
print(f"\nANOVA (scipy): F = {f_stat:.2f}, p = {p_anova:.4f}")

# Boxplot
datos.boxplot(column="pH", by="Genotipo", grid=False, patch_artist=True,
              boxprops=dict(facecolor="#66c2a5"), medianprops=dict(color="black"))
plt.title("Distribución del pH por Genotipo RyR1")
plt.suptitle("")
plt.ylabel("pH a los 45 min post mortem")
plt.xlabel("Genotipo")
plt.show() 