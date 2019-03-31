from PIL import ImageDraw


class Object:
    def __init__(self, width: int, height: int,
                 frame_width: int, frame_height: int,
                 degree: float, speed: float = 10.0):
        self._width = width
        self._height = height
        self._frame_width = frame_width
        self._frame_height = frame_height
        self._available_x_range = range(0, self._frame_width - self._width + 1)
        self._available_y_range = range(0, self._frame_height - self._height + 1)

        self._degree = degree
        self._speed = speed
        self._position_x = None
        self._position_y = None

    def update(self):
        raise NotImplementedError

    def draw(self, draw: ImageDraw):
        raise NotImplementedError

    def _reflect_vertically(self):
        if self._degree not in [0.0, 180.0]:
            self._degree = 180.0 - self._degree
        else:
            self._degree += 180.0
        self._degree %= 360

    def _reflect_horizontally(self):
        if self._degree not in [90.0, 270.0]:
            self._degree = 360.0 - self._degree
        else:
            self._degree += 180.0
        self._degree %= 360
