import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pylab as pl
df = pd.read_csv(r'C:\Users\madha\OneDrive\Desktop\Research Discovery\ESI_Habitable.csv')
df.tail(3)

plt.scatter(df['ESIg'], df['Temp'])

def func(x, a, b):
    return a/(np.exp((b*x))**2)

xData = df['ESIg']
yData = df['Temp']

plt.plot(xData, yData, 'bo', label = 'experimental data')

popt, pcov = curve_fit(func, xData, yData)
print(popt)

xFit = np.arange(0.0, 0.75, 0.001)

plt.plot(xFit, func(xFit, *popt), 'r', label = 'fit params')
plt.xlabel('ESI')
plt.ylabel('Temp')
plt.legend()
plt.show()
