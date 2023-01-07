class Rectangle: 
    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width},height={self.height})'

    def set_width(self,new_width):
        self.width = new_width       
    
    def set_height(self,new_height):
        self.height = new_height        

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return ((2*self.width) + (2*self.height))

    def get_diagonal(self): #Posso arredondar o resultado
        diagonal = (((self.width ** 2) + (self.height ** 2)) ** .5)
        round(diagonal,2)
        return diagonal
    def get_picture(self):
        output=''        
        if ((self.width) or (self.height)) > 50:
            return 'Too big for picture' 
        for each_step_height in range(self.height):
            for each_step_width in range(self.width):
                output +='*'
            output +='\n'
        return output 
       
    def get_amount_inside(shape):
        area = self.get_area()
        arg_area = shape.get_area()
        how_many_shapes_inside = area / arg_area
        return how_many_shapes_inside
        #How many times can the shape in the argument fit the main shape? 
    #     pass

class Square (Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.width = side
        Rectangle.height =side

    def __str__(self):
        return f'Square(side={self.side})'
    def set_side(self,new_side):
        self.side = new_side

    def set_width(self,new_width):
        self.width = side      
    
    def set_height(self,new_height):
        self.height = side 


sq = Square(2)
print(sq)

sq.width(4)
print(sq)