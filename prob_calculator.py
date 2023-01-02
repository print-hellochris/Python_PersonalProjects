import copy
import random

class Hat:
      def __init__(self, **kwargs):        
        self.contents = []   
        self.total_number_balls = sum( kwargs.values())
        self.list_keys = list(kwargs.keys())
        self.dict = dict(kwargs)
        for keys in kwargs:
            num_balls = kwargs[keys]
            colour_name = keys
            for balls in range(num_balls):
                self.contents.append(colour_name) 
         
    
      def draw (self,num_balls):
        #_______Remove balls at random from the hat      
        
        content_copy = self.contents.copy()
        random_balls_list = []
        ball_drawn = ''

        for draws in range(num_balls):
          if num_balls < len(self.contents):
            ball_drawn = random.choice(self.contents)                        
            random_balls_list.append(ball_drawn)
            self.contents.remove(ball_drawn)
          else:
            self.contents = content_copy
          
          
        return random_balls_list

def experiment (hat,num_balls_drawn,num_experiments,expected_balls):
# def experiment (hat=None,num_balls_drawn=None,num_experiments=None,expected_balls=None):
    event = 0
    total_trials =0
    draws = []
    sum_expected_values = sum(expected_balls.values())
    
    for trials in range(num_experiments):
      
        draws= hat.draw(num_balls=num_balls_drawn)        
        for keys in draws: 
            values = draws.count(keys)
            for expected_keys,expected_values in expected_balls.items():
              if keys == expected_keys and values >= expected_values:
                total_trials +=1
                print(total_trials)
        if total_trials >= sum_expected_values:
          event += 1
          total_trials = 0
                   
        else:
          total_trials = 0
          
      
    
    return total_trials, sum_expected_values

Hat = Hat(blue=3,red=2,green=6)

print(experiment(hat=Hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
