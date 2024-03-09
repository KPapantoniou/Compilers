
## first we need to open the .cpy file from terminal in order to translate it in an assembly language 

import string
import sys

global cpyFile

class Token:
    def __init__(self, token, tokenType):
        self.token = token 
        self.tokenType = tokenType

##------------------------------------ Lexical Analyzer ------------------------------------##
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
        ## file = open(sys.argv[1], 'r')
        file = open(self.filename, 'r')
        compilationFile = open('compilationFile.txt', 'w')
        compilationFile.write("lexigram analysis of the file: %s \n" %file.name)
        fileContent = file.read()
        alpha = False
        digit = False
        col = 0
        #the keyword that can not be the same with any variable 
        keywords=['main', 'def','#def','#int','global','if','elif','else','while','print','return','input','int','and','or','not']
        token = '' 
        finalWord=[]
        line = 0 
        index = 0
        state = self.STATES['stateBegin']
        numLetters=0
        intToken = 0
        while(index<len(fileContent)and state not in[self.STATES['stateOK'],self.STATES['stateERROR']]):
            currentCharacter = fileContent[index]
        
            if index < len(fileContent)-2:
                nextchar = fileContent[index+1]
            else:
                state = self.STATES['stateEOF']
           # implementing the state machine logic
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
                # elif(index == len(fileContent)-2):
                #     state = self.STATES['stateEOF']
                else:
                    state = self.STATES['stateOK']
                    token = currentCharacter
                    if currentCharacter == '+':
                        finalWord += [token] + ['Arithmetic_Operator']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '-':
                        finalWord += [token] + ['Arithmetic_Operator']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '*':
                        finalWord += [token] + ['Arithmetic_Operator']
                        state = self.STATES['stateOK']
                    elif currentCharacter == '%':
                        finalWord += [token] + ['Arithmetic_Operator']
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
                    #fileWord += currentCharacter
                        token += currentCharacter
                        state = self.STATES['stateLetter']
                    else:
                     
                         print("Error: Word must contain up to 30 characters")
                         print('Line: %d:%d'%(line,col))
                         state = self.STATES['stateERROR']
                else:
                    state = self.STATES['stateOK']
                #token+=currentCharacter
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
                    if(intToken>=-32767 and intToken<=32767):                    
                        state = self.STATES['stateDigit']

                    else:
                     
                         print("Error: Number must be between -32767 and 32767")
                         print('Line: %d:%d'%(line,col))
                         state = self.STATES['stateERROR']
            
                else:
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['number']

        
            if state == self.STATES['stateDivision']:
                if currentCharacter == '/':
                    if(nextchar == '/'):
                        token = '//'
                        index += 1
                        state = self.STATES['stateOK']
                        finalWord += [token] + ['division']
                else:
                    
                    print("Error: Invalid character")
                    print('Line: %d:%d'%(line,col)) 
                    state = self.STATES['stateERROR'] 
                    
            if state == self.STATES['stateLess']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['less']
                else:
                    token = currentCharacter
                    state = self.STATES['stateOK']
                    finalWord += [currentCharacter] + ['less']

            if state == self.STATES['stateMore']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['more']
                else:
                    token   = currentCharacter
                    state = self.STATES['stateOK']
                    finalWord += [currentCharacter] + ['more']

            if state == self.STATES['stateEqual']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['equal']
                else:
                    token = currentCharacter
                    state = self.STATES['stateOK']
                    finalWord += [currentCharacter] + ['variable']        
        
            if state == self.STATES['stateDiffernt']:
                if nextchar == '=':
                    token = currentCharacter+nextchar
                    state = self.STATES['stateOK']
                    finalWord += [token] + ['different']
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
                        index += 2 
                    finalWord += [token] + ['comment']
                    state = self.STATES['stateOK']
                
                
                
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
                compilationFile.write("---------------------------------------------------------\n")
                compilationFile.write("("+finalWord[0] + " -> " + finalWord[1] +")\n")
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
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndex = 0
        self.currentToken = self.tokens[0] if self.tokens else None

    def nextToken(self):
        if self.tokenIndex < len(self.tokens):
            self.tokenIndex += 1
            self.currentToken = self.tokens[self.tokenIndex]
            
        else:
            self.currentToken = None

    def tokenCheck(self, expectedToken):
        if self.currentToken.token == expectedToken:
            self.nextToken()
        else:
            print(f"Syntax error: expected {expectedToken} received {self.currentToken.token}")
            print(f"Line : {self.tokenIndex}")

    def startRule(self):
        
        if self.currentToken.token == '#def':
                self.tokenCheck('#def')
                self.def_main()
        elif self.currentToken.token == '#int':
                self.tokenCheck('#int')
                self.declarations()
        elif self.currentToken.token == 'def':
                self.tokenCheck('def')
                self.def_function()
        else:
                print(f"Syntax error: expected #def, #int, or def received {self.currentToken.token}")
                print(f"Line : {self.tokenIndex}")
        
        if self.currentToken.token == 'EOF':
            self.syntaxCorect()   
        
        #self.startRule()

        

    def def_main(self):
        self.tokenCheck('main')
        self.tokenCheck(':')
        self.declarations()
        while self.currentToken.token == 'def':
            self.def_function()
        self.code_block()

    def def_function(self):
       
        if self.currentToken.tokenType == 'identifier':
            self.nextToken()
        self.tokenCheck('(')
        self.formal_pars()
        self.tokenCheck(')')
        self.tokenCheck(':')
        self.tokenCheck('#{')

        if self.currentToken.token == '#int':
             self.tokenCheck('#int')
             self.declarations()
             
        if self.currentToken.token == 'global':
            self.tokenCheck('global')
            if self.currentToken.tokenType == 'identifier':
                    self.nextToken()


        # while self.currentToken.token in ['global', 'def']:
        #     if self.currentToken.token == 'global':
        #         self.tokenCheck('global')
        #         if self.currentToken.tokenType == 'identifier':
        #             self.nextToken()
            # elif self.currentToken.token == 'def':
            #     self.tokenCheck('def')
            #     self.def_function()

        #self.assignment_statements()
    
        self.code_block()
        self.tokenCheck('#}')

    def declarations(self):
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
        elif self.currentToken.token in ['if', 'while', 'print', 'return', 'input']:
            self.other_statements()
        else:
            print(f"Syntax error: expected identifier, if, while, print, return, or input received {self.currentToken.token}")
            print(f"Line : {self.tokenIndex}")

    def assignment_statements(self):
        if self.currentToken.tokenType == 'identifier':
            self.nextToken()
        self.tokenCheck('=')
        self.expression()

    def other_statements(self):
        if self.currentToken.token == 'if':
            self.if_statements()
        elif self.currentToken.token == 'while':
            self.while_statements()
        elif self.currentToken.token == 'print':
            self.print_statements()
        elif self.currentToken.token == 'return':
            self.return_statements()
        elif self.currentToken.token == 'input':
            self.input_statements()

    def if_statements(self):
        self.tokenCheck('if')
        self.condition()
        self.tokenCheck(':')
        self.code_block()
        if self.currentToken.token == 'elif':
            self.elif_statements()
        if self.currentToken.token == 'else':
            self.else_statements()

    def elif_statements(self):
        self.tokenCheck('elif')
        self.condition()
        self.tokenCheck(':')
        self.code_block()

    def else_statements(self):
        self.tokenCheck('else')
        self.tokenCheck(':')
        self.code_block()

    def while_statements(self):
        self.tokenCheck('while')
        self.condition()
        self.tokenCheck(':')
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

    def input_statements(self):
        self.tokenCheck('identifier')
        self.tokenCheck('=')
        self.tokenCheck('int')
        self.tokenCheck('(')
        self.tokenCheck('input')
        self.tokenCheck('(')
        self.tokenCheck(')')
        self.tokenCheck(')')

    def code_block(self):
        while self.currentToken.token in [ 'if', 'while', 'print', 'return', 'input'] or self.currentToken.tokenType == 'identifier':
            self.statements()

    def condition(self):
        self.bool_term()
        while self.currentToken.token == 'or':
            self.tokenCheck('or')
            self.bool_term()

    def bool_term(self):
        self.bool_factor()
        while self.currentToken.token == 'and':
            self.tokenCheck('and')
            self.bool_factor()

    def bool_factor(self):
        if self.currentToken.token == 'not':
            self.tokenCheck('not')
            self.condition()
        elif self.currentToken.token in ['<', '>', '==', '!=', '<=', '>=']:
            
            self.tokenCheck(self.currentToken.token)
            
            
           
        elif self.currentToken.tokenType == 'identifier':
            self.nextToken()
            self.condition()
        else:
            print(f"Syntax error: expected not, <, >, ==, !=, <=, >=, or identifier received {self.currentToken.token}")
            print(f"Line : {self.tokenIndex}")

    def expression(self):
        self.optional_sign()
        self.term()
        while self.currentToken.token in ['+', '-']:
            if self.currentToken.token == '+':
                self.tokenCheck('+')
            else:
                self.tokenCheck('-')
            self.term()

    def optional_sign(self):
        if self.currentToken.token == '+':
            self.tokenCheck('+')
        elif self.currentToken.token == '-':
            self.tokenCheck('-')
        else:
            print(f"Syntax error: expected + or - received {self.currentToken.token}")

    def term(self):
        self.factor()
        while self.currentToken.token in ['*', '/', '%']:
            if self.currentToken.token == '*':
                self.tokenCheck('*')
            elif self.currentToken.token == '//':
                self.tokenCheck('//')
            else:
                self.tokenCheck('%')
            self.factor()

    def factor(self):
        if self.currentToken.tokenType in ['identifier', 'number']:
            self.tokenCheck(self.currentToken.token)
        elif self.currentToken.token == '(':
            self.tokenCheck('(')
            self.expression()
            self.tokenCheck(')')
        else:
            print(f"Syntax error: expected identifier, number, or ( received {self.currentToken.token}")
            print(f"Line : {self.currentToken.token}")
    
    def syntaxCorect(self):
        if self.currentToken.tokenType == 'EOF':
            print('\n\nSyntax is correct\n\n')

# Example usage
lex = LexicalAnalyzer('test.cpy')   
tokens = lex.lexical_analyzer()
syntax = SyntaxAnalyzer(tokens)
syntax.startRule()

  
##------------------------------------ Main ------------------------------------##
lex = LexicalAnalyzer('./test.cpy')   
tokens = lex.lexical_analyzer()
#print(tokens)

# for token in tokens:
#     print(token.token, token.tokenType)

tokensList = []
for token in tokens:
    # Append the token name (token) to the first column
    tokensList.append([token.token, token.tokenType])
print(tokensList)
syntax = SyntaxAnalyzer(tokens)
syntax.startRule()
print("\n\n%d"%syntax.tokenIndex)
#syntax.syntaxCorect()
# print(tokensList)
