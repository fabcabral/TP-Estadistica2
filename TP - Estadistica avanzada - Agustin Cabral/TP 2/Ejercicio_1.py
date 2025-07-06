# Ejercicio 1
# El promedio mostrado en el primer grafico representa un parametro poblacional, generalmente desconocido y que para una poblacion y momento determinados es unico, es decir, es una constante (mu). En este caso, su valor es 16.
# El promedio calculado con los primeros 5 datos es un estadistico muestral, ya que proviene de una muestra. Puede variar, por lo que es una variable aleatoria (x-barra).

# Ejercicio 2
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
poblacion = np.random.normal(loc=16, scale=5, size=100000)
plt.hist(poblacion, bins=40, color="lightblue")
plt.title("Poblacion Normal (mu=16, sigma=5)")
plt.xlabel("X")
plt.axvline(np.mean(poblacion), color="blue", linewidth=2)
plt.axvline(np.median(poblacion), color="magenta", linewidth=2)
plt.show()

n = 5
reps = 10000
medias = [np.mean(np.random.choice(poblacion, n)) for _ in range(reps)]
plt.hist(medias, bins=40, color="lightgreen")
plt.title("Distribucion Muestral de la Media (n=5)")
plt.xlabel("Media Muestral")
plt.show()

print("Media poblacional:", np.mean(poblacion))
print("Media muestral:", np.mean(medias))
print("Desvio estandar de las medias:", np.std(medias, ddof=1))
print("Teorico sigma/sqrt(n):", np.std(poblacion, ddof=1)/np.sqrt(n))

# Ejercicio 3
n2 = 25
medias2 = [np.mean(np.random.choice(poblacion, n2)) for _ in range(reps)]
plt.hist(medias2, bins=40, color="orange")
plt.title("Distribucion Muestral (n=25)")
plt.xlabel("Media Muestral")
plt.show()

print("Error estandar n=5:", np.std(medias, ddof=1))
print("Error estandar n=25:", np.std(medias2, ddof=1))

# Ejercicio 4
poblacion_unif = np.random.uniform(0, 32, 100000)
medias_unif = [np.mean(np.random.choice(poblacion_unif, n2)) for _ in range(reps)]
plt.hist(medias_unif, bins=40, color="cyan")
plt.title("Media Muestral (Uniforme, n=25)")
plt.xlabel("Media Muestral")
plt.show()

# Ejercicio 5
poblacion_exp = np.random.exponential(scale=16, size=100000)
medias_exp = [np.mean(np.random.choice(poblacion_exp, n2)) for _ in range(reps)]
plt.hist(medias_exp, bins=40, color="salmon")
plt.title("Media Muestral (Exponencial, n=25)")
plt.xlabel("Media Muestral")
plt.show()

# Ejercicio 6
medianas = [np.median(np.random.choice(poblacion_exp, n2)) for _ in range(reps)]
plt.hist(medianas, bins=40, color="gray")
plt.title("Distribucion de la Mediana")
plt.xlabel("Mediana Muestral")
plt.show() 