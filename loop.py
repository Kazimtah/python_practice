n = 10 
i = 1

while True:
    if i%9 == 0:
        print("Inside if")
        break
    else:
        print("inside else")
        i = i+1 # i+=1
print("done")