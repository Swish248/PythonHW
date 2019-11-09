print("Hello World!")
msg = "Hello World!"
print(msg)
first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)
bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
last_bike = bikes[-1]
for bikeee in bikes:
    print(bikeee)
bikess = []
bikess.append('trek')
bikess.append('redline')
bikess.append('giant')
print(bikes)
squares = []
for x in range(1, 11):
    squares.append(x**2)
squaress = [x**2 for x in range(1, 11)]
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two)
copy_of_bikes = bikes[:]
print(copy_of_bikes)
dimensions = (1920, 1080)
print(dimensions)
x = 31
if x == 42 or x != 42 or x > 42 or x >= 42 or x < 42 or x <= 42:
    print("BLEH")
if 'trek' in bikes:
    print("YAY")
if 'surly' not in bikes:
    print("OOF")
game_active = True
can_edit = False
age = 19
if age >= 18:
 print("You can vote!")
if age < 4:
 ticket_price = 0
elif age < 18:
 ticket_price = 10
else:
 ticket_price = 15
alien = {'color': 'green', 'points': '5'}
print("The alien's color is " + alien['color'])
alien['x_position'] = 0
fav_numbers = {'eric': '17', 'ever': '14'}
for name, number in fav_numbers.items():
    print(name + ' loves a number')
fav_numbers = {'eric': '17', 'ever': '14'}
for name in fav_numbers.keys():
    print(name + ' loves a number')
fav_numbers = {'eric': '17', 'ever': '14'}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')
name = input("What is your name? ")
print("Hello, " + name + "!")
ageeee = input("How old are you? ")
ageeee = int(ageeee)
pi = input("What's the value of pi? ")
pi = float(pi)
current_value = 1
while current_value <= 5:
    print(current_value)
current_value += 1
msgg = ''
while msgg != 'quit':
    msgg = input("What's your message? ")
print(msgg)
def greet_user():
    print("Hello")

greet_user()
def greet_user(username):
    print("Hello, " + username + "!")
greet_user('jesse')
def make_pizza(topping = 'bacon'):
    print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')
def add_numbers(x, y):
    return x + y

sum = add_numbers(3, 5)
print(sum)
class Dog():
 def __init__(self, name):
    self.name = name
 def sit(self):
    print(self.name + " is sitting.")
my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()
class SARDog(Dog):
 """Represent a search dog."""
 def __init__(self, name):
    super().__init__(name)
 def search(self):
    print(self.name + " is searching.")
my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()
class SARDog(Dog):
    def __init__(self, name):
        super
            ().__init__(name)
 def search(self):
    print(self.name + " is searching.")
my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()
filename = 'siddhartha.txt'
with open(filename) as file_object:
 lines = file_object.readlines()
for line in lines:
 print(line)
filename = 'journal.txt'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.")
 filename = 'journal.txt'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.")
 filename = 'journal.txt'
with open(filename, 'w') as file_object:
 file_object.write("I love programming.")











































































































