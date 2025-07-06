# Ejercicio 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
media_poblacional = 100
varianza_poblacional = 100
tamano_muestra = 10
num_muestras = 100
nivel_confianza = 0.95
desviacion_estandar = np.sqrt(varianza_poblacional)
ICs = np.empty((num_muestras, 2))
aciertos = 0

for i in range(num_muestras):
    muestra = np.random.normal(loc=media_poblacional, scale=desviacion_estandar, size=tamano_muestra)
    media_muestra = np.mean(muestra)
    error_estandar = desviacion_estandar / np.sqrt(tamano_muestra)
    z_critico = norm.ppf(1 - (1 - nivel_confianza) / 2)
    LI = media_muestra - z_critico * error_estandar
    LS = media_muestra + z_critico * error_estandar
    ICs[i, :] = [LI, LS]
    if LI <= media_poblacional <= LS:
        aciertos += 1

plt.figure(figsize=(10, 5))
for i in range(num_muestras):
    plt.plot([i+1, i+1], [ICs[i, 0], ICs[i, 1]], color='blue', linewidth=2)
plt.axhline(media_poblacional, color='red', linewidth=2)
plt.xlabel('Muestra')
plt.ylabel('Intervalos de Confianza')
plt.title(f'Cobertura: {aciertos / num_muestras * 100:.1f}%')
plt.show()

# Ejercicio 2
# 1. No se obtiene exactamente el 95% por azar, pero el metodo es valido.
# 2. Si el nivel de confianza sube al 99%, los intervalos seran mas amplios y cubriran mas veces la media.
# 3. Si el tamano de muestra aumenta a 20, los intervalos se hacen mas estrechos.
# 4. Se espera mayor precision, pero no necesariamente mayor cobertura.
# 5. Aumentar la cantidad de intervalos mejora la estimacion del porcentaje real de cobertura. 