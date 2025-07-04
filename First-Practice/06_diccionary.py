import math

"""
###DICTIONARIES
Are sometimes found in other languages as "associative memories" or "associative arrays". Unlikes sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; string and numbers can always be keys. Tuples can be used as keys if contain only string, numbers or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can't use list as keys, since list can be modified in place using index assignments, slice assignments, or methods like append() an extended()

it is best to think of a dictionary as a set of key: value pairs, with the requirement that keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial keys:value pairs to the dictionary, this also the way dictionaries are written on output.

the main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pairs with del. If you store using a key that is already in use, the old value associated with that key is forgotten. it is an error to extract a value  using a non-existent key.

Performing list (d) on a dictionary returns a list of all key used in dictionary, in insertion order (if you want it sorted jus use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.
"""

tel =  {'Jack': 4098, 'aspe':4125}
tel['guido']=4127 #add key:valor pairs
print (tel) #--> {'Jack': 4098, 'aspe': 4125, 'guido': 4127}

print(tel ['Jack']) #--> 4098
tel['irv']=4127
print(tel) #--> {'Jack': 4098, 'aspe': 4125, 'guido': 4127, 'irv': 4127}

del tel['aspe']
print(tel) #--> {'Jack': 4098, 'guido': 4127, 'irv': 4127}

list(tel)
print(list(tel)) #--> ['Jack', 'guido', 'irv']
print(type(list(tel))) #--> <class 'list'>
print(sorted(tel)) #--> ['Jack', 'guido', 'irv']

print('guido' in tel) # --> True
print("victor" in tel) #--> False

# The dict() constructor builds dictionaries directly from sequences of key:value pairs.

print(dict([('sape', 4139), ('guido', 4127),('Jack', 4098)])) #--> {'sape': 4139, 'guido': 4127, 'Jack': 4098}

# In additio, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions.
print({x:x**2 for x in {2,4,6}}) #--> {2: 4, 4: 16, 6: 36}, es decir cuando indicamos que la key vale 2, su valor se eleva al cuadrado y da como resultado 4 (2*2), si key=4, valor=16(4*4)


# when the keys are simple strings, it is sometimes easier to specify pairs using keywords arguments
print(dict(sape=4139, guido=4127, jack= 4099)) #--> {'sape': 4139, 'guido': 4127, 'jack': 4099}


""" LOOPING TECHNIQUES """
#  whn looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

knights = {'Gallahand': 'the pure', 'Robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Gallahand the pure
# Robin the brave

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate()

for i, v in enumerate(['tic', 'tic', 'tic']):
    print(i, v)

# 0 tic
# 1 tic
# 2 tic

# To loop over two or mmore sequence at the same time, the entries can be with the zip() function

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('Whats is your {0}? It is {1}.'.format(q,a))

# Whats is your name? It is lancelot.
# Whats is your quest? It is the holy grail.
# Whats is your favorite color? It is blue.

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered

basket = ['apple', 'orange', 'apple','pear','orange','banana']
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

print('------')
# Using set() on an sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorteed order.


basket = ['apple', 'orange', 'apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear

# It is sometimes tempting to change a list while you are looping over it, however, it is often simpler and safer to create a new list instead


raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
#--> [56.2, 51.7, 55.3, 52.5, 47.8]







# A dictionary is a data structure that stores key:Values pairs
data_dictionary = {'clave' : 'valor'}

data_dictionary_one = {'name': 'Victor Hernandez', 'age':45, 'city': 'Cojedes'}


# Acceder a los valores mediante claves
# Access values via key.
print(data_dictionary_one['name']) # --> Victor Hernandez

#Agregar Elementos
# Add Elements
