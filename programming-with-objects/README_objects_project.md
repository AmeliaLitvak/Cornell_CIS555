# Python Objects, Methods, and Data Structures

## Overview

This project explores Python objects, object mutation, class invariants, string and tuple methods, and the difference between functions that return new objects and functions that modify existing objects.

The exercises use Cornell's `introcs` package and a provided `Time` class to demonstrate object creation and manipulation. Additional exercises practice built-in string and tuple methods without using loops or recursion.

## Project Components

### RGB Objects and Color Blending

The project introduces object creation using `introcs.RGB`. A demonstration script creates opaque green and semi-transparent red RGB objects, blends them into a new color, and demonstrates modifying an existing RGB object through alpha blending.

The supplied `blend(color1, color2)` function returns a new RGB object, while `blendUnder(color1, color2)` modifies `color1` directly. This demonstrates the difference between creating a new object and changing the state of an existing mutable object.

### The `Time` Class

The project uses a `Time` class representing a duration in hours and minutes. Its attributes are controlled by invariants:

- `hours` must be a nonnegative integer.
- `minutes` must be an integer from 0 through 59.

Properties and setters enforce these requirements. The class also implements initialization, equality and inequality comparisons, and string representations.

### Adding Time Objects

`add_time1(time1, time2)` returns a new `Time` object containing the sum of two times without modifying either argument.

`add_time2(time1, time2)` performs the same calculation but modifies `time1` directly and returns nothing.

These functions demonstrate the distinction between returning a new object and modifying an existing mutable object.

### Extracting Text from Parentheses

`first_in_parens(s)` returns the substring inside the first pair of parentheses.

```python
first_in_parens('A (B) C')
# 'B'

first_in_parens('A (B) (C)')
# 'B'
```

The implementation uses built-in string methods and slicing without loops or recursion.

### Cornell NetID Validation

`isnetid(s)` determines whether a string follows the expected Cornell NetID format: two or three lowercase letters followed by digits.

```python
isnetid('wmw2')
# True

isnetid('ww2345')
# True

isnetid('WW345')
# False
```

The function uses string methods including `isalpha()`, `islower()`, and `isdecimal()`.

### Replacing the First Tuple Value

`replace_first(tup, a, b)` returns a copy of a tuple with the first occurrence of `a` replaced by `b`.

```python
replace_first((1, 2, 1), 1, 3)
# (3, 2, 1)

replace_first((1, 2, 1), 4, 3)
# (1, 2, 1)
```

The implementation uses tuple membership, `index()`, slicing, and concatenation rather than loops or recursion.

## Testing

The project includes automated tests using Cornell's `introcs` package. The tests verify object types and attributes, object mutation behavior, preservation of arguments, parentheses extraction, NetID validation, and tuple replacement across normal and edge cases.

The object tests demonstrate that testing mutable objects requires checking not only return values but also whether function arguments were changed when the specification permits or prohibits mutation.

## Requirements

- Python 3
- Cornell `introcs` package

## Concepts Demonstrated

- Object-oriented programming fundamentals
- Object creation and instances
- Attributes
- Properties and setters
- Class invariants
- Mutable objects and object mutation
- Returning new objects versus modifying existing objects
- String methods
- Tuple methods
- String and tuple slicing
- Structured validation
- Alpha blending
- Automated testing
- Testing object state and side effects

## Author

Amelia Litvak
