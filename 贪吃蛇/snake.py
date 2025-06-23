from config import GRID_WIDTH, GRID_HEIGHT

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = RIGHT
        self.grow_flag = False

    def set_direction(self, new_dir):
        # 防止反向
        if (new_dir[0] + self.direction[0], new_dir[1] + self.direction[1]) != (0, 0):
            self.direction = new_dir

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def grow(self):
        self.grow_flag = True

    def hit_wall(self):
        head = self.body[0]
        return (
            head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT
        )

    def hit_self(self):
        return self.body[0] in self.body[1:] 