#Authors: 1. Konstantinos Papantoniou-Xatzigiosis, AM: 4769
#         2. Natalia Michou                      , AM: 4922
# Date: 2024-05-29
# Description: A compiler for the cpy language,
# including a lexical analyzer, a syntax analyzer,
#  an intermediate code generator and a symbol table. 
#The compiler is written in Python and the output is written in a file called final_code.asm.



from sys import argv

fileName = argv[1] 
quad_file = open('quadruples.int', 'w')
temporaryVariables = []
quadrupleList = []
lineCount =0
line_final = 0
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
        self.symbol_table = SymbolTable()
        self.final_code = FinalCode(quadrupleList, self.symbol_table)


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
            if self.symbol_table.current_scope == None:
                self.symbol_table.enter_scope()
            self.declarations()
            self.startRule()
        elif self.currentToken.token == 'def':
            self.tokenCheck('def')
            if self.symbol_table.current_scope == None:
                self.symbol_table.enter_scope()
            if self.def_function():
                self.startRule()
        elif self.currentToken.token == '#def':
            self.tokenCheck('#def')
            self.def_main()     
        else:
            raise Exception(f"Syntax error: expected #def, #int, or def received '{self.currentToken.token}' token number '{self.tokenIndex}'")

    def def_main(self):
        self.tokenCheck('main')
        mainfunc = Procedure('main', None, None)
        self.symbol_table.insert(mainfunc)
        self.symbol_table.enter_scope()
        while self.currentToken.token == '#int':
            self.tokenCheck('#int')
            self.declarations()
        while self.currentToken.token == 'def':
            self.def_function()
        self.symbol_table.update(mainfunc, starting_quad=Quadruple.nextquad()) 
        Quadruple.genquad("begin_block",'main','_','_')
        beginBlock = Quadruple.beginBlock(quadrupleList)
        self.code_block()
        Quadruple.genquad("halt",'_','_','_')
        self.symbol_table.update(mainfunc, frame_length=self.symbol_table.stack_position[self.symbol_table.current_stack])
        Quadruple.genquad("end_block",'main','_','_')
        endBlock = Quadruple.endBlock(quadrupleList)
        self.final_code.final_code(Quadruple.blockLength(beginBlock, endBlock, quadrupleList))
        self.final_code.final_codef.close()
        self.symbol_table.exit_scope()
        if self.currentToken.token == 'EOF':
                self.syntaxCorect() 

    def def_function(self):
        programName = self.currentToken.token
        if self.currentToken.tokenType == 'identifier':
            func = Function(programName, None, None, 'integer')
            self.symbol_table.insert(func)
            self.symbol_table.enter_scope()
            self.nextToken()
            self.tokenCheck('(')
            params = self.formal_pars()
            for param in params:
                func.formalParameters.append(Parameter(param, 'integer', 'in', None))
                self.symbol_table.insert(Parameter(param, 'integer', 'in', None))
            self.tokenCheck(')')
            self.tokenCheck(':')
            self.tokenCheck('#{')               
            while self.currentToken.token == '#int':
                self.tokenCheck('#int')
                self.declarations()
            if self.currentToken.token == 'global':
                self.tokenCheck('global')
                if self.currentToken.tokenType == 'identifier':
                    self.nextToken()
                    while self.currentToken.token == ',':
                        self.tokenCheck(',')
                        if self.currentToken.tokenType == 'identifier':
                            self.nextToken()
            while self.currentToken.token == 'def':
                self.nextToken()
                self.def_function()
            self.symbol_table.update(func, starting_quad=Quadruple.nextquad()) 
            Quadruple.genquad("begin_block",programName,'_','_')
            beginBlock = Quadruple.beginBlock(quadrupleList)      
            self.code_block()
            self.symbol_table.update(func, frame_length=self.symbol_table.stack_position[self.symbol_table.current_stack])
            Quadruple.genquad("end_block",programName,'_','_')
            endBlock = Quadruple.endBlock(quadrupleList)
            self.final_code.final_code(Quadruple.blockLength(beginBlock, endBlock, quadrupleList))
            self.symbol_table.exit_scope()
            if self.tokenCheck('#}'):
                return True

    def declarations(self):
        if self.currentToken.tokenType == 'identifier':
            self.symbol_table.insert(Variable(self.currentToken.token, 'integer', None))
            self.nextToken()
            while self.currentToken.token == ',':
                self.tokenCheck(',')
                if self.currentToken.tokenType == 'identifier':
                    self.symbol_table.insert(Variable(self.currentToken.token, 'integer', None))
                    self.nextToken()

    def formal_pars(self):
        param_list = []
        if self.currentToken.tokenType == 'identifier':
            param_list.append(self.currentToken.token)
            self.nextToken()
            while self.currentToken.token == ',':
                self.tokenCheck(',')
                if self.currentToken.tokenType == 'identifier':
                    param_list.append(self.currentToken.token)
                    self.nextToken()
        return param_list

    def statements(self):
        if self.currentToken.tokenType == 'identifier':
            self.assignment_statements()
        elif self.currentToken.token == '=':
            self.assignment_statements()
        elif self.currentToken.token == 'global':
            self.tokenCheck('global')
            if self.currentToken.tokenType == 'identifier':
                    self.nextToken()
        elif self.currentToken.token in ['if', 'while', 'print', 'return', 'int']:
            result = None
            self.other_statements(result)

    def assignment_statements(self):
        global isFunction
        if self.currentToken.tokenType == 'identifier':
            result = self.currentToken.token
            self.nextToken()
        self.tokenCheck('=')
        if self.currentToken.token == 'int':
            self.input_statements(result)
        else:
            expression = self.expression()
            Quadruple.genquad(':=',expression,'_',result)
            isFunction = False

    def other_statements(self, result):
        if self.currentToken.token == 'if':
            self.if_statements()
        elif self.currentToken.token == 'while':
            self.while_statements()
        elif self.currentToken.token == 'print':
            self.print_statements()
        elif self.currentToken.token == 'return':
            self.return_statements()
        elif self.currentToken.token == 'int':
            self.input_statements(result)

    def if_statements(self):
        global lineCount,quadrupleList
        self.tokenCheck('if')        
        cond_result = self.condition()     
        self.tokenCheck(':')
        Quadruple.backpatch(cond_result[0],Quadruple.nextquad())
        stet =self.statements()
        if_statment = Quadruple.makelist(Quadruple.nextquad())
        Quadruple.genquad('jump','_','_','_')
        Quadruple.backpatch(cond_result[1],Quadruple.nextquad())
        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
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
        Quadruple.backpatch(if_statment,Quadruple.nextquad())
 
    def elif_statements(self):
        self.tokenCheck('elif')
        cond_true,cond_false =self.condition()
        self.tokenCheck(':')
        Quadruple.backpatch(cond_true,Quadruple.nextquad())
        self.code_block()
        Quadruple.backpatch(cond_false,Quadruple.nextquad())
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
        quad = Quadruple.nextquad()
        cond_true,cond_false = self.condition()
        self.tokenCheck(':')
        if self.currentToken.token == '#{':
            self.tokenCheck('#{')
            
            Quadruple.backpatch(cond_true,Quadruple.nextquad())
            while self.currentToken.token != '#}':
                self.statements()
            Quadruple.genquad('jump','_','_',quad)
            Quadruple.backpatch(cond_false,Quadruple.nextquad())
            self.tokenCheck('#}')
            return
        else:
            Quadruple.backpatch(cond_true,Quadruple.nextquad())
            while self.currentToken.token != 'return':                
                self.statements()
            Quadruple.genquad('jump','_','_',quad)
            Quadruple.backpatch(cond_false,Quadruple.nextquad())
        

    def return_statements(self):
        self.tokenCheck('return')
        expression = self.expression()
        Quadruple.genquad('ret',expression,'_','_')

    def print_statements(self):
        self.tokenCheck('print')
        self.tokenCheck('(')
        expression = self.expression()
        self.tokenCheck(')')
        Quadruple.genquad('out',expression,'_','_')

    def input_statements(self, id):
        self.tokenCheck('int')
        self.tokenCheck('(')
        self.tokenCheck('input')
        self.tokenCheck('(')
        self.tokenCheck(')')
        self.tokenCheck(')')
        Quadruple.genquad('inp', id, '_', '_')

    def code_block(self):
        while self.currentToken.token in [ 'if', 'while', 'print', 'return', 'input','global','int'] or self.currentToken.tokenType == 'identifier':
            self.statements()

    def condition(self):
        cond_true = []
        cond_false = []
        cond_true,cond_false = self.bool_term()
        while self.currentToken.token == 'or':            
            self.tokenCheck('or')
            if cond_false:
                Quadruple.backpatch(cond_false,Quadruple.nextquad())
            bool_term2 = self.bool_term()
            cond_true = Quadruple.mergelist(cond_true,bool_term2[0])
            cond_false = bool_term2[1]
        return cond_true,cond_false
    
    def bool_term(self):
        B_true = []
        B_false = []
        B_true,B_false =self.bool_factor()
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
            B_true = condition[0]
            B_false = condition[1]
        elif self.currentToken.token == '(':
            self.tokenCheck('(')
            condition = self.condition()
            self.tokenCheck(')')
            B_true = condition[0]
            B_false = condition[1]
        else:
            ex1 = self.expression()
            if self.currentToken.token in ['<', '>', '==', '!=', '<=', '>=']:
                op = self.currentToken.token
                self.nextToken()
                ex2 = self.expression()
                B_true = Quadruple.makelist(Quadruple.nextquad())
                Quadruple.genquad(op, ex1, ex2,'_')
                jump_target = Quadruple.nextquad()
                B_false = Quadruple.makelist(Quadruple.nextquad())
                Quadruple.genquad('jump','_','_','_')
        return B_true,B_false


    def expression(self):
        z = ''
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
                self.symbol_table.insert(TemporaryVariable(z, 'integer', None))
                Quadruple.genquad(operator, first_place, second_place,z)
                first_place = z
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
            self.symbol_table.insert(TemporaryVariable(z, 'integer', None))
            Quadruple.genquad(operator,res,res2,z)
            res= z
        temp = res
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
            self.symbol_table.insert(TemporaryVariable(new_temp, 'integer', None))
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
        return lineCount

    def genquad(operation, x, y, z):
        global quadrupleList, lineCount
        lineCount +=1
        newQuad = Quadruple(operation, x, y, z)
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
    
    def to_list(self):
        return [self.operation, self.x, self.y, self.z]
    
    def makelist(x):
        newList = []
        newList.append(x)
        return newList

    def backpatch(list,z):
        global quadrupleList
        for quad in quadrupleList:
            if quad.id in list:
                quad.z = str(z)

    def beginBlock(quadlist):
        blockStart = len(quadlist)-1
        return blockStart
    
    def endBlock(quadlist):
        blockEnd = len(quadlist)
        return blockEnd
    
    def blockLength(blockStart, blockEnd, quadlist):
        return quadlist[blockStart:blockEnd]


##------------------------------------ Symbol Table ------------------------------------##

class Entity:
    def __init__(self, name):
        self.name = name

class Variable(Entity):
    def __init__(self, name, type, offset):
        super().__init__(name)
        self.type = type
        self.offset = offset

    def __str__(self):
        return f'Variable: name: {self.name}, offset: {self.offset}'


class TemporaryVariable(Variable):
    def __init__(self, name, type, offset):
        super().__init__(name, type, offset)

    def __str__(self):
        return f'TempVar: name: {self.name}, offset: {self.offset}'

class Constant(Entity):
    def __init__(self, name, type, value):
        super().__init__(name)
        self.type = type
        self.value = value

    def __str__(self):
        return f'Const: name: {self.name}'

class FormalParameter(Entity):
    def __init__(self, name, type, mode):
        super().__init__(name)
        self.type = type
        self.mode = mode

    def __str__(self):
        return f'FormalParam: name: {self.name}, mode: {self.mode}'


class Parameter(FormalParameter):
    def __init__(self, name, type, mode, offset):
        super().__init__(name, type, mode)
        self.offset = offset

    def __str__(self):
        return f'Param: name: {self.name}, mode: {self.mode} offset: {self.offset}'


class Procedure(Entity):
    def __init__(self, name, starting_quad, frame_length):
        super().__init__(name)
        self.starting_quad = starting_quad
        self.frame_length = frame_length
        self.formalParameters = []

    def __str__(self):
        return f'Proc: name: {self.name} startingQuad: {self.starting_quad} framelen: {self.frame_length}'


class Function(Procedure):
    def __init__(self, name, starting_quad, frame_length, type):
        super().__init__(name, starting_quad, frame_length)
        self.type = type

    def __str__(self):
        return f'Func: name: {self.name} startquad:{self.starting_quad} framelen:{self.frame_length}'


class SymbolTable:
    def __init__(self):
        self.scopes = []
        self.stack_position = []
        self.current_scope = None
        self.current_stack = -1
        self.function_scopes = {}
        self.outputFile = "symbolTable.sym"
        self.fd = open(self.outputFile, "w")

    def __str__(self):
        string = ''
        for scope in self.scopes:
            for entity in scope.values():
                string += f'{entity}'

    def enter_scope(self):
        if len(self.scopes) > 0:
            self.function_scopes[self.scopes[-1][-1].name] = len(self.scopes)
        self.scopes.append([])
        self.stack_position.append(12)
        self.current_scope = self.scopes[-1]
        self.current_stack += 1

    def print_state(self):
        self.fd.write("Exiting a scope, printing current state of Symbol table\n")
        for scope in self.scopes:
             self.fd.write(f'scope:{self.scopes.index(scope)}\n')
             for entity in scope:
                self.fd.write(f'\t{entity}\n')

    def exit_scope(self):
        global quadrupleList,quad_file
        self.print_state()  
        for quad in quadrupleList:
            quad_file.write(f"{quad.id} {quad.operation} {quad.x} {quad.y} {quad.z}\n")
        quadrupleList.clear()
        self.scopes.pop()
        
        if len(self.scopes) == 0:
            return
        self.current_scope = self.scopes[-1]
        self.update(self.current_scope[-1], frame_length=self.stack_position[self.current_stack])
        self.stack_position.pop()        
        self.current_stack -= 1
        

    def get_last_frame_length(self):
        return self.stack_position[self.current_stack]

    def insert(self, entity):
        if entity.__class__.__name__ == 'Parameter' or entity.__class__.__name__ == 'Variable' or entity.__class__.__name__ == 'TemporaryVariable':
            entity.offset = self.stack_position[self.current_stack]
            self.stack_position[self.current_stack] += 4
        self.current_scope.append(entity)

    def varlookup(self, name):
        scopeNum = 0
        for scope in reversed(self.scopes):
            scopeNum += 1
            for entity in scope:
                if entity.name == name:
                    return scopeNum, entity
        exit('Variable '+name+' not found')

    def funclookup(self, name):
        for scope in reversed(self.scopes):
            for entity in scope:
                if entity.name == name:
                    if entity.__class__.__name__ == 'Procedure' or entity.__class__.__name__ == 'Function':
                        return entity.starting_quad, entity.frame_length, entity.formalParameters
        exit('Function not found')

    def update(self, entity, frame_length=-1, starting_quad=-1):
        if entity.__class__.__name__ == 'Function' or entity.__class__.__name__ == 'Procedure':
            if frame_length != -1:
                entity.frame_length = frame_length
            if starting_quad != -1:
                entity.starting_quad = starting_quad

    def add_parameter(self, entity, formal_parameter):
        if entity.__class__.__name__ == 'Function' or entity.__class__.__name__ == 'Procedure':
            entity.formalParameters.append(formal_parameter)
##-------------------------------------------- Final Code --------------------------------------##

class FinalCode:

    def __init__(self, quadrupleList, symbol_table):
        self.quadrupleList = quadrupleList
        self.symbol_table = symbol_table
        self.labelCount = 0
        self.paramList =[]
        self.final_codef = open('final_code.asm', 'w')

        self.final_codef.write('.data\n')
        self.final_codef.write('str_nl: .asciz "\\n"\n')
        self.final_codef.write('.text\n')
        self.final_codef.write('j Lmain\n')

    def gnvlcode(self, v):
            scope_number, entity = self.symbol_table.varlookup(v)
            if scope_number == 1:
                return
            for i in range(scope_number-1):
                if i == 0:
                    self.final_codef.write("\tlw t0, -4(sp)\n")
                else:
                    self.final_codef.write("\tlw t0, -4(t0)\n")
            self.final_codef.write(f"\taddi t0, t0, -{entity.offset}\n")
            
    def loadvr(self, v, r):
        if v.lstrip('-').isdigit(): 
            self.final_codef.write(f"\tli {r}, {v}\n")
        else:
            scope_number, entity = self.symbol_table.varlookup(v)
            if scope_number and (isinstance(entity, Variable) or isinstance(entity, TemporaryVariable) or isinstance(entity, Parameter))  == 1:
                self.final_codef.write(f"\tlw {r}, -{entity.offset}(sp)\n")
            elif scope_number > 1 and (isinstance(entity, Variable) or isinstance(entity, TemporaryVariable) or isinstance(entity, Parameter)):
                self.gnvlcode(v)
                self.final_codef.write(f"\tlw {r}, (t0)\n")
            elif scope_number == len(self.symbol_table.scopes) and isinstance(entity, Variable):
                self.final_codef.write(f"\tlw {r}, -{entity.offset}(gp)\n")

    def storerv(self, r, v):
        if v.lstrip('-').isdigit(): 
            self.loadvr(r, 't0')
            self.storerv('t0', v)
        scope_number, entity = self.symbol_table.varlookup(v)
        if scope_number == 1:
            self.final_codef.write(f"\tsw {r}, -{entity.offset}(sp)\n")
        elif scope_number > 1:
            self.gnvlcode(v)
            self.final_codef.write(f"\tsw {r}, (t0)\n")
        elif scope_number == len(self.symbol_table.scopes):
            self.final_codef.write(f"\tsw {r}, -{entity.offset}(gp)\n")

    def createLabel(self):
        self.final_codef.write("L"+str(self.labelCount)+":\n")
        self.labelCount += 1

    def final_code(self, quadruple):
        if quadruple[0].x == 'main':
            self.final_codef.write("Lmain:\n")
            starting_quad, frame_length, formal_parameters = self.symbol_table.funclookup('main')
            self.final_codef.write(f"\taddi sp, sp, -{frame_length}\n")
            self.final_codef.write("\tmv fp, sp\n")
        else:
            self.createLabel()
            self.final_codef.write("\tsw ra,(sp)\n")
        for quad in quadruple[1:-1]:
            if quad.operation == 'par':
                self.paramList.append(quad)
            if quad.operation == 'call':
                starting_quad, frame_length, formal_parameters = self.symbol_table.funclookup(quad.x)
                for param in self.paramList:
                    self.createLabel()
                    if self.paramList.index(param) == 0:
                        self.final_codef.write(f"\taddi fp, sp, -{frame_length}\n")
                    if param.y == 'CV':
                        d = 12+4*(self.paramList.index(param))
                        self.loadvr(param.x, 't0')
                        self.final_codef.write(f"\tsw t0, -{d}(fp)\n")
                    elif param.y == 'RET':
                        scope, entity = self.symbol_table.varlookup(param.x)
                        self.final_codef.write(f"\taddi t0, sp, -{entity.offset}\n")
                        self.final_codef.write("\tsw t0, -8(fp)\n")
                self.createLabel()
                scope, entity = self.symbol_table.varlookup(quad.x)
                starting_quad, frame_length, formal_parameters = self.symbol_table.funclookup(quad.x)
                current_scope_level = len(self.symbol_table.scopes)
                called_scope_level = current_scope_level - scope -1
                if current_scope_level == called_scope_level:
                    self.final_codef.write("\tlw t0, -4(sp)\n")
                    self.final_codef.write("\tsw t0, -4(fp)\n")
                else:
                    self.final_codef.write("\tsw sp, -4(fp)\n")
                
                self.final_codef.write(f"\taddi sp, sp, -{frame_length}\n")
                self.final_codef.write(f"\tjal L{starting_quad}\n")
                self.final_codef.write(f"\taddi sp, sp, {frame_length}\n")
                self.paramList = []
            

            self.createLabel()
            if quad.operation == ":=":
                self.loadvr(quad.x, 't1')
                self.storerv('t1', quad.z)
            elif quad.operation == '+':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tadd t1, t1, t2\n")
                self.storerv('t1', quad.z)
            elif quad.operation == '-':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tsub t1, t1, t2\n")
                self.storerv('t1', quad.z)
            elif quad.operation == '*':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tmul t1, t1, t2\n")
                self.storerv('t1', quad.z)
            elif quad.operation == '//':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tdiv t1, t1, t2\n")
                self.storerv('t1', quad.z)
            elif quad.operation == '%':
                self.loadvr(quad.x, 't1')   
                self.loadvr(quad.y, 't2')                   
                self.final_codef.write("\trem t1, t1, t2\n")
                self.storerv('t1', quad.z)
            elif quad.operation == '<':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tblt t1, t2, L"+str(quad.z)+"\n")
            elif quad.operation == '>':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tbgt t1, t2, L"+str(quad.z)+"\n")
            elif quad.operation == '==':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tbeq t1, t2, L"+str(quad.z)+"\n")
            elif quad.operation == '!=':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tbne t1, t2, L"+str(quad.z)+"\n")
            elif quad.operation == '<=':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tble t1, t2, L"+str(quad.z)+"\n")
            elif quad.operation == '>=':
                self.loadvr(quad.x, 't1')
                self.loadvr(quad.y, 't2')
                self.final_codef.write("\tbge t1, t2, L"+str(quad.z)+"\n")
            elif quad.operation == 'jump':
                self.final_codef.write("\tj L"+str(quad.z)+"\n")
            elif quad.operation == 'out':
                self.loadvr(quad.x, 'a0')
                self.final_codef.write("\tli a7, 1\n")
                self.final_codef.write("\tecall\n")
                self.final_codef.write("\tla a0, str_nl\n")
                self.final_codef.write("\tli a7, 4\n")
                self.final_codef.write("\tecall\n")
            elif quad.operation == 'inp':
                self.final_codef.write("\tli a7, 5\n")
                self.final_codef.write("\tecall\n")
                self.final_codef.write("\tadd t1, zero, a0\n")
                self.final_codef.write("\tsw t1, -12(sp)\n")	
                self.storerv('a0', quad.x)
            elif quad.operation == 'ret':
                self.final_codef.write("\tlw t0, -8(sp)\n")
                self.loadvr(quad.x, 't1')
                self.final_codef.write("\tsw t1, 0(t0)\n")
                self.final_codef.write("\tlw ra, (sp)\n")
                frame_length = self.symbol_table.get_last_frame_length()
                self.final_codef.write(f"\taddi sp, sp, {frame_length}\n")
                self.final_codef.write("\tjr ra\n")
            elif quad.operation == 'halt':
                self.final_codef.write("\tli a0, 0\n")
                self.final_codef.write("\tli a7, 93\n")
                self.final_codef.write("\tecall\n")
                return
            
        self.createLabel()
        if quadruple[0].x == 'main':
                self.final_codef.write("\n")
        else:
            frame_length = self.symbol_table.get_last_frame_length()
            self.final_codef.write("\tlw ra, 0(sp)\n")
            self.final_codef.write(f"\taddi sp, sp, {frame_length}\n")
            self.final_codef.write("\tjr ra\n")
   

##-------------------------------------------- Main --------------------------------------------##

lex = LexicalAnalyzer(fileName)   
tokens = lex.lexical_analyzer()
syntax = SyntaxAnalyzer(tokens)
syntax.startRule()