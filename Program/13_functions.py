
###FUNCTIONS###
# A function is a block of code wich only runs when it is called.
# You can pass data, know as parameters, into a function.
# A function can return data as a result.

"""Create a function"""
# in python a function is defined using a def keyword.
# Example
from datetime import datetime


def my_function():
    print('A new function example')
    
"""Call a function"""
# to call a function, use the function name followed by parenthesis
my_function()

"""Arguments"""
# information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a fucntion with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
    print(fname + " Hernandez")
  
my_function('Victor') #--> Victor Hernandez
# my_function('Karina')
my_function('Adrian') #--> Adrian Hernandez
my_function('Mathias') #--> Mathias Hernandez
my_function('Sofia') #--> Sofia Hernandez  


""" Parameters or Arguments """

# The terms parameter and argument can be used for the same thing: information that are passed into a function.

## From a function perspective: 
# A parameter is the variable listed inside the parentheses in the function definition.
# An Arguments is the value that is sent to the function  when it is called.

"""Number of arguments"""
# by default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have call the function with 2 arguments, not more, and not less.

#example
# this function expects 2 arguments, and gets 2 arguments
def m_function(fname, lname):
    print(fname +" "+ lname)
    
m_function('Karina','Jimenez') #--> Karina Jimenez

# If you try call the fucntion with 1 or 3 arguments, you will get an error:

"""Arbitrary Arguments, *args"""
#if you do not know how many arguments that will be passed into your function, add a asterisk  * before the parameter name in the function definition  
# this way the function will receive a tuple arguments, and can access the items accordingly

#Example
# if the number of arguments is unknown, add a * before the parameter name
def my_function(*kids):
    print(f"The youngest child is {kids[2]}")

my_function('Adrian', 'Mathias','Sofia')


##microsoft
#print the current time

def print_time():
    print('Task completed')
    print(datetime.now())
    print()

firs_name = 'Sofia'
print_time() 

for x in range(0,10):
    print(x)
print_time()

    
"""Pass the task name as a parameter"""
#print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()
first_name = 'Sofia'
print_time('first name assigned')

for x in range (0,10):
    print(x)
print_time('Loop Completed')
    

## Fix the next code.
first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]

last_name  = input('Enter your last name: ')
last_name_initial =  last_name[0:1]

print('Your initials are: ' + first_name_initial + last_name_initial)
#imprime las iniciales de los nombres tipeados.

## Functions that return values allow clever code, but you migth trade readability for less code.

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print('Your initial are: '+ get_initial(first_name) + get_initial(last_name))


##Functions With parameters

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your name: ')
first_name_initial =  get_initial(first_name)

print(f'Your initial name is: {first_name_initial}')

#You can also assign the values to  parameters by name whe you call the function

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
first_name =  input('enter your first name: ')
first_name_initial = get_initial(force_uppercase=True, name=first_name)
print(f'Your initial is: {first_name_initial}')

#Using the named notation when calling functions makes your code more readable
# def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
#     print(f'oh no error {error_message}')
#     #imagine code here that logs our error to database a file.
    
# first_number = 10
# second_number = 5
# if first_number > second_number:
#     error_logger(45, 1, True, 'second number than first','may_math_method')


def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error:' + error_message)
    #imagine code here that logs our error to database or file
    
first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code = 45, error_severity=1, log_to_db = True, error_message= 'second number greater than first', source_module='May math method')

















    
# # Exercises (simple)
# def my_function():
#     print('this is a function')
    
# my_function() #Esta es la llamada a la funcion, con esto aparece en pantalla: 'esto es una funcion'


# def sum_two_values (first_num,  second_num):
#     print(first_num + second_num) #hace una suma entre dos parametros.
    
# sum_two_values(23, 21) #ejecuta la funcion e imprime la suma dentro de la funcion.

# def sum_a_b (a, b):
#     return(a+b)

# print(sum_a_b(2,2)) #  --> devuelve e imprime la suma de 2+2 = 4
# print(sum_a_b(1.4,22.8)) # --> 24.2 


# # Al tipado no funciona aqui.
# # Aqui he tipado el numero, pero al indicar que son string los datos, no toma en cuenta este tipado. NO sirve de nada por el tiempo de ejecucion, pues tomara los datos que le metamos datos. 
# def function_2(numb1:int, numb2:int): #aqui probamos tipando los parametros
#     return(numb1+numb2)
# print(function_2('22','20'))

# ###
# def sum_two_val (a, b):
#     return(a + b)

# my_result = sum_two_val(2,3)
# print(my_result) #-->5

# ### Usando el retorn 
# def sum1(a,b):
#     my_sum = a + b
#     return my_sum

# operation = sum1(2,32)
# print(operation) #--> 34

# def print_name(name, surname):
#     print(f"{name} {surname}")

# print_name('Victor','Hernandez') #--> Victor Hernandez
# print_name(surname="Hernandez",name='Victor') #aqui reordene el nombre, indicando el valor de los parametros en la llamada. ##--> Victor Hernandez


# ### Aqui utilizamos parametros definidos dentro de la funcion, sin usar el constructor.
# def print_name_with_default(name,surname, alias = 'Sin Alias'):
#     print(f"{name} {surname} {alias}")
    
# print_name_with_default('Victor','Hernandez','Victordev06') #--> Victor Hernandez Victordev06
# print_name_with_default('Victor','Hernandez') #--> Victor Hernandez Sin Alias

# ### el asterico indica que puedo incluir muchos parametros del mismo tipo
# def print_texts(*text):
#     print(text)
    
# print_texts('Hola')# --> ('Hola',)


# ### El asteristo * indica que es una funcion con parametros arbitrarios
# def print_texts(*texts):
#     for text in texts:
#         print(text.upper())

# print_texts('Victor','Karina','Adrian','Mathias','Sofia')
# # VICTOR
# # KARINA
# # ADRIAN
# # MATHIAS
# # SOFIA

# """MICROSOFT PYTHON """

# def print_time():
#     print('task completed')
#     print(datetime.datetime.now())
#     print()

# first_name  = 'Victor'
# print_time()

# for x in range(0,10):
#     print(x)

 


