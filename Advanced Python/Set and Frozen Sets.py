basket = {"orange", "apple", "mango", "apple", "orange"}
print(basket) #duplicate elements removed

a = set()
a.add(1)
a.add(2)
print(a)


numbers = [1, 2, 3, 4, 2, 3,  4]
print(numbers) #list prints duplicate elements
unique_numbers = set(numbers)
print(unique_numbers) #set removes duplicate elements

fs = frozenset(numbers)
print(fs)
#fs.add(5) -> will give error


x = {"a", "b", "c"}
y = {"a", "g", "h"}
print(x | y) #union
print(x & y) #intersection
print(x - y) #difference
print(x < y) #check if x is subset of y