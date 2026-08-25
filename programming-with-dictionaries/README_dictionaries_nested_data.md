# Dictionaries, Nested Data, and Keyword Arguments

## Overview

This project focuses on Python dictionaries and several ways they can be used to organize, transform, and analyze structured data. The exercises progress from simple grade dictionaries to nested weather data and variable-length keyword arguments.

A major theme is the difference between functions that return new dictionaries and functions that modify existing dictionaries in place.

## Project Components

### Average Grade

`average_grade(adict)` calculates the average numerical grade stored in a dictionary whose keys are student NetIDs and whose values are grades from 0 to 100.

```python
average_grade({'wmw2': 55, 'abc3': 90, 'jms45': 86})
# 77.0
```

An empty dictionary returns `0`.

The function uses a numerical accumulator while iterating over dictionary keys and leaves the original dictionary unchanged.

### Non-Mutating Letter Grade Conversion

The non-mutating version of `letter_grades(adict)` creates and returns a new dictionary in which numerical grades are converted to letter grades.

The grading scale is:

- 90–100: A
- 80–89: B
- 70–79: C
- 60–69: D
- Below 60: F

The original dictionary remains unchanged.

### Mutating Letter Grade Conversion

A second version of `letter_grades(adict)` performs the same conversion but modifies the original dictionary directly.

This exercise demonstrates the difference between copying a dictionary and changing values in an existing mutable object.

### Dropping Grades Below a Limit

`drop_below(adict, limit)` modifies a grade dictionary by deleting students whose grades are below a specified threshold.

```python
grades = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
drop_below(grades, 60)

# grades becomes:
# {'abc3': 90, 'jms45': 86}
```

Because dictionary size should not be changed while iterating directly over its keys, the function first collects the keys to remove and then deletes them in a separate loop.

### Nested Weather Dictionaries

The project uses a large `weather.json` dataset containing timestamped weather reports.

Each timestamp maps to another dictionary containing information such as:

- Visibility
- Wind
- Temperature
- Sky conditions
- Weather conditions
- Report codes

Not every report contains a temperature measurement, and temperature values may be stored in either Fahrenheit or Celsius.

### Counting Reports Above a Temperature

`reports_above_temp(weather, temp)` counts weather reports with temperatures strictly above a specified Celsius temperature.

The function:

1. Iterates through the weather-report dictionary.
2. Checks whether each report contains temperature data.
3. Detects whether the measurement is Fahrenheit or Celsius.
4. Converts Fahrenheit values to Celsius when necessary.
5. Counts temperatures above the requested threshold.

The supporting `to_celsius(x)` function performs Fahrenheit-to-Celsius conversion.

This exercise demonstrates navigating and processing nested dictionary structures loaded from JSON.

### Keyword Expansion

`circ_area(**kwd)` demonstrates variable-length keyword arguments.

A circle can be specified using either:

```python
circ_area(radius=3)
```

or:

```python
circ_area(diameter=4)
```

The function calculates the circle's area using `math.pi`.

It intentionally raises an `AssertionError` when:

- Neither `radius` nor `diameter` is supplied.
- Both `radius` and `diameter` are supplied.

Additional unrelated keyword arguments are ignored.

The project also demonstrates dictionary expansion:

```python
kwargs = {'diameter': 4, 'foo': 20, 'bar': 10}
circ_area(**kwargs)
```

## Testing

The project includes automated tests using Cornell's `introcs` package.

The tests cover:

- Average grades across dictionaries of different sizes
- Empty grade dictionaries
- Grade boundaries from F through A
- Preservation of dictionaries in non-mutating functions
- In-place modification of mutable dictionary functions
- Removal of grades using several cutoff values
- Empty and single-entry dictionaries
- Weather-report temperature thresholds
- Fahrenheit and Celsius weather data
- Circle areas specified by radius or diameter
- Required assertion failures for invalid circle specifications
- Extra keyword arguments
- Dictionary expansion with `**`

Several tests use `copy.deepcopy()` to verify that non-mutating functions preserve their original dictionary arguments.

## Requirements

- Python 3
- Cornell `introcs` package
- `weather.json`

## Concepts Demonstrated

- Dictionaries
- Dictionary keys and values
- Dictionary iteration
- Dictionary copying
- Mutable versus non-mutating functions
- Dictionary deletion
- Nested dictionaries
- JSON data
- Structured data processing
- Missing-key checks
- Temperature conversion
- Numerical accumulators
- Conditional logic
- `**kwargs`
- Keyword expansion
- Assertions
- `math.pi`
- Automated testing
- Deep-copy testing

## Author

Amelia Litvak
