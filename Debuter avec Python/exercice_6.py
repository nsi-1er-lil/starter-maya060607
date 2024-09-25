from math import pi
#Exercice 6
#1) V_cylindre = pi*r**2*h et A_cylindre = 2*pi*r**2 + 2*pi*r*h
#2) On a r = rayon et h = hauteur, et les deux sont des float
#3)

def V_cylindre(r, h):
    return(pi*r**2*h)

def A_cylindre(r, h):
    return(2*pi*r**2+2*pi*r*h)

R = 5
H = 8
print(V_cylindre(r=R,h=H))
print(A_cylindre(r=R,h=H))
