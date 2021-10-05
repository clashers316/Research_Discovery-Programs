import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

ESI = [0.352062926, 0.430803912, 0.495865291, 0.524760076, 0.533055288, 0.578943661, 0.625187177, 0.646292406, 0.646292406, 0.68013828, 0.714046438, 0.726770832, 0.731012845, 0.760708253, 0.794629925, 0.853871813, 0.870754527, 1]

Temp = [163, 183, 199, 206, 208, 219, 230, 235, 235, 243, 251, 254, 255, 262, 270, 284, 288, 288]

pl.title("ESI v Temp Graph")
pl.xlabel("ESI")
pl.ylabel("Temp")
pl.scatter(ESI, Temp)

from scipy.optimize import curve_fit

def func(x, a, b):
    return 

xData = np.array(ESI)
yData = np.array(Temp)

plt.plot(xData, yData, 'bo', label = 'experimental data')

popt, pcov = curve_fit(func, xData, yData)
print(popt)

xFit = np.arange(0.0, 1.0, 0.01)
plt.plot(xFit, func(xFit, *popt), 'r', label = 'fit params: a = %5.3f, b = %5.3f')
plt.xlabel('ESI')
plt.ylabel('Temp')
plt.legend()
plt.show()
