import cv2

class ImageProcessor:

    def __init__(self, image_path):

        self.image_path = image_path

        self.original = None

        self.gray = None

        self.blur = None

        self.binary = None

    def load_image(self):

        self.original = cv2.imread(self.image_path)

        if self.original is None:

            raise FileNotFoundError(
                f"Image not found: {self.image_path}"
            )

        return self.original

    def convert_to_gray(self):

        self.gray = cv2.cvtColor(
            self.original,
            cv2.COLOR_BGR2GRAY
        )

        return self.gray

    def remove_noise(self):

        self.blur = cv2.GaussianBlur(
            self.gray,
            (5, 5),
            0
        )

        return self.blur

    def threshold_image(self):

        self.binary = cv2.adaptiveThreshold(
            self.blur,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        return self.binary

    def invert_image(self):

        self.binary = cv2.bitwise_not(
            self.binary
        )

        return self.binary

    def process(self):

        self.load_image()

        self.convert_to_gray()

        self.remove_noise()

        self.threshold_image()

        self.invert_image()

        return self.binary