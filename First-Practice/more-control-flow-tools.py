""" MORE CONTROL FLOW TOOLS """

# As well as the while statement just introduced, Python uses a few more that we will encounter in this part.

''' IF STATEMENTS'''

# Perhaps the most well-known statement.
# x = int(input("Please enter an integer: "))
x = 42
if x< 0:
    x = 0
    print('Negative change to zero')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')

#--> More

''' FOR STATEMENTS'''
# The for statement in python differs a bit form may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of number (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C) Python's for statement iterates over the items of any sequence(a list or a string), in the order that they appear in the sequence.

#Measure some strings
words = ['cat', 'window', 'defenestrate']
print(type(words)) #--> <class 'list'>
for w in words:
    print(w, len(w))
# cat 3
# window 6
# defenestrate 12

# Code that modifies a collection while iterating over that same collection can be tricky to get right. instead, its is usually more  straight-forward to loop over a copy of the collection or to create collection.

# Create a sample collection
users = {'Hans':'Active', 'Eleonore':'inactive','vjh':'active'}

#strategy: iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

#Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


''' THE RANGE() FUNCTION'''
# if you do need to iterate over a sequence of numbers, the build-in function range() come in handy. it generates arithmetic progressions:

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

a =  ['Mary','had','a', 'litle','lamb']
for i in range(len(a)):
    print(i, a[i])
# 0 Mary
# 1 had
# 2 a
# 3 litle
# 4 lamb

print(range(10))
#--> range(0, 10)


print(sum(range(4)))
#--> 0+1+2+3 --> 6

print(list(range(5,10))) # --> [5, 6, 7, 8, 9]
print(list(range(0,10,3))) #--> [0, 3, 6, 9]
print(list(range(-10,-100,-30))) #--> [-10, -40, -70]

# To iterate over the indices of a sequence, you can combine range() and len() as follows:

a = ['mary', 'had','a','litle', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 0 mary
# 1 had
# 2 a
# 3 litle
# 4 lamb

