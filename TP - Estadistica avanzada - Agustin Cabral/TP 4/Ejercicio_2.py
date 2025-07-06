# Ejercicio 2
# Planteamiento del problema: Calidad de Semillas de Soja
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt

# Frecuencias observadas
obs_semillas = np.array([80, 15, 5])
nombres_calidad = ["Alta", "Media", "Baja"]

# Probabilidades esperadas según el productor
prob_esperadas_semillas = np.array([0.95, 0.03, 0.02])

# Tamaño de muestra
total = obs_semillas.sum()

# Frecuencias esperadas
esp_semillas = total * prob_esperadas_semillas

# Tabla comparativa
print("Tabla comparativa - Calidad de semillas:")
print("Calidad\tObservado\tEsperado\tProp.Esperada\tProp.Observada")
for i in range(3):
    print(f"{nombres_calidad[i]}\t{obs_semillas[i]}\t\t{esp_semillas[i]:.2f}\t\t{prob_esperadas_semillas[i]:.3f}\t\t{obs_semillas[i]/total:.3f}")

# Prueba chi-cuadrado
chi2, p = chisquare(obs_semillas, f_exp=esp_semillas)
print(f"\nChi2 = {chi2:.4f}, p-value = {p:.4f}")

# Gráficos
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
# Barras observados vs esperados
axs[0].bar(np.arange(3)-0.15, obs_semillas, width=0.3, label="Observado", color="darkgreen")
axs[0].bar(np.arange(3)+0.15, esp_semillas, width=0.3, label="Esperado", color="orange")
axs[0].set_xticks(np.arange(3))
axs[0].set_xticklabels(nombres_calidad)
axs[0].set_title("Calidad de Semillas")
axs[0].set_xlabel("Calidad")
axs[0].set_ylabel("Frecuencia")
axs[0].legend()
# Gráfico de proporciones
prop_obs = obs_semillas / total
axs[1].bar(np.arange(3)-0.15, prop_obs, width=0.3, label="Observada", color="darkgreen")
axs[1].bar(np.arange(3)+0.15, prob_esperadas_semillas, width=0.3, label="Esperada", color="orange")
axs[1].set_xticks(np.arange(3))
axs[1].set_xticklabels(nombres_calidad)
axs[1].set_title("Proporciones")
axs[1].set_xlabel("Calidad")
axs[1].set_ylabel("Proporción")
axs[1].legend()
plt.tight_layout()
plt.show()

# Conclusión
alpha = 0.05
decision = "rechazamos" if p < alpha else "no rechazamos"
conclusion = ("La calidad del lote NO corresponde a las proporciones garantizadas por el productor."
              if p < alpha else "La calidad del lote corresponde a las proporciones garantizadas por el productor.")
print(f"\nCon p = {p:.4f}, {decision} H₀. {conclusion}") 