def arithmetic_arranger(self):


    for i in self:
        # Removes blank space before continuing
        i = i.replace(" ", "")
        #Checks if there are more than 5 problems to the function
        if len(self) > 5:
            print("Error: Too many problems")
            break
        #Checks if there is a division operation in the arguments
        elif "/" in i:
            print("Error:Operator must be either '+' or '-' ")
            break
        #checks if there is a multiplication operation in the arguments
        elif "*" in i:
            print("Error:Operator must be either '+' or '-' ")
            break
        #Checks if there is a + operator.
        elif "+" in i:
            n = i.index("+")
            # Separates operand1 and operand2 based on the index of the operator
            num1 = int(i[0:n])
            num2 = int(i[n + 1:])
            # Prints the equation
            print(' ', num1, '\n', '+', num2, '\n______\n ', num1 + num2, "\n", sep='')
        # Checks if there is a - operator.
        elif "-" in i:
            # Separates operand1 and operand2 based on the index of the operator
            n = i.index("-")
            num1 = int(i[0:n])
            num2 = int(i[n + 1:])
            # Prints the equation
            print(' ', num1, '\n', '-', num2, '\n______\n ', num1 - num2, "\n", sep='')



    return " "

formula = arithmetic_arranger(['2*2'])
print(formula)
# formula2 = arithmetic_arranger(["320 - 5"])
# print(formula2)