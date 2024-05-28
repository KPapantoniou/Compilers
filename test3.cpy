##Authors: 1. Konstantinos Papantoniou-Xatzigiosis, AM: 4769
#         2. Natalia Michou                      , AM: 4922
# Date: 2024-05-10##

##test variable scope of the cpy language##


    
def func1():
#{
    #int cover
    def func2():
    #{
        #int cover
        def func3():
        #{
            #int cover
            def func4():
            #{
                    #int localvar, cover
                    global var1, var2
                    cover = 4
                    localvar = 10
                    var2 = localvar
                    var1 = var2 + localvar
                    return cover

            #}
            cover = func4()
            return cover + 1
        #}

        cover = func3()
        return cover + 1
    #}
    cover = func2()
    return cover + 1
#}

#def main
print(func1()) ## should be 3 ##
print(var2) ## should be 10 ##
print(var1) ## should be 20 ##

