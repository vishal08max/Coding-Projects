print("/--------Hard Rock Cafe And Restaurent - Ur Food Station--------/")
class Table_Reservation:
    def Table(self):
        print("Tables Available To Reserve In Our Restuarent")
        print("Table 1")
        print("Table 2")
        print("Table 3")
        a = 1
        b = 2
        c = 3
        print("                                          ")
        choice = int(input("Enter Your Desired Table Code To Book Your Table:"))
        if choice == a:
            print("Table 1 Booked")
        elif choice == b:
            print("Table 2 Booked")
        elif choice == c:
            print("Table 3 Booked")
class Menu:
    def Menu(self):
        d = "yes"
        e = "yes"
        print("                                          ")
        choice = input("Do You Wanna See Our Menu Sir (Yes/No):")
        print("                                          ")
        if choice == d:
            print("Our Cafe Menu And Their Prices")
            print("Main-Course Menu.")
            print("1.Cheeseburger:Rs 670")
            print("2.Grilled Salmon:Rs 800")
            print("3.Crinkle-Cut Fries:Rs 400")
            print("4.Fishes & Chips:Rs 1200")
class order:
    def order(self):
        f1 = "1"
        f2 = "2"
        f3 = "3"
        f4 = "4"
        I1 = "1 2"
        I2 = "2 3"
        I3 = "3 4"
        I4 = "1 4"
        I5 = "1 3"
        I6 = "1 2 3"
        I7 = "2 3 4"
        I8 = "1 2 4"
        I9 = "1 3 4"
        I10 = "1 2 3 4"
        ord = input("Enter the Food Code to order:")
        print("                                          ")
        if ord == f1:
            print("Orderd Cheeseburger")
            print("Your Grand Total:Rs 670")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == f2:
            print("Orderd Grilled Salmon")
            print("Your Grand Total:Rs 800")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == f3:
            print("Orderd Crinkle-Cut Fries")
            print("Your Grand Total:Rs 400")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == f4:
            print("Orderd Fishes & Chips")
            print("Your Grand Total:Rs 1200")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I1:
            print("Orderd CheeseBurger and Grilled Salmon")
            print("Total Cost:Rs 670 + Rs 800")
            print("Your Grand Total:Rs 1470")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I2:
            print("Orderd Grilled Salmon and Crinkle-Cut Fries")
            print("Total Cost:Rs 800 + Rs 400")
            print("Your Grand Total:Rs 1200")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I3:
            print("Orderd Crinkle-Cut Fries and Fishes & Chips")
            print("Total Cost:Rs 400 + Rs 1200")
            print("Your Grand Total:Rs 1600")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I4:
            print("Orderd CheeseBurger and Fishes & Chips")
            print("Total Cost:Rs 670 + Rs 1200")
            print("Your Grand Total:Rs 1870")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I5:
            print("Orderd CheeseBurger and Crinkle-Cut Fries")
            print("Total Cost:Rs 670 + Rs 400")
            print("Your Grand Total:Rs 1070")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I6:
            print("Orderd CheeseBurger, Grilled Salmon and Crinkle-Cut Fries")
            print("Total Cost:Rs 670 + Rs 800 + Rs 400")
            print("Your Grand Total:Rs 1870")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I7:
            print("Orderd Grilled Salmon, Crinkle-Cut Fries and Fishes & Chips")
            print("Total Cost:Rs 800 + Rs 400 + Rs 1200")
            print("Your Grand Total:Rs 1470")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I8:
            print("Orderd CheeseBurger, Grilled Salmon and Fishes & Chips")
            print("Total Cost:Rs 670 + Rs 800 + Rs 1200")
            print("Your Grand Total:Rs 2670")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I9:
            print("Orderd CheeseBurger, Crinkle-Cut Fries and Fishes & Chips")
            print("Total Cost:Rs 670 + Rs 400 + Rs 1200")
            print("Your Grand Total:Rs 2270")
            print("Happy Eating,Enjoy Your Meal")
        elif ord == I10:
            print("Orderd CheeseBurger, Grilled Salmon, Crinkle-Cut Fries and Fishes & Chips")
            print("Total Cost:Rs 670 + Rs 800 + Rs 400 + Rs 1200")
            print("Your Grand Total:Rs 3070")
            print("Happy Eating,Enjoy Your Meal")        
R = Table_Reservation()
R.Table()
M = Menu()
M.Menu()
o = order()
o.order()
            