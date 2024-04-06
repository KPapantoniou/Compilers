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
                                return True
        else:
            print(f"Syntax error: expected #{{ received {self.currentToken.token}")
            print(f"Line : {self.tokenIndex}")
            raise Exception("Unexpected token received")

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
        if self.currentToken.tokenType == 'identifier':
            result = self.currentToken.token
            self.nextToken()
       
        self.tokenCheck('=')
        
        self.other_statements()
        expression = self.expression()
        # print(expression,result)
        Quadruple.genquad('=',expression,'_',result)
        Quadruple.functionFormat('=',expression,'_',result)

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
        self.tokenCheck('if')
        self.condition()
        self.tokenCheck(':')
        self.code_block()
        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
            self.code_block()
            self.tokenCheck('#}')

        while self.currentToken.token == 'elif':
            self.elif_statements()
        if self.currentToken.token == 'else':
            self.else_statements()

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
        self.expression()

    def print_statements(self):
        self.tokenCheck('print')
        self.tokenCheck('(')
        self.expression()
        self.tokenCheck(')')

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
    # def code_block(self):
    #     while self.currentToken.token != '#}':
    #         self.statements()
    #         # if self.currentToken.token != '#}':
    #         #     self.code_block()
    #         self.nextToken()

    def condition(self):
        self.bool_term()
        while self.currentToken.token == 'or':
            self.tokenCheck('or')
            self.bool_term()
        return self.currentToken.token
    
    def bool_term(self):
        self.bool_factor()
        while self.currentToken.token == 'and':
            self.tokenCheck('and')
            self.bool_factor()
        return self.currentToken.token

    # def bool_factor(self):
    #     if self.currentToken.token == 'not':
    #         self.tokenCheck('not')
    #         self.condition()
    #     elif self.currentToken.token in ['<', '>', '==', '!=', '<=', '>=']:
    #         if self.currentToken.tokenType == 'CompareOperation':
    #             self.nextToken() 
    #             self.expression() 
    #             # self.factor()
    #     elif self.currentToken.token in ['(',')']:
    #         if self.currentToken.token == '(':
    #             self.tokenCheck('(')
    #             self.condition()
            
    #         elif self.currentToken.token == ')':
    #             self.tokenCheck(')')
    #             # self.condition()
    #     else:    
    #         self.expression()
    #         if self.currentToken.tokenType == 'ArithmeticOperation': 
    #             self.expression()
    #             # self.condition()
    #         # elif self.currentToken.tokenType in ['identifier', 'number']:
    #         #     self.nextToken() 
    #         #     self.condition()
            
    #         # elif self.currentToken.token == ',':
    #         #     self.nextToken()
    #         #     self.condition()
    def bool_factor(self):
        if self.currentToken.token == 'not':
            self.tokenCheck('not')
            self.condition()
        elif self.currentToken.token == '(':
            self.tokenCheck('(')
            self.condition()
            self.tokenCheck(')')
        else:
            self.expression()
            if self.currentToken.token in ['<', '>', '==', '!=', '<=', '>=']:
                self.nextToken()
                self.expression()
        
            
            # elif self.currentToken.tokenType in ['identifier', 'number']:
            #     self.expression()
        return self.currentToken.token


    def expression(self):
        new_temp = ''
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
            
            while self.currentToken.token in ['+', '-', '=']:
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
                Quadruple.functionFormat(operator, first_place, second_place,z)
                new_temp = z
                # print(operator, firs_place, second_place,z)
                
                # if self.currentToken.token not in ['+', '-', '='] and self.currentToken.token != '#}': 
                #     self.expression()
        return  new_temp
    
    
    
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
        res = self.factor()
        while self.currentToken.token in ['*', '//', '%']:
            if self.currentToken.token == '*':
                self.tokenCheck('*')
            elif self.currentToken.token == '//':
                self.tokenCheck('//')
            else:
                self.tokenCheck('%')
            res = self.factor()
        return res

    # def factor(self):
    #     if self.currentToken.tokenType in ['identifier', 'number', 'keyword']:
    #         self.nextToken() #changing this
    #         if self.currentToken.token == '(':
    #             self.tokenCheck('(')
    #             self.expression()
    #             self.tokenCheck(')')
    
            
        # elif self.currentToken.token == '(':
        #     self.tokenCheck('(')
        #     self.expression()
        #     self.tokenCheck(')')
        #     self.bool_factor()
        # print(self.currentToken.token)
        # return self.currentToken.token
    
    def factor(self):
        res = ''
        if self.currentToken.tokenType in [ 'number', 'keyword']:
            res = self.currentToken.token
            self.nextToken()
        elif self.currentToken.token == '(':
            res = self.currentToken.token
            self.tokenCheck('(')
            self.expression()
            self.tokenCheck(')')
        elif self.currentToken.tokenType == 'identifier':
            res = self.currentToken.token
            self.nextToken()
            self.idtail()
        return res
    
    def idtail(self):
        if self.currentToken.token == '(':
            self.tokenCheck('(')
            self.actual_pars()
            self.tokenCheck(')')
        return  self.currentToken.token
    
    def actual_pars(self):
        self.expression()
        while self.currentToken.token == ',':
            self.tokenCheck(',')
            self.expression()
        return self.currentToken.token

    def syntaxCorect(self):
        if self.currentToken.tokenType == 'EOF':
            self.syntaxFile.write("\n\nEnding Token: "+self.currentToken.token+"Index of Ending Token: "+str(self.tokenIndex))
            print("\n\nEnding Token: "+self.currentToken.token)            
            print('Syntax is correct\n\n')


##------------------------------------ Intermediate Code -------------------------------##
  
class Quadruple:

    def __init__(self, operation, x, y, z):
        self.operation = str(operation)
        self.x = str(x)
        self.y = str(y)
        self.z = str(z)
        

    def functionFormat(operation, x, y, z):
        
        print(lineCount,":" + operation +","+ x + "," + y + "," + z)
        
        # return lineCount,":" + operation +","+ x + "," + self.y + "," + self.z
    @classmethod
    def nextquad(cls):

        global lineCount
        lineCount += 1
        return 


    def genquad(operation, x, y, z):
        global quadrupleList, lineCount
                
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

    def backpatch(list,z):
        for quadruple in quadrupleList:
            if quadruple in list:
                quadruple[-1] = str(z)

##-------------------------------------------- Main --------------------------------------------##

lex = LexicalAnalyzer(fileName)   
tokens = lex.lexical_analyzer()
syntax = SyntaxAnalyzer(tokens)
syntax.startRule()
quad = Quadruple.genquad('+','x','y','z')

# temp = quad.newtemp()
# for quad in quadrupleList:
#     quad.functionFormat()



