def acceleration_moyenne(vitesse_initiale_m_par_s:float, vitesse_finale_m_par_s:float, temps_s:float) -> float:
    return (vitesse_finale_m_par_s-vitesse_initiale_m_par_s)/temps_s

vitesse_initiale_m_par_s=0
vitesse_finale_m_par_s=10
temps_s = 9.57
print(f"L'acceleration moyenne pour passer d'une vitesse de {vitesse_initiale_m_par_s} m/s a une vitesse de  {vitesse_finale_m_par_s} m/s est: {acceleration_moyenne(vitesse_initiale_m_par_s, vitesse_finale_m_par_s, temps_s):,.3f} m/s^2")