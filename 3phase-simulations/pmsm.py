import numpy as np
import matplotlib.pyplot as plt


class PMSM():
    
    def __init__(self, R_s, L_d, L_q, pm_flux, omega, poles=2):
        # Set parameters
        self.R_s = R_s
        self.L_d = L_d
        self.L_q = L_q
        self.pm_flux = pm_flux
        self.omega = omega
        self.poles = poles
        
        # Initialise state space values
        self.x = np.zeros(2, dtype=np.float32)
        self.dx = np.zeros(2, dtype=np.float32)

        self.torque = 0

        # Initialize state space matrices
        self.A = np.array([[-R_s/L_d, omega*L_q/L_d],
                           [-omega*L_d/L_q, -R_s/L_q]])
        
        self.B = np.array([[1/L_d, 0], 
                           [0, 1/L_q]])

        self.C = np.array([0, -omega*pm_flux/L_q])
    
    
    def id(self):
        return self.x[0]

    
    def iq(self):
        return self.x[1]


    def time_step(self, u = np.zeros(2, dtype=np.float32), t_step=0.01):
        self.dx = np.dot(self.A, self.x) + np.dot(self.B, u) + self.C
        self.x = self.x + self.dx*t_step


    def simulate(self, u, t_step=0.01):
        duration = u.shape[1]
        id = []
        iq = []
        time = []
        torque = []
        
        for t in range(duration):
            self.time_step(u[:,t], t_step)
            id.append(self.x[0])
            iq.append(self.x[1])
            torque.append(0.75*self.poles*(self.pm_flux+(self.L_d-self.L_q)*self.x[0]*self.x[1]))
            time.append(t_step*t)
        
        plt.figure("Simulation Results - Currents")
        plt.plot(time, id)
        plt.plot(time, iq)
        plt.xlabel("Time")
        plt.ylabel("Currents")
        plt.legend(["I_d", "I_q"])
        plt.grid()

        plt.figure("Simulation Results - Torque")
        plt.plot(time, torque)
        plt.xlabel("Time")
        plt.ylabel("Torque")
        plt.grid()

        plt.show()


motor = PMSM(10,3,4,1,1)
u = np.ones((2, 1000))
motor.simulate(u)
