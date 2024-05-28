#int a, b

def func(a):
#{ 
    #int c
    global b 
    c = a + 1
    b = c + a
    print(b)
    return c
#}

#def main
a = int(input())
b = func(a)
print(b)

