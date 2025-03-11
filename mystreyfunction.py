def mystery_function(lst):
    result = []
    for i in range(len(lst)):
        print(i)
        if i%2 == 0:
            result.append(lst[i] * 2)
        else:
            result.append(lst[i] - 2 )
    return result
print(mystery_function([1,2,3,4,5,6]))
#print(lst[i])
print( 6%2==0)
print(1-2)
print(2%2 == 0)
print(len([1,2,3,4,5,6]))
print(range(6))
print(0-2)