from collections import deque


class MazeUtils:

    @staticmethod
    def find_start(grid):

        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows):

            for x in range(cols):

                if grid[y][x] == 0:

                    return x, y

        return 1, 1
    
    @staticmethod
    def bfs_farthest_cell(
            grid,
            start_x,
            start_y
    ):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        queue.append(
            (start_x, start_y)
        )

        visited = set()

        visited.add(
            (start_x, start_y)
        )

        farthest = (
            start_x,
            start_y
        )

        while queue:

            x, y = queue.popleft()

            farthest = (
                x,
                y
            )

            directions = [

                (1, 0),
                (-1, 0),

                (0, 1),
                (0, -1)
            ]

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if (

                    0 <= nx < cols

                    and

                    0 <= ny < rows

                    and

                    grid[ny][nx] == 0

                    and

                    (nx, ny)
                    not in visited

                ):

                    visited.add(
                        (nx, ny)
                    )

                    queue.append(
                        (nx, ny)
                    )

        return farthest
    
    @staticmethod
    def find_best_exit(
            grid,
            start_x,
            start_y
    ):

        return MazeUtils.bfs_farthest_cell(

            grid,

            start_x,

            start_y
        )