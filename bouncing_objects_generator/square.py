import math
import random

from PIL import ImageDraw

from bouncing_objects_generator.object import Object


class Square(Object):
    def update(self):
        if self._position_x is None or self._position_y is None:
            self._init_position()

        temp_x = self._position_x
        temp_y = self._position_y

        temp_x += math.cos(math.radians(self._degree)) * self._speed
        temp_y -= math.sin(math.radians(self._degree)) * self._speed

        while self._is_overwrapped(temp_x, temp_y):
            if self._degree in range(0, 91):
                if temp_y < 0:
                    temp_y *= -1
                    self._reflect_horizontally()
                if temp_x > self._available_x_range[-1]:
                    temp_x -= (temp_x - self._available_x_range[-1])
                    self._reflect_vertically()
            elif self._degree in range(90, 181):
                if temp_y < 0:
                    temp_y *= -1
                    self._reflect_horizontally()
                if temp_x < 0:
                    temp_x *= -1
                    self._reflect_vertically()
            elif self._degree in range(180, 271):
                if temp_y > self._available_y_range[-1]:
                    temp_y -= (temp_y - self._available_y_range[-1])
                    self._reflect_horizontally()
                if temp_x < 0:
                    temp_x *= -1
                    self._reflect_vertically()
            elif self._degree in range(270, 361):
                if temp_y > self._available_y_range[-1]:
                    temp_y -= (temp_y - self._available_y_range[-1])
                    self._reflect_horizontally()
                if temp_x > self._available_x_range[-1]:
                    temp_x -= (temp_x - self._available_x_range[-1])
                    self._reflect_vertically()

        self._position_x = temp_x
        self._position_y = temp_y

    def draw(self, draw: ImageDraw):
        draw.rectangle(
            (self._position_x, self.position_y,
             self._position_x + self._width, self._position_y + self._height),
            fill=255, outline=None)

    @property
    def position_x(self):
        return self._position_x

    @property
    def position_y(self):
        return self._position_y

    def _init_position(self):
        self._position_x = random.choice(self._available_x_range)
        self._position_y = random.choice(self._available_y_range)

    def _is_overwrapped(self, x, y):
        x_is_overwrapped = x < self._available_x_range[0] or self._available_x_range[-1] < x
        y_is_overwrapped = y < self._available_y_range[0] or self._available_y_range[-1] < y
        return x_is_overwrapped or y_is_overwrapped
