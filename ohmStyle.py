import random
import time
Weather_set = ['hot','sunny', 'rainy', 'cloudy', 'snowy']
Light_time_limit = 120 # seconds
Place_list = ["Normal","tourist_attraction","School","Pub","city"]
max_nor_car_range , min_nor_car_range = 5.822 , 4.064 # meters
min_ex_car_range , max_ex_car_range = 6 , 8 # meters
Priority = 0 
lane_size = 3 # meters
lane = 2 # lanes
#-----------------------Time---------------------#

localtime = random.randint(0, 24) # random time

if localtime >= 6 and localtime <= 9:
    print("It's morning. ")
elif localtime > 9 and localtime <= 14:
    print("It's afternoon." )
elif localtime > 14 and localtime <= 17:
    print("It's afternoon." )
else:
    print("It's evening.")

#ยิ่งนาน priority ยิ่งสูง
# Ambulance + 50 , Firetruck + 40 , Police + 30
#ยิ่งแถวยาวยิ่งมีความสำคัญสูง

#-----------------random values-----------------#
#Argency_Case = random.randint(0,4)
#match Argency_Case:
#    case 0:
#        Argency_Case = Null
#    case 1:
#        Argency_Case = Ambulance
#    case 2:
#        Argency_Case = Firetruck
#    case 3:
#        Argency_Case = Police
random_Ambulance = random.uniform(0, 1) # random 0 or 1
random_Firetruck = random.uniform(0, 1) # random 0 or 1
random_Police = random.uniform(0, 1) # random 0 or 1
lane_size_random = random.randint(2, 3) # random lane size ( meters )

Weather = random.choice(Weather_set) # random weather

#-----------------Traffic-----------------#

#if main road high traffic volume, it will stack sub road to 500m .
# always random car for high volumn traffic
traffic_volume_low = random.randint(0, 30) # random traffic volume
traffic_volume_high = random.randint(31, 100) # random traffic volume 
Places = random.choice(Place_list) # random place


#-----------------Priority-----------------#
if random_Ambulance <= 0.15:
    Priority += 50
if random_Firetruck <= 0.01:
    Priority += 60
if random_Police <= 0.03:
    Priority += 30

localtime = random.uniform(0,24) # random time
Car_range_1st=[]
Car_range_2nd=[]
Yelloe_light = 3
traffic_volume = random.choice([traffic_volume_high,traffic_volume_low])
if localtime >= 6 and localtime <= 9:
    if Car_range_2nd == [] :
        traffic_volume = 10
    print("Not many cars")
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have',0]) == 'Have':
            Car_range_1st.append(random.choice([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3]))
            print(Car_range_1st)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
            print(sum(Car_range_1st))
            if sum(Car_range_1st) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
    traffic_volume = traffic_volume_low
    Yelloe_light = 3
    if Car_range_1st == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have',0]) == 'Have':
            Car_range_2nd.append(random.choice(random.choices([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3],[0.8,0.2],k=1)))
            print(Car_range_2nd)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
            print(sum(Car_range_2nd))
            if sum(Car_range_2nd) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
    traffic_volume = traffic_volume_low
    Yelloe_light = 3
    print(Car_range_1st,Car_range_2nd)
elif localtime > 9 and localtime <= 14:
    print("Not many cars" )
    if Car_range_2nd == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have',0]) == 'Have':
            Car_range_1st.append(random.choice([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3]))
            print(Car_range_1st)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
            print(sum(Car_range_1st))
            if sum(Car_range_1st) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
    traffic_volume = traffic_volume_low
    Yelloe_light = 3
    if Car_range_1st == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have',0]) == 'Have':
            Car_range_2nd.append(random.choice(random.choices([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3],[0.8,0.2],k=1)))
            print(Car_range_2nd)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
            print(sum(Car_range_2nd))
            if sum(Car_range_2nd) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
    traffic_volume = traffic_volume_low
    Yelloe_light = 3
    print(Car_range_1st,Car_range_2nd)    
elif localtime > 14 and localtime <= 17:
    print("Not many cars" )
    if Car_range_2nd == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have',0]) == 'Have':
            Car_range_1st.append(random.choice([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3]))
            print(Car_range_1st)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
            print(sum(Car_range_1st))
            if sum(Car_range_1st) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
    traffic_volume = traffic_volume_low
    Yelloe_light = 3
    if Car_range_1st == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have',0]) == 'Have':
            Car_range_2nd.append(random.choice(random.choices([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3],[0.8,0.2],k=1)))
            print(Car_range_2nd)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
            print(sum(Car_range_2nd))
            if sum(Car_range_2nd) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
    traffic_volume = traffic_volume_low
    Yelloe_light = 3
    print(Car_range_1st,Car_range_2nd)
else:
    print("many cars")
    if Car_range_2nd == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have']) == 'Have':
            Car_range_1st.append(random.choice([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3]))
            print(Car_range_1st)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
            print(sum(Car_range_1st))
            if sum(Car_range_1st) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_2nd == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_2nd.remove(Car_range_2nd[0])
    traffic_volume = traffic_volume_high
    Yelloe_light = 3
    if Car_range_1st == [] :
        traffic_volume = 10
    while traffic_volume >= 0 or Yelloe_light >= 0 :
        traffic_volume -= 1
        print(traffic_volume)
        if random.choice(['Have']) == 'Have':
            Car_range_2nd.append(random.choice(random.choices([random.uniform(min_nor_car_range,max_nor_car_range)+3,random.uniform(min_ex_car_range,max_ex_car_range)+3],[0.8,0.2],k=1)))
            print(Car_range_2nd)
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
            print(sum(Car_range_2nd))
            if sum(Car_range_2nd) > 500:
                traffic_volume = -1
        else:
            time.sleep(2)
            traffic_volume -= 1
            if traffic_volume < 0 :
                Yelloe_light -= 2
            else :
                if Car_range_1st == []:
                    if traffic_volume > 10:
                        traffic_volume = 10
                else :
                    Car_range_1st.remove(Car_range_1st[0])
    traffic_volume = traffic_volume_high
    Yelloe_light = 3
    print(Car_range_1st,Car_range_2nd)
