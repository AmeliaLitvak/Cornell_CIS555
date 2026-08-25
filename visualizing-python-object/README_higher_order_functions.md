# Higher-Order Functions and Functional Programming

## Overview

This project introduces higher-order functions in Python: functions that accept other functions as arguments. The exercises demonstrate the ideas behind `map`, `filter`, and `fold`/`reduce`, along with function variables and reusable data-processing patterns.

Supporting examples also demonstrate temperature conversion functions and named constants.

## Project Components

### Function Variables

The `fcnvar.py` module demonstrates that Python functions can be passed as values to other functions.

It defines `add_one(x)` and `minus_one(x)`, then uses:

```python
doit(f, arg)
```

to call whichever function is supplied as `f`.

Examples:

```python
doit(add_one, 2)
# 3

doit(minus_one, 2)
# 1
```

This introduces the concept of treating functions as first-class values.

### Map

The `mapper.py` module implements a custom version of `map`.

```python
map(f, data)
```

applies function `f` to every element in a tuple and returns a new tuple containing the transformed values.

Supporting functions include:

- `add_one(x)` — adds one to a number
- `negate(x)` — reverses the sign of a number

For example, mapping `add_one` over `(1, 2, 3)` produces `(2, 3, 4)`.

### Filter

The `filterer.py` module implements a custom version of `filter`.

```python
filter(f, data)
```

creates a new tuple containing only the values for which Boolean function `f` returns `True`.

Supporting predicates include:

- `iseven(x)` — tests whether an integer is even
- `ispos(x)` — tests whether a number is positive

This demonstrates how a function can determine which values from a collection should be retained.

### Fold Left

`fold_left(f, seq, value)` repeatedly combines an accumulator with the next element of a sequence, processing the sequence from left to right.

For subtraction:

```text
seq = (1, 2, 3, 4)
value = 0

((((0 - 1) - 2) - 3) - 4) = -10
```

The function works with different compatible functions and sequence types, including tuples and strings.

### Fold Right

`fold_right(f, seq, value)` performs a similar operation but processes the sequence from right to left.

For subtraction:

```text
1 - (2 - (3 - (4 - 0))) = -2
```

The difference between left and right folds is especially important for operations such as subtraction that are not associative.

Fold is closely related to `reduce`, a common functional-programming operation and a concept associated with map-reduce processing.

### Temperature Conversion

The `temp.py` module contains functions for converting temperatures between Fahrenheit and centigrade:

```python
to_centigrade(x)
to_fahrenheit(x)
```

It also demonstrates named constants such as:

```python
FREEZING_C
FREEZING_F
BOILING_C
BOILING_F
```

These examples show how functions can be reused to calculate constant values.

## Testing

The project includes an extensive automated test suite for `fold_left()` and `fold_right()` using Cornell's `introcs` package.

Tests use several functions as fold arguments, including:

- Addition
- Subtraction
- Character removal

The test cases cover:

- Empty tuples
- Single-element tuples
- Multi-element tuples
- Positive and negative numbers
- Empty strings
- String concatenation
- String character removal
- Differences between left and right folding

These tests demonstrate that the behavior of a higher-order function depends both on the sequence and on the function passed into it.

## Requirements

- Python 3
- Cornell `introcs` package for the fold test suite

## Concepts Demonstrated

- Higher-order functions
- Functions as values
- Functions as parameters
- Function variables
- `map`
- `filter`
- `fold`
- `reduce`
- Boolean predicate functions
- Tuple processing
- Accumulators
- Left-to-right and right-to-left iteration
- Reusable data-processing patterns
- Named constants
- Automated testing

## Author

Amelia Litvak
