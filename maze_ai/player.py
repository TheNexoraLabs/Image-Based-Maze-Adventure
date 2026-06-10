class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def move(self, dx, dy, grid):

        new_x = self.x + dx
        new_y = self.y + dy

        rows = len(grid)
        cols = len(grid[0])

        if (
            0 <= new_x < cols
            and
            0 <= new_y < rows
        ):

            if grid[new_y][new_x] == 0:

                self.x = new_x
                self.y = new_y

                return True

        return False


