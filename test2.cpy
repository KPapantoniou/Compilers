##checking different testcases of the cpy language##

def factorial(n):
    #{
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    #}
    
def gcd(a, b):
    #{
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    #}
    
def power(x, y):
    #{
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
    #}
    
def isEven(n):
    #{
    if n == 0:
        return 1
    else:
        return isOdd(n-1)
    #}

def isOdd(n):
    #{
    if n == 0:
        return 0
    else:
        return isEven(n-1)
    #}
    


#def main
#int i
#int j

i = int(input())
j = int(input())
print(factorial(i))
print(gcd(200, 321))
print(power(i, j))
while i > 0:
   
    i = i - 1
    
while j > 0:#{
    
    j = j - 1
#}
if isEven(i):
    print(isEven(i))

elif isOdd(i):
    print(isOdd(i))
else:
    print(0)