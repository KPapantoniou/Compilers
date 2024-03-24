##Authors: 1. Konstantinos Papantoniou-Xatzigiosis, AM: 4769
#         2. Natalia Michou                      , AM: 4922
# Date: 2024-03-25##

##Test to check arithmetic operations##

#int a

def add(b):
#{
    #int result
    global a
    result = a+b
    return result
#}

def subtract(b):
#{
    #int result
    global a
    result = a-b
    return result
#}

def multiply(b):
#{
    #int result
    global a
    result = a*b
    return result
#}

def divide(b):
#{
    #int result
    global a
    result = a//b
    return result
#}

def modOp(b):
#{
    #int result
    global a
    result = a%b
    return result
#}

def power(b):
#{
    #int result
    global a
    result = 1
    while b > 0:
        result = result*a
        b = b-1
    return result
#}

def gcd(b):
#{
    #int t
    global a
    if b == 0:
        return a
    while b != 0:
        t = b
        b = a%b
        a = t
    return a
#}

#def main
#int x
#int gcdre
x = int(input())
a = 10
gcdre = gcd(x)

print(add(x))
print(subtract(x))
print(multiply(x))
print(divide(x))
print(modOp(x))
print(power(x))
print(gcdre)

