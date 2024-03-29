import matplotlib.pyplot as plt
import numpy as np

def saturazione(pO2_iniz, temp=37, pH=7.4, pCO2=40):
    a1 = -8.5322289*10**3
    a2 = 2.1214010*10**3
    a3 = -6.7073989*10**1
    a4 = 9.3596087*10**5
    a5 = -3.1346258*10**4
    a6 = 2.3961674*10**3
    a7 = -6.7104406*10**1
    pO2 = pO2_iniz*10**(0.024*(37-temp)+0.4*(pH-7.4)+0.06*(np.log10(40)-np.log10(pCO2)))
    spO2 = 100*(a1*pO2+a2*(pO2)**2+a3*(pO2)**3+(pO2)**4)/(a4+a5*(pO2)+a6*(pO2)**2+a7*(pO2)**3+(pO2)**4)
    return spO2

PO2 = np.linspace(0, 100, 100)

# imposta subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# SpO2
ax1.plot(PO2, saturazione(PO2), label="SpO2")
ax1.set_xlabel("pO2")
ax1.set_ylabel("Sp02 (%)")

# SpO2 con variazione temperatura
temperatura = [t for t in range(35, 40)]
for t in temperatura:
    ax2.plot(PO2, saturazione(PO2, t), label=f'T = {t}°C')
ax2.legend(loc='lower right')
ax2.set_title("dT")
ax2.set_xlabel("pO2")
ax2.set_ylabel("Sp02 (%)")

# SpO2 con variazione pH
pH = [p for p in np.arange(7.2, 7.7, 0.1)]
for p in pH:
    ax3.plot(PO2, saturazione(PO2, pH=p), label=f'pH = {round(p, 1)}')
ax3.legend(loc='lower right')
ax3.set_title("dpH")
ax3.set_xlabel("pO2")
ax3.set_ylabel("Sp02 (%)")

# SpO2 con variazione pCO2
pCO2 = [c for c in np.arange(0, 100, 20)]
for c in pCO2:
    ax4.plot(PO2, saturazione(PO2, pCO2=c), label=f'pCO2 = {c} mmHg')
ax4.legend(loc='lower right')
ax4.set_title("dpCO2")
ax4.set_xlabel("pO2")
ax4.set_ylabel("Sp02 (%)")

# mostra grafico
plt.show()
