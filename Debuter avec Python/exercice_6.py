#Exercice 6
#1) V_cylindre = pi*r**2*h et A_cylindre = 2*pi*r**2 + 2*pi*r*h
#2) On a r = rayon et h = hauteur, et les deux sont des integers
#3)

r = 5
h = 8
def V_cylindre():
    return(3.14*r**2*h)
print(V_cylindre())

def A_cylindre():
    return(2*3.14*r**2+2*3.14*r*h)
print(A_cylindre())