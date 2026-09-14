# part A - Function fundementals
#1
def greet():
    print("hello")

def show_course():
    print("python")


def print_separator():
     print("_"*40)

print_separator()
greet()
show_course()
print_separator()

greet()
show_course()
print_separator()

#2
def greet_person(name):
    print("hello:",name)

def introduce(name, city):
    print(name,"is from ", city)

print_separator
greet_person("Ada")
introduce("Ada", "new york")
print_separator()

#3

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print(add(5,3))
print(subtract(5,3))
print(multiply(5,3))
print(divide(5,3))
print_separator()

#4 
def multiply(a,b): #parameter is a and b
    return a*b
print(multiply(5,3))# argument is 5 and 3 the value you send to the function
print_separator()

#5  
def calculate_area(width, height):
    return width*height

print(add(5,calculate_area(2,4))) 
#Using the retunrn from culate_area in a new calculation
print_separator()

#part B 
#1
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))
print_separator()

#2
def get_larger(a,b):
    if a > b:
        return a
    else:
        return b

largest_number = get_larger(5,7)
print(largest_number, "is larger")

largest_number = get_larger(7,5)
print(largest_number, "is larger")

largest_number = get_larger(7,9)
print(largest_number, "is larger")
print_separator()

#3

def classify_score(score):
    if score >= 70:
        return "pass"
    else:
        return "fail"
    
print(classify_score(78))
print(classify_score(50))
print_separator()

#4

def full_name(first_name, last_name):
    return first_name + " " +last_name

print(full_name("anna","svensson"))
print_separator()

#5
def calculate_discount(price, percent):
    return price* (1 - percent/100)

print(calculate_discount(1000,10))
print_separator()

#6 

# return in a function allow you to use the retuned vaule in more calulations
#print (result) inside a funtcion gives you the value but in printed form and can not be used for caluclation.

def add_with_print(a, b):
     print(a+b)

result = add_with_print(5,3)

print(result) #gives none
print ("with print gives none: ", add_with_print(5,3))


def add_with_return(a, b): #using return
     return a+b

result = add_with_return(5,3) # value is saved in result

print(result) #return 8
print("using return:", add_with_return(5,3)) 
print_separator()

#part C
#1

def greet(name, greeting="hello"):
    print (f"  {greeting}, {name}")

# diffrent orders on the argument    
greet("sven")
greet("sven", "good night")
greet( "good night", "sven")

# using keyword so oder on the argument dont mater
greet(name ="anna", greeting="good bye" )
greet( greeting="good bye", name ="anna" )
print_separator()

#2

def calculate_price(price, quantity =1, discount =0):
    return price * quantity - discount

print(calculate_price(100,2,50))

#3

def creat_profile(name, city="unknown", active=True):
    return { 
         "name":name,
         "city" : city,
         "active" : active
    }
print(creat_profile("anna"))
print_separator()

#4

def greet(name, greeting="hello"):
    print (f"  {greeting}, {name}")
#key-word allows me to have greetin first in the argument
greet( greeting="good bye", name ="anna" )
print_separator()

#5
#def greet(greeting="hello", name):
# This doesn't work because default parameters need to be last.

#part D

#1














