#Python Fundamentals
# Primitive data types 
    # Boolean Values
    # Number
        # integers and floating number
    # Strings

#Composite types
    # Tuples - a type of data that is immutable (can't be modified fter its creation) and can hold a group of values. Tuples can contain mixed data types.
        # dog =('bruce', 'cocker spaniel', 19, False)
        # print(dog[0])
        # dog[1]='dachshund' #Error: can't be modifed('tuple' object does not support item assignment)
    # Lists - type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

    # Dictionaries - a group of key - value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

#Common Functions
#if we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:

print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

