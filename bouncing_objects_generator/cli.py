import argparse
import random
import sys

import numpy as np

from bouncing_objects_generator.frame import Frame
from bouncing_objects_generator.square import Square


class Cli:

    @classmethod
    def run(cls, frame_width: int, frame_height: int,
            object_width: int, object_height: int, objects_size: int,
            frames_per_window: int, window_size: int, npy_output: str):

        frame = Frame(width=frame_width, height=frame_height)
        for _ in range(objects_size):
            frame.register_object(
                Square(width=object_width, height=object_height,
                       frame_width=frame.width, frame_height=frame.height,
                       degree=random.choice(range(0, 360)),
                       speed=random.choice(range(1, 20)))
            )

        all_windows = []
        window_shape = (frames_per_window, 1, frame_height, frame_width)
        for i in range(window_size):
            sys.stderr.write(f'{i + 1}/{window_size}\r')
            sys.stderr.flush()

            window = None
            for _ in range(frames_per_window):
                image = np.asarray(frame.draw(), dtype=np.uint8).reshape(1, frame_height, frame_width)
                if window is None:
                    window = image
                else:
                    window = np.vstack((window, image))

            all_windows.append(window.reshape(window_shape[0], window_shape[1], window_shape[2], window_shape[3]))
        sys.stderr.write('\n')
        np.save(npy_output, np.concatenate(all_windows, axis=1))


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
