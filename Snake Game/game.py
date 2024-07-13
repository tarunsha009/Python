from collections import deque
import random

class SnakeGame:

    def __init__(self, width = 10, height = 10):
        self.width = width
        self.height = height
        self.snake = deque([(0,0)])
        self.food = self.place_food()
        self.direction = (0,1)


    def place_food(self):
        while True:
            x = random.randint(0 , self.width -1)
            y = random.randint(0, self.height - 1)

            if (x, y) not in self.snake:
                return (x, y)


    def change_direction(self, new_direction):
        self.direction = new_direction
