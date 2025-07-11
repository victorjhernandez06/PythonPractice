"""CONDITIONALS"""
# Python Conditions and If statements
### Conditions IF

my_conditions =  True

if my_conditions == True:
    print("la condicion se ejecuta la condicion del if")

print("la condicion no se ejecuta")

# Es la tercera vez que lo hagosource venv/bin/activate
my_conditions = 5*2*3

if my_conditions == 20:
    print(f"The value in my conditions is {my_conditions}")
elif my_conditions == 10:
    print(f"The value in my conditions is {my_conditions}")
else:
    print(f"The value in my conditions is {my_conditions}")
    
# Short hand if..else
a = 2
b = 330

print("A") if a>b else print("B") #--> B

a = 200
b = 33
if b > a:
    print("B is greater than A")
else:
    print("A is greater than B")
    
    
# Short Hand If
if a>b: print ("A is greater than B")

# This technique is known as Ternary Operators, or Conditional Expressions.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

"""AND"""

# the AND keyword is a logical operator, and is used to combine conditionals statements

