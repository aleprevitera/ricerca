#       Modello informatico a partire dai dati dello studio:
#       "Simulation of continuous blood 02 equilibrium curve over physiological pH, DPG, and Pco2 range"

import pandas as pd

def sat(pO2 = 50, temp=37, pH=7.4, pCO2=40):
    dati  = {
    "A": [
        0.6675 * 10**-3, -0.2077 * 10**-2, 0.1389 * 10**-2, 
        -0.1323 * 10**-3, 0.3564 * 10**-3, -0.257 * 10**-3, 
        -0.4558 * 10**-3, 0.1411 * 10**-2, -0.100 * 10**-2, 
        0.3562 * 10**-3, -0.9808 * 10**-3, -0.4721 * 10**-1, 
        0.1151 * 10**-2, 0.2031 * 10**-2, -0.3756 * 10**-1, 
        -0.7407 * 10**-3, 0.2855 * 10**-2, -0.1325 * 10**-2, 
        0.3457 * 10**-3, -0.1019 * 10**-2, 0.6414 * 10**-3, 
        0.6947 * 10**-4, -0.3443 * 10**-3, 0.2638 * 10**-3
    ], "B": [
        -0.3351 * 10**-1, 0.1057, -0.8233 * 10**-1, 
        -0.1180 * 10**-2, 0.8291 * 10**-2, -0.1163 * 10**-2, 
        0.1002 * 10**-1, -0.2945 * 10**-1, 0.3303 * 10**-1, 
        -0.243 * 10**-1, 0.5823 * 10**-3, -1.016, 
        -0.1023, -0.1639, 0.3432 * 10**-1, 
        0.5148 * 10**-1, 0.2157, 0.8771 * 10**-1, 
        -0.2257 * 10**-1, 0.6913 * 10**-1, -0.4939 * 10**-1, 
        -0.1197 * 10**-1, 0.5013 * 10**-1, -0.3888 * 10**-1
    ], "C": [
        -0.8114 * 10**-1, 0.2550, -1.522, 
        0.5527, -1.815, -0.7493, 
        0.3322, -1.643, -2.432, 
        0.2996, 0.6717 * 10**-1, -1.768, 
        -1.660, 2.278, -4.632, 
        -3.654, 2.78, -4.129, 
        0.4241, -1.774, -4.796, 
        0.5114, -2.214, -3.541
    ]
}

    dati = pd.DataFrame(dati)
    #s = (a1*pO2 + 2*a2*pO2**2 + 3*a3*pO2**3 + 4*a4*pO2**4)/(4(1+a1*pO2 + a2*pO2**2 + a3*pO2**3 + a4*pO2**4))
    return dati

dati  = {
    "Parametro": ['a1']*6 + ['a2']*6+ ['a3']*6 + ['a4']*6,
    "pH": [7.0] * 3 + [7.8] * 3 + [7.0] * 3 + [7.8] * 3 + [7.0] * 3 + [7.8] * 3 + [7.0] * 3 + [7.8] * 3,
    "wyz": ['w', 'y', 'z']*8,
    "A": [
        0.6675 * 10**-3, -0.2077 * 10**-2, 0.1389 * 10**-2, 
        -0.1323 * 10**-3, 0.3564 * 10**-3, -0.257 * 10**-3, 
        -0.4558 * 10**-3, 0.1411 * 10**-2, -0.100 * 10**-2, 
        0.3562 * 10**-3, -0.9808 * 10**-3, -0.4721 * 10**-1, 
        0.1151 * 10**-2, 0.2031 * 10**-2, -0.3756 * 10**-1, 
        -0.7407 * 10**-3, 0.2855 * 10**-2, -0.1325 * 10**-2, 
        0.3457 * 10**-3, -0.1019 * 10**-2, 0.6414 * 10**-3, 
        0.6947 * 10**-4, -0.3443 * 10**-3, 0.2638 * 10**-3
    ], "B": [
        -0.3351 * 10**-1, 0.1057, -0.8233 * 10**-1, 
        -0.1180 * 10**-2, 0.8291 * 10**-2, -0.1163 * 10**-2, 
        0.1002 * 10**-1, -0.2945 * 10**-1, 0.3303 * 10**-1, 
        -0.243 * 10**-1, 0.5823 * 10**-3, -1.016, 
        -0.1023, -0.1639, 0.3432 * 10**-1, 
        0.5148 * 10**-1, 0.2157, 0.8771 * 10**-1, 
        -0.2257 * 10**-1, 0.6913 * 10**-1, -0.4939 * 10**-1, 
        -0.1197 * 10**-1, 0.5013 * 10**-1, -0.3888 * 10**-1
    ], "C": [
        -0.8114 * 10**-1, 0.2550, -1.522, 
        0.5527, -1.815, -0.7493, 
        0.3322, -1.643, -2.432, 
        0.2996, 0.6717 * 10**-1, -1.768, 
        -1.660, 2.278, -4.632, 
        -3.654, 2.78, -4.129, 
        0.4241, -1.774, -4.796, 
        0.5114, -2.214, -3.541
    ]
}

dati = pd.DataFrame(dati)
# per cercare dentro a un df, scrivo df[(df['parametro'] == valore)]
print(dati[(dati["pH"] == 7.0) & (dati["wyz"] == 'y')]) 
