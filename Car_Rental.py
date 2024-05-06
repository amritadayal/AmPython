import datetime
class CarRental:

    def __init__(self,car_id, model, make, availability, price_hour, price_day, price_week,stock=0):
        """
        Constructor class to instantiate car rental shop.
        """
        self.car_id = car_id
        self.model = model
        self.make = make
        self.availability = availability
        self.price_hour = price_hour
        self.price_day = price_day
        self.price_week = price_week

        self.stock = stock

    def displaystock(self):
        """
        Displays the currently available cars for rent.
        """
        return self.availability


    def rentCarOnHourlyBasis(self,duration,n):
        """
        Rent a car on hourly basis to a customer.
        """
        if duration == "hour":
           return self.price_hour
        elif duration == "day":
            return self.price_day
        elif duration == "week":
            return self.price_week
        else:
            return None


    def rentCarOnDailyBasis(self, n):
        """
        Rents a car on daily basis to a customer.
        """


    def rentCarOnWeeklyBasis(self, n):
        """
        Rents a car on weekly basis to a customer.
        """




    def returnCar(self, request):
        """
        1. Accept a rented car from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfCars = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfCars

            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfCars

            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfCars


            if (3 <= numOfCars <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your car. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None



class Customer:

    def __init__(self,customer_id, name, contact_info):
        """
        Constructor method to instantiate various customer objects.
        """

        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0


    def requestCar(self):
        """
        Takes a request from the customer for the number of cars.
        """

        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if cars < 1:
            print("Invalid input. Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
        return self.cars

    def returnCar(self):
        """
        Allows customers to return their cars to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars
        else:
            return 0,0,0