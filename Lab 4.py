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





