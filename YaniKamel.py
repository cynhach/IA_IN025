# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Kamel NEHLIL
#  Prénom Nom: Yani  Mendas

from pyroborobo import Pyroborobo, Controller, AgentObserver, WorldObserver, CircleObject, SquareObject, MovableObject
import math

r0=0
r1=0
r2=0
r3=0
r4=0
r5=0
r6=0
r7=0

def get_team_name():
    return "NewTeam" # à compléter (comme vous voulez)

def step(robotId, sensors):
    sensors = get_extended_sensors(sensors)
    if(robotId==0 or robotId==7): 		#comportement pour les robots sur les extrem 
    	return comp07(robotId,sensors)
    
    if(robotId==1 or robotId==6):		#compoortement pour les robots 1 et 6
    	return comp16(robotId,sensors)
    
    if(robotId==2 or robotId==5):		#comportement pour les robots 2 et 5
    	return comp25(robotId,sensors)
    	
    if(robotId==3 or robotId==4):		#comportement pour les robots 3 et 4
    	return comp25(robotId,sensors)


    
def get_extended_sensors(sensors):
    for key in sensors:
        sensors[key]["distance_to_robot"] = 1.0
        sensors[key]["distance_to_wall"] = 1.0
        if sensors[key]["isRobot"] == True:
            sensors[key]["distance_to_robot"] = sensors[key]["distance"]
        else:
            sensors[key]["distance_to_wall"] = sensors[key]["distance"]
    return sensors


def followBot(sensors):
    translation = 1 * sensors["sensor_front"]["distance_to_wall"]
    rotation = (1) * sensors["sensor_front_left"]["distance_to_robot"] + (-1) * sensors["sensor_front_right"]["distance_to_robot"]

    # limite les valeurs de sortie entre 1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation

def avoidBot(sensors):
    translation = 1 * sensors["sensor_front"]["distance_to_wall"]
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_robot"] + (1) * sensors["sensor_front_right"]["distance_to_robot"] + -0.1 * sensors["sensor_front"]["distance_to_robot"]

    # limite les valeurs de sortie entre 1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation

def avoidWall(sensors):
    translation = 1 * sensors["sensor_front"]["distance"]
    rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"] + -0.1 * sensors["sensor_front"]["distance_to_robot"]

    # limite les valeurs de sortie entre 1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation,rotation

def followWall07(robotId,sensors):
    global r0
    global r7
    #L
    if(robotId%8==0 and r0==0):
        r0+=1
        return 1,-1
    
    if(robotId%8==7 and r7<100):
        r7+=1
        return 1,1

    if(robotId%8==0 ):                                                                  #Braintenberg suit le mur gauche
        translation = 1 * sensors["sensor_front"]["distance"]
        rotation = (-0.9) * abs(sensors["sensor_front_left"]["distance_to_wall"])+0.8  
        r0+=1
    
    if(robotId%8==7):                                                                   #Braintenberg suit le mur droit
        translation = 1 * sensors["sensor_front"]["distance"]
        rotation = (0.9) * abs(sensors["sensor_front_right"]["distance_to_wall"])-0.8  
        r7+=1
    
    # limite les valeurs de sortie entre 1 et +1
    translation = max(-1,min(translation,1))     
    rotation = max(-1, min(rotation, 1))
    

    return translation,rotation

def diagonalAttack16(robotId,sensors):
    global r1
    global r6
    
    if(robotId%8==1 and r1==0):
        r1+=1
        return 1,-1
    
    if(robotId%8==6 and r6==0):
        r6+=1
        return 1,1

    r1+=1
    r6+=1
    return 1,0



def comp07(robotId, sensors):
    global r0, r7

    if(r0<800 or r7<800):
        #print(RobotId," comportement actuel : followWall...")
        return followWall07(robotId,sensors)
    if(sensors["sensor_front"]["distance_to_wall"]<1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1):
        #print(RobotId," comportement actuel : avoidWall...")
        return avoidWall(sensors)
    enemyClose=False
    for _,i in sensors.items():
        if(i["distance_to_robot"]<1 and not i["isSameTeam"]):
            enemyClose=True
            break
    
    if(enemyClose):
        #print(RobotId," comportement actuel : followdBot...")
        return followBot(sensors)
    #print(RobotId," comportement : goAhead...")
    return 1,0
    
def comp16(robotId, sensors):
    global r1, r6

    teamClose=False
    for _,i in sensors.items():
        if(i["distance_to_robot"]<1 and i["isSameTeam"]):
            teamClose=True
            break

    if(r1==0 or r6==0):
        return diagonalAttack16(robotId,sensors)

    if(teamClose):
        #print(RobotId, " comportement actuel : avoidBot...")
        return avoidBot(sensors)
    
    enemyClose=False
    for _,i in sensors.items():
        if(i["distance_to_robot"]<1 and not i["isSameTeam"]):
            enemyClose=True
            break
    
    if(enemyClose):
        #print(RobotId," comportement actuel : followdBot...")
        return followBot(sensors)
    if(sensors["sensor_front"]["distance_to_wall"]<1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1):
        #print(RobotId, " comportement actuel : avoidWall...")
        return avoidWall(sensors)
    #print(RobotId," comportement actuel : goAhead...")
    return 1,0
    
def comp25(robotId, sensors):
    global r1, r5

    teamClose=False
    for _,i in sensors.items():
        if(i["distance_to_robot"]<1 and i["isSameTeam"]):
            teamClose=True
            break

    if(teamClose):
        #print(RobotId, " comportement actuel : avoidBot...")
        return avoidBot(sensors)
    
    enemyClose=False
    for _,i in sensors.items():
        if(i["distance_to_robot"]<1 and not i["isSameTeam"]):
            enemyClose=True
            break
    
    if(enemyClose):
        #print(RobotId," comportement actuel : followdBot...")
        return followBot(sensors)
    if(sensors["sensor_front"]["distance_to_wall"]<1 or sensors["sensor_front_left"]["distance_to_wall"] < 1 or sensors["sensor_front_right"]["distance_to_wall"] < 1):
        #print(RobotId, " comportement actuel : avoidWall...")
        return avoidWall(sensors)
    #print(RobotId," comportement actuel : goAhead...")
    return 1,0
    
def comp34(robotId, sensors):
    #pasfinis
    return 1,0

