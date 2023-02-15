import numpy as np
import matplotlib.pyplot as plt
import math

PI = math.pi

U_a = 1
U_b = 1
U_c = 1

ph_a = 0
ph_b = 2*PI/3
ph_c = 4*PI/3

omega = 1

t = np.arange(start=0, stop=2*PI, step=PI/50)

v_a = U_a*np.cos(omega*t + ph_a)
v_b = U_b*np.cos(omega*t + ph_b)
v_c = U_c*np.cos(omega*t + ph_c)

plt.figure("Phase voltages")
plt.plot(v_a)
plt.plot(v_b)
plt.plot(v_c)

tf_ab = np.array([[2/3, -1/3, -1/3],
                  [0,   1/math.sqrt(3), -1/math.sqrt(3)]])

v = np.array([v_a, v_b, v_c])

v_stator = np.dot(tf_ab, v)


plt.figure("Stator voltage")
plt.title("Rotating stator voltage")
plt.xlim(-2, 2)
plt.ylim(-2, 2)

for i in range(len(t)):
    plt.arrow(0,0,v_stator[0,i], v_stator[1,i])
    plt.pause(0.1)

plt.show()
