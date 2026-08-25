# Image Processing Tool

## Overview

This project implements a command-line image processing application in Python. Images are loaded into a beginner-friendly two-dimensional table of `introcs.RGB` objects, transformed by plug-in functions, and then saved back to image files.

The project combines nested lists, mutable objects, command-line arguments, dynamic function lookup, image manipulation, and plug-in architecture.

## Project Files

### `pictool.py`

`pictool.py` provides the application framework. It is responsible for:

- Loading images with Pillow
- Converting image pixels into two-dimensional lists of `introcs.RGB` objects
- Validating image buffers
- Saving processed images
- Parsing command-line arguments
- Reading optional plug-in parameters
- Looking up image-processing commands dynamically
- Running the selected plug-in

The application uses `hasattr()` and `getattr()` to locate functions in the `plugins` module by command name.

The general command-line format is:

```text
python3 pictool.py command [options] input [output]
```

### `plugins.py`

`plugins.py` contains the image-processing operations used by the application.

A valid plug-in function accepts an image buffer as its first parameter, provides default values for any additional parameters, and indicates whether it modified the image.

## Required Image Operations

### Monochrome and Sepia

`mono(image, sepia=False)` converts an image to greyscale or sepia.

Brightness is calculated from the RGB channels using:

```text
0.3 × red + 0.6 × green + 0.1 × blue
```

In greyscale mode, all three color channels are set to the calculated brightness.

In sepia mode:

- Red is set to the brightness.
- Green is set to 60% of the brightness.
- Blue is set to 40% of the brightness.

The alpha channel is preserved.

### Flip

`flip(image, vertical=False)` reflects an image.

By default, it flips the image horizontally. When `vertical=True`, it flips the image vertically.

The operation modifies the nested image list directly.

### Transpose

`transpose(image)` swaps the rows and columns of an image.

Because transposition changes the image dimensions, the function creates a transposed representation and then replaces the rows in the original image buffer.

For example, a 10 × 20 image becomes a 20 × 10 image.

### Rotate

`rotate(image, right=False)` rotates an image 90 degrees.

By default, the image rotates left. With `right=True`, it rotates right.

The function reuses the existing `transpose()` and `flip()` operations rather than duplicating the transformation logic.

## Additional Utilities

The plug-in module also contains supporting and optional operations.

`display(image)` prints pixel information for debugging without modifying the image.

`dered(image)` demonstrates image mutation by setting the red channel of every pixel to zero.

Specifications are also provided for advanced optional effects including:

- Vignetting
- Blurring
- Pixellation

These optional functions are left unimplemented in the supplied project code.

## Command-Line Options

The application supports plug-in options written in the form:

```text
--name=value
```

Option values are automatically converted to Python booleans, integers, or floating-point values when possible.

This allows commands to receive optional parameters such as:

```text
--sepia=True
--vertical=True
--right=True
```

## Image Representation

Internally, an image is represented as a nested list:

```text
image[row][column]
```

Each element is an `introcs.RGB` object containing red, green, blue, and alpha components.

This representation makes image processing an application of concepts used throughout the course, including nested lists, loops, mutable objects, and row/column transformations.

## Requirements

- Python 3
- Cornell `introcs` package
- Pillow (`PIL`)
- NumPy

## Concepts Demonstrated

- Image processing
- Nested lists and two-dimensional data
- RGB and alpha channels
- Mutable objects
- Nested loops
- Row and column transformations
- Command-line applications
- `sys.argv`
- Optional command-line arguments
- Dictionaries
- Dynamic function lookup
- `hasattr()` and `getattr()`
- Functions as plug-ins
- Default parameters
- Boolean options
- Assertions and preconditions
- Reusing helper functions
- Pillow image input/output
- NumPy transposition
- Modular program design

## Author

Amelia Litvak
