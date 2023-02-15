import numpy as np
import matplotlib.pyplot as plt
import control

A = [[0, 1], 
     [-1, -3]]

B = [[1], 
     [0]]

C = [[5, 6]]

D = [[1]]

A = np.array(A)
B = np.array(B)
C = np.array(C)
D = np.array(D)

# Using control library

ssmodel = control.ss(A, B, C, D)

# Step response for the system
t, y = control.step_response(ssmodel)
plt.figure("Control Toolbox")
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()


# without library

i=0
t_step = 0.01
T_sim = 18

y = []
t = []
x = np.zeros((2,1), dtype=np.float32)

y.append((np.dot(C,x) + D)[0,0])
t.append(0)

while i<T_sim:
    dx = np.dot(A,x)+B
    x = x + dx*t_step
    y.append((np.dot(C,x) + D)[0,0])
    t.append(i)
    i += t_step

plt.figure("Calculated")
plt.title("Calculated")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()
plt.plot(t,y)
plt.show()