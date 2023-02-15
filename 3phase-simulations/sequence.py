import numpy as np
import matplotlib.pyplot as plt
import math

PI = math.pi


U_a = 1.5
U_b = 1.5
U_c = 1.5

ph_a = 0
ph_b = 2*PI/3
ph_c = 4*PI/3

pos_seq = 2
neg_seq = 1
zer_seq = 0

omega = 1

t = np.arange(start=0, stop=2*PI, step=PI/50)

V_p = np.array([U_a*np.exp(1j*(omega*t+ph_a)), U_b*np.exp(1j*(omega*t+ph_b)), U_c*np.exp(1j*(omega*t+ph_c))])

for i in range(len(t)):
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    plt.arrow(0, 0, np.real(V_p[0,i]), np.imag(V_p[0,i]))
    plt.arrow(0, 0, np.real(V_p[1,i]), np.imag(V_p[1,i]))
    plt.arrow(0, 0, np.real(V_p[2,i]), np.imag(V_p[2,i]))

    plt.pause(0.1)

plt.show()
