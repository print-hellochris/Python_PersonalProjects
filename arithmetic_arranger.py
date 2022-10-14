def arithmetic_arranger(self):

    for i in self:

        i = i.replace(" ", "")

        if "+" in i:
            n = i.index("+")
            num1 = int(i[0:n])
            num2 = int(i[n + 1:])
            result = num1 + num2

            print(' ', num1, '\n', '+', num2, '\n______\n ', num1 + num2, "\n", sep='')

            # return " "

        elif "-" in i:
            n = i.index("-")
            num1 = int(i[0:n])
            num2 = int(i[n + 1:])
            print(' ', num1, '\n', '-', num2, '\n______\n ', num1 - num2, "\n", sep='')
            # return " "

    return " "

formula = arithmetic_arranger(["1500 +50", "320-5", "7-6"])
print(formula)
# formula2 = arithmetic_arranger(["320 - 5"])
# print(formula2)