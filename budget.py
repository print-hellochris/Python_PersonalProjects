class category:
    def __init__(self,name):
        self.name = name
        self.ledger = []  
        self.amounts =[]
        self.deposits=[]
        self.withdrawals=[]
            
        
    def __str__(self): 

        n = int((30 - len(self.name))/2) #n - number of asterisks       
        num_asterisks = '*' * n    
        headline = num_asterisks+self.name+num_asterisks+'\n'
        line = ''
        
        num_spaces = 0
        display = headline+line
        
        for i in self.ledger:
            
            value = float(self.get_balance())
            total = f'Total: {value:.2f}'
            white_space = ''
#___________ Finds index for description and amount
            index_description = i.rfind(':')
            index_amount = i.index(':')
#___________Slices description in separate variable
            description = i[index_description+1:]
            length_description = len(description)
#___________Slices amount in a separate variable
            comma = i.index(',')           
            amount = i[index_amount+1:comma]
               
            if length_description > 23:
                length_description = 23
                description = description[0:length_description]    

            amount = float(amount) # Converts amount (Str) to Float()
            amount = '{:.2f}'.format(amount) # Adds two decimal numbers                     
            num_spaces = 30 - (length_description + len(amount)) 
                     
            for i in range(num_spaces):
                white_space += ' '

            line = f'{description}{white_space}{amount}\n'
            display +=line
            display
        display +=total
        return display       
        
    def deposit (self, amount, description=''):
        '''A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.'''
              
        self.amounts.append(amount)
        self.deposits.append(amount)
        self.ledger.append(f'amount:{amount}, description:{description}')
        
        return True
    
    def withdraw (self, amount, description=''): 
        '''A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.'''
        if self.check_funds(amount):
            self.ledger.append(f'amount:{amount*-1}, description:{description}')
            self.amounts.append(amount*-1)
            self.withdrawals.append(amount)
            
            return True
        else:
            return False        
    
    def get_balance(self):
        '''A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.'''
      
        balance = sum(self.amounts)
        return balance
      
    def transfer (self, amount, other_category):
        '''A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.'''
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to '+ other_category.name)
            other_category.deposit(amount,'Transfer from'+self.name)
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

    for items in category:
        withdrawal = sum(items.withdrawals)
        deposits = sum(items.deposits)
        percentage_spent = (withdrawal * 100) / deposits

        how_many_os = percentage_spent / 10  
        for i in range(index, int(how_many_os)):
            lista[i] = lista[i]+' o'        
#___Post parsing    
    lista.reverse()
    display = '\n'.join(lista)
    length_category = len(category)
#___Adjusting the dashes size
    for i in range(length_category):
        zero_line_dashes = margin+'-' *((length_category*2)+2)
    output = title+'\n'+display+'\n'+zero_line_dashes

#___Now for the 'fun' part
    for words in category:
        i = 0
       
     
        
    return output


Food = category('Food')
Money = category('Money')
dip =category('Dip')
Do = category('Do')
print(Food.deposit(900,'Salário'))
print(Food.withdraw(200,'Compras semanais'))
print(Food.deposit(50, 'Groceries'))
print(Food.withdraw(100, 'Comission'))
print(Food.deposit(50, 'Bribe'))
print(Food.transfer(100, Money))
Money.deposit(1000,'Initial deposit')
Money.deposit(100, 'Bribes')
Money.withdraw(200,'Bills')
Do.deposit(1000,'Initial deposit')
Do.deposit(100, 'Bribes')
Do.withdraw(200,'Bills')
# print(Food)
print(create_spend_chart([Food,Money,Do]))





