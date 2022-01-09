import math
import numpy as np


D = 100
# D is a distance between cameras

# test1
# alpha1 = math.radians(60)
# betta1 = math.radians(30)
# alpha2 = math.radians(50)
# betta2 = math.radians(27.053198)

# test2
alpha1 = math.radians(60)
betta1 = math.radians(89.9)
alpha2 = math.radians(2)
betta2 = math.radians(87)

alpha3 = math.radians(180)-alpha1-alpha2

# AF / math.sin(alpha2) = CF / math.sin(alpha1) = D / math.sin(180-alpha1-alpha2)
AF = (math.sin(alpha2) * D) / math.sin(alpha3)
CF = (math.sin(alpha1) * D) / math.sin(alpha3)
print("map distance from 1 =", str(AF)+"m", "map distance from 2 =", str(CF)+"m")
AB = AF / math.cos(betta1)
CB = CF / math.cos(betta2)
H1 = math.sin(betta1) * AB
H2 = math.sin(betta2) * CB

print(H1, H2)
