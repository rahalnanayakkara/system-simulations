pkg load control

OMEGA = 2*pi*1.2;

s = tf('s');

G = [4/(s+2) 4/(s+1) ; 3/(s+1) 5/(s+5)]

Gw = G(OMEGA)

T = 0:0.01:10;
L = length(T);
U = [sin(OMEGA*T)' cos(OMEGA*T)'];
lsim(G,U,T)

[Uc, Sv, Vc] = svd(Gw)
