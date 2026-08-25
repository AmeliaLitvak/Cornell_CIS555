# Cornell Python Programming: Data Structures and Advanced Functions

## Overview

This repository contains Cornell Python programming projects focused on objects, higher-order functions, mutable data structures, nested collections, dictionaries, structured data, and image processing.

Across six projects, the coursework progresses from manipulating individual objects and sequences to building programs that process complex nested data and images. A recurring theme is understanding mutation: when a function should create and return a new value and when it should modify an existing object directly.

## Projects

### Project 1: Objects, Methods, and Data Structures

This project introduces Python objects and object mutation.

Exercises include:

- Creating and blending `introcs.RGB` color objects
- Comparing functions that return new objects with functions that modify existing objects
- Working with a `Time` class
- Enforcing class invariants with properties and setters
- Adding `Time` objects
- Extracting text from parentheses
- Validating Cornell NetIDs
- Replacing the first occurrence of a value in a tuple

Key concepts include classes, objects, attributes, mutable state, properties, setters, string methods, tuple methods, and testing side effects.

### Project 2: Higher-Order Functions and Functional Programming

This project explores functions that accept other functions as arguments.

Exercises include:

- Treating functions as values
- Passing functions into other functions
- Implementing custom `map` behavior
- Implementing custom `filter` behavior
- Implementing left and right folds
- Comparing sequence processing directions
- Temperature conversion and named constants

The project introduces functional-programming patterns for transforming, filtering, and reducing data.

### Project 3: Lists, Mutation, and Tuple Expansion

This project focuses on Python lists and mutable data.

Exercises include:

- Inserting values into sorted lists
- Rotating lists
- Non-mutating and mutating versions of `clamp()`
- Non-mutating and mutating versions of `removeall()`
- Indexed list modification
- Variable-length positional arguments
- Tuple expansion with `*`

The exercises emphasize the behavioral difference between returning a new collection and modifying the caller's collection.

### Project 4: Nested Lists and Two-Dimensional Data

This project extends list processing to two-dimensional tables.

Exercises include:

- Calculating row sums
- Removing rows and columns
- Comparing mutating and non-mutating table transformations
- Adding calculated sum columns
- Working with row-major data
- Testing nested mutable structures with deep copies

These exercises develop techniques for processing rows, columns, and nested mutable data.

### Project 5: Dictionaries, Nested Data, and Keyword Arguments

This project introduces dictionaries and more complex structured data.

Exercises include:

- Calculating average grades
- Converting numerical grades to letter grades
- Mutable and non-mutating dictionary operations
- Removing entries below a threshold
- Navigating nested weather dictionaries
- Processing `weather.json`
- Converting Fahrenheit measurements to Celsius
- Counting reports above temperature thresholds
- Variable-length keyword arguments with `**kwargs`
- Dictionary expansion with `**`

The project applies dictionary processing to structured weather observations and demonstrates flexible keyword-based function interfaces.

### Project 6: Image Processing Tool

The final project applies many of the repository's earlier concepts to a command-line image-processing application.

Images are represented as two-dimensional tables of mutable `introcs.RGB` objects. A plug-in architecture allows image-processing functions to be selected from the command line.

Implemented operations include:

- Greyscale conversion
- Sepia conversion
- Horizontal flipping
- Vertical flipping
- Image transposition
- 90-degree left rotation
- 90-degree right rotation

The application framework also handles:

- Image loading and saving with Pillow
- Command-line argument parsing
- Optional plug-in parameters
- Image-buffer validation
- Dynamic plug-in lookup with `hasattr()` and `getattr()`
- Conversion between Pillow pixel data and `introcs.RGB` objects

The project also contains specifications for optional vignette, blur, and pixellation effects.

## Testing and Program Correctness

Testing and validation are important throughout the repository.

The projects demonstrate:

- Equality assertions
- Floating-point comparisons
- Checking object types and attributes
- Verifying in-place mutation
- Verifying that arguments remain unchanged
- Deep-copy snapshots of mutable structures
- Empty and boundary cases
- Preconditions and assertions
- Validation of nested data structures
- Defensive checks before saving processed image data

These techniques reinforce that correct Python programs must account for both returned values and changes to mutable state.

## Requirements

Depending on the project, the repository uses:

- Python 3
- Cornell `introcs` package
- Pillow (`PIL`)
- NumPy
- Python standard-library modules including `math`, `copy`, `sys`, and `os`
- `weather.json` for weather-data exercises

## Programming Concepts Demonstrated

Across the six projects, this repository demonstrates:

- Objects and classes
- Object attributes
- Properties and setters
- Class invariants
- Mutable objects
- Mutating versus non-mutating functions
- Higher-order functions
- Functions as values
- `map`, `filter`, and fold/reduce patterns
- Lists and tuples
- Nested lists
- Dictionaries and nested dictionaries
- JSON data
- String, tuple, list, and dictionary methods
- Iteration and nested loops
- Accumulators
- Row and column processing
- `*args`
- Tuple expansion with `*`
- `**kwargs`
- Dictionary expansion with `**`
- Assertions and preconditions
- Deep copying
- Command-line arguments
- Dynamic function lookup
- Modular plug-in architecture
- RGB image manipulation
- Image transformations
- Automated testing
- Testing mutation and side effects

## Repository Progression

The projects increase steadily in both data complexity and program structure.

The repository begins with individual objects and simple sequences, moves through higher-order functions and mutable collections, then introduces nested tables and dictionaries. The final image-processing project combines nested data, mutable RGB objects, helper functions, command-line processing, dynamic function selection, and external libraries in a larger modular application.

Together, the projects demonstrate how core Python concepts can be combined to build programs that organize, transform, validate, and process increasingly complex forms of data.

## Author

Amelia Litvak
