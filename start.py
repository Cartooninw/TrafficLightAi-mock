import numpy as np
import random
import time
import threading
import concurrent.futures
#---------------decrale variables---------------#
Weather_set = ['hot','sunny', 'rainy', 'cloudy', 'strom']
Traffic_Light_time_limit = 120 # seconds
Place_list = [
    "Normal",
    "tourist_attraction",
    "School",
    "Pub",
    "city"]

Place_List_Weight = {"Normal":1,
                     "tourist_attraction":1.5,
                     "School":1.2,
                     "Pub":1.3,
                     "city":1.5}

max_nor_car_range , min_nor_car_range = 5.822 , 4.064 # meters
min_ex_car_range , max_ex_car_range = 6 , 8 # meters
lane_size = 3 # meters
lane = 2 # lanes


MajorSwitch = threading.Event()

#Priority control Red/Green Light
#Priority Property
#The futher how long red light take the more priority
MaxPriority = 400
Limit_Lane_Range = 500 #meters , If greater than this will be highest priority, The first one hit limit is the most priority.

Major_lane_one , Major_lane_two , Sub_lane_one , Sub_lane_two = [], [] , [] , []
Major_lane_one2 , Major_lane_two2 , Sub_lane_one2 , Sub_lane_two2 = [], [] , [] , []
Yellow_Light_cooldown = 3
EmergencyCar_Count_lane_one ,EmergencyCar_Count_lane_two ,EmergencyCar_Count_lane_three ,EmergencyCar_Count_lane_four  = [0] , [0] , [0] , [0] 
EmergencyCar_Count_lane_one2 ,EmergencyCar_Count_lane_two2 ,EmergencyCar_Count_lane_three2 ,EmergencyCar_Count_lane_four2  = [0] , [0] , [0] , [0] 
#There will be only one lane can be True , True is mean GreenLight 
#                          major            sub           major            sub
crossRoad =  [[0,None], [True,"Major",Major_lane_one,EmergencyCar_Count_lane_one], [False,"Sub",Sub_lane_one,EmergencyCar_Count_lane_two], [True,"Major",Major_lane_two,EmergencyCar_Count_lane_three], [False,"Sub",Sub_lane_two,EmergencyCar_Count_lane_four]]
#Cross one and two Major will connected.
crossRoad2 = [[0,None],[True,"Major",Major_lane_one2 ,EmergencyCar_Count_lane_one2] ,[False,"Sub", Major_lane_two2 ,EmergencyCar_Count_lane_two2] ,[True,"Major", Sub_lane_one2 ,EmergencyCar_Count_lane_three2] , [False,"Sub", Sub_lane_two2,EmergencyCar_Count_lane_four2]] #-----------------------Time---------------------#

initial_localtime = random.randint(0, 24) # random time
localtime = initial_localtime
time_state = None
LocalTimeWeight = 0
def time_statement_set():
    global LocalTimeWeight , time_state
    if localtime >= 7 and localtime <= 9:
        LocalTimeWeight = 1.5
        time_state = "moring"
        print("It's morning. ")
    elif localtime > 9 and localtime <= 16:
        LocalTimeWeight = 1.2
        time_state = "daytime"
        print("It's daytime." )
    elif localtime > 16 and localtime <= 19:
        LocalTimeWeight = 1.5
        time_state = "afternoon"
        print("It's afternoon." )
    else:
        LocalTimeWeight = 0.8
        time_state = "evening"
        print("It's evening.")

#ยิ่งนาน priority ยิ่งสูง
# Ambulance + 50 , Firetruck + 40 , Police + 30
#ยิ่งแถวยาวยิ่งมีความสำคัญสูง

#-----------------random values-----------------#

lane_size_random = random.randint(0, 3) # random lane size ( meters )

#Weather = random.choice(Weather_set) # random weather
#-----------------Traffic-----------------#

#second
TimeStacked = 2
TimeFactor = 60
#North
TrafficVolumeN = 0
#South
TrafficVolumeS = 0
#East
TrafficVolumeE = 0
#West
TrafficVolumeW = 0

#if main road high traffic volume, it will stack sub road to 500m .
# always random car for high volumn traffic

Places = random.choice(Place_list) # random place
print(Places)
#Vehicle per hours
TimeCycle = 60
def traffic_volumeN_generate():
    global TrafficVolumeN
    Twominutes = 1
    while True:
        TrafficVolumeN = (len(crossRoad[1][2]) / TimeStacked) * TimeFactor * Place_List_Weight[Places] * LocalTimeWeight
        time.sleep(Twominutes)


def traffic_volumeS_generate():
    global TrafficVolumeS
    Twominutes = 1
    while True:
        TrafficVolumeS = (len(crossRoad[3][2]) / TimeStacked) * TimeFactor * Place_List_Weight[Places] * LocalTimeWeight
        time.sleep(Twominutes)

def traffic_volumeE_generate():
    global TrafficVolumeE
    Twominutes = 1
    while True:
        TrafficVolumeE = (len(crossRoad[2][2]) / TimeStacked) * TimeFactor * Place_List_Weight[Places] * LocalTimeWeight
        time.sleep(Twominutes)

def traffic_volumeW_generate():
    global TrafficVolumeW
    Twominutes = 1
    while True:
        TrafficVolumeW = (len(crossRoad[4][2]) / TimeStacked) * TimeFactor * Place_List_Weight[Places] * LocalTimeWeight
        time.sleep(Twominutes)
#def random_traffic_volume():
#    traffic_volume = random.randint(0, 100) # random traffic volume
#    if traffic_volume > 30:
#        return ["High_volume_Traffic",traffic_volume]
#    else:
#        return ["Low_volume_Traffic",traffic_volume]

#-----------------Priority5-----------------#
def random_Priority():
    random_Ambulance = random.uniform(0, 1) # random 0 or 1
    random_Firetruck = random.uniform(0, 1) # random 0 or 1
    random_Police = random.uniform(0, 1) # random 0 or 1
    box = []
    if random_Ambulance <= 0.09:
        print("Ambulance added")
        box.append({"width":2.41 , "type" : "Special"})
    #if random_Firetruck <= 0.005:
    #    print("Firetruck added")
    #    box.append({"width":1.5 , "type" : "Special"})
    #if random_Police <= 0.003:
    #    print("Police added")
    #    box.append({"width":2.48 , "type" : "Special"})
    return box

def Priority_on_CarAdded(Priority):
    print("something")
#-----------------------------mainly action high volumn Case-----------------------------------------
def CarStacking(Box , Stack_state ,onMajor, onSpecialCar , number):
    #print("start")
    while not Stack_state.is_set():
        CarSpawnerChance = random.uniform(0 , 1)
        CarSpawnRate = 0.15
        #print((CarSpawnerChance * Place_List_Weight[Places] * LocalTimeWeight))
        #Adjust CarRate Later.
        if (onMajor*CarSpawnerChance * Place_List_Weight[Places] * LocalTimeWeight) > CarSpawnRate:
           # print("inside")
            SpecialCars = random_Priority() 
            if SpecialCars :
                print("there Special Car")
                for Car in SpecialCars:
                    onSpecialCar[0] += 1
                    print(onSpecialCar , number)
                    Box.append(Car)
            Nor_Ex = random.uniform(0,1)
            if Nor_Ex < 0.2:
                append_car = random.uniform(min_ex_car_range,max_ex_car_range)
                append_car = {"width":append_car , "type" : "Extra regular"}
                Box.append(append_car)
            else:
                append_car = random.uniform(min_nor_car_range,max_nor_car_range)
                append_car = {"width":append_car , "type" : "regular"}
                Box.append(append_car)
                                   
        time.sleep(1.5)
TimeExtra = 1
q_table = np.zeros((2,2))

alpha = 0.1 
gamma = 0.9
epsilon = 0.1

def action_choosen(state):
    if np.random.rand() < epsilon:

        return np.random.choice([0,1])
    else:

        return np.argmax(q_table[state])

def GreenLightTimeExtra(data = {} , reward=0 ):
    global q_table,TimeExtra
    current_state = 0 if data['crossRoad1'] == 0 and data['crossRoad2'] == 0 else 1

    action = action_choosen(current_state)

    if action == 0 :
        TimeExtra -= 0.1
    else:
        TimeExtra += 0.1

    new_state = 0 if data["crossRoad1"] == 0 and data["crossRoad2"] == 0 else 1

    q_table[current_state,action] = q_table[current_state,action] + alpha * (reward + gamma * np.max(q_table[new_state]) - q_table[current_state,action])

    return action


def GreenLightTime(TrafficVolume , onMajor):
    #print(TrafficVolumeS+TrafficVolumeW+TrafficVolumeE+TrafficVolumeN)
    #((TrafficVolumeE if TrafficVolumeE > TrafficVolumeW else TrafficVolumeW)+(TrafficVolumeS if TrafficVolumeS > TrafficVolumeN else TrafficVolumeN))
    
    GreenLight = (TrafficVolume / (TrafficVolumeN + TrafficVolumeW + TrafficVolumeE + TrafficVolumeS )) * TimeCycle *0.8 
    if GreenLight <=120 :
        return GreenLight
    else:
        return 120

Stack_setUp = threading.Event()

def FirstCrossLine():

    global crossRoad,crossRoad2 , TrafficVolumeN ,TrafficVolumeS,TrafficVolumeE,TrafficVolumeW ,EmergencyCar_Count_lane_one,EmergencyCar_Count_lane_two,EmergencyCar_Count_lane_three,EmergencyCar_Count_lane_four



    #initial 
    Stack_setUp.clear()
    CarStackingThread1 = threading.Thread(target=CarStacking , args=(crossRoad[1][2],Stack_setUp,1  ,EmergencyCar_Count_lane_one  , 1 ,))
    CarStackingThread2 = threading.Thread(target=CarStacking , args=(crossRoad[2][2],Stack_setUp,0.7,EmergencyCar_Count_lane_two , 2 ,))
    CarStackingThread3 = threading.Thread(target=CarStacking , args=(crossRoad[3][2],Stack_setUp,1  ,EmergencyCar_Count_lane_three , 3,))
    CarStackingThread4 = threading.Thread(target=CarStacking , args=(crossRoad[4][2],Stack_setUp,0.7,EmergencyCar_Count_lane_four , 4,))

    CarStackingThread1.start()
    CarStackingThread2.start()
    CarStackingThread3.start()
    CarStackingThread4.start()

    #CarStackingThread1.join()
    #CarStackingThread2.join()
    #CarStackingThread3.join()
    #CarStackingThread4.join()
    time.sleep(30)
    print(EmergencyCar_Count_lane_one[0], EmergencyCar_Count_lane_two[0] ,EmergencyCar_Count_lane_three[0],EmergencyCar_Count_lane_four[0])
    print("start")
    TrafficVolumeNThread =  threading.Thread(target=traffic_volumeN_generate)
    TrafficVolumeSThread =  threading.Thread(target=traffic_volumeS_generate)
    TrafficVolumeEThread =  threading.Thread(target=traffic_volumeE_generate)
    TrafficVolumeWThread =  threading.Thread(target=traffic_volumeW_generate)
    
    #print(TrafficVolumeN)
    #print(TrafficVolumeS)
    #print(TrafficVolumeE)
    #print(TrafficVolumeW)
    TrafficVolumeNThread.start()
    TrafficVolumeSThread.start()
    TrafficVolumeEThread.start()
    TrafficVolumeWThread.start()

    print(f"Road one :{len(crossRoad[1][2])}\nRoad three :{len(crossRoad[3][2])}")
    print(f"Road two :{len(crossRoad[2][2])}\nRoad four :{len(crossRoad[4][2])}")
    #TrafficVolumeNThread.join()
    #TrafficVolumeSThread.join()
    #TrafficVolumeEThread.join()
    #TrafficVolumeWThread.join()
    #start
    forever = threading.Event()
    while not forever.is_set():

        #After Green Light turning into Yellow Light for cooldown into RedLight 
        if crossRoad[1][0] and crossRoad[3][0]:
            #loop until turn into yellow light.
            #switch Sub and Major.
            MajorSwitch.set()

            GreenLight1 = GreenLightTime(TrafficVolumeN,1.2)
            GreenLight2 = GreenLightTime(TrafficVolumeS,1.2)
            GreenLight = GreenLight1 if GreenLight1 > GreenLight2 else GreenLight2
            
            print(GreenLight)
            switch = threading.Event()
            EmergencyCar = threading.Event()
            def switchoff(Greenlights):
                time.sleep(Greenlights)
                if not  EmergencyCar_Count_lane_one[0] and not  EmergencyCar_Count_lane_three[0]:
                    while not EmergencyCar.is_set():
                        print("time reserve for emergency")
                        if not  EmergencyCar_Count_lane_one[0] and not  EmergencyCar_Count_lane_three[0] :
                            print(  EmergencyCar_Count_lane_one[0] ,  EmergencyCar_Count_lane_three[0])
                            EmergencyCar.set()
                        time.sleep(1)
                EmergencyCar.clear()
                switch.set()
                print("switch off because over 120 seconds")
                
            TimeCountdown = threading.Thread(target=switchoff , args=(GreenLight,))
            TimeCountdown.start()
           # TimeCountdown.join()
            #our Light system no longer show time.
            print("GreenLight on Major Road")
            IsGreenLight = threading.Event()
            def ReleaseCars():
                
                #global crossRoad[1][2],crossRoad[3][2]
                while not IsGreenLight.is_set():
                    releaseCount = random.randint(1,2)
#-----------------------------------------------------------------------------
                    if not EmergencyCar_Count_lane_three[0] :

                        if len(crossRoad[3][2]) >= 2:
                            for _ in range(releaseCount):
                                crossRoad[3][2].pop(0)
                        elif len(crossRoad[3][2]) < 2 and len(crossRoad[3][2]) > 0:
                            crossRoad[3][2].pop(0)
                    else:

                        if len(crossRoad[3][2]) >= 2:
                            for _ in range(releaseCount):
                                if crossRoad[3][2][0]["type"] == "Special":
                                    crossRoad[3][2].pop(0)
                                    EmergencyCar_Count_lane_three[0] -= 1
                                else:
                                    crossRoad[3][2].pop(0)
                        elif len(crossRoad[3][2]) < 2 and len(crossRoad[3][2]) > 0:
                                if crossRoad[3][2][0]["type"] == "Special":
                                    crossRoad[3][2].pop(0)
                                    EmergencyCar_Count_lane_three[0] -= 1
                                else:
                                    crossRoad[3][2].pop(0)
#-----------------------------------------------------------------------------
                    if not  EmergencyCar_Count_lane_one[0]:

                        if len(crossRoad[1][2]) >= 2 : 
                            for _ in range(releaseCount):
                                crossRoad[1][2].pop(0)
                        elif len(crossRoad[1][2]) < 2 and len(crossRoad[1][2]) > 0:
                            crossRoad[1][2].pop(0)
                    else:

                        if len(crossRoad[1][2]) >= 2 : 
                            for _ in range(releaseCount):
                                if crossRoad[1][2][0]["type"] == "Special":
                                    crossRoad[1][2].pop(0)
                                    EmergencyCar_Count_lane_one[0]  -= 1
                                else:
                                    crossRoad[1][2].pop(0)
                        elif len(crossRoad[1][2]) < 2 and len(crossRoad[1][2]) > 0:
                            if crossRoad[1][2][0]["type"] == "Special":
                                crossRoad[1][2].pop(0)
                                EmergencyCar_Count_lane_one[0] -= 1
                            else:
                                crossRoad[1][2].pop(0)

#-----------------------------------------------------------------------------
                    time.sleep(1)
            CarsMoveStart = threading.Thread(target=ReleaseCars)
            CarsMoveStart.start()
            while not switch.is_set():
                crossRoad[1][0] ,crossRoad[3][0] = False , False
                crossRoad[2][0] , crossRoad[4][0] = True , True
                print(f"Road one :{len(crossRoad[1][2])}\nRoad three :{len(crossRoad[3][2])}")
                #print("There Some Special Car" if crossRoad[1][3] > 0 or crossRoad[3][3] > 0 else "")
                print(EmergencyCar_Count_lane_one[0] , EmergencyCar_Count_lane_three[0])
                #switch will change after achieve one of these goal.
                #-------------
                #Argency on others lane
                
                #Priority  limit to 0


                time.sleep(1)
            if len(crossRoad[1][2]) > 0 and len(crossRoad[3][2]) > 0:
                GreenLightTimeExtra( data={'crossRoad1':len(crossRoad[1][2]) , 'crossRoad2':len(crossRoad[3][2])} , reward = -10)
            else:
                GreenLightTimeExtra(data={'crossRoad1':0,'crossRoad2':0} , reward = 10)
            IsGreenLight.set()
            CarsMoveStart.join()
            print("yellow Light 3 seconds")
            time.sleep(3)
            print("Switch!")
        elif crossRoad[2][0] and crossRoad[4][0]:
            MajorSwitch.clear()
            #loop until turn into yellow light.
            #switch Sub and Major.
            GreenLight1 = GreenLightTime(TrafficVolumeE,1)
            GreenLight2 = GreenLightTime(TrafficVolumeW,1)
            GreenLight = GreenLight1 if GreenLight1 > GreenLight2 else GreenLight2
            print(GreenLight)
            switch2 = threading.Event()
            def switchoff(Greenlights):
                time.sleep(Greenlights)
                if not EmergencyCar_Count_lane_two[0]  and not EmergencyCar_Count_lane_four[0] :
                    while not EmergencyCar.is_set():
                        print("time reserve for emergency")
                        if not EmergencyCar_Count_lane_two[0]  and not EmergencyCar_Count_lane_four[0] :
                            print(EmergencyCar_Count_lane_two[0]  , EmergencyCar_Count_lane_four[0] )
                            EmergencyCar.set()
                        time.sleep(1)
                EmergencyCar.clear()
                switch2.set()
                print("switch off because over 120 seconds")
            TimeCountdown = threading.Thread(target=switchoff , args=(GreenLight,))
            TimeCountdown.start()
            #TimeCountdown.join()
            #our Light system no longer show time.
            print("GreenLight on Major Road")
            IsGreenLight = threading.Event()
            def ReleaseCars():
                while not IsGreenLight.is_set():
                    releaseCount = random.randint(1,2)
#-----------------------------------------------------------------------------
                    if not EmergencyCar_Count_lane_two[0] :

                        if len(crossRoad[2][2]) >= 2:
                            for _ in range(releaseCount):
                                crossRoad[2][2].pop(0)
                        elif len(crossRoad[2][2]) < 2 and len(crossRoad[2][2]) > 0:
                            crossRoad[2][2].pop(0)
                    else:

                        if len(crossRoad[2][2]) >= 2:
                            for _ in range(releaseCount):
                                if crossRoad[2][2][0]["type"] == "Special":
                                    crossRoad[2][2].pop(0)
                                    EmergencyCar_Count_lane_two[0]  -= 1
                                else:
                                    crossRoad[2][2].pop(0)
                        elif len(crossRoad[2][2]) < 2 and len(crossRoad[2][2]) > 0:
                            if crossRoad[2][2][0]["type"] == "Special":
                                crossRoad[2][2].pop(0)
                                EmergencyCar_Count_lane_two[0] -= 1
                            else:
                                crossRoad[2][2].pop(0)
#-----------------------------------------------------------------------------
                    if not  EmergencyCar_Count_lane_four[0]:

                        if len(crossRoad[4][2]) >= 2 : 
                            for _ in range(releaseCount):
                                crossRoad[4][2].pop(0)
                        elif len(crossRoad[4][2]) < 2 and len(crossRoad[4][2]) > 0:
                            crossRoad[4][2].pop(0)
                    else:

                        if len(crossRoad[4][2]) >= 2 : 
                            for _ in range(releaseCount):
                                if crossRoad[4][2][0]["type"] == "Special":
                                    crossRoad[4][2].pop(0)
                                    EmergencyCar_Count_lane_four[0]  -= 1
                                else:
                                    crossRoad[4][2].pop(0)
                        elif len(crossRoad[4][2]) < 2 and len(crossRoad[4][2]) > 0:
                            if crossRoad[4][2][0]["type"] == "Special":
                                crossRoad[4][2].pop(0)
                                EmergencyCar_Count_lane_four[0]  -= 1
                            else:
                                crossRoad[4][2].pop(0)

#-----------------------------------------------------------------------------
                    time.sleep(1)
            CarsMoveStart = threading.Thread(target=ReleaseCars )
            CarsMoveStart.start()
            while not switch2.is_set():
                
                crossRoad[2][0] ,crossRoad[4][0] = False , False
                crossRoad[1][0] , crossRoad[3][0] = True , True
                
                print(f"Road two :{len(crossRoad[2][2])}\nRoad four :{len(crossRoad[4][2])}")
                #print("There Some Special Car" if crossRoad[2][3] > 0 or crossRoad[4][3] else "")
                print(EmergencyCar_Count_lane_two[0]  , EmergencyCar_Count_lane_four[0] )
                time.sleep(1)
            IsGreenLight.set()
            CarsMoveStart.join()
            print("yellow Light 3 seconds")
            time.sleep(3)
            print("Switch!")
    Stack_setUp.set()
    CarStackingThread1.join()
    CarStackingThread2.join()
    CarStackingThread3.join()
    CarStackingThread4.join()




#------------------------------------------------mainly start-----------------------------------
#random for initial the program
time_statement_set()
FirstCrossLine()
