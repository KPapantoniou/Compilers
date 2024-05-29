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



#def main
#int x,y,z,w,v,u,k
#int gcdre
x = int(input())
a = 10
w = multiply(x)
y =add(x)
z = subtract(x)

v = divide(x)
u = modOp(x)
k = power(x)
print(y)    
print(z)
print(w)
print(v)
print(u)
print(k)


