# Projet "robotique" IA&Jeux 2021
import braitenberg_loveWall
import braitenberg_loveBot
# Binome:
#  Prénom Nom: Warintara MUNSUP
#  Prénom Nom: Cynthia HACHED

def get_team_name():
    return "[ WC ]" # à compléter (comme vous voulez)

def step(robotId, sensors):
    enemy_detected_by_front_sensor = False
    
    # à modifier 2 comportement braitenberg
    if robotId in range(0,3): # stratégie qui permet d'avancer tout droit en evitant ainsi les obstacles 
        translation = 1 # vitesse de translation (entre -1 et +1)
        rotation = 0 # vitesse de rotation (entre -1 et +1)
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
            rotation = 0.5  # rotation vers la droite
        elif sensors["sensor_front_right"]["distance"] < 1:
            rotation = -0.5  # rotation vers la gauche
    if robotId in range(3,6): #strategie qui êrmet de suivre chercher le mur 
        return braitenberg_loveWall.step(robotId,sensors)
        
    if robotId in range(6,8) : # strategie qui permet de suivre le robot ennemie 
        if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
            return braitenberg_loveBot.step(robotId,sensors)
        else : 
            translation = 1 # vitesse de translation (entre -1 et +1)
            rotation = 0
            if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
                rotation = 0.5  # rotation vers la droite
            elif sensors["sensor_front_right"]["distance"] < 1:
                rotation = -0.5  # rotation vers la gauche
    return translation, rotation
