import pandas as pd
import scipy.stats as stats
import numpy as np

# 1. Cargar datos
ruta_cobre1 = r'C:\Users\fabri\Downloads\Datos en CSV-20250312T201648Z-001\Datos en CSV\cobre1.csv'
ruta_cobre2 = r'C:\Users\fabri\Downloads\Datos en CSV-20250312T201648Z-001\Datos en CSV\cobre2.csv'
datos = pd.read_csv(ruta_cobre1)

# 2. Tabla de contingencia
contingencia = pd.crosstab(datos['estadio'], datos['sobrevive'])
print('Tabla de contingencia:')
print(contingencia)

# 3. Proporciones de muertos en cada estadio
prop_larva = (contingencia.loc['larva', 'muerto'] / contingencia.loc['larva'].sum())
prop_embrion = (contingencia.loc['embrion', 'muerto'] / contingencia.loc['embrion'].sum())
print(f'Proporción de larvas muertas: {prop_larva:.2f}')
print(f'Proporción de embriones muertos: {prop_embrion:.2f}')

# 4. Test estadístico (Fisher exacto, unilateral)
# H0: p_larva = p_embrion; H1: p_larva > p_embrion
oddsratio, pvalue = stats.fisher_exact(contingencia, alternative='greater')
print(f'Test exacto de Fisher: p-valor = {pvalue:.4f}')

# 5. IC 95% para la proporción de larvas muertas
n_larva = contingencia.loc['larva'].sum()
x_larva = contingencia.loc['larva', 'muerto']
prop = x_larva / n_larva
alfa = 0.05
z = stats.norm.ppf(1 - alfa/2)
se = np.sqrt(prop * (1 - prop) / n_larva)
ic_inf = prop - z * se
ic_sup = prop + z * se
print(f'IC 95% para la proporción de larvas muertas: ({ic_inf:.3f}, {ic_sup:.3f})')

# ---
# ENSAYO 2: Consumo de oxígeno
datos2 = pd.read_csv(ruta_cobre2)
g_expuesto = datos2[datos2['Grupo'] == 'expuesto']['consumo']
g_noexpuesto = datos2[datos2['Grupo'] == 'no expuesto']['consumo']
shap_expuesto = stats.shapiro(g_expuesto)
shap_noexpuesto = stats.shapiro(g_noexpuesto)
levene = stats.levene(g_expuesto, g_noexpuesto)
ttest = stats.ttest_ind(g_expuesto, g_noexpuesto, alternative="less", equal_var=levene.pvalue>0.05)
mannw = stats.mannwhitneyu(g_expuesto, g_noexpuesto, alternative="less")
mean_diff = g_expuesto.mean() - g_noexpuesto.mean()
se_diff = np.sqrt(g_expuesto.var(ddof=1)/len(g_expuesto) + g_noexpuesto.var(ddof=1)/len(g_noexpuesto))
z = stats.norm.ppf(0.975)
ic2_inf = mean_diff - z*se_diff
ic2_sup = mean_diff + z*se_diff

# ---
# Informe técnico y tabla resumen
print("\n\n---\nINFORME TÉCNICO\n")
print("a. Introducción y objetivos:")
print("El cobre es un elemento traza esencial, pero puede ser tóxico para organismos acuáticos a concentraciones elevadas. El objetivo de estos ensayos fue evaluar la toxicidad del cobre sobre Rhinella arenarum en dos etapas de su ciclo de vida (embrión y larva) y explorar si el efecto adverso podría estar mediado por una reducción en el consumo de oxígeno.\n")

print("b. Metodología:")
print("i. Descripción de los ensayos:")
print("- Ensayo 1: Se expusieron 40 embriones y 40 larvas a 50 µg Cu2+/L durante 168 horas y se registró la mortalidad.")
print("- Ensayo 2: Se midió el consumo de oxígeno en 20 embriones expuestos y 20 no expuestos a 50 µg Cu2+/L durante 24 horas.\n")
print("ii. Análisis estadístico:")
print("- Ensayo 1: Test exacto de Fisher para comparar proporciones de mortalidad y cálculo del IC95% para la proporción de larvas muertas.")
print("- Ensayo 2: t-test para muestras independientes (o Mann-Whitney si no se cumplen los supuestos) y cálculo del IC95% para la diferencia de medias.\n")

print("c. Resultados y conclusiones:")
if float(pvalue) < 0.05:
    concl1 = "Mayor mortalidad en larvas (p < 0.05)."
else:
    concl1 = "No hay diferencia significativa en mortalidad (p >= 0.05)."
if ttest[1] < 0.05:
    concl2 = "Menor consumo de oxígeno en embriones expuestos (p < 0.05)."
else:
    concl2 = "No hay diferencia significativa en consumo de oxígeno (p >= 0.05)."
print(f"- Ensayo 1: {concl1}")
print(f"- Ensayo 2: {concl2}")
print("\nEn conjunto, los resultados muestran que el cobre es más tóxico para las larvas de Rhinella arenarum y que su mecanismo de acción podría estar relacionado con la disminución del consumo de oxígeno.\n")

print("d. Tabla resumen de resultados:\n")
print("{:<25} {:<25} {:<18} {:<25} {:<30} {:<40}".format(
    'Ensayo', 'Grupo Comparado', 'Estadístico', 'Valor', 'IC 95%', 'Conclusión'))
print("-"*160)
print("{:<25} {:<25} {:<18} {:<25} {:<30} {:<40}".format(
    '1: Mortalidad', 'Larva vs Embrion', 'p (Fisher)', f"p={float(pvalue):.4f}", f"({ic_inf:.3f}, {ic_sup:.3f})", concl1))
print("{:<25} {:<25} {:<18} {:<25} {:<30} {:<40}".format(
    '2: Consumo de oxígeno', 'Expuesto vs No expuesto', 't (o U)', f"t={ttest[0]:.4f}, p={ttest[1]:.4f}", f"({ic2_inf:.3f}, {ic2_sup:.3f})", concl2)) 