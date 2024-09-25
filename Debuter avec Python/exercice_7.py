#Exercice
#1) les variables sont m = masse de l'individu et t = taille de l'individu
#2) la fonction doit retourner l'indice de masse corporelle de l'individu (IMC), qui est un float
#3)

def IMC(masse_kg:float, taille_m:float) -> float:
    return masse_kg / taille_m**2

#4)
masse_kg=65
taille_m=1.75
print(f"l'IMC d'un individu de masse {masse_kg} kg et de taille {taille_m} m est : {IMC(masse_kg=masse_kg, taille_m=taille_m):.3f}")