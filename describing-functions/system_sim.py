import numpy as np

class System():
    
    def __init__(self, G_ss, t_step=0.01):
        self.G_ss = G_ss
        self.x = np.zeros((len(G_ss.A), 1), dtype=np.float32)
        self.dx = np.zeros((len(G_ss.A), 1), dtype=np.float32)
        self.y = 0
        self.t_step = t_step

    def __call__(self, u):
        self.dx = np.dot(self.G_ss.A, self.x) + self.G_ss.B*u
        self.x += self.dx*self.t_step
        self.y = (np.dot(self.G_ss.C, self.x) + self.G_ss.D*u)[0,0]
        return self.y
        