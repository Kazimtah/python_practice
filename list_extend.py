def add(*args):
    sum = 0
    for i in range (len(args)):
        sum += args[i]
    return sum 

print(add(3,4,5,6,7))

def printAllvarialbe(**args):
    for x in args:
        print("Variable name is ", x, "And value is :", args[x])

print(printAllvarialbe(a= 3, b= "B", c="CC"))