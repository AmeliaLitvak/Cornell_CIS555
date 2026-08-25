# Cornell Python Programming: Data Structures and Advanced Functions

## Overview

This repository contains a collection of Cornell Python programming projects focused on working with objects, higher-order functions, mutable data structures, nested collections, dictionaries, and structured data.

Across the projects, the coursework progresses from creating and modifying Python objects to processing increasingly complex collections of data. The exercises emphasize the difference between mutable and non-mutating functions, careful testing of side effects, reusable functions, and techniques for organizing and transforming structured information.

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

Key concepts include objects, classes, attributes, mutable state, properties, setters, string methods, tuple methods, and testing object side effects.

### Project 2: Higher-Order Functions and Functional Programming

This project explores functions that accept other functions as arguments.

Exercises include:

- Treating functions as values
- Passing functions into other functions
- Implementing custom `map` behavior
- Implementing custom `filter` behavior
- Implementing left and right folds
- Comparing the effect of processing sequences from different directions
- Temperature conversion and named constants

The project introduces functional-programming ideas and reusable patterns for transforming, filtering, and reducing collections.

### Project 3: Lists, Mutation, and Tuple Expansion

This project focuses on Python lists and the consequences of working with mutable data.

Exercises include:

- Inserting values into sorted lists
- Rotating lists
- Creating non-mutating versions of `clamp()` and `removeall()`
- Creating mutating versions of the same operations
- Modifying lists through indexed assignment
- Using variable-length positional arguments
- Expanding tuples with `*`

A major theme is understanding whether a function should return a new collection or modify the collection supplied by the caller.

### Project 4: Nested Lists and Two-Dimensional Data

This project extends list processing to nested lists representing two-dimensional tables.

Exercises include:

- Calculating row sums
- Removing a row and column from a table
- Comparing mutating and non-mutating table transformations
- Adding calculated sum columns to tables
- Working with row-major data
- Testing nested mutable structures

The tests use deep copies to verify whether nested structures are preserved or modified as required.

### Project 5: Dictionaries, Nested Data, and Keyword Arguments

This project introduces dictionaries and more complex structured data.

Exercises include:

- Calculating average grades from dictionaries
- Converting numerical grades to letter grades
- Comparing mutable and non-mutating dictionary functions
- Removing dictionary entries below a threshold
- Navigating nested weather-report dictionaries
- Processing data loaded from `weather.json`
- Converting Fahrenheit measurements to Celsius
- Counting weather reports above temperature thresholds
- Accepting variable-length keyword arguments with `**kwargs`
- Expanding dictionaries into keyword arguments with `**`

The weather exercise applies dictionary processing to a large real-world-style JSON dataset containing timestamped weather observations.

## Testing

Automated testing is used throughout the repository with Cornell's `introcs` package.

The tests verify both return values and side effects. This is especially important for mutable objects, lists, nested lists, and dictionaries, where a function may be required either to preserve its argument or modify it directly.

Testing techniques demonstrated across the projects include:

- Equality assertions
- Floating-point comparisons
- Checking object attributes
- Checking returned object types
- Verifying in-place mutation
- Verifying that arguments remain unchanged
- Using `copy.deepcopy()` to snapshot mutable structures
- Testing empty collections
- Testing boundary conditions
- Testing expected assertion failures

## Requirements

- Python 3
- Cornell `introcs` package
- Python standard library modules such as `math` and `copy`
- `weather.json` for the weather-data exercises

## Programming Concepts Demonstrated

Across the repository, the projects demonstrate:

- Objects and classes
- Object attributes
- Properties and setters
- Class invariants
- Mutable objects
- Mutating versus non-mutating functions
- Functions as first-class values
- Higher-order functions
- `map`, `filter`, and fold/reduce patterns
- Lists
- Tuples
- Nested lists
- Dictionaries
- Nested dictionaries
- JSON data
- String and tuple methods
- List and dictionary methods
- Accumulators
- Iteration
- Row and column processing
- Structured data transformation
- Positional arguments
- `*args`
- Tuple expansion with `*`
- `**kwargs`
- Dictionary expansion with `**`
- Assertions
- Data validation
- Numerical conversion
- Deep copying
- Automated testing
- Testing mutation and side effects

## Repository Progression

The projects build on one another by increasing the complexity of the data being manipulated.

The repository begins with individual objects and simple sequences, progresses to higher-order functions and mutable lists, then moves into nested tables and dictionaries containing structured data. By the final project, the exercises combine iteration, nested dictionaries, JSON data, unit conversion, mutation, and flexible function arguments.

Together, these projects demonstrate how Python programs can organize and manipulate complex data while maintaining clear expectations about function behavior and object state.

## Author

Amelia Litvak
