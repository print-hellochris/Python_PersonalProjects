class Category:
    def __init__(self,name):
        self.name = name
        
        self.ledger =[]
        self.deposits=[]
        self.withdrawals=[]
        
    def __str__(self): 

        n = int((30 - len(self.name))/2) #n - number of asterisks       
        num_asterisks = '*' * n    
        headline = num_asterisks+self.name+num_asterisks+'\n'
        line = ''        
        num_spaces = 0
        display = headline+line
        
        for transactions in self.ledger:
            
            amount = float(self.get_balance())
            total = f'Total: {amount:.2f}'
            white_space = ''            
            description = transactions['description']
            amount = transactions['amount']          
            length_description = len(description)
               
            if length_description > 23:
                length_description = 23
                description = description[0:length_description]    

            amount_float = float(amount) 
            amount_str = '{:.2f}'.format(amount_float) # Adds two decimal numbers
            num_spaces = 30 - (length_description + len(amount_str))
            for i in range(num_spaces):
                white_space += ' '
            line = f'{description}{white_space}{amount_str}\n'
            display +=line
            display
        display +=total
        return display       
        
    def deposit (self, amount, description=''):
        '''A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.'''              
        self.ledger.append(dict(amount=amount, description=description))
        self.deposits.append(amount)       
        return True
    
    def withdraw (self, amount, description=''): 
        '''A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.'''
        if self.check_funds(amount):           
            self.ledger.append(dict(amount=amount*-1, description=description))
            self.withdrawals.append(amount)            
            return True
        else:
            return False

    def get_balance(self):
        '''A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.'''        
        balance = 0
        for amount in self.ledger:
            balance += amount['amount']
        return balance
      
    def transfer (self, amount, other_category):
        '''A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.'''
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to '+ other_category.name)
            other_category.deposit(amount,'Transfer from '+self.name)
            return True
        else: 
            return False

    def check_funds(self,amount):
        '''A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.'''
        if amount > self.get_balance():
            return False
        else:
            return True
def create_spend_chart(category):
    zero_line = '  0|'
    separator = '  '
    dashes = '-'
    white_space = ' '
    margin = '    '
    lower_margin= '     '
    zero_line_dashes = margin+'-'
    ten_line = ' 10|'
    twenty_line= ' 20|'
    thirty_line= ' 30|'
    forty_line= ' 40|'
    fifty_line = ' 50|'
    sixty_line = ' 60|'
    seventy_line = ' 70|'
    eighty_line = ' 80|'
    ninety_line = ' 90|'
    hundred_line = '100|'
    title = 'Percentage spent by category'
    lista = [zero_line,ten_line,twenty_line,thirty_line,forty_line,fifty_line,sixty_line,seventy_line,eighty_line,ninety_line,hundred_line]    
    index = lista.index(zero_line)    
#___Variables for the for loops
    all_expenses = []
    how_many_os =0
    percentages =[]
    all_withdrawals =0
    withdrawal = 0 
#___Loop in items of category to get each withdrawals, total sum and percentage
    for items in category: 

#_______How many withdrawals were made in total by each item? 
        withdrawal = sum(items.withdrawals)
#_______Adding each withdrawal to this list        
        all_expenses.append(withdrawal)        
#___All_withdrawals equals 100% of the withdrawals
    all_withdrawals = sum(all_expenses)
    total_percents = []
    os_list = [] 

    for withdrawals in all_expenses:
        percentage_spent = (withdrawals * 100) / all_withdrawals
        how_many_os = (percentage_spent/10)
        if how_many_os >1:
            how_many_os = int((percentage_spent / 10)+1)    
        else:
            how_many_os = 1 

        for i in range(index, int(how_many_os)):     
            #   spaces = ' '     
            
            if i > index:      
                if 'o' in lista[i]:
                    lista[i].replace('   ', '')
                else:          
                    lista[i] = lista[i] +'   '
                
            lista[i] +=' o '
            
            
    length_category = len(category)        
    for indices in lista:
        difference = (length_category*2) +4
        idxs = lista.index(indices)
        if 'o' in indices:
            lista[idxs] += 'ç' *(difference - len(indices)+4)
            
        if 'o' not in indices:                       
            lista[idxs] += 's' *((length_category*2)+4)
        
            
                # elif 'o' in lista:
            # lista[idx] = ' ' * (difference - len(indices)
    

    lista[0] +=' '
    lista.reverse()
    display = '\n'.join(lista)
    length_category = len(category)    
#___Adjusting the dashes size
    for i in range(length_category):
        zero_line_dashes = margin+'-' *((length_category*2)+4) 
    
    output = title+'\n'+display+'\n'+zero_line_dashes
    letters_list = []
    vertical_words = ['\n']   
    longest_length = 0
    lengths = []
#___Turns each letter in category.name into a list of strings
    for words in category:        
#_______Creates a list from the category.name
        category_names = words.name
        category_names = category_names.capitalize()
        letters = list(category_names)
#_______
        lengths.append((len(words.name)))
#_______Creates a list of lists
        letters_list.append(letters)
#____Finds the longest length of this new list
#___ Deixar de fora do loop para fazer a consulta apenas uma vez.    
    longest_length = max(lengths)
    

    for idx in range(longest_length):
        vertical_words.append(lower_margin)
        for letters in letters_list:            
            if len(letters) > idx:                
                vertical_words.append(letters[idx])
                vertical_words.append('  ')                
            else:
                vertical_words.append(' ')
                vertical_words.append('  ')
               
        
        vertical_words.append('\n')
    vertical_words.pop()
    vertical_display = ''.join(vertical_words)
    output+=vertical_display
        
    return output




food = Category('food')
business = Category('business')
entertainment = Category('entertainment')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
# print(create_spend_chart([food,business]))
# print(business)



# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")

# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)

# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)
# print(auto)

# print(create_spend_chart([food, clothing, auto]))

# Food = Category('Food')
# Money = Category('Money')
# dip =Category('Dip')
# Do = Category('Do')
# Food.deposit(900,'Salário')
# Food.withdraw(200,'Compras semanais')
# Food.deposit(50, 'Groceries')
# Food.withdraw(100, 'Comission')
# Food.deposit(50, 'Bribe')
# Food.transfer(100, Money)
# # print(Food)
# Money.deposit(1000,'Initial deposit')
# Money.deposit(100, 'Bribes')
# Money.withdraw(200,'Bills')
# Do.deposit(1000,'Initial deposit')
# Do.deposit(100, 'Bribes')
# Do.withdraw(200,'Bills')
# # print(Food)
# print(create_spend_chart([Food,Money,Do]))


