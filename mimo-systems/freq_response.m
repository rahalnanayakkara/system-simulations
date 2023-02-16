pkg load control

s = tf('s');

G = [4/(s+2) 4/(s+1) ; 3/(s+1) 5/(s+5)]

W = [0 logspace(-4,4,100)];

G_max = zeros(size(W));
G_min = zeros(size(W));

for i = 1:length(W)
  [U,S,V] = svd(G(W(i)));
  G_max(i) = max(diag(S));
  G_min(i) = min(diag(S));
 endfor

 figure(1);
 semilogx(W,G_max,'b-', W, G_min, 'g-');
 xlabel('Frequency \omega / (rad/s)');
 ylabel('Gain');
 legend('\sigma_{max}', '\sigma_{min}')
 set(gca, 'FontSize', 12)

 figure(2);
 loglog(W,G_max,'b-', W, G_min, 'g-');
 xlabel('Frequency \omega / (rad/s)');
 ylabel('Log_{10} |Gain|');
 legend('\sigma_{max}', '\sigma_{min}')
 set(gca, 'FontSize', 12)
