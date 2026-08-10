# UCS420: Cognitive Computing
# Assignment 2 - Python Data Structures
# Lists, Tuples, Sets, Dictionaries

import random
import math
from collections import Counter


# ============================
# Q1. LIST OPERATIONS
# ============================

roll_no = "1024170004"  

digits = [int(i) for i in roll_no]

L = [digit * 10 for digit in digits]

print("Original List L:", L)

# append() adds an element at the end of the list
L.append(250)
print("After append:", L)  # 250 added at the end

# insert() adds an element at a specific position
L.insert(2, 150)
print("After insert:", L)  # 150 added at index 2

# remove() removes the first occurrence of a value
L.remove(150)
print("After remove:", L)  # 150 removed

# pop() removes element using index
L.pop(0)
print("After pop:", L)  # First element removed


# Sorting ascending
L.sort()
print("Ascending order:", L)

# Sorting descending
L.sort(reverse=True)
print("Descending order:", L)


# Slicing
print("First three elements:", L[:3])
print("Last three elements:", L[-3:])


# List comprehension
average = sum(L) / len(L)

greater_than_average = [x for x in L if x > average]

print("Elements greater than average:", greater_than_average)



# ============================
# Q2. TUPLE OPERATIONS
# ============================

scores = tuple(L[:8])

print("\nTuple scores:", scores)


# Highest score and index
highest = max(scores)
highest_index = scores.index(highest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)


# Lowest score and frequency
lowest = min(scores)

print("Lowest score:", lowest)
print("Lowest score frequency:", scores.count(lowest))


# Reverse tuple and convert to list
# Tuple cannot be reversed in-place because tuples are immutable
reverse_scores = list(reversed(scores))

print("Reversed tuple as list:", reverse_scores)


# User input search
user_score = int(input("Enter a score to search: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score not present in tuple")


# Tuple modification attempt
try:
    scores[0] = 100
except Exception as e:
    print("Error while modifying tuple:", e)

# Tuples cannot be modified because they are immutable,
# unlike lists which allow element modification.


# Tuple unpacking using *
first, second, *remaining = scores

print("First:", first)
print("Second:", second)
print("Remaining:", remaining)



# ============================
# Q3. RANDOM NUMBER LIST
# ============================

random.seed(int(roll_no))

random_numbers = [random.randint(100, 900) for _ in range(100)]

print("\nRandom Numbers:")
print(random_numbers)


# Odd numbers
odd_numbers = [x for x in random_numbers if x % 2 != 0]

print("Odd count:", len(odd_numbers))
print("Odd numbers:", odd_numbers)


# Even numbers
even_numbers = [x for x in random_numbers if x % 2 == 0]

print("Even count:", len(even_numbers))
print("Even numbers:", even_numbers)



# Prime checking function
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


prime_numbers = [x for x in random_numbers if is_prime(x)]

print("Prime count:", len(prime_numbers))
print("Prime numbers:", prime_numbers)



# Most frequent number

frequency = Counter(random_numbers)

most_common_number, count = frequency.most_common(1)[0]

print("Most frequent number:", most_common_number)
print("Frequency:", count)



# ============================
# Q4. SET OPERATIONS
# ============================


digits = [int(i) for i in roll_no[:8]]

A = {digit * 7 for digit in digits}

B = {digit * 9 for digit in digits}


print("\nSet A:", A)
print("Set B:", B)


# Union
print("Union:", A.union(B))


# Intersection
print("Intersection:", A.intersection(B))


# Difference
print("A - B:", A.difference(B))
print("B - A:", B.difference(A))

# difference() gives elements present in one set but not another,
# whereas symmetric_difference() gives elements present in either set but not both.


# Symmetric difference

print("Symmetric Difference:", A.symmetric_difference(B))


# Subset and Superset

print("Is A subset of B:", A.issubset(B))
print("Is B superset of A:", B.issuperset(A))


# discard()
X = int(input("Enter value to remove from set A: "))

A.discard(X)

print("Set A after discard:", A)

# discard() is safer than remove() because it does not raise an error
# if the element does not exist.



# ============================
# Q5. DICTIONARY OPERATIONS
# ============================


my_dict = {
    "name": "Dhruv",
    "roll_no": roll_no,
    "branch": "CSE",
    "age": 19,
    "city": "Mumbai"
}


print("\nOriginal Dictionary:")
print(my_dict)



# Rename city to location using pop()

my_dict["location"] = my_dict.pop("city")

print("After renaming city:", my_dict)



# Add CGPA

my_dict["cgpa"] = 9.17

print("After adding CGPA:", my_dict)



# Increase age

my_dict["age"] += 1

print("After updating age:", my_dict)



# Delete branch using pop()

dict_pop = my_dict.copy()

removed_branch = dict_pop.pop("branch")

print("Dictionary after pop:", dict_pop)



# Delete branch using del

dict_del = my_dict.copy()

del dict_del["branch"]

print("Dictionary after del:", dict_del)


# pop() returns the removed value, while del only deletes the key.



# Iterating dictionary

print("\nDictionary items:")

for key, value in my_dict.items():
    print(key, "→", value)



# Checking email existence

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email key does not exist")



# Friend dictionary

friend_dict = {
    "name": "Rahul",
    "roll_no": "12345678",
    "branch": "ECE",
    "age": 20,
    "city": "Delhi"
}


merged_dict = {**my_dict, **friend_dict}

print("\nMerged Dictionary:")
print(merged_dict)


# When duplicate keys exist, values from the second dictionary overwrite the first.



# Dictionary comprehension

string_values = {
    key: value 
    for key, value in my_dict.items()
    if isinstance(value, str)
}


print("\nDictionary containing only string values:")
print(string_values)