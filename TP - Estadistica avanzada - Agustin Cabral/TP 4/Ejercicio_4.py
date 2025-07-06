# Ejercicio 4
# Planteamiento del problema: Asociación entre Mutación RYR1 y Sexo
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

genotipos = ["CC", "CT", "TT"]
sexos = ["macho", "hembra"]
tabla_ryr1 = np.array([[182, 151],  # CC
                       [71, 58],    # CT
                       [8, 7]])     # TT

print("Tabla de contingencia - Genotipo vs Sexo:")
print(tabla_ryr1)

# Totales marginales
print("\nTotales marginales:")
print("Por genotipo:", np.sum(tabla_ryr1, axis=1))
print("Por sexo:", np.sum(tabla_ryr1, axis=0))
print("Total general:", np.sum(tabla_ryr1))

# Prueba de independencia
chi2, p, dof, expected = chi2_contingency(tabla_ryr1)
print(f"\nChi2 = {chi2:.4f}, gl = {dof}, p-value = {p:.4f}")

print("\nFrecuencias esperadas:")
print(np.round(expected, 2))

# Proporciones
prop_filas = tabla_ryr1 / tabla_ryr1.sum(axis=1, keepdims=True)
prop_columnas = tabla_ryr1 / tabla_ryr1.sum(axis=0, keepdims=True)
print("\nProporciones por genotipo (filas):")
print(np.round(prop_filas, 3))
print("\nProporciones por sexo (columnas):")
print(np.round(prop_columnas, 3))

# Gráficos
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
# Frecuencias observadas
axs[0, 0].bar(np.arange(2)-0.2, tabla_ryr1[0], width=0.2, label=genotipos[0], color="lightblue")
axs[0, 0].bar(np.arange(2), tabla_ryr1[1], width=0.2, label=genotipos[1], color="lightgreen")
axs[0, 0].bar(np.arange(2)+0.2, tabla_ryr1[2], width=0.2, label=genotipos[2], color="lightcoral")
axs[0, 0].set_xticks(np.arange(2))
axs[0, 0].set_xticklabels(sexos)
axs[0, 0].set_title("Distribución de Genotipos RYR1 por Sexo")
axs[0, 0].set_xlabel("Sexo")
axs[0, 0].set_ylabel("Frecuencia")
axs[0, 0].legend()
# Proporciones por genotipo
axs[0, 1].bar(np.arange(3)-0.1, prop_filas[:,0], width=0.2, label=sexos[0], color="darkblue")
axs[0, 1].bar(np.arange(3)+0.1, prop_filas[:,1], width=0.2, label=sexos[1], color="darkgreen")
axs[0, 1].set_xticks(np.arange(3))
axs[0, 1].set_xticklabels(genotipos)
axs[0, 1].set_title("Proporción de Sexos por Genotipo")
axs[0, 1].set_xlabel("Genotipo")
axs[0, 1].set_ylabel("Proporción")
axs[0, 1].legend()
# Residuos estandarizados
residuos = (tabla_ryr1 - expected) / np.sqrt(expected)
axs[1, 0].bar(np.arange(2)-0.2, residuos[0], width=0.2, label=genotipos[0], color="lightblue")
axs[1, 0].bar(np.arange(2), residuos[1], width=0.2, label=genotipos[1], color="lightgreen")
axs[1, 0].bar(np.arange(2)+0.2, residuos[2], width=0.2, label=genotipos[2], color="lightcoral")
axs[1, 0].axhline(2, color="red", linestyle="dashed")
axs[1, 0].axhline(-2, color="red", linestyle="dashed")
axs[1, 0].set_xticks(np.arange(2))
axs[1, 0].set_xticklabels(sexos)
axs[1, 0].set_title("Residuos Estandarizados")
axs[1, 0].set_xlabel("Sexo")
axs[1, 0].set_ylabel("Residuo")
axs[1, 0].legend()
# Frecuencias esperadas
axs[1, 1].bar(np.arange(2)-0.2, expected[0], width=0.2, label=genotipos[0], color="lightblue")
axs[1, 1].bar(np.arange(2), expected[1], width=0.2, label=genotipos[1], color="lightgreen")
axs[1, 1].bar(np.arange(2)+0.2, expected[2], width=0.2, label=genotipos[2], color="lightcoral")
axs[1, 1].set_xticks(np.arange(2))
axs[1, 1].set_xticklabels(sexos)
axs[1, 1].set_title("Frecuencias Esperadas")
axs[1, 1].set_xlabel("Sexo")
axs[1, 1].set_ylabel("Frecuencia")
axs[1, 1].legend()
plt.tight_layout()
plt.show()

# Conclusión
alpha = 0.05
decision = "rechazamos" if p < alpha else "no rechazamos"
conclusion = ("Existe asociación entre el genotipo RYR1 y el sexo." if p < alpha
              else "No hay evidencia de asociación entre el genotipo RYR1 y el sexo.")
print(f"\nCon p = {p:.4f}, {decision} la hipótesis de independencia.")
print(conclusion)

# Verificar condiciones
min_esperada = np.min(expected)
print(f"Frecuencia esperada mínima: {min_esperada:.2f}")
print(f"¿Se cumplen las condiciones? {'SÍ' if min_esperada >= 5 else 'NO'}") 