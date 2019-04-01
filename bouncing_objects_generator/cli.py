import argparse
import random

import numpy as np

from bouncing_objects_generator.frame import Frame
from bouncing_objects_generator.square import Square


class Cli:

    @classmethod
    def run(cls, frame_width: int, frame_height: int,
            object_width: int, object_height: int, objects_size: int,
            frames_per_window: int, window_size: int, npy_output: str):

        frame = Frame(width=frame_width, height=frame_height)
        all_windows = None
        for _ in range(objects_size):
            frame.register_object(
                Square(width=object_width, height=object_height,
                       frame_width=frame.width, frame_height=frame.height,
                       degree=random.choice(range(0, 360)),
                       speed=random.choice(range(1, 20)))
            )

        for _ in range(window_size):
            window = None
            for _ in range(frames_per_window):
                image = np.asarray(frame.draw(), dtype=np.uint8).reshape(1, frame_height, frame_width)
                if window is None:
                    window = image
                else:
                    window = np.vstack((window, image))

            window_shape = window.shape
            if all_windows is None:
                all_windows = window.reshape(1, window_shape[0], window_shape[1], window_shape[2])
            else:
                all_windows = np.vstack((all_windows,
                                         window.reshape(1, window_shape[0], window_shape[1],
                                                        window_shape[2])))
        all_windows = all_windows.transpose(1, 0, 2, 3)
        np.save(npy_output, all_windows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame_width', type=int, default=128)
    parser.add_argument('--frame_height', type=int, default=128)
    parser.add_argument('--object_width', type=int, default=32)
    parser.add_argument('--object_height', type=int, default=32)
    parser.add_argument('--frames_per_window', type=int, default=20)
    parser.add_argument('--window_size', type=int, default=100)
    parser.add_argument('--objects_size', type=int, default=3)
    parser.add_argument('--npy_output', type=str, default='bouncing_objects.npy')
    args = parser.parse_args()
    Cli.run(**vars(args))


if __name__ == '__main__':
    main()
