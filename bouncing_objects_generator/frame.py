from PIL import Image, ImageDraw

from bouncing_objects_generator.object import Object


class Frame:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._objects = []
        self._base_frame = Image.new('L',
                                     (self._width, self._height),
                                     0)

    def register_object(self, obj: Object):
        self._objects.append(obj)

    def draw(self) -> Image:
        frame = self._base_frame.copy()
        draw = ImageDraw.Draw(frame)
        for obj in self._objects:
            obj.update()
            obj.draw(draw)

        return frame

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
