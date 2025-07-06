# Ejercicio 5
# Planteamiento del problema: Expresión de microARN miR-150 en Cáncer de Próstata
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Conteos aproximados basados en la información del problema
condiciones = ["normal", "adenoma", "CCR"]
n_por_condicion = [53, 52, 81]

# Tabla de contingencia para antecedentes familiares
tabla_antecedentes = np.array([[6, 47],   # normal: sí, no
                               [8, 44],   # adenoma: sí, no
                               [12, 69]]) # CCR: sí, no

print("Tabla de contingencia - Condición vs Antecedentes familiares:")
print(tabla_antecedentes)

# Prueba de independencia
chi2, p, dof, expected = chi2_contingency(tabla_antecedentes)
print(f"\nChi2 = {chi2:.4f}, gl = {dof}, p-value = {p:.4f}")

# Proporciones
prop_antecedentes = tabla_antecedentes / tabla_antecedentes.sum(axis=1, keepdims=True)
print("\nProporciones de antecedentes por condición:")
print(np.round(prop_antecedentes, 3))

# Gráficos
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
# Gráfico de antecedentes familiares
for i, cond in enumerate(condiciones):
    axs[0, 0].bar([0+i*0.3, 1+i*0.3], tabla_antecedentes[i], width=0.3, label=cond)
axs[0, 0].set_xticks([0.3, 1.3])
axs[0, 0].set_xticklabels(["sí", "no"])
axs[0, 0].set_title("Antecedentes Familiares por Condición")
axs[0, 0].set_xlabel("Antecedentes")
axs[0, 0].set_ylabel("Frecuencia")
axs[0, 0].legend()
# Gráfico de proporciones
for i, cond in enumerate(condiciones):
    axs[0, 1].bar([0+i*0.3, 1+i*0.3], prop_antecedentes[i], width=0.3, label=cond)
axs[0, 1].set_xticks([0.3, 1.3])
axs[0, 1].set_xticklabels(["sí", "no"])
axs[0, 1].set_title("Proporción de Antecedentes por Condición")
axs[0, 1].set_xlabel("Antecedentes")
axs[0, 1].set_ylabel("Proporción")
axs[0, 1].legend()
# Simulación de datos de expresión miR-150
np.random.seed(123)
expr_normal = np.random.normal(2.5, 0.6, 53)
expr_adenoma = np.random.normal(2.4, 0.5, 52)
expr_ccr = np.random.normal(4.8, 0.7, 81)
# Boxplot de expresión
axs[1, 0].boxplot([expr_normal, expr_adenoma, expr_ccr], labels=["Normal", "Adenoma", "CCR"], patch_artist=True,
                  boxprops=dict(facecolor="lightblue"), medianprops=dict(color="black"))
axs[1, 0].set_title("Expresión de miR-150 por Condición")
axs[1, 0].set_xlabel("Condición")
axs[1, 0].set_ylabel("miR-150 (μU/mg tejido)")
# Estadísticas descriptivas
print("\nEstadísticas descriptivas de miR-150:")
for nombre, datos in zip(["Normal", "Adenoma", "CCR"], [expr_normal, expr_adenoma, expr_ccr]):
    print(f"\n{nombre} (n={len(datos)}):")
    print(f"  Media: {np.mean(datos):.2f}")
    print(f"  Mediana: {np.median(datos):.2f}")
    print(f"  DE: {np.std(datos, ddof=1):.2f}")
    print(f"  Rango: {np.min(datos):.2f} - {np.max(datos):.2f}")
# Histograma
axs[1, 1].hist(expr_ccr, color="lightcoral", alpha=0.7)
axs[1, 1].set_title("Distribución de miR-150 en CCR")
axs[1, 1].set_xlabel("miR-150 (μU/mg tejido)")
axs[1, 1].set_ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# Conclusión antecedentes familiares
decision = "existe" if p < 0.05 else "no hay evidencia de"
conclusion = f"{decision} asociación entre la condición del paciente y los antecedentes familiares."
print(f"\n**Antecedentes familiares:** Con p = {p:.4f}, {conclusion}")

# Conclusión expresión miR-150
print("\n**Expresión de miR-150:** Se observan diferencias notables en los niveles de expresión")
print("entre las condiciones, con valores más altos en pacientes con cáncer de próstata (CCR)")
print("comparado con pacientes normales y con adenoma. Esto sugiere que miR-150 podría ser")
print("un biomarcador útil para el diagnóstico de cáncer de próstata.") 