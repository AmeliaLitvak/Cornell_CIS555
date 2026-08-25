# Python Lists, Mutation, and Tuple Expansion

## Overview

This project explores Python lists as mutable data structures and compares functions that modify lists directly with functions that create and return new lists. It also introduces tuple expansion with variable-length function arguments.

The exercises emphasize list methods, copying, mutation, accumulators, positional iteration, and testing side effects.

## Project Components

### Inserting into a Sorted List

`put_in(alist, value)` adds a value to an already sorted list and keeps the list sorted.

```python
a = [0, 2, 3, 4]
put_in(a, 1)
# a becomes [0, 1, 2, 3, 4]
```

The function modifies the original list and uses list methods rather than a `for` loop.

### Rotating a List

`rotate(alist)` rotates a non-empty list one position to the right.

```python
a = [0, 2, 3, 4]
rotate(a)
# a becomes [4, 0, 2, 3]
```

The last element is removed with `pop()` and inserted at position zero with `insert()`.

### Non-Mutating Clamp

One version of `clamp(alist, min, max)` returns a new list in which all numerical values are restricted to the specified range.

Values below `min` become `min`, values above `max` become `max`, and values already inside the range are unchanged.

```python
clamp([-1, 1, 3, 5], 0, 4)
# [0, 1, 3, 4]
```

The original list remains unchanged.

### Non-Mutating Remove All

`removeall(alist, n)` returns a copy of a list with every occurrence of `n` removed.

```python
removeall([1, 2, 2, 3, 1], 2)
# [1, 3, 1]
```

The function works on a copied list so that the original argument is preserved.

### Mutating Clamp

A second implementation of `clamp(alist, min, max)` performs the same numerical restriction but modifies the supplied list directly instead of returning a new list.

This version demonstrates list mutation through indexed assignment.

### Mutating Remove All

The mutating version of `removeall(alist, n)` removes every occurrence of `n` directly from the original list.

The implementation demonstrates the extra care required when removing list elements while iterating because list positions change after each removal.

### Tuple Expansion and Variable Arguments

`avg(*args)` demonstrates Python tuple expansion and variable-length argument lists.

The function accepts any number of numerical arguments and returns their average.

```python
avg(1.0, 2.0, 3.0)
# 2.0

avg(1.0, 1.0, 3.0, 5.0)
# 2.5
```

With no arguments, it returns `0`.

Tuple expansion also allows an existing tuple to be supplied as separate arguments:

```python
values = tuple(range(10, 20))
avg(*values)
# 14.5
```

## Testing

The project contains automated tests using Cornell's `introcs` package.

The tests verify:

- Inserting values into sorted lists
- Duplicate values and empty lists
- Repeated list rotations
- Single-element lists
- Clamping values to different ranges
- Preservation of original lists in non-mutating functions
- Correct mutation in mutating functions
- Removing repeated, missing, and single values
- Empty-list behavior
- Averages with integers and floating-point values
- Zero, one, and many arguments
- Tuple expansion with `*`

A major focus of the tests is verifying whether each function changes its argument or leaves it unchanged according to its specification.

## Requirements

- Python 3
- Cornell `introcs` package

## Concepts Demonstrated

- Lists
- Mutable data structures
- List methods
- `append()`
- `sort()`
- `pop()`
- `insert()`
- `copy()`
- Indexed assignment
- Mutating versus non-mutating functions
- List accumulators
- Positional iteration
- Removing elements during iteration
- Variable-length arguments
- `*args`
- Tuple expansion
- Automated testing
- Testing side effects and mutation

## Author

Amelia Litvak
