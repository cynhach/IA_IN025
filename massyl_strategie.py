# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: _________
#  Prénom Nom: _________

import random

def get_team_name():
    return "[ massyl beats you hahahahahahahhahahahahah! ]" # à compléter (comme vous voulez)
def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors

def step(robotId, sensors):
    sensors = get_extended_sensors(sensors)
    translation = 1# vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        rotation = random.uniform(-1,1) # rotation vers la droite
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = random.uniform(-1,1)  # rotation vers la gauche

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        translation =-1
        rotation = 0.5

    return translation, rotation