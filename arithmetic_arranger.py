def arithmetic_arranger(self,show_answer=False):

    

#---Checks if the length of the list is larger than 5. 
    if len(self)>5:
        return 'Error: Too many problems.'        
    row_one = [ ]
    new_line= ['\n']
    row_two = [ ]
    row_three = [ ]
    row_four = [ ]
    rows_combined =[]
    minus = 0
    
 #--Beginning of the For Loop   
    for each_index in self:
        each_index = each_index.replace(' ','')
 #------If/else block, the operator will have different values depending on which operator is present in the string.       
        if '+' in each_index:
            operator = '+'
        elif '-' in each_index:
            operator = '-'
        else: 
            return "Error: Operator must be '+' or '-'."
        n = each_index.index(operator)
        operand_one = each_index[0:n]
        operand_two = each_index[n+1:]
        combinedoperands = operand_one+operand_two
#-------Checks if the operands have only digits.
        if combinedoperands.isdigit() == False:
            return 'Error: Numbers must only contain digits.'
            break
    #-------Assigning the variables to compose the operands and result.        
        
        
        
        num1 = int(operand_one)
        num2 = int(operand_two)
#-------Checks operands lengths
        if len(operand_one) >4:
            return 'Error: Numbers cannot be more than four digits.'
            break
        elif len(operand_two)>4:
            return 'Error: Numbers cannot be more than four digits.'
            break
#------Based on the value of the operator, the operation will change.        
        if operator =='+':
            addition = num1+num2
            result = str(addition)
            
        elif operator =='-':
            minus = num1-num2
            # if num1>num2:
            #     minus = num1-num2
            # else:
            #     minus = num2-num1
            result=str(minus)
#-------Assigning variables that will compose the display of the problem.            

        left_margin = ' '            
        
        whitespace =''
        left_space =''
        space = ' '
        margin = ' '
        line_four_margin = ' '
        
        
#------If/else block to adjust the formating of the output depending on the length of the smaller operand.
        
        if len(operand_one) == len(operand_two):
            line_four_margin = ' '*len(operand_one)
        
        # elif len(result) > len(operand_one):
        #     line_four_margin =' '
       
        elif len(operand_one) > len(operand_two):
            difference = len(operand_one)-len(operand_two)
            whitespace = ' '*difference
            if len(result) == len(operand_one):
                line_four_margin = ' '*len(operand_two)
            elif len(result) == len(operand_one)+1:
                line_four_margin = ' '
        
        elif len(operand_one) < len(operand_two):
            difference = len(operand_two)-len(operand_one)
            left_space = ' '*difference
            if minus < 0:
                line_four_margin = ' '
            else:
                line_four_margin = '  '


        
        
            
 #------Assigning variables to compose the output (display of the problem)       
        separator='    '
        line_one = space+left_margin+left_space+operand_one
        line_two = operator+space+whitespace+operand_two
        dashes = '-'*len(line_two)
        line_three = dashes
        # line_four= space+margin+result
        line_four = line_four_margin+result
        # line_four= line_four_margin+result
        
        row_one.append(line_one)
        row_one.append(separator)
        
        row_two.append(line_two)
        row_two.append(separator)
        
        row_three.append(line_three)
        row_three.append(separator)
        
        row_four.append(line_four)
        row_four.append(separator)

        # rows_combined = row_one+new_line+row_two+new_line+row_three+new_line+row_four
        
        
        # rows_combined.pop()
       
        # display = ''.join(rows_combined)     
        # display = display.replace('    \n','\n')  

        if show_answer == True:
            rows_combined = row_one+new_line+row_two+new_line+row_three+new_line+row_four
            rows_combined.pop()
            display = ''.join(rows_combined)     
            display = display.replace('    \n','\n')  
            # rows_combined = row_one+new_line+row_two+new_line+row_three+new_line+row_four
            # rows_combined.pop()       
            # display = ''.join(rows_combined)     
            # display = display.replace('    \n','\n')  
        else:
            rows_combined = row_one+new_line+row_two+new_line+row_three
            rows_combined.pop()       
            display = ''.join(rows_combined)     
            display = display.replace('    \n','\n') 
                       
    return display

# print(arithmetic_arranger(["32 + 8u", "2 - 3801", "9999 + 9999", "523 - 4999"]))
# print(arithmetic_arranger(["2 - 3801",'4000+5']))
# print( '  3801      123\n-    2    +  49\n------    -----')
# print('  3801      123\n-    2    +  49\n------    -----\n  3799      172')
# print('  3801      123\n-    2    +  49\n------    -----')
# print(arithmetic_arranger([  '123 + 49', '988 + 40'], True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print('==================================================')
print(arithmetic_arranger(["3 + 855", "988 + 40"],True))

