# Projet "robotique" IA&Jeux 2021
import braitenberg_loveWall
import braitenberg_loveBot
import braitenberg_hateBot
import braitenberg_avoider
import random
# Binome:
#  Prénom Nom: Warintara MUNSUP
#  Prénom Nom: Cynthia HACHED

def get_team_name():
    return "[ WC ]" # à compléter (comme vous voulez)

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
    enemy_detected_by_front_sensor = False
    sensors = get_extended_sensors(sensors)
    translation = 0
    rotation = 0
    # à modifier 2 comportement 
    if robotId in range(0,4): # stratégie qui permet d'avancer tout droit en evitant ainsi les obstacles 
        translation = 1
        rotation = 0
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
            rotation = random.uniform(0,1)  # rotation vers la droite
        elif sensors["sensor_front_right"]["distance"] < 1:
            rotation = random.uniform(-1,0)  # rotation vers la gauche"""
#
#
    #
    #if robotId in range(3,6): #strategie qui êrmet de suivre chercher le mur
    #    if sensors["sensor_front"]["isRobot"] or sensors["sensor_front_left"]["isRobot"] or sensors["sensor_front_right"]["isRobot"] and sensors["sensor_front"]["isSameTeam"] == True:
    #        return braitenberg_hateBot.step(robotId, sensors)
    #    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1 :
    #        translation = 1
    #        rotation = random.uniform(0,1) # rotation vers la droite
    #    elif sensors["sensor_front_right"]["distance"] < 1:
    #        translation = 1
    #        rotation = random.uniform(-1,0) # rotation vers la gauche"""
#
#

    if robotId in range(4,8) : # strategie qui permet de suivre le robot ennemie  """
        rotation = 0
        translation = 1
        if (sensors["sensor_front"]["isRobot"] or sensors["sensor_front_left"]["isRobot"] or sensors["sensor_front_right"]["isRobot"]) and (sensors["sensor_front"]["isSameTeam"] == False):
            return braitenberg_loveBot.step(robotId, sensors)
        if (sensors["sensor_front"]["isRobot"] or sensors["sensor_front_left"]["isRobot"] or sensors["sensor_front_right"]["isRobot"]) and (sensors["sensor_front"]["isSameTeam"] == True):
            return braitenberg_hateBot.step(robotId, sensors)
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
            rotation = random.uniform(0,1)  # rotation vers la droite
        elif sensors["sensor_front_right"]["distance"] < 1:
            rotation = random.uniform(-1,0)  # rotation vers la gauche"""


    return translation, rotation
