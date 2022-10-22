''' https://forum.freecodecamp.org/t/scientific-computing-with-python-projects-arithmetic-formatter/562679'''


def arithmetic_arranger(self):


    for i in self:
#--------------------- Removes blank space before continuing--------------------------------------------------------------
        i = i.replace(" ", "")
#---------------------Checks if there are more than 5 problems to the function-----------------------------------------------------------------------------
        if len(self) > 5:
            return "Error: Too many problems"
            break
#---------------------checks if there's a plus operator. I am working only with the Plus operator for now to see if I can get the problems displayed correctly.---------
        elif "+" in i:
            n = i.index("+")
            operator = '+'
#-------------------- Separates operand1 and operand2 based on the index of the operator------------------------------------------------------------------------------
            num1 = (i[0:n])
            num2 = (i[n + 1:])
            '''
            Checks the lengths of digits.
            '''
            if len(num1)>4:
                return 'Number {0} cannot be more than four digits'.format(num1)
                break
            else:
                operand_one = int(num1)            
            if len(num2)>4:
                return 'Number {0} cannot contain more than four digits'.format(num2)
                break
            else:
                operand_two = int(num2)
            #Creates a variable result that sums both operands. 
            result = operand_one+operand_two
        elif "-" in i:
            n = i.index("-")
            operator = '-'
#-------------------- Separates operand1 and operand2 based on the index of the operator------------------------------------------------------------------------------
            num1 = (i[0:n])
            num2 = (i[n + 1:])
                      
            if len(num1)>4:
                return 'Number {0} cannot be more than four digits'.format(num1)
                break
            else:
                operand_one = int(num1)            
            if len(num2)>4:
                return 'Number {0} cannot contain more than four digits'.format(num2)
                break
            else:
                operand_two = int(num2)
                #Creates a variable result that sums both operands. 
                result = operand_one-operand_two
        else:         
            
            return "Error:Operator in {0} must be either '+' or '-' .format(i)"
            break
        
        
        if len(num2) > len(num1):
            
            left_margin = ' '*len(num2)

        line_One = left_margin + num1
        output = '{line_One}\n{line_Two}\n{dashLine}\n{line_Three}'.format(line_One=line_One,line_Two=line_Two,dashLine=dashLine,line_Three=line_Three)
        return result
    #I added this empty string because the function kept returning None.
    
    
formula = arithmetic_arranger(['1+2'])
print(formula)
# formula2 = arithmetic_arranger(["320 - 5"])
# print(formula2)