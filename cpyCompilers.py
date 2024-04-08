#Authors: 1. Konstantinos Papantoniou-Xatzigiosis, AM: 4769
#         2. Natalia Michou                      , AM: 4922
# Date: 2024-03-25
# Description: A lexical and syntax analyzer for the cpy language.
# The lexical analyzer reads a file and generates tokens.
# The syntax analyzer checks the syntax of the cpy language.


# from sys import argv

# fileName = argv[1] 
fileName = './test.cpy'
temporaryVariables = []
quadrupleList = []
lineCount =0
tempVariableCount =0 
isFunction = False
class Token:
    def __init__(self, token, tokenType):
        self.token = token 
        self.tokenType = tokenType

##-------------------------------------------- Lexical Analyzer --------------------------------------------##
class LexicalAnalyzer:

    def __init__(self, filename):
        self.filename = filename
        self.tokens = []
        
        self.STATES = {
         'stateBegin': 0,
        'stateLetter': 1,
        'stateDigit': 2,
        'stateDivision':3, 
        'stateLess': 4,
        'stateMore': 5,
        'stateEqual': 6,
        'stateDiffernt': 7,
        'stateSharp': 8,
        'stateCommentBegin': 9,
        'stateCommentEnd': 10,
        'stateERROR': -1,
        'stateOK': -2,
        'stateEOF': -3
    
       }


    def lexical_analyzer(self):
        file = open(self.filename, 'r')
        compilationFile = open('lexicalAnalyzer.txt', 'w')
        compilationFile.write("lexigram analysis of the file: %s \n" %file.name)
        fileContent = file.read()
        alpha = False
        digit = False
        col = 0
        counter = 0
        
        keywords=[
            'main',
            'def',
            '#def',
            '#int',
            'global',
            'if',
            'elif',
            'else',
            'while',
            'print',
            'return',
            'input',
            'int',
            'and',
            'or',
            'not'
            ]
        
        token = '' 
        finalWord=[]
        line = 0 
        index = 0
        state = self.STATES['stateBegin']
        numLetters=0
        intToken = 0
        while(index<len(fileContent)and state not in[self.STATES['stateOK'],self.STATES['stateERROR']]):
            currentCharacter = fileContent[index]
        
            if index < len(fileContent)-1:
                nextchar = fileContent[index+1]
            elif not fileContent:
                state = self.STATES['stateEOF']
            else:
                state = self.STATES['stateEOF']
            if(currentCharacter=='\n'):
                line += 1
                col = 0
            else:
                col += 1
            if(state==self.STATES['stateBegin']):
                if (currentCharacter==' ' or currentCharacter== '/t' or currentCharacter=='\n'):
                    state = self.STATES['stateBegin']
                    token = ''
                
                    
                    index +=1
                    continue

                elif(currentCharacter.isalpha()):
                    state = self.STATES['stateLetter']
                elif(currentCharacter.isdigit()):
                    state = self.STATES['stateDigit']

                elif(currentCharacter=='/'):
                    state = self.STATES['stateDivision']
                elif(currentCharacter == '<'):
                    state = self.STATES['stateLess']

                elif(currentCharacter == '>'):
                    state = self.STATES['stateMore']

                elif(currentCharacter=='='):
                    state = self.STATES['stateEqual']
                elif(currentCharacter=='!'):
                    state = self.STATES['stateDiffernt']  
                elif(currentCharacter=='#'):
                    state = self.STATES['stateSharp']
                else:
                    state = self.STATES['stateOK']
                    token = currentCharacter
                    if currentCharacter == '+':
                        finalWord += [token] + ['ArithmeticOperation']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '-':
                        finalWord += [token] + ['ArithmeticOperation']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '*':
                        finalWord += [token] + ['ArithmeticOperation']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '%':
                        finalWord += [token] + ['ArithmeticOperation']
                        state = self.STATES['stateOK']
                    elif currentCharacter == ',':
                        finalWord += [token] + ['delimiter']
                        state = self.STATES['stateOK']
                    elif currentCharacter == ':':
                        finalWord += [token] + ['delimiter']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '(':
                        finalWord += [token] + ['Grouping']
                        state = self.STATES['stateOK']
                    elif currentCharacter == ')':
                        finalWord += [token] + ['Grouping']
                        state = self.STATES['stateOK']


            if(state == self.STATES['stateLetter']):
                alpha = currentCharacter.isalpha()
                digit = currentCharacter.isdigit()
                if (alpha or digit):
                    numLetters += 1
                    if(numLetters<30):
                        token += currentCharacter
                        state = self.STATES['stateLetter']
                    else:
                     
                         print("Error: Word must contain up to 30 characters")
                         print('Line: %d:%d'%(line,col))
                         state = self.STATES['stateERROR']
                else:
                    state = self.STATES['stateOK']
                    index -= 1
                    if token in keywords:
                        finalWord += [token] + ['keyword']
                    else:
                        finalWord += [token] + ['identifier']
       
            if(state == self.STATES['stateDigit']):            
                digit = currentCharacter.isdigit()
                if (digit):
                    token += currentCharacter
                    intToken = int(token)
                    if(intToken<=-32767 and intToken>=32767):                    
                         print("Error: Number must be between -32767 and 32767")
                         print('Line: %d:%d'%(line,col))
                         state = self.STATES['stateERROR']
                    
                    state = self.STATES['stateDigit']
                else:
                    state = self.STATES['stateOK']
                    index -= 1
                    finalWord += [token] + ['number']

        
            if state == self.STATES['stateDivision']:
                if currentCharacter == '/':
                    if(nextchar == '/'):
                        token = '//'
                        index += 1
                        state = self.STATES['stateOK']
                        finalWord += [token] + ['ArithmeticOperation']
                else:
                    
                    print("Error: Invalid character")
                    print('Line: %d:%d'%(line,col)) 
                    state = self.STATES['stateERROR'] 
                    
            if state == self.STATES['stateLess']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['CompareOperation']
                    index += 1
                else:
                    token = currentCharacter
                    state = self.STATES['stateOK']
                    finalWord += [currentCharacter] + ['CompareOperation']

            if state == self.STATES['stateMore']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['CompareOperation']
                    index += 1
                else:
                    token   = currentCharacter
                    state = self.STATES['stateOK']
                    finalWord += [currentCharacter] + ['CompareOperation']

            if state == self.STATES['stateEqual']:
                if nextchar == '=':
                    token = currentCharacter +nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['CompareOperation']
                    index += 1
                else:
                    token = currentCharacter
                    state = self.STATES['stateOK']
                    finalWord += [currentCharacter] + ['variable']    
                      
        
            if state == self.STATES['stateDiffernt']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['CompareOperation']
                    index += 1
                else:
                
                    print("Error: Invalid character")
                    print('Line: %d:%d'%(line,col))
                    state = self.STATES['stateERROR']
        
            if state == self.STATES['stateSharp']:  
                if nextchar == '{':
                    token += currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['Grouping']
                    index += 1
                elif nextchar == '}':
                    token += currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    index += 1
                    finalWord += [token] + ['Grouping']
                elif nextchar == '#':
                    token += currentCharacter + nextchar
                    index += 1
                    while index < len(fileContent) - 1 and not (fileContent[index] == '#' and fileContent[index + 1] == '#'):
                        index += 1
                    
                    if index < len(fileContent) - 1:
                        index += 1
                    state = self.STATES['stateBegin']
                
                
                
                elif nextchar == 'i' or nextchar == 'd':
                    token += currentCharacter
                    state = self.STATES['stateLetter']            
                else:
                
                    print("Error: Invalid character")
                    print('Line: %d:%d'%(line,col))
                    state = self.STATES['stateERROR']

       
        
            if state == self.STATES['stateEOF']:
                state = self.STATES['stateOK']
                token += 'EOF'
                finalWord += ['EOF'] + ['EOF']
                
        
            if state == self.STATES['stateOK']:
                numLetters = 0
                if token:
                    self.tokens.append(Token(token,finalWord[1]))
                token = ''
                counter += 1
                compilationFile.write("---------------------------------------------------------\n")
                compilationFile.write("{ "+finalWord[0] + " -> " + finalWord[1] +" }"+ "\nToken number: "+ str(counter) +"\n")
                compilationFile.write("---------------------------------------------------------\n")
                finalWord = []
               
                state = self.STATES['stateBegin']
       
            if state == self.STATES['stateERROR']:
            
                compilationFile.write("---------------------------------------------------------\n")
                compilationFile.write("Error: Invalid character\n") 
                compilationFile.write('Line: %d:%d\n'%(line,col))
                compilationFile.write("---------------------------------------------------------\n")
                finalWord = []
                state = self.STATES['stateBegin']
        
        
            index +=1
   
        
        file.close()
        compilationFile.close() 
        return self.tokens

##------------------------------------ Syntax Analyzer ------------------------------------##
class SyntaxAnalyzer:
    syntaxFile = open('SyntaxAnalyzer.txt', 'w')
    syntaxFile.write("Syntax analysis of the file: %s \n" %fileName)
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndex = 0
        if self.tokens:
            self.currentToken = self.tokens[0]
        else:
            print("Warning: No tokens generated by the lexical analyzer")
            self.currentToken = None


    def nextToken(self):
       
        if self.tokenIndex < len(self.tokens):
            self.tokenIndex += 1
            self.currentToken = self.tokens[self.tokenIndex]
        else:
            self.currentToken = None
        

    def tokenCheck(self, expectedToken):
        self.syntaxFile.write(f"Token Checking: {expectedToken}\t Token index: {self.tokenIndex}\n")
        if self.currentToken.token == expectedToken:
            self.nextToken()
            return True
        else:
            raise Exception(f"Syntax error: expected '{expectedToken}' received '{self.currentToken.token}' token number '{self.tokenIndex}'")
            

    def startRule(self):
        
        if self.currentToken.token == '#int':
            self.tokenCheck('#int')
            self.declarations()
            self.startRule()
        elif self.currentToken.token == 'def':
            self.tokenCheck('def')
            if self.def_function():
                self.startRule()
        elif self.currentToken.token == '#def':
            self.tokenCheck('#def')
            self.def_main()     
        else:
            raise Exception(f"Syntax error: expected #def, #int, or def received '{self.currentToken.token}' token number '{self.tokenIndex}'")


        

    def def_main(self):
        self.tokenCheck('main')
        while self.currentToken.token == '#int':
            self.tokenCheck('#int')
            self.declarations()
        while self.currentToken.token == 'def':
            self.def_function()
        self.code_block()
        if self.currentToken.token == 'EOF':
                self.syntaxCorect() 

    def def_function(self):
        programName = self.currentToken.token
        Quadruple.genquad("begin_block",programName,'_','_')
        # Quadruple.functionFormat("begin_block",programName,'_','_')
        if self.currentToken.tokenType == 'identifier':
            self.nextToken()
            if self.tokenCheck('('):
                self.formal_pars()
                if self.tokenCheck(')'):
                    if self.tokenCheck(':'):
                        if self.tokenCheck('#{'):
                            while self.currentToken.token == '#int':
                                self.tokenCheck('#int')
                                self.declarations()
                            if self.currentToken.token == 'global':
                                self.tokenCheck('global')
                                if self.currentToken.tokenType == 'identifier':
                                        self.nextToken()
                            while self.currentToken.token == 'def':
                                self.nextToken()
                                self.def_function()
                        
                            self.code_block()
                            if self.tokenCheck('#}'):
                                # Quadruple.genquad("halt",'_','_','_')
                                # Quadruple.functionFormat("halt",'_','_','_')
                                Quadruple.genquad("end_block",programName,'_','_')
                                # Quadruple.functionFormat("end_block",programName,'_','_')
                                return True

    def declarations(self):
        if self.currentToken.tokenType == 'identifier':
            self.nextToken()
            while self.currentToken.token == ',':
                self.tokenCheck(',')
                if self.currentToken.tokenType == 'identifier':
                    self.nextToken()

    def formal_pars(self):
        if self.currentToken.tokenType == 'identifier':
            self.nextToken()
            while self.currentToken.token == ',':
                self.tokenCheck(',')
                if self.currentToken.tokenType == 'identifier':
                    self.nextToken()

    def statements(self):
        if self.currentToken.tokenType == 'identifier':
            self.assignment_statements()
        elif self.currentToken.token == '=': ## this here
            self.assignment_statements()
        elif self.currentToken.token == 'global':
            self.tokenCheck('global')
            if self.currentToken.tokenType == 'identifier':
                    self.nextToken()
        elif self.currentToken.token in ['if', 'while', 'print', 'return', 'int']:
            self.other_statements()

    def assignment_statements(self):
        global isFunction
        if self.currentToken.tokenType == 'identifier':
            result = self.currentToken.token
            self.nextToken()
       
        self.tokenCheck('=')
        
        self.other_statements()
        expression = self.expression()
        if isFunction:
            Quadruple.genquad('=',temporaryVariables[-1],'_',result)
            isFunction = False
        else:
            if temporaryVariables:
                Quadruple.genquad('=',temporaryVariables[-1],'_',result)
            else:
                Quadruple.genquad('=',expression,'_',result)

    def other_statements(self):
        if self.currentToken.token == 'if':
            self.if_statements()
        elif self.currentToken.token == 'while':
            self.while_statements()
        elif self.currentToken.token == 'print':
            self.print_statements()
        elif self.currentToken.token == 'return':
            self.return_statements()
        elif self.currentToken.token == 'int':
            self.input_statements()

    def if_statements(self):
        global lineCount,quadrupleList
        self.tokenCheck('if')        

        cond_result = self.condition()     
        print(f"here: -> {cond_result[0]} quad id: {quadrupleList[-1].id}")
        self.tokenCheck(':')
        
        Quadruple.backpatch(cond_result[0],Quadruple.nextquad())
        # print(quadrupleList[-1])
        self.code_block()
        if_statment = Quadruple.makelist(Quadruple.nextquad())
        Quadruple.genquad('jump','_','_','_')
        Quadruple.backpatch(cond_result[1],Quadruple.nextquad())
        

        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
            
            self.code_block()
            Quadruple.backpatch(cond_result[0],Quadruple.nextquad())

            self.code_block()
            if_statment = Quadruple.makelist(Quadruple.nextquad())
            Quadruple.genquad('jump','_','_','_')
            Quadruple.backpatch(cond_result[1],Quadruple.nextquad())

            self.tokenCheck('#}')

        while self.currentToken.token == 'elif':
            self.elif_statements()
        
        if self.currentToken.token == 'else':
            self.else_statements()
            Quadruple.backpatch(if_statment,Quadruple.nextquad())

        
    def elif_statements(self):
        self.tokenCheck('elif')
        self.condition()
        self.tokenCheck(':')
        self.code_block()
        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
            self.code_block()
            self.tokenCheck('#}')

    def else_statements(self):
        self.tokenCheck('else')
        self.tokenCheck(':')
        self.code_block()
        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
            self.code_block()
            self.tokenCheck('#}')

    def while_statements(self):
        self.tokenCheck('while')
        self.condition()
        self.tokenCheck(':')
        self.code_block()
        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
            self.code_block()
            self.tokenCheck('#}')

    def return_statements(self):
        self.tokenCheck('return')
        expression = self.expression()
        # print(f"the expression inside the reterun statment: {expression}")
        Quadruple.genquad('retv',expression,'_','_')

    def print_statements(self):
        self.tokenCheck('print')
        self.tokenCheck('(')
        expression = self.expression()
        
        self.tokenCheck(')')
        Quadruple.genquad('out',expression,'_','_')
        # Quadruple.functionFormat('out',expression,'_','_')

    def input_statements(self):
        self.tokenCheck('int')
        self.tokenCheck('(')
        self.tokenCheck('input')
        self.tokenCheck('(')
        self.tokenCheck(')')
        self.tokenCheck(')')

    def code_block(self):
        while self.currentToken.token in [ 'if', 'while', 'print', 'return', 'input','global','int'] or self.currentToken.tokenType == 'identifier':
            self.statements()

    def condition(self):
        cond_true = []
        cond_false = []
        cond_true,cond_false = self.bool_term()
        z =''
        while self.currentToken.token == 'or':            
            self.tokenCheck('or')
            # bool_terms.append(self.bool_term())
            if cond_false:
                Quadruple.backpatch(cond_false,Quadruple.nextquad())
            bool_term2 = self.bool_term()

            cond_true = Quadruple.mergelist(cond_true,bool_term2[0])
            # print(f"Here: {cond_true}")
            cond_false = bool_term2[1]
            # z= Quadruple.nextquad()
            # Quadruple.genquad("or",bool_terms[0],bool_terms[1],z)
        print(cond_true)
        return cond_true,cond_false
    
    def bool_term(self):
        B_true = []
        B_false = []
        B_true,B_false =self.bool_factor()
        # print(f"Here the rsult of bool_factor: {res}\n")
        while self.currentToken.token == 'and':
            self.tokenCheck('and')
            Quadruple.backpatch(B_true,Quadruple.nextquad())
            bool_factor =  self.bool_factor()

            B_false= Quadruple.mergelist(B_false,bool_factor[1])
            B_true = bool_factor[0]
        return B_true,B_false

    def bool_factor(self):
        B_true = []
        B_false = []
        if self.currentToken.token == 'not':
            self.tokenCheck('not')
            condition = self.condition()
            # result = Quadruple.nextquad()
            # Quadruple.genquad("!", self.currentToken.token, '_', result)
            B_true = condition[0]
            B_false = condition[1]
        elif self.currentToken.token == '(':
            self.tokenCheck('(')
            condition = self.condition()
            self.tokenCheck(')')
            B_true = condition[0]
            B_false = condition[1]
        else:
            first_part = self.currentToken.token
            self.expression()
            if self.currentToken.token in ['<', '>', '==', '!=', '<=', '>=']:
                op = self.currentToken.token
                self.nextToken()
                second_part = self.currentToken.token
                self.expression()
                # result = Quadruple.nextquad()
                B_true = Quadruple.makelist(Quadruple.nextquad())
                Quadruple.genquad(op, first_part, second_part,'_')
                jump_target = Quadruple.nextquad()
                B_false = Quadruple.makelist(Quadruple.nextquad())
                Quadruple.genquad('jump','_','_','_')
                
            
        return B_true,B_false


    def expression(self):
        new_temp = ''
        first_place = ''
        if self.currentToken.token in ['if','elif','else','while','print','return','input']:
            self.statements()
            if self.currentToken.token != '#}' and self.currentToken.token not in ['+', '-', '=']:
                self.expression()
        elif self.currentToken.token =='#}':
            self.tokenCheck('#}')
        
        else:
            sign =self.optional_sign()
            res = self.term()
            first_place = sign + res
            
            while self.currentToken.token in ['+','-', '=']:
                if self.currentToken.token == '+':
                    operator = self.currentToken.token
                    self.tokenCheck('+')
                elif self.currentToken.token == '=':
                    operator = self.currentToken.token
                    self.tokenCheck('=')
                else:
                    operator = self.currentToken.token
                    self.tokenCheck('-')
                
                second_place = self.term()
                z = Quadruple.newtemp()
                Quadruple.genquad(operator, first_place, second_place,z)

        return  first_place
    
    
    
    def optional_sign(self):
        sign = ''
        if self.currentToken.token == '+':
            sign = self.currentToken.token
            self.tokenCheck('+')
        elif self.currentToken.token == '-':
            sign = self.currentToken.token
            self.tokenCheck('-')
        
        return sign

    def term(self):
        temp = ''
        res = self.factor()
        operator =''
        while self.currentToken.token in ['*', '//', '%']:
            operator = self.currentToken.token
            if self.currentToken.token == '*':                
                self.tokenCheck('*')
            elif self.currentToken.token == '//':                
                self.tokenCheck('//')
            else:                
                self.tokenCheck('%')
            res2 = self.factor()
            z = Quadruple.newtemp()
            Quadruple.genquad(operator,res,res2,z)
            # Quadruple.functionFormat(operator,res,res2,z)
            res= z
        temp = res
        # print(temp)
        return temp
    
    def factor(self):
        res = ''
        if self.currentToken.tokenType in [ 'number', 'keyword']:
            res = self.currentToken.token
            self.nextToken()
        elif self.currentToken.token == '(':
            res = self.currentToken.token
            self.tokenCheck('(')
            exp =self.expression()
            self.tokenCheck(')')
            res = exp
        elif self.currentToken.tokenType == 'identifier':
            res = self.currentToken.token
            self.nextToken()
            tail = self.idtail(res)
        return res
    
    def idtail(self,name):
        global isFunction
        res = ''
        if self.currentToken.token == '(':
            isFunction = True
            self.tokenCheck('(')
            res =self.actual_pars()
            self.tokenCheck(')')
            new_temp = Quadruple.newtemp()
            Quadruple.genquad('par',new_temp,'RET','_')

            Quadruple.genquad('call',name,'_','_')

        return res
    
    def actual_pars(self):
        res = ''
        res = self.expression()
        Quadruple.genquad('par',res,'CV','_')

        while self.currentToken.token == ',':
            self.tokenCheck(',')
            res =self.expression()
            Quadruple.genquad('par',res,'CV','_')

        return res

    def syntaxCorect(self):
        if self.currentToken.tokenType == 'EOF':
            self.syntaxFile.write("\n\nEnding Token: "+self.currentToken.token+"Index of Ending Token: "+str(self.tokenIndex))
            print("\n\nEnding Token: "+self.currentToken.token)            
            print('Syntax is correct\n\n')


##------------------------------------ Intermediate Code -------------------------------##
  
class Quadruple:
    current_id = 0
    def __init__(self, operation, x, y, z):
        self.id = Quadruple.current_id
        Quadruple.current_id+=1
        self.operation = str(operation)
        self.x = str(x)
        self.y = str(y)
        self.z = str(z)
        
    def __str__(self):
        return f"({self.operation}, {self.x}, {self.y}, {self.z})"
    
    @staticmethod
    def functionFormat(operation, x, y, z):
        global lineCount
        print(f"{lineCount}:{operation},{x},{y},{z}\n")
        lineCount += 1
    @classmethod
    def nextquad(cls):

        global lineCount
        lineCount += 1
        
        return lineCount


    def genquad(operation, x, y, z):
        global quadrupleList, lineCount
        # self.id += 1
        newQuad = Quadruple(operation, x, y, z)
        newQuad.nextquad()
        quadrupleList.append(newQuad)

    def emptylist():
        newList = []
        return newList
    
    def mergelist(list1,list2):
        merged = list1 + list2
        return merged

    def newtemp():
        global tempVariableCount,temporaryVariables
        tempVariableCount += 1
        temporaryVariables.append(f"T_{tempVariableCount}")
        return f"T_{tempVariableCount}"

    def makelist(x):
        newList = []
        newList.append(x)
        return newList

    # def backpatch(list,z):
    #     for quadruple in quadrupleList:
    #         if quadruple in list:
    #             quadruple[-1] = str(z)

    def backpatch(list,z):
        global quadrupleList
        for quad in quadrupleList:
            # print(type(quad.id))
            # print(type(list[0]))
            if quad.id in list:
                print("Found!")
                quad.z = str(z)




##-------------------------------------------- Main --------------------------------------------##

lex = LexicalAnalyzer(fileName)   
tokens = lex.lexical_analyzer()
syntax = SyntaxAnalyzer(tokens)
syntax.startRule()
# quad = Quadruple.genquad('+','x','y','z')

with open('quadruples.txt', 'w') as f:
    line = 1
    for quadruple in quadrupleList:
        # Construct each line with proper formatting
        line_to_write = f"{quadruple.id}: {quadruple.operation},{quadruple.x},{quadruple.y},{quadruple.z}\n"
        f.write(line_to_write)
        line += 1

    
