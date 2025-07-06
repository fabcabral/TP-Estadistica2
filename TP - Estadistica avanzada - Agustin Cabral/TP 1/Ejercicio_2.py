# Ejercicio 2: Análisis de Alturas en la Distribución Normal
import numpy as np
from scipy.stats import norm

# Parámetros de la distribución normal
y_mu = 146    # media en cm
sigma = 8     # desviación estándar en cm

# Cálculo de puntajes Z para casos específicos
z_alto = (170 - y_mu) / sigma
z_medio = (148 - y_mu) / sigma

# Cálculo de altura para Z dado
altura_z_positivo = y_mu + 1.5 * sigma

# Cálculo de rangos para Z = ±2.25
rango_inferior = y_mu - 2.25 * sigma
rango_superior = y_mu + 2.25 * sigma

# Vector de alturas a clasificar
alturas_muestra = np.array([150, 130, 165, 140])

# Función de clasificación
def clasificar_altura(altura):
    z_score = (altura - y_mu) / sigma
    if z_score < -1:
        return "Inusualmente baja"
    elif z_score > 1:
        return "Inusualmente alta"
    else:
        return "Cercana a la media"

# Aplicar clasificación
resultados = [clasificar_altura(a) for a in alturas_muestra]

# Cálculo de percentiles específicos
p90 = y_mu + norm.ppf(0.90) * sigma
p99 = y_mu + norm.ppf(0.99) * sigma

# Presentación de resultados
print("\nAnalisis de Alturas en la Distribucion Normal\n")

print("\nAnalisis de Casos Individuales:")
print(f"Caso 1: 170 cm esta a {z_alto:.2f} DE del promedio")
print(f"Caso 2: 148 cm esta a {z_medio:.2f} DE del promedio")
print(f"Caso 3: A 1.5 DE corresponde {altura_z_positivo:.2f} cm")

print("\nRango de Referencia (±2.25 DE):")
print(f"Limite inferior: {rango_inferior:.2f} cm")
print(f"Limite superior: {rango_superior:.2f} cm")

print("\nClasificacion de Muestra:")
for altura, resultado in zip(alturas_muestra, resultados):
    print(f"Altura {altura} cm: {resultado}")

print("\nPercentiles de Referencia:")
print(f"Percentil 90: {p90:.2f} cm")
print(f"Percentil 99: {p99:.2f} cm") 