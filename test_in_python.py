a = 10

def add(b):

    global a
    result = a+b
    return result


def subtract(b):

    global a
    result = a-b
    return result

def multiply(b):

    global a
    result = a*b
    return result

def divide(b):
    global a
    result = a//b
    return result

def modOp(b):
    global a
    result = a%b
    return result

def power(b):


    global a
    result = 1
    while b > 0:
        result = result*a
        b = b-1
    return result


def gcd(b):

    global a
    if b == 0:
        return a
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

def main():
    x = 4
    
    gcdre = gcd(x)

    print(add(x),"addition")
    print(subtract(x),"subtraction")
    print(multiply(x),"multiplication")
    print(divide(x),"division")
    print(modOp(x), "modulus")
    print(power(x),"power")
    print(gcdre,"gcd")

main()