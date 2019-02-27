from math import radians, sin,cos, tan

angulo = float(input('Digite o angulo que voce deseja'))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de: {:.2f}'.format(angulo, seno))

conseno = cos(radians(angulo))
print('O angulo de {} tem o COSENO de {:.2f}'. format(angulo, conseno))

tangente = tan(radians(angulo))
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))