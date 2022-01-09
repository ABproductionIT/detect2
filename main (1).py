import numpy as np
from math import pi

D = int(input('Enter camera distance (metr) : '))
alpha1 = int(input('Enter the angle of the camera N1 : '))
alpha2 = int(input('Enter the angle of the camera N2 : '))
betta = int(input('Enter the angle of the detected target1 : '))
betta1 = int(input('Enter the angle of the detected target2 : '))
alpha3 = 180 - (alpha1 + alpha2)
AF = (D * np.sin((alpha3 + alpha1) * pi / 180)) / np.sin(alpha3 * pi / 180)
FC = (D * np.sin((alpha3 + alpha2) * pi / 180)) / np.sin(alpha3 * pi / 180)
print('=' * 50)
print(f'AF = {AF}, FC = {FC}')
print('=' * 50)


AB = AF / np.cos(betta * pi / 180)
BC = FC / np.cos(betta1 * pi / 180)
print(f'AB = {AB}, BC = {BC}')
print('=' * 50)


H1 = np.sqrt(AB ** 2 - AF ** 2)
H2 = np.sqrt(BC ** 2 - FC ** 2)
K = AB / BC

print(f'Coefficient of similar triangles  = {K}')
print('=' * 50)
if K <= 1:
    H2 *= K
else:
    H1 /= K
print(H1, H2)
