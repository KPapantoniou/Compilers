##checking different testcases of the cpy language##

def factorial(n):
    #{
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
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

print(factorial(i))
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