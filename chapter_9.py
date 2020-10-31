import math
(m, n) = (3, 4)
def dist_from_origin(a, b):
    distance = math.sqrt(a ** 2 + b ** 2)
    return distance

print(dist_from_origin(m, n))

bob = ("Bob", "male", 20)
(name, gender, age) = bob
print(name, gender, age)