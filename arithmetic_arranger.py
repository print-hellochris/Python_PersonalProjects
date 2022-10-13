def arithmetic_arranger(a):
    a = a.replace(" ", "")



    if "+" in a:
        n = a.index("+")
        num1 = int(a[0:n])
        num2 = int(a[n + 1:])
        result = num1 + num2

        print(' ', num1, '\n', '+', num2, '\n______\n ', num1 + num2, sep='')

        return " "

    elif "-" in a:
        n = a.index("-")
        num1 = int(a[0:n])
        num2 = int(a[n + 1:])
        print(' ', num1, '\n', '-', num2, '\n______\n ', num1 - num2, sep='')
        return " "

formula = arithmetic_arranger("1500 +50")
print(formula)
formula2 = arithmetic_arranger("320 - 5")
print(formula2)