# Lambda Functions

add = lambda a,b: a+b

print(add(5,3))

# Lambda with map

numbers = [1,2,3,4]

square = list(map(lambda x: x*x, numbers))

print(square)
