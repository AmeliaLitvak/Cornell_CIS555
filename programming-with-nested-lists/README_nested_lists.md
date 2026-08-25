# Nested Lists and Two-Dimensional Data

## Overview

This project focuses on working with nested Python lists as two-dimensional tables. The exercises compare immutable-style functions that create new tables with mutable functions that modify their table arguments directly.

The project demonstrates nested iteration, row and column processing, deep-copy testing, table mutation, accumulators, and handling numerical data stored in row-major order.

## Project Components

### Row Sums

`row_sums(table)` returns a new list containing the sum of each row in a numerical table.

```python
row_sums([
    [0.1, 0.3, 0.5],
    [0.6, 0.2, 0.7],
    [0.5, 1.1, 0.1]
])
# [0.9, 1.5, 1.7]
```

The function processes each row independently and does not modify the original table.

### Non-Mutating Crossout

The non-mutating version of `crossout(table, row, col)` returns a new table with the specified row and column removed.

```python
crossout(
    [[1, 3, 5],
     [6, 2, 7],
     [5, 8, 4]],
    1,
    2
)
# [[1, 3], [5, 8]]
```

The original nested list remains unchanged.

This implementation uses nested loops to construct a completely new table while skipping the selected row and column.

### Mutating Crossout

A second version of `crossout(table, row, col)` performs the same operation by modifying the original table.

It first removes the requested row and then removes the requested column from every remaining row.

This exercise highlights the difference between returning a transformed copy and changing a mutable nested structure in place.

### Adding Row Sums to a Table

`place_sums(table)` modifies a table that contains a header row.

The function:

- Adds `'Sum'` to the header.
- Calculates the sum of each numerical row.
- Appends that sum to the end of the corresponding row.

For example:

```python
table = [
    ['First', 'Second', 'Third'],
    [0.1, 0.3, 0.5],
    [0.6, 0.2, 0.7],
    [0.5, 1.1, 0.1]
]

place_sums(table)
```

modifies the table to include a new `Sum` column.

## Nested List Representation

The exercises treat nested lists as two-dimensional tables in row-major order.

For numerical tables:

- The outer list represents the table.
- Each inner list represents one row.
- Each row contains the same number of values.

Some exercises also use a header row containing strings followed by rows containing numerical data.

## Testing

The project includes automated tests using Cornell's `introcs` package.

Tests verify:

- Row sums for tables of different dimensions
- Positive and negative floating-point values
- Removal of different rows and columns
- Rectangular and square tables
- Single-element tables
- Preservation of the original table in non-mutating functions
- Correct in-place changes in mutable functions
- Addition of a `Sum` header
- Correct sums appended to numerical rows

The non-mutating tests use Python's `copy.deepcopy()` to take snapshots of nested lists before calling a function. This allows the tests to verify that neither the outer list nor any inner row was modified.

Floating-point nested lists are tested with `introcs.assert_float_lists_equal()`.

## Requirements

- Python 3
- Cornell `introcs` package

## Concepts Demonstrated

- Nested lists
- Two-dimensional tables
- Row-major data
- Nested loops
- Row and column processing
- List accumulators
- Mutable versus non-mutating functions
- In-place list modification
- `append()`
- `pop()`
- `sum()`
- `range()`
- Deep copying
- Testing mutable nested structures
- Floating-point testing
- Table transformations

## Author

Amelia Litvak
