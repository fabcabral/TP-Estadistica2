# Ejercicio: Análisis de Fosfolípidos en Aceite de Girasol
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lectura y preparación de datos
datos_girasol = pd.read_csv("C:/Users/fabri/Downloads/Datos en CSV-20250312T201648Z-001/Datos en CSV/girasol.csv")
fosfolipidos = datos_girasol['fosfolipidos'].astype(str).str.replace(',', '.').astype(float)

# Estadísticas descriptivas básicas
n_muestras = len(fosfolipidos)
media_fosfo = np.mean(fosfolipidos)
mediana_fosfo = np.median(fosfolipidos)
desv_est = np.std(fosfolipidos, ddof=1)
coef_var = 100 * desv_est / media_fosfo
p10 = np.percentile(fosfolipidos, 10)

# Análisis de calidad
muestras_baja_calidad = np.sum(fosfolipidos > 0.40)
porcentaje_baja_calidad = 100 * muestras_baja_calidad / n_muestras

# Visualización
plt.boxplot(fosfolipidos, patch_artist=True, boxprops=dict(facecolor='skyblue'))
plt.title("Distribucion de Fosfolipidos")
plt.ylabel("Concentracion (g/100g)")
plt.show()

plt.hist(fosfolipidos, bins='fd', color='lightgreen')
plt.title("Frecuencia de Concentraciones")
plt.xlabel("Concentracion (g/100g)")
plt.show()

# Resultados
print("\nAnalisis de Fosfolipidos en Aceite de Girasol\n")
print(f"Tamano de muestra: {n_muestras}")
print(f"Media: {media_fosfo:.4f} g/100g")
print(f"Mediana: {mediana_fosfo:.4f} g/100g")
print(f"Desviacion estandar: {desv_est:.4f} g/100g")
print(f"Coeficiente de variacion: {coef_var:.2f} %")
print("\nAnalisis de Calidad\n")
print(f"Muestras de baja calidad: {muestras_baja_calidad}")
print(f"Porcentaje de baja calidad: {porcentaje_baja_calidad:.2f} %")
print(f"Percentil 10: {p10:.4f} g/100g")

# Evaluación de la distribución
print("\nCaracteristicas de la Distribucion\n")
if abs(media_fosfo - mediana_fosfo) < 0.01:
    print("Distribucion aproximadamente simetrica")
elif media_fosfo > mediana_fosfo:
    print("Asimetria positiva")
else:
    print("Asimetria negativa")

if coef_var < 10:
    print("Distribucion homogenea")
else:
    print("Distribucion heterogenea") 