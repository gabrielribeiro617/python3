import math
a = int(input('\033[1;35mDigite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('\033[33mO valor do seu seno é {:.2f}'.format(s))
print('\033[33mO valor do seu cosseno é {:.2f}'.format(c))
print('\033[33mO valor da sua tangente é {:.2f}'.format(t))
