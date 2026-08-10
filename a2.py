# UCS420 Assignment 2

import random
import math
from collections import Counter


# Q1

roll = "1024170004"

d = [int(x) for x in roll]

L = [x * 10 for x in d]

print("L =", L)

L.append(200)
print("After append:", L)

L.insert(2, 50)
print("After insert:", L)

L.remove(50)
print("After remove:", L)

L.pop(0)
print("After pop:", L)

L.sort()
print("Ascending:", L)

L.sort(reverse=True)
print("Descending:", L)

print("First 3:", L[:3])
print("Last 3:", L[-3:])

avg = sum(L) / len(L)

newL = [x for x in L if x > avg]

print("Above average:", newL)



# Q2

scores = tuple(L[:8])

print("\nScores:", scores)

high = max(scores)
idx = scores.index(high)

print("Highest:", high)
print("Index:", idx)

low = min(scores)

print("Lowest:", low)
print("Lowest count:", scores.count(low))


rev = list(reversed(scores))
print("Reverse:", rev)


n = int(input("Enter score: "))

if n in scores:
    print("Index:", scores.index(n))
else:
    print("Not present")


try:
    scores[0] = 100
except Exception as e:
    print(e)

# Tuple is immutable so its values cannot be changed like lists.


a, b, *c = scores

print(a, b, c)



# Q3

random.seed(int(roll))

nums = []

for i in range(100):
    nums.append(random.randint(100,900))

print("\nNumbers:", nums)


odd = [x for x in nums if x % 2 != 0]
even = [x for x in nums if x % 2 == 0]


print("Odd count:", len(odd))
print("Odd:", odd)

print("Even count:", len(even))
print("Even:", even)



def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True


primes = [x for x in nums if prime(x)]

print("Prime count:", len(primes))
print("Primes:", primes)


cnt = Counter(nums)

num, freq = cnt.most_common(1)[0]

print("Most repeated:", num)
print("Frequency:", freq)



# Q4

d = [int(x) for x in roll[:8]]

A = {x*7 for x in d}
B = {x*9 for x in d}

print("\nA =", A)
print("B =", B)


print("Union:", A.union(B))

print("Intersection:", A.intersection(B))


print("A-B:", A.difference(B))
print("B-A:", B.difference(A))

# difference gives one side elements whereas symmetric difference gives all uncommon elements.

print("Symmetric difference:", A.symmetric_difference(B))


print("A subset B:", A.issubset(B))
print("B superset A:", B.issuperset(A))


x = int(input("Enter value to remove from A: "))

A.discard(x)

print("A after discard:", A)

# discard does not give error if value is not present.



# Q5


my_dict = {
    "name": "Dhruv",
    "roll_no": roll,
    "branch": "CSE",
    "age": 19,
    "city": "Mumbai"
}


print("\nDictionary:", my_dict)


my_dict["location"] = my_dict.pop("city")

my_dict["cgpa"] = 9.17

my_dict["age"] += 1


print(my_dict)



d1 = my_dict.copy()

d1.pop("branch")

print("Using pop:", d1)



d2 = my_dict.copy()

del d2["branch"]

print("Using del:", d2)


# pop returns deleted value, del only removes it.


for k,v in my_dict.items():
    print(k, "→", v)



if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email not found")



friend_dict = {
    "name":"Rahul",
    "roll_no":"12345678",
    "branch":"ECE",
    "age":20,
    "city":"Delhi"
}


merge = {**my_dict, **friend_dict}

print("Merged:", merge)

# If same key exists, second dictionary value is used.



str_dict = {k:v for k,v in my_dict.items() if isinstance(v,str)}

print("String values:", str_dict)