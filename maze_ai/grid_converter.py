import numpy as np


class GridConverter:

    def __init__(self, binary_image):

        self.binary_image = binary_image

        self.grid = None

    def image_to_grid(
            self,
            cell_size=8,
            wall_threshold=0.25
    ):

        height, width = self.binary_image.shape

        rows = height // cell_size
        cols = width // cell_size

        grid = []

        for row in range(rows):

            grid_row = []

            for col in range(cols):

                y1 = row * cell_size
                y2 = y1 + cell_size

                x1 = col * cell_size
                x2 = x1 + cell_size

                block = self.binary_image[
                    y1:y2,
                    x1:x2
                ]

                white_pixels = np.sum(
                    block == 255
                )

                total_pixels = (
                    block.shape[0] *
                    block.shape[1]
                )

                ratio = (
                    white_pixels /
                    total_pixels
                )

                if ratio > wall_threshold:
                    grid_row.append(1)
                else:
                    grid_row.append(0)

            grid.append(grid_row)

        self.grid = grid

        return grid

    def print_grid(self):

        if self.grid is None:
            return

        for row in self.grid:

            print(
                "".join(
                    str(cell)
                    for cell in row
                )
            )