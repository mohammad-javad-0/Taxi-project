from math import sqrt

map = [["**" for _ in range(20)] for _ in range(8)]

def print_map(map):
    print("To request a taxi, enter T :")
    print("Enter U to add a new user :")
    print("Enter R to remove a user :")
    print("Enter A to add a new taxi :")
    print("Enter D to delete a taxi :")
    print("Enter M to check the details of a taxi :")
    for l in map:
        for i in l:
            print(i, end=" ")
        print()


# error classes
class InvalidAgeError(Exception):
    pass


class InvalidPhoneNumberError(Exception):
    pass


class InvalidGenderError(Exception):
    pass


class UserNameError(Exception):
    pass


class UserPlatesError(Exception):
    pass


class LocationRangeError(Exception):
    pass

class LocationError(Exception):
    pass


class User:
    def __init__(self, user_name, age, phone_number, gender):
        self.user_name = user_name
        self.age = age
        self.phone_number = phone_number
        self.gender = gender


class Taxi(User):
    def __init__(self, user_name, age, phone_number, gender, car_model, number_plates, location):
        super().__init__(user_name, age, phone_number, gender)
        self.car_model = car_model
        self.number_plates = number_plates
        self.location = {"x" : location[0], "y" : location[1]}
        map[self.location["y"]][self.location["x"]] = f"{self.number_plates:2}"

    def info(self):
        return f"{self.user_name} phone number : {self.phone_number}\ncar model : {self.car_model} plates : {self.number_plates} \
    x : {self.location['x']} y : {self.location['y']}"
    
    def __str__(self):
        return self.info()

    def __del__(self):
        map[self.location["y"]][self.location["x"]] = "**"


list_user_name = list()
list_taxi_name = list()
list_number_plates = list()
user = list()
user_num = 0
taxi_num = 0
taxi = list()


def get_taxi_location(taxi_number):
    while(True):
        try:
            x, y = input("Enter your location(0 <= x <= 19 and 0 <= y <= 7): ").split(" ")
            x, y = int(x), int(y)

            if (x < 0 or x > 19) or (y < 0 or y > 7):
                raise LocationRangeError

            for i in range(taxi_number):
                if taxi[i].location["x"] == x and  taxi[i].location["y"] == y:
                    raise LocationError
            
        except ValueError:
            print("Cannot use letters and Enter two entries separated by a space.Try again..")
        except LocationRangeError:
            print("Out of bounds location.Try again..")
        except LocationError:
            print("This place is occupied by another car.Try again..")
        else:
            return x, y
        

def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 15 or age > 100:
                raise InvalidAgeError()
        except ValueError:
            print("Cannot use letters.Try again..")
        except InvalidAgeError:
            print("Age is not allowed.Try again..")
        else:
            return age


def get_phone_number():
    while True:
        try:
            phone_number = input("Enter your phone number: ")
            if not phone_number.isdigit():
                raise ValueError()
            elif len(phone_number) != 11:
                raise InvalidPhoneNumberError()
        except ValueError:
            print("Cannot use letters.Try again..")
        except InvalidPhoneNumberError:
            print("Phone number is not allowed.Try again..")
        else:
            return phone_number
        

def get_gender():
    while True:
        try:
            gender = input("Enter your gender(male or female): ")
            if gender.lower() in ["male", "female"]:
                return gender
            raise InvalidGenderError()
        except InvalidGenderError:
            print("Invalid input.Please enter male or female..")


def get_and_check_user_name(flag1, flag2= 0):
    """flag1 = 0, flag2 = 0 -> make user name for user
    flag1 = 0, flag2 = 1  -> make user name for taxi
    flag1 = 1 -> check user name for user"""
    while True:
        user_name = input("Enter user name: ")
        if flag1 == 0:
            try:
                if (flag2 == 0 and user_name in list_user_name) or (flag2 == 1 and user_name in list_taxi_name):
                    raise UserNameError()
            except UserNameError:
                print("Username is already selected.Please try again..")
            else:
                return user_name
        else:
            try:
                if not user_name in list_user_name:
                    raise UserNameError()
            except UserNameError:
                print("Username not found.Please try again..")
            else:
                return user_name


def get_and_check_number_plates(flag):
    """flag = 0 -> make taxi
    flag = 1 -> check taxi"""
    while True:
        number_plates = input("Enter the license plate number of the taxi: ")
        if flag == 0:
            try:
                if number_plates in list_number_plates:
                    raise UserPlatesError()
            except UserPlatesError:
                print("Number plates is already selected.Please try again..")
            else:
                return number_plates
        else:
            try:
                if not number_plates in list_number_plates:
                    raise UserPlatesError()
            except UserPlatesError:
                print("Number plates not found.Please try again..")
            else:
                return number_plates


def remove_user(user_name):
    for num, user_obj in enumerate(user):
            if user_obj.user_name == user_name:
                list_user_name.remove(user_name)
                del user[num]
                break


def delete_taxi(number_plates):
    for num, taxi_obj in enumerate(taxi):
            if taxi_obj.number_plates == number_plates :
                list_number_plates.remove(number_plates)
                list_taxi_name.remove(taxi_obj.user_name)
                del taxi[num]
                break


def get_location():
    while True:
        try:
            x, y = input().split(" ")
            x, y = int(x), int(y)
            if (x < 0 or x > 19) or (y < 0 or y > 7):
                raise LocationRangeError
        except LocationRangeError:
            print("Out of bounds location.Try again..")
        except ValueError:
            print("Cannot use letters and Enter two entries separated by a space.Try again..")
        else:
            return x, y

def request_taxi(x1, y1, x2, y2, taxi_number):
    for i in range(taxi_number):
            t_x = taxi[i].location["x"]
            t_y = taxi[i].location["y"]

            if  (t_x <= x1 + 3 and t_x >= x1 -3) and (t_y <= y1 + 3 and t_y >= y1 - 3):
                print("A taxi was found..")
                travel_amount = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                print(taxi[i].info())
                print(f"Travel amount : {travel_amount}")
                confirm_trip = input("Do you want to travel (yes or no)? ")

                if confirm_trip.lower() == "no":
                    print("The trip was cancelled...")
                    continue

                elif confirm_trip.lower() == "yes":
                    map[taxi[i].location["y"]][taxi[i].location["x"]] = "**"
                    taxi[i].location["x"] = x2
                    taxi[i].location["y"] = y2
                    print("The trip was successful...")
                    map[taxi[i].location["y"]][taxi[i].location["x"]] = f"{taxi[i].number_plates:2}"
                    with open(f"{taxi[i].number_plates}.txt", "a") as writer:
                        writer.write(f"{taxi[i].info()} and travel amount: {travel_amount}\n")

                else:
                    try:
                        raise ValueError
                    except ValueError:
                        print("Invalid input.Try again..")

                break