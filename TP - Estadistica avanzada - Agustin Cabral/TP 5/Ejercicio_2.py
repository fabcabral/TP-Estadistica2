# Ejercicio 2
# Problema: Expresión de miR-150 en cáncer de próstata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, bartlett, f_oneway, t, kruskal
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Crear los datos
microARN = pd.DataFrame({
    'Paciente': np.arange(1, 187),
    'condicion': ['normal']*53 + ['adenoma']*52 + ['CCR']*81,
    'antecedentes': ['no']*46 + ['sí']*7 + ['no']*44 + ['sí']*8 + ['no']*70 + ['sí']*11,
    'miR_150': [
        # Normal
        2.98978144587455, 2.25165260914388, 2.99503058297549, 2.20110846430925, 2.89260497454953, 
        3.65334277752922, 2.11998135434844, 2.98285317832893, 2.21547029266114, 2.30011286839711,
        3.09710148352439, 2.87620007240994, 2.99393274186548, 2.56962119894339, 1.54131267454965,
        1.88159389040803, 3.89, 2.63945212060497, 2.06044380688855, 2.30617169033692,
        2.74015746326211, 2.51572852951469, 2.11476211768857, 1.81870514385818, 2.69413377903779,
        2.18587927611712, 2.34298977204523, 2.0607969405838, 2.05446037304098, 2.16675768168861,
        2.00002144129338, 2.10942622787543, 2.8991380732435, 2.39233139105424, 3.92,
        3.05, 2.84310569260961, 3.43598372473841, 2.53916217728675, 2.41704866324454,
        1.86331426193605, 3.59178275341942, 2.2760735896777, 3.73248646683776, 2.55094508743124,
        2.93167206854603, 2.32169052751504, 3.00304725073705, 2.0872883161983, 2.65307330769411,
        2.50672596267276, 1.76763804373104, 1.71566866717357,
        # Adenoma
        2.69070471144294, 1.83766405871922, 2.26717144632199, 2.66202125222037, 2.00344802847558,
        2.21982534371624, 2.89281199986941, 1.88385235893988, 2.26654374125921, 1.88559501420901,
        3.28620596342306, 2.06238485187411, 3.49076788430681, 2.05033704117468, 3.23964414823696,
        1.57231146452147, 1.94483656421199, 2.69431045862675, 1.88600845837806, 2.09822117669139,
        2.5849869283861, 3.33714026126109, 2.52537105410441, 2.39184835445283, 2.63150558519933,
        3.50, 1.96074980014637, 2.77730400966567, 1.96104421048556, 3.36823586891764,
        2.40102604987969, 1.91958948889895, 3.03501209499729, 1.86071059529761, 3.42661903217408,
        1.94321294277271, 1.73303570294996, 2.71658355077821, 3.36727357207243, 3.37946783545839,
        2.17536065335193, 3.22238551953393, 2.67, 2.4833298761721, 3.07226383993473,
        1.68890033951493, 1.58639951506468, 1.97682254141277, 3.09862753661527, 3.04774920979207,
        1.75421578907616, 3.83471449083791,
        # CCR
        4.94840659288623, 5.29852916257576, 5.86927099551706, 5.37586559502015, 4.84627459626573,
        4.74864898883711, 4.05324779989015, 5.43969345675463, 6.11, 4.41314420379153,
        4.14010837265582, 5.04417731508475, 4.85980751099535, 4.60640991062681, 6.10051423173172,
        4.29290019666253, 4.17847932449023, 5.58941187530727, 4.25061382538464, 4.1931101692976,
        4.94567230765971, 4.50231879420965, 4.9573484682663, 4.34980233512935, 4.64447613585678,
        5.00074583063125, 5.99, 5.36047424029355, 5.91058637100053, 4.50413842468876,
        5.2516261265041, 4.43778579369002, 4.76756981287259, 5.14981080444458, 5.69870168806911,
        4.18620462004806, 4.75567119123991, 5.74909785494535, 5.13013732990927, 4.95379714109329,
        4.19826671480708, 5.27472799428468, 4.55345890175244, 4.85232263530956, 4.36868903613361,
        4.52473286437206, 4.29588635867426, 4.61450738529267, 4.45636538741324, 5.56154842516932,
        5.85191054002803, 4.38611955661926, 4.14804872266627, 5.52666769334171, 4.99717750984892,
        4.61300438480099, 4.51895020091752, 4.43727156754503, 5.99517273573838, 4.76192681577842,
        4.66, 4.3290261704658, 4.30047630315361, 4.70346771481705, 4.32711528071713,
        4.56226343736766, 4.56765646341913, 4.04970376599583, 4.37464152118541, 5.08823189854665,
        5.78, 5.22565624997606, 4.99971016455216, 4.51065195585863, 4.37554855896893,
        4.66322793185386, 4.45321813295178, 5.37917732578874, 4.94465188188104, 4.11440182675953,
        4.57086323479552
    ]
})

# Estadísticas descriptivas por condición
groups = ['normal', 'adenoma', 'CCR']
print("\nEstadísticas descriptivas por condición:")
print(microARN.groupby('condicion')['miR_150'].agg(['count', 'mean', 'std', 'median', 'min', 'max']))

# Boxplot principal
plt.figure(figsize=(8, 5))
microARN.boxplot(column='miR_150', by='condicion', grid=False, patch_artist=True,
                 boxprops=dict(facecolor='lightblue'), medianprops=dict(color='black'))
plt.title('Expresión de miR-150 por condición')
plt.suptitle('')
plt.xlabel('Condición')
plt.ylabel('miR-150 (microunidades/mg)')
plt.show()

# Boxplot por antecedentes
plt.figure(figsize=(8, 5))
microARN.boxplot(column='miR_150', by='antecedentes', grid=False, patch_artist=True,
                 boxprops=dict(facecolor='lightgray'), medianprops=dict(color='black'))
plt.title('Expresión de miR-150 por antecedentes familiares')
plt.suptitle('')
plt.xlabel('Antecedentes familiares')
plt.ylabel('miR-150 (microunidades/mg)')
plt.show()

# Histograma general
plt.hist(microARN['miR_150'], bins=20, color='lightblue', alpha=0.7)
plt.title('Distribución de miR-150')
plt.xlabel('miR-150 (microunidades/mg)')
plt.ylabel('Frecuencia')
plt.show()

# Stripchart (jitter)
plt.figure(figsize=(8, 5))
for i, group in enumerate(groups):
    y = microARN[microARN['condicion'] == group]['miR_150']
    x = np.random.normal(i+1, 0.04, size=len(y))
    plt.plot(x, y, 'o', alpha=0.6, label=group)
plt.xticks([1, 2, 3], groups)
plt.xlabel('Condición')
plt.ylabel('miR-150 (microunidades/mg)')
plt.title('Distribución de valores por condición')
plt.show()

# Outliers por condición
def detect_outliers(x):
    Q1 = np.percentile(x, 25)
    Q3 = np.percentile(x, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return x[(x < lower) | (x > upper)]

print("\nAnálisis de outliers:")
for group in groups:
    outliers = detect_outliers(microARN[microARN['condicion'] == group]['miR_150'])
    print(f"{group} - Outliers: {list(outliers)}")

# Supuestos: Normalidad y homocedasticidad
print("\nTest de Shapiro-Wilk por grupo (primeras 50 observaciones):")
for group in groups:
    vals = microARN[microARN['condicion'] == group]['miR_150'][:50]
    stat, p = shapiro(vals)
    print(f"{group}: W = {stat:.4f}, p = {p:.4f}")

# Test de Bartlett
stat_bartlett, p_bartlett = bartlett(
    microARN[microARN['condicion'] == 'normal']['miR_150'],
    microARN[microARN['condicion'] == 'adenoma']['miR_150'],
    microARN[microARN['condicion'] == 'CCR']['miR_150'])
print(f"\nTest de Bartlett: K = {stat_bartlett:.4f}, p = {p_bartlett:.4f}")

# ANOVA
f_stat, p_anova = f_oneway(
    microARN[microARN['condicion'] == 'normal']['miR_150'],
    microARN[microARN['condicion'] == 'adenoma']['miR_150'],
    microARN[microARN['condicion'] == 'CCR']['miR_150'])
print(f"\nANOVA: F = {f_stat:.2f}, p = {p_anova:.4f}")
 