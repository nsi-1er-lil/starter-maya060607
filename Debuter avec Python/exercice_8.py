#Exercice 8

def vitesse_moyenne(distance_m:float, temps_s:float) -> float:
    return distance_m/temps_s

distance_m=100
temps_s = 9.57
print(f"La vitesse moyenne pour parcourir une distance de {distance_m} metres en {temps_s} secondes est: {vitesse_moyenne(distance_m, temps_s):,.3f} m/s")