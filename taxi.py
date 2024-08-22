import os
import time
# from taxi_module import *
from taxi_module import *

while(True):
    time.sleep(2)
    os.system("cls")
    print_map(map)
    order = input().upper()
    
    if order == "C" or order == "\n":
        pass
    
    elif order == "U":
        user_name = get_and_check_user_name(0, 0)
        age = get_age()
        phone_number = get_phone_number()
        gender = get_gender()

        user.append(User(user_name, age, phone_number, gender))
        user_num += 1
        list_user_name.append(user_name)


    elif order == "R":
        if user_num == 0:
            print("There is no person in the system.")
        else:
            user_name = get_and_check_user_name(1, 0)
            remove_user(user_name)
            user_num -= 1
            print("User deleted successfully.")

    elif order == "A":
        user_name = get_and_check_user_name(0, 1)
        age = get_age()
        phone_number = get_phone_number()
        gender = get_gender()
        car_model = input("Enter your car model: ")
        number_plates = get_and_check_number_plates(0)
        location = get_taxi_location(taxi_num)
        
        taxi.append(Taxi(user_name, age, phone_number, gender, car_model, number_plates, location))
        taxi_num += 1
        list_taxi_name.append(user_name)
        list_number_plates.append(number_plates)
        
    elif order == "D":
        if taxi_num == 0:
            print("There are no taxis in the system.")
        else:
            number_plates = get_and_check_number_plates(1)
            delete_taxi(number_plates)
            taxi_num -= 1
            print("Taxi was successfully deleted.")

    elif order == "T":
        if user_num == 0 or taxi_num == 0:
            print("You cannot apply. There are no taxis or person in the system.")
        else:
            user_name = get_and_check_user_name(1, 0)

            print("Enter the origin location(0 <= x <= 19 and 0 <= y <= 7): ", end=" ")
            x1, y1 = get_location()

            print("Enter the destination location(0 <= x <= 19 and 0 <= y <= 7): ", end=" ")
            x2, y2 = get_location()

            request_taxi(x1, y1, x2, y2, taxi_num)

    elif order == "M":
        taxi_plates = get_and_check_number_plates(1)
        with open(f"{taxi_plates}.txt", "r") as reader:
            while True :
                travel_history = reader.readline()
                if travel_history == "":
                    break
                print(travel_history)

    elif order == "E":
        exit()

    elif order == "WW":
        print(f"plat = {list_number_plates}, user = {list_user_name}, taxi = {list_taxi_name}")
        a = input()
    else:
        print("Invalid input..")