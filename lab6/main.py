def ex1():
    class Shape:
        def area(self):
            pass
        def perimeter(self):
            pass
        def get_name(self):
            pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
            self.pi = 3.14159
        def area(self):
            return self.pi * self.radius ** 2
        def perimeter(self):
            return 2 * self.pi * self.radius
        def get_name(self):
            return "Circle"

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            return self.width * self.height
        def perimeter(self):
            return 2 * (self.width + self.height)
        def get_name(self):
            return "Rectangle"

    class Triangle(Shape):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
        def area(self):
            s = self.perimeter() / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        def perimeter(self):
            return self.a + self.b + self.c
        def get_name(self):
            return "Triangle"


    for form in [Circle(5), Rectangle(2, 3), Triangle(3, 4, 5)]:
        print(f'Shape of type {form.get_name()} with Area: {form.area()} and Perimeter: {form.perimeter()}')

def ex2():
    class Account:
        def __init__(self, name, balance):
            self.name = name
            self.balance = balance
        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
        def get_balance(self):
            return self.balance
        def get_name(self):
            return self.name

    class SavingsAccount(Account):
        def __init__(self, name, balance, interest_rate):
            super().__init__(name, balance)
            self.interest_rate = interest_rate
        def calculate_interest(self):
            return self.balance * self.interest_rate

    class CheckingAccount(Account):
        def __init__(self, name, balance):
            super().__init__(name, balance)

    savingsAccDorian = SavingsAccount('Dorian', 900, 0.1)
    checkingAccDorian = CheckingAccount('Dorian', 90)

    print(f'CheckingAccount for {checkingAccDorian.get_name()} has {checkingAccDorian.get_balance()} RON left')
    print(f'SavingsAccount for {savingsAccDorian.get_name()} has {savingsAccDorian.get_balance()} RON left and Interest: {savingsAccDorian.calculate_interest()}')
    print('Adding 500 to SavingsAccount')
    savingsAccDorian.deposit(500)
    print(f'SavingsAccount for {savingsAccDorian.get_name()} has {savingsAccDorian.get_balance()} RON left and Interest: {savingsAccDorian.calculate_interest()}')
    print('Withdrawing 20 from CheckingAccount')
    checkingAccDorian.withdraw(20)
    print(f'CheckingAccount for {checkingAccDorian.get_name()} has {checkingAccDorian.get_balance()} RON left')

def ex3():
    class Vehicle:
        def __init__(self, make, model, year, fuel_max):
            self.make = make
            self.model = model
            self.year = year
            self.mileage = 0
            self.fuel_max = fuel_max
            self.fuel_left = fuel_max
        def add_mileage(self, mileage):
            if mileage > 0:
                self.mileage += mileage
        def spend_fuel(self, fuel):
            if 0 < fuel <= self.fuel_left:
                self.fuel_left -= fuel

    class Car(Vehicle):
        def __init__(self, make, model, year, fuel_max):
            super().__init__(make ,model, year, fuel_max)
        def calculate_mileage(self):
            return self.mileage / (self.fuel_max - self.fuel_left)

    class Motorcycle(Vehicle):
        def __init__(self, make, model, year, fuel_max):
            super().__init__(make, model, year, fuel_max)
        def calculate_mileage(self):
            return self.mileage / (self.fuel_max - self.fuel_left)

    class Truck(Vehicle):
        def __init__(self, make, model, year, fuel_max, towing_capacity):
            super().__init__(make, model, year, fuel_max)
            self.towing_capacity = towing_capacity
        def add_towing_weight(self, weight):
            if 0 < weight <= self.towing_capacity:
                self.towing_capacity -= weight
        def drop_towing_weight(self, weight):
            if 0 < weight:
                self.towing_capacity += weight
        def calculate_towing_capacity(self):
             return self.towing_capacity

    car = Car('Honda', 'Civic', 1990, 200)
    car.add_mileage(100)
    car.spend_fuel(10)
    print(f'Calculated Mileage for {car.make} {car.model} from {car.year} after spending 10Fuel for 100Miles: {car.calculate_mileage()}')

    motorcycle = Motorcycle('Honda', 'Shadow', 2000, 200)
    motorcycle.add_mileage(100)
    motorcycle.spend_fuel(10)
    print(f'Calculated Mileage for {motorcycle.make} {motorcycle.model} from {motorcycle.year} after spending 10Fuel for 100Miles: {motorcycle.calculate_mileage()}')

    truck = Truck('Mercedes', 'Vidos', 2014, 700, 1000)
    truck.add_towing_weight(100)
    print(f'Calculated towing capacity for {truck.make} {truck.model} from {truck.year} after picking up 100KG: {truck.calculate_towing_capacity()}')



def ex4():
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary
        def get_name(self):
            return self.name
        def get_salary(self):
            return self.salary

    class Manager(Employee):
        def __init__(self, name, salary):
            super().__init__(name, salary)
        def start_meeting(self):
            print(f'Manager {self.name} started a meeting')

    class Engineer(Employee):
        def __init__(self, name, salary):
            super().__init__(name, salary)
        def write_blueprint(self):
            print(f'Engineer {self.name} is writing a new blueprint')

    class Salesperson(Employee):
        def __init__(self, name, salary):
            super().__init__(name, salary)
        def make_sale(self):
            print(f'Salesperson {self.name} made a sale')

    for employee in [Engineer('Mike', 8000), Manager('George', 12000), Salesperson('Jon', 10000)]:
        print(f'Salary for Employee {employee.name} is {employee.salary}')
        if isinstance(employee, Engineer):
            print(f'Their role is Engineer')
            employee.write_blueprint()
        if isinstance(employee, Manager):
            print(f'Their role is Manager')
            employee.start_meeting()
        if isinstance(employee, Salesperson):
            print(f'Their role is Salesperson')
            employee.make_sale()

def ex5():
    class Animal:
        def __init__(self, name):
            self.name = name

    class Mammal(Animal):
        def __init__(self, name, legs, has_fur, species):
            super().__init__(name)
            self.legs = legs
            self.has_fur = has_fur
            self.species = species
        def get_info(self):
            str_fur = "" if self.has_fur else "no"
            return f'My name is {self.name}, I\'m a {self.species} with {self.legs} legs and have {str_fur} fur'

    class Bird(Animal):
        def __init__(self, name, legs, can_fly, species):
            super().__init__(name)
            self.legs = legs
            self.can_fly = can_fly
            self.species = species
        def get_info(self):
            str_fly = "" if self.can_fly else "not"
            return f'My name is {self.name}, I\'m a {self.species} with {self.legs} legs and can {str_fly} fly'

    class Fish(Animal):
        def __init__(self, name, deep_water, species):
            super().__init__(name)
            self.deep_water = deep_water
            self.species = species
        def get_info(self):
            str_water = "deep" if self.deep_water else "shallow"
            return f'My name is {self.name}, I\'m a {self.species} and swim in {str_water} water'

    dog = Mammal('Skippy', 4, True, 'Dog')
    penguin = Bird('Waddles', 2, False, 'Penguin')
    anglerfish = Fish('Ugly', True, 'Anglerfish')

    for animal in [dog, penguin, anglerfish]:
        print(animal.get_info())

def ex6():
    class LibraryItem():
        def __init__(self, name):
            self.name = name
            self.checked_out = False
        def check_out(self):
            if not self.checked_out:
                self.checked_out = True
            else:
                print(f'Already checked this out: {self.name}')
        def item_return(self):
            if self.checked_out:
                self.checked_out = False
            else:
                print(f'You haven\'t checked this out yet: {self.name}')

    class Book(LibraryItem):
        def __init__(self, name, author, pages):
            super().__init__(name)
            self.author = author
            self.pages = pages
        def display_info(self):
            print(f'Author: {self.author}, Pages: {self.pages}')

    class DVD(LibraryItem):
        def __init__(self, name, director, duration):
            super().__init__(name)
            self.director = director
            self.duration = duration
        def display_info(self):
            print(f'Director: {self.director}, Duration: {self.duration}')

    class Magazine(LibraryItem):
        def __init__(self, name, publisher, topic):
            super().__init__(name)
            self.publisher = publisher
            self.topic = topic
        def display_info(self):
            print(f'Publisher: {self.publisher}, Topic: {self.topic}')

    book = Book('Inima de cerneala', 'Cornelia Funke', 496)
    dvd = DVD('8 Mile', 'Curtis Hanson', '1h 46m')
    magazine = Magazine('Muscle & Health', 'IFBB Official', 'Fitness')

    print(f'Checking out DVD: {dvd.name}')
    dvd.check_out()
    print(f'Checkout out Book: {book.name}')
    book.check_out()

    for item in [book, dvd, magazine]:
        item.display_info()

    print(f'Returning DVD: {dvd.name}')
    dvd.item_return()
    print(f'Checking out Book: {book.name} again')
    book.check_out()

def main():
    print("======EX1======")
    ex1()
    print("======EX2======")
    ex2()
    print("======EX3======")
    ex3()
    print("======EX4======")
    ex4()
    print("======EX5======")
    ex5()
    print("======EX6======")
    ex6()

if __name__ == "__main__":
    main()

