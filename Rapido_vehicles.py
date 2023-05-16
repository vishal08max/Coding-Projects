print("<-------Online Vehicle Renting Company - Rapido------->")
r = "/---Rental Plans For Two Wheelers---/"
Bike = "Two Wheeler"
print(r)
a = "per hour" #per hour
b = "one day" #one day
c = "three days" #3 days
print("For per_hour: ",400)
print("For one_day: ",9600)
print("For three_days: ",28800)
choice_1 = "yes"
choice_2 = "no"
a1 = input("Enter your vehicle type: ")
if a1 == Bike:
    t1 = input("Enter your Time of usage: ")
    if t1 == a:
        choice = input("Can I Confirm Your Ride Sir: ")
        if choice == choice_1:
            print("\n/----Invoice Of Your Travel----/ \nRental Type: Bike \nno of hours: Per_Hour \nFor Per_hour Cost Is: 400 \nTax = 18%---> Rs72+400 \nYour Grand Total: 472 \nEnjoy Your Ride, Have a Safe Journey")
    elif t1 == b:
        choice = input("Can I Confirm Your Ride Sir: ")
        if choice == choice_1:
            print("\n/----Invoice Of Your Travel----/ \nRental Type: Bike \nno of hours: One_Day \nFor One_Day Cost Is: 9600 \nTax = 18%---> Rs1728+9600 \nYour Grand Total: 11328 \nEnjoy Your Ride, Have a Safe Journey")
    elif t1 == c:
        choice = input("Can I Confirm Your Ride Sir: ")
        if choice == choice_1:
            print("\n/----Invoice Of Your Travel----/ \nRental Type: Bike \nno of hours: Three_Days \nFor Three_Days Cost Is: 28800 \nTax = 18%---> Rs5184+28800 \nYour Grand Total: 33984 \nEnjoy Your Ride, Have a Safe Journey")
else:
    Car = "Four Wheeler"
    r = "/---Rental Plans For Four Wheelers---/"
    print(r)
    a = "per hour" #per hour
    b = "one day" #one day
    c = "three days" #3 days
    print("For per_hour: ",800)
    print("For one_day: ",19200)
    print("For three_days: ",57600)
    if a1 == Car:
        t1 = input("Enter your Time of usage: ")
        if t1 == a:
            choice = input("Can I Confirm Your Ride Sir: ")
            if choice == choice_1:
                print("\n/----Invoice Of Your Travel----/ \nRental Type: Car \nno of hours: Per_hour \nFor Per_hour Cost Is: 800 \nTax = 18% ---> Rs144+800 \nYour Grand Total: 944 \nEnjoy Your Ride, Have a Safe Journey")
        elif t1 == b:
            choice = input("Can I Confirm Your Ride Sir: ")
            if choice == choice_1:
                print("\n/----Invoice Of Your Travel----/ \nRental Type: Car \nno of hours: One_Day \nFor One_Day Cost Is: 19200 \nTax = 18% ---> Rs3456+19200 \nYour Grand Total: 22656 \nEnjoy Your Ride, Have a Safe Journey")
        elif t1 == c:
            choice = input("Can I Confirm Your Ride Sir: ")
            if choice == choice_1:
                print("\n/----Invoice Of Your Travel----/ \nRental Type: Car \nno of hours: Three_Days \nFor Three_Days Cost Is: 57600 \nTax = 18% ---> Rs10368+57600 \nYour Grand Total: 67968 \nEnjoy Your Ride, Have a Safe Journey")
    else:
        print("This Vehicle Service Is Not Available In Us")
