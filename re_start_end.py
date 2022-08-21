string = input("Please input your string:")
check = input("Please input your substring:")
try:
    index = string.index(check)
    print((index, index+len(check)-1))
    for i in range(index, len(string)-len(check)):
        try:
            location = string[index+1:].index(check)
            index += location+1
            print((index, index+len(check)-1))
        except:
            pass
except:
    print((-1,-1))