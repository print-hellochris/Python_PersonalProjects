


def arithmetic_arranger(self):
    if len(self)>5:
        return 'Error: Too many problems'        
    else:
        for each_index in self:
            if '+' in each_index:
                operator = '+'
            elif '-' in each_index:
                operator = '-'
            else: 
                return 'Error: Operator must either be + or -'
            
            n = each_index.index(operator)
            operand_one = each_index[0:n]
            operand_two = each_index[n+1:]
            combinedoperands = operand_one+operand_two
            num1 = int(operand_one)
            num2 = int(operand_two)

            if combinedoperands.isdigit() == False:
                return ' Numbers must only contain digits'
                break
            if len(operand_one) >4:
                return 'Numbers cannot be more than four digits'
                break
            elif len(operand_two)>4:
                return 'Numbers cannot be more than four digits'
                break
            
            if operator =='+':
                addition = num1+num2
                result = str(addition)
            elif operator =='-':
                subtraction = num1-num2
                result(str(subtraction))

            left_margin = ' '            
            slashn = '\n'
            whitespace =''
            left_space =''

            if len(operand_one) > len(operand_two):
                difference = len(operand_one)-len(operand_two)
                whitespace = ' '*difference

            elif len(operand_one) < len(operand_two):
                difference = len(operand_two)-len(operand_one)
                left_space = ' '*difference
            
            line_one = left_margin+left_space+operand_one
            line_two = slashn+operator+whitespace+operand_two
            dashes = '_'*len(line_two)
            line_three = slashn+dashes
            line_four= slashn+left_margin+result
           
            output = '{0}{1}{2}{3}'.format(line_one,line_two,line_three,line_four)
            
            return output        
     
    return ' '


print(arithmetic_arranger(['600+3000', '30+7', '800-400']))