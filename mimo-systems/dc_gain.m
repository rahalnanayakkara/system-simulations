pkg load control

s = tf('s');

G = [4/(s+2) 4/(s+1) ; 3/(s+1) 5/(s+5)]

T = 0:0.01:10;
L = length(T);
U = ones(L,2);

lsim(G,U,T)
