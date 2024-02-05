# Projet "robotique" IA&Jeux 2021
import braitenberg_loveWall
import braitenberg_loveBot
# Binome:
#  Prénom Nom: Warintara MUNSUP
#  Prénom Nom: Cynthia HACHED

import braitenberg_loveBot
import braitenberg_hateWall
import braitenberg_loveWall
import braitenberg_hateBot      # Pour les robots de la meme equipe
import braitenberg_avoider
import genetic_algorithms

def get_team_name():
    return "WC"

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
    # Chacun de nos robots a une stratégie prédéfinie
    sensors = get_extended_sensors(sensors)

    #translation, rotation = genetic_algorithms.step(robotId, sensors)      # Application de l'algortihme génétique

    translation = 0
    rotation = 0
    # Les robots qui ont un id entre 0 et 2 (compris) vont aller tout droit en évitant les obstacles
    # Architecture de subsomption
    if robotId in range(0,3): 
        # va tout droit tant qu'aucun obstacle est rencontré
        translation = 1
        rotation = 0 
        # Si un obstacle quelconque est rencontré
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1 or sensors["sensor_front_right"]["distance"] < 1:
            return braitenberg_avoider.step(robotId, sensors)

    # Les robots qui ont un id 3 et 4 longent les murs en évitant les robots
    if robotId in range(3,6): 
        translation = 1
        rotation = 0
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1 or sensors["sensor_front_right"]["distance"] < 1:
            return braitenberg_loveWall.step(robotId,sensors)

    # Les robots qui ont un id entre 5 et 7 (compris) suivent les robots ennemis 
    # Les robots suivent une architecture de subsomption 
    if robotId in range(6,8) :
        translation = 1
        rotation = 0
        # Si l'obstacle robot est rencontré on le suit
        if not (sensors["sensor_front"]["isSameTeam"] or sensors["sensor_front_left"]["isSameTeam"] or sensors["sensor_front_right"]["isSameTeam"]):
            if sensors["sensor_front"]["isRobot"] or sensors["sensor_front_left"]["isRobot"] or sensors["sensor_front_right"]["isRobot"]:
                    return braitenberg_loveBot.step(robotId, sensors)
            if sensors["sensor_front"]["distance_to_wall"] < 1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1:
                return braitenberg_hateWall.step(robotId, sensors)
        else:
            return braitenberg_avoider.step(robotId, sensors)
            

    """
    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
        rotation = 0.5  # rotation vers la droite
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.5  # rotation vers la gauche

    if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
        enemy_detected_by_front_sensor = True # exemple de détection d'un robot de l'équipe adversaire (ne sert à rien)
    """
    

    return translation, rotation
