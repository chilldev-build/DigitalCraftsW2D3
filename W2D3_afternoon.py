# DC 08 2019 W2 D3 Afternoon Stuff

## OOP Object oriented programming

#Way of coding, data set that has some methods to work on data.
# attributes properties or states can apply
# have abilities or 'methods' available to work on data
# created by instantiating via a 'constructor'. 
#official name is instances. 

#class - is like a blueprint/ it defines the constructor/ 
#class - it specifies what attributes instances have/it contains the defs of the methods instances have

#class Cat:
#    #class attribute
#    species = 'mammal'
#
#    # initialize / Instance Attributes
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#gus = Cat('Gus', 8)
#print('{} is {}'.format(gus.name, gus.age))

#class Cat:
#    #class attribute
#    species = 'mammal'
#
#    # initialize / Instance Attributes
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def description(self):
#        return '{} is {}'.format(self.name, self.age)
#
#gus = Cat('Gus', 8)
#beans = Cat('Beans', 10)
#
#print(gus.description())
#print(beans.description())

## Class Assignments

# 1 Basics


class Person:
    def __init__(self, name, email, phone, friends = [], greet_count = 0):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greet_count = 0

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person):
        print( 'Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greet_count += 1

# Add a method to class

    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}'.format(self.name, self.email, self.name, self.phone)) 

# Add a method to class to add friend

    def add_friend(self, friend_name):
        return self.friends.append(friend_name.name)

# Add a method to class to find number of friends

    def count_friends(self):
        print(len(self.friends))

    def print_count(self):
        print(self.greet_count)


sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')

print_name = input('Enter a name for details: ')

print(print_name)


#Adding the long way
jordan.friends.append('Sonny')
sonny.friends.append('Jordan')

#Adding the hidden way
sonny.add_friend(jordan)

print(len(sonny.friends))

# Run the friend count method
sonny.count_friends()

sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email, sonny.phone, sonny.friends)
print(jordan.email, jordan.phone, jordan.friends)

#Run added method above

sonny.print_contact_info()
jordan.print_contact_info()

#print greet_count

print('Count', sonny.greet_count)
print('Count', jordan.greet_count)


# 2 Make your own class

class Vehicle:
    def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year

    def print_info(self):
        return '{} {} {}'.format(self.year, self.model, self.make)

car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make, car.model, car.year)

