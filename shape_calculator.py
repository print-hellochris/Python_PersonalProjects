'''

eif an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)


'''

class Rectangle: 
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle(width={self.width},height={self.height})'
    def set_width(self,new_width):
        pass
    
    def set_height(self,new_height):
        pass


    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return ((2*self.width) + (2*self.height))
    def get_diagonal(self): #Posso arredondar o resultado
        return (((self.width ** 2) + (self.height ** 2)) ** .5)
    def get_picture(self):
        
        output = ''
        line=''
        # line = '*' * self.width
        # line += '\n'
        line_list = []
        line_list = list(line)
        for i in range(self.width):  
            
            line +='*'
        
        line +='\n'

       
            
        # return output = ''.join(line_list)

 
        # for i in range(self.width):
        #     output +='*'
        # for i in range(self.height):
        #     output += '*'
        # output+='\n'
        
        return output
       
    # def get_amount_inside(self):
    #     pass

# class Square (Rectangle(width, height)):
#     pass

a = Rectangle(width=5, height=4)
print(a)
# print(a.get_area())
# print(a.get_perimeter())
# print(a.get_diagonal())
print(a.get_picture())
