import math

D = 1500
alpha1 = 30
betta1 = 30
alpha2 = 80
betta2 = 85
# AB / math.sin(alpha2) = BC / math.sin(alpha1) = D / math.sin(180-alpha1-alpha2)
AF = math.sin(alpha2) * (D / math.sin(180-(alpha1+alpha2)))
CF = math.sin(alpha1) * (D / math.sin(180-alpha1-alpha2))
if AF / math.sin(alpha2) == CF / math.sin(alpha1) == D / math.sin(180-alpha1-alpha2):
    print(AF, CF)

AB = AF*math.tan(betta1)
CB = CF*math.tan(betta2)

H1 = math.sqrt(AB**2 - AF**2)
H2 = math.sqrt(abs(CB**2) - abs(CF**2))
print(H1,H2)
