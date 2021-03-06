# bouncing_objects_generator
- This is a CLI tool to generate bouncing objects images dataset like [Moving MNIST](http://www.cs.toronto.edu/~nitish/unsupervised_video/)
- This tool outputs generated images as npy format

![](example.gif)

# usage
```sh
$ git clone git@github.com:serihiro/bouncing_objects_generator.git
$ cd bouncing_objects_generator
$ pip install -e .
$ bouncing_objects_generator
```

## options

```sh
$ bouncing_objects_generator --help
  usage: bouncing_objects_generator [-h] [--frame_width FRAME_WIDTH]
                                    [--frame_height FRAME_HEIGHT]
                                    [--object_width OBJECT_WIDTH]
                                    [--object_height OBJECT_HEIGHT]
                                    [--frames_per_window FRAMES_PER_WINDOW]
                                    [--window_size WINDOW_SIZE]
                                    [--objects_size OBJECTS_SIZE]
                                    [--npy_output NPY_OUTPUT]
```

# requirements
- python >= 3.6
- numpy >= 1.15
- pillow >= 5.0

# LICENSE
MIT
