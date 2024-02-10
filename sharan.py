import numpy as np
import matplotlib.pyplot as plt
def sat(pO2, pCO2=40, pH=7.4):
    C8 = 10**(-pH)
    K1 = 10**10 #cm3/mol
    K2 = 5*10**9 #cm3/mol
    K = 8.365*10**(3) #valore corretto da (-15) a (3) dopo simulazione
    n = 2.7038757
    l = 1.0114518
    K5 = 3.99*10**(-4)
    K6 = 1.9*10**(-4)
    gamma = 3.21 * 10**(-8)
    K0 = ((1 + K2 * C8 + (gamma * K6 * pCO2) / C8) * K * (C8 ** l))/(1 + K1 * C8 + (gamma * K5 * pCO2) / C8)
    s = (K0 * pO2**n)/(1 + K0 * pO2**n)
    return s

pO2 = np.linspace(0, 100, 100)
plt.plot(pO2, sat(pO2))
plt.show()
