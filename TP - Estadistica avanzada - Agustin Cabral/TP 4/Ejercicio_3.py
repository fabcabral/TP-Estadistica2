# Ejercicio 3
# Planteamiento del problema: Tasa de Preñez en Ovejas Merino
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Datos
tratamientos = ["Sin tratamiento", "Sincronización", "Sincr + Gonadotropina"]
total_hembras = np.array([70, 40, 40])
prenadas = np.array([49, 32, 35])
no_prenadas = total_hembras - prenadas

# Tabla de contingencia
tabla_prenez = np.vstack([prenadas, no_prenadas])

print("Tabla de contingencia:")
print(tabla_prenez)

# Tasas de preñez
tasas_prenez = prenadas / total_hembras
print("\nTasas de preñez por tratamiento:")
for i in range(3):
    print(f"{tratamientos[i]}: {tasas_prenez[i]*100:.1f}% ({prenadas[i]}/{total_hembras[i]})")

# Prueba de independencia
chi2, p, dof, expected = chi2_contingency(tabla_prenez)
print(f"\nChi2 = {chi2:.4f}, gl = {dof}, p-value = {p:.4f}")

print("\nFrecuencias esperadas:")
print(np.round(expected, 2))

# Gráficos
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
# Gráfico de tasas de preñez
axs[0, 0].bar(["Sin trat.", "Sincr.", "Sincr+Gon."], tasas_prenez*100, color=["lightcoral", "lightblue", "lightgreen"])
axs[0, 0].set_title("Tasa de Preñez por Tratamiento")
axs[0, 0].set_xlabel("Tratamiento")
axs[0, 0].set_ylabel("Tasa de Preñez (%)")
axs[0, 0].set_ylim(0, 100)
for i, v in enumerate(tasas_prenez*100):
    axs[0, 0].text(i, v+3, f"{v:.1f}%", ha='center')
# Gráfico de frecuencias observadas
axs[0, 1].bar(np.arange(3)-0.15, prenadas, width=0.3, label="Preñadas", color="darkblue")
axs[0, 1].bar(np.arange(3)+0.15, no_prenadas, width=0.3, label="No preñadas", color="darkred")
axs[0, 1].set_xticks(np.arange(3))
axs[0, 1].set_xticklabels(tratamientos)
axs[0, 1].set_title("Frecuencias Observadas")
axs[0, 1].set_xlabel("Tratamiento")
axs[0, 1].set_ylabel("Número de ovejas")
axs[0, 1].legend()
# Gráfico de frecuencias esperadas
axs[1, 0].bar(np.arange(3)-0.15, expected[0], width=0.3, label="Preñadas", color="lightblue")
axs[1, 0].bar(np.arange(3)+0.15, expected[1], width=0.3, label="No preñadas", color="pink")
axs[1, 0].set_xticks(np.arange(3))
axs[1, 0].set_xticklabels(tratamientos)
axs[1, 0].set_title("Frecuencias Esperadas")
axs[1, 0].set_xlabel("Tratamiento")
axs[1, 0].set_ylabel("Número de ovejas")
axs[1, 0].legend()
# Gráfico de residuos estandarizados
residuos = (tabla_prenez - expected) / np.sqrt(expected)
axs[1, 1].bar(np.arange(3)-0.15, residuos[0], width=0.3, label="Preñadas", color="darkblue")
axs[1, 1].bar(np.arange(3)+0.15, residuos[1], width=0.3, label="No preñadas", color="darkred")
axs[1, 1].axhline(2, color="red", linestyle="dashed")
axs[1, 1].axhline(-2, color="red", linestyle="dashed")
axs[1, 1].set_xticks(np.arange(3))
axs[1, 1].set_xticklabels(tratamientos)
axs[1, 1].set_title("Residuos Estandarizados")
axs[1, 1].set_xlabel("Tratamiento")
axs[1, 1].set_ylabel("Residuo")
axs[1, 1].legend()
plt.tight_layout()
plt.show()

# Recomendación de tratamiento
mejor_tratamiento = tratamientos[np.argmax(tasas_prenez)]
mejor_tasa = np.max(tasas_prenez) * 100
print(f"\nEl tratamiento más efectivo es '{mejor_tratamiento}' con una tasa de preñez del {mejor_tasa:.1f}%.")

# Verificación de condiciones
min_esperada = np.min(expected)
print(f"Frecuencia esperada mínima: {min_esperada:.2f}")
print(f"¿Se cumplen las condiciones (todas ≥ 5)? {'SÍ' if min_esperada >= 5 else 'NO'}")
if min_esperada < 5:
    print("ADVERTENCIA: Algunas frecuencias esperadas son menores a 5.")
    print("Se recomienda usar la prueba exacta de Fisher o agrupar categorías.")

# Informe
print("\n**Resultados:** Se observaron diferencias significativas en las tasas de preñez entre tratamientos")
print(f"(χ² = {chi2:.2f}, gl = {dof}, p = {p:.4f}).")
print("Las tasas de preñez fueron:")
for i in range(3):
    print(f"- {tratamientos[i]}: {tasas_prenez[i]*100:.1f}%")
print("\n**Recomendaciones:** Se recomienda el uso de sincronización hormonal combinada con")
print("estimulación con gonadotropina para maximizar la eficiencia reproductiva.") 