from snake import UP, DOWN, LEFT, RIGHT
from config import GRID_WIDTH, GRID_HEIGHT

class SimpleSnakeAI:
    @staticmethod
    def get_direction(snake, food):
        head = snake.body[0]
        dx = food[0] - head[0]
        dy = food[1] - head[1]
        # 优先x方向靠近食物
        if dx != 0:
            new_dir = RIGHT if dx > 0 else LEFT
        elif dy != 0:
            new_dir = DOWN if dy > 0 else UP
        else:
            new_dir = snake.direction
        return new_dir

class SafeSnakeAI:
    @staticmethod
    def get_direction(snake, food):
        from collections import deque
        head = snake.body[0]
        body = snake.body[:]
        directions = [UP, DOWN, LEFT, RIGHT]
        width = GRID_WIDTH
        height = GRID_HEIGHT
        # BFS
        queue = deque()
        queue.append((head, []))
        visited = set()
        occupied = set(body)
        tail = body[-1]
        found_path = None
        while queue:
            pos, path = queue.popleft()
            if pos == food:
                found_path = path
                break
            for d in directions:
                next_pos = (pos[0] + d[0], pos[1] + d[1])
                if next_pos in visited:
                    continue
                # 允许走到当前蛇尾（因为下一步蛇尾会移动）
                if next_pos in occupied and next_pos != tail:
                    continue
                if not (0 <= next_pos[0] < width and 0 <= next_pos[1] < height):
                    continue
                visited.add(next_pos)
                queue.append((next_pos, path + [d]))
        if found_path and found_path:
            return found_path[0]
        # 没有安全路径，选择一个不撞墙/不撞自己的方向
        for d in directions:
            next_pos = (head[0] + d[0], head[1] + d[1])
            if next_pos not in occupied and 0 <= next_pos[0] < width and 0 <= next_pos[1] < height:
                return d
        # 实在没路，保持原方向
        return snake.direction 