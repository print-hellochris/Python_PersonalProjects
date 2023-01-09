import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.total_number_balls = sum(kwargs.values())
        self.list_keys = list(kwargs.keys())
        self.dict = dict(kwargs)
        for keys in kwargs:
            num_balls = kwargs[keys]
            colour_name = keys
            for balls in range(num_balls):
                self.contents.append(colour_name)

    def draw(self, num_balls):
        # _______Remove balls at random from the hat

        content_copy = self.contents.copy()
        random_balls_list = []
        if num_balls > len(content_copy):
            self.contents = content_copy
        else:
            for draws in range(num_balls):
                ball_drawn = random.choice(self.contents)
                self.contents.remove(ball_drawn)
                random_balls_list.append(ball_drawn)

        # for draws in range(num_balls):
        #   if num_balls > len(content_copy):
        #     self.contents = content_copy
        #     break

        #   ball_drawn = random.choice(self.contents)
        #   self.contents.remove(ball_drawn)
        #   random_balls_list.append(ball_drawn)
        #   print(draws,self.contents)

        # if num_balls < len(content_copy):
        #   ball_drawn = random.choice(content_copy)
        #   random_balls_list.append(ball_drawn)
        #   content_copy.remove(ball_drawn)
        # else:
        #   self.contents = content_copy
        # if num_balls > len(content_copy):
        #   self.contents= content_copy

        # ball_drawn = random.choice(content_copy)
        # random_balls_list.append(ball_drawn)
        # content_copy.remove(ball_drawn)
        # self.contents.remove(ball_drawn)

        return random_balls_list


def experiment(hat, num_balls_drawn, num_experiments, expected_balls):
    # def experiment (hat=None,num_balls_drawn=None,num_experiments=None,expected_balls=None):
    for experiment in range(num_experiments):
        draw_balls = hat.draw(num_balls=num_balls_drawn)
        balls_value = 0
        correct_check = 0

        for balls in draw_balls:
            balls_value = draw_balls.count(balls)
            for expected_ball, expected_value in expected_balls.items():
                if balls == expected_ball:
                    if balls_value >= expected_value:
                        correct_check += 1
            #             print(
            #                 f"balls={balls}/ value drawn = {balls_value} and expected ball = {expected_ball}/ expected value = {expected_value}"
            #             )
            # print(draw_balls)
    print(draw_balls)
    return correct_check / num_experiments


# def experiment(hat, num_balls_drawn, num_experiments, expected_balls):
#     # def experiment (hat=None,num_balls_drawn=None,num_experiments=None,expected_balls=None):
#     event = 0
#     total_trials = 0
#     draws = []
#     sum_expected_values = sum(expected_balls.values())
#     sucess = True
#     failure = False

#     for trials in range(num_experiments):

#         draws = hat.draw(num_balls=num_balls_drawn)
#         copy_hat = draws.copy()

#         for keys in copy_hat:
#             values = copy_hat.count(keys)
#             for expected_keys, expected_values in expected_balls.items():

#                 if keys == expected_keys and values >= expected_values:
#                     print(sucess)
#                     # print(f'==========SUCESS==========\nTrial number {trials}:\nKey:{keys} | Value: {values} \nExpected Key: {expected_keys} | Expected Values: {expected_values}\nTotal trials = {total_trials}\n====================\n')
#                     total_trials += 1
#                 else:
#                     print(failure)

#                     # print(f'============FAILURE==========\nTrial number {trials}:\nKey:{keys} | Value: {values} \nExpected Key: {expected_keys} | Expected Values: {expected_values}\nTotal trials = {total_trials}\n====================\n')
#         if copy_hat == []:
#             copy_hat = hat

#         print(trials, total_trials, sum_expected_values)

#     # if total_trials >= sum_expected_values:
#     #   event += 1
#     #   total_trials = 0

#     # else:
#     #   total_trials = 0

#     return total_trials / num_experiments


Hat = Hat(blue=3, red=2, green=6)

print(
    experiment(
        hat=Hat,
        expected_balls={"blue": 2, "green": 1},
        num_balls_drawn=4,
        num_experiments=1000,
    )
)
