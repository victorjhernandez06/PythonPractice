"""LISTS"""
# the list are used store multiple items in a single variable.
# Lists area created using square brackets []


myList = ["apple","banana","cherry"]
print(myList) # --> ['apple', 'banana', 'cherry']

thisList = ["apple","banana","cherry"]
print(thisList) # --> ['apple', 'banana', 'cherry']

"""List Items"""
# List items are ordered, changeable,and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index[1]...etc.

"""Ordered"""
# when we say that lists are ordered, it means that the items have a defined order, and that order will not change. 
# if you add new items to a list, the new items will be placed at the end of the list.

"""Changeable"""
# the list is changeable, meaning that we can change, add, and remove items in the list after it hass been created.

"""Allow Suplica"""
# Since lists are indexed, lists can have items with the same value
thisList = ["apple","banana","cherry","apple","cherry"]
print(thisList) # --> ["apple","banana","cherry","apple","cherry"]

"""List Length"""
# to determine how many items a list has, use the len() function
print(len(thisList)) #--> 5

"""List items =  data types"""
# List items can be of any data type:
# String, int and boolean data type
list1 = ["apple","banana","cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, True]

# A list can contain different data types
list4 = ["abc",34,True,40.3,"male"]

"""Type()"""
print(type(list4)) # --> <class 'list'>

"""The list constructor"""
theList = list(("apple","banana","cherry")) # note the double round-brackets
print(theList) #-->['apple', 'banana', 'cherry']

""" Access List Items"""
# List items are indexed and you can access them by refering to te index number.
print(thisList[2]) # --> cherry.

"""Negative Indexing"""
# -1 refers to the las item -2, refers to the second las items, etc..
print(thisList[-1]) #--> cherry

"""Range of indexes"""
# you can specify a range of indexes by specifying where to start and where to end the range.
# when specifiying a range, the return value will be a new list with the specified items

thisList = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thisList[2:5]) #--> exclude the las item, start in 2, and finish in 4. 
# --> ['cherry', 'orange', 'kiwi']

# this example returns the items from the beginning to, but NOT including, "kiwi"
print(thisList[:4]) #--> ['apple', 'banana', 'cherry', 'orange']

# By leaving out the end value, the range will go on the end of the list
print(thisList[2:]) #--> ['cherry', 'orange', 'kiwi', 'melon', 'mango']

"""Range of negative indexes"""
# specify negative indexes if you want to start the search the search from the end of the list.
print(thisList[-4:-1]) #--> ['orange', 'kiwi', 'melon']

"""Check if item exists"""
# to determine if specified item is present in a list use the in keyword.
# check if "apple" is present in the list.
thisList = ["apple", "banana","cherry"]
if "apple" in thisList:
    print("yes, 'apple' is in the fruits list") 
    
"""PYTHON - CHANGE LIST ITEMS"""

"""Change item value"""
# To change the value of a specific item, refer to the index number
thisList = ["apple", "banana","cherry"]
thisList[1] = "mango"
print(thisList) # --> ['apple', 'mango', 'cherry']


"""Change a range of item values"""
# To change the value of items withi a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.
thisList=["apple", "banana", "cherry", "orange", "kiwi","mango"]
thisList[1:3] = ["blackcurrant", "watermelon"]
print(thisList) #--> ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thisList = ["apple","banana","cherry"]
thisList[1:2] = ["blackcurrant","watermelon"]
print(thisList) # --> ['apple', 'blackcurrant', 'watermelon', 'cherry']

thisList = ["apple","banana","cherry"]
thisList[1:3] = ["watermelon"]
print(thisList)



