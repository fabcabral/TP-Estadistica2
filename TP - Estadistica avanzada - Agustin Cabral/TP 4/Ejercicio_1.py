# Ejercicio 1
# Planteamiento del problema: Prueba de bondad de ajuste (Cruzamiento de Dihíbridos)
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt

# Frecuencias observadas
observados = np.array([85, 28, 35, 12])
nombres_fenotipos = ["A-B-", "A-bb", "aaB-", "aabb"]

# Probabilidades esperadas según el modelo mendeliano
probabilidades_esperadas = np.array([9/16, 3/16, 3/16, 1/16])

# Tamaño de la muestra
total = observados.sum()
print("Tamaño de muestra:", total)

# Frecuencias esperadas
esperados = total * probabilidades_esperadas

# Tabla comparativa
print("\nTabla comparativa:")
print("Fenotipo\tObservado\tEsperado\tProp.Esperada\tProp.Observada")
for i in range(4):
    print(f"{nombres_fenotipos[i]}\t\t{observados[i]}\t\t{esperados[i]:.2f}\t\t{probabilidades_esperadas[i]:.4f}\t\t{observados[i]/total:.4f}")

# Prueba de bondad de ajuste
chi2, p = chisquare(observados, f_exp=esperados)
print(f"\nChi2 = {chi2:.4f}, p-value = {p:.4f}")

# Gráficos
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
# Barras observados vs esperados
axs[0].bar(np.arange(4)-0.15, observados, width=0.3, label="Observado", color="lightblue")
axs[0].bar(np.arange(4)+0.15, esperados, width=0.3, label="Esperado", color="lightcoral")
axs[0].set_xticks(np.arange(4))
axs[0].set_xticklabels(nombres_fenotipos)
axs[0].set_title("Frecuencias Observadas vs Esperadas")
axs[0].set_xlabel("Fenotipo")
axs[0].set_ylabel("Frecuencia")
axs[0].legend()
# Residuos estandarizados
residuos = (observados - esperados) / np.sqrt(esperados)
axs[1].bar(nombres_fenotipos, residuos, color=["red" if abs(r)>2 else "lightgreen" for r in residuos])
axs[1].axhline(2, color="red", linestyle="dashed")
axs[1].axhline(-2, color="red", linestyle="dashed")
axs[1].set_title("Residuos Estandarizados")
axs[1].set_xlabel("Fenotipo")
axs[1].set_ylabel("Residuo")
plt.tight_layout()
plt.show()

# Conclusión
alpha = 0.05
decision = "rechazamos" if p < alpha else "no rechazamos"
conclusion = ("Los datos NO se ajustan al modelo genético postulado." if p < alpha
              else "Los datos se ajustan al modelo genético postulado.")
print(f"\nCon un valor p = {p:.4f} y α = {alpha:.2f}, {decision} la hipótesis nula.")
print(conclusion) 