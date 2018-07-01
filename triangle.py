a = int(raw_input("Enter a First side:"))
b = int(raw_input("Enter a second Side:"))
c = int(raw_input("Enter a third side:"))
def checktriangle(x,y,z):
    if (a+b<=c):
        return false
    if (b+c<=a):
        return false
    if (a+c<=b):
        return false
    return true
    res = checktriangle(a,b,c)
    if res == true:
        print("Valid triangle")
    else:
        print("invalid triangle")
