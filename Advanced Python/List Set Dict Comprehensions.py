#list comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7]
even = [i for i in numbers if i%2 == 0]
print(even)

sqr = [i*i for i in numbers]
print(sqr)

#set comprehensions
s = set([1, 2, 34, 56, 77])
print(s)
even1 = {i for i in s if i%2 == 0}
print(even1)

#dictionary comprehensions
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]
z = zip(cities, countries)

for a in z:
    print(a)

d = {city: country for city, country in zip(cities, countries)}
print(d)