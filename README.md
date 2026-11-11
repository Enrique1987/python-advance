# Advanced Python Notes

![Python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg)

This repository contains my personal notes from Python courses and books, along with examples and interview questions.

## Python Interview Questions

### What bad practices have you encountered as a Python developer?

The following examples are listed in no particular order:

- **Not following PEP 8 (low severity).** Run a linter automatically before each commit to check for style issues.
- **Duplicated code (medium severity).** Repetition makes code harder to maintain. As a personal habit, I like to review code after a few days with fresh eyes to identify opportunities for improvement.
- **Unclear variable and function names (medium severity).** Names should communicate their purpose. For example, `x` and `var1` provide little context:

  ```python
  for x in var1:
      # Do something with x.
      pass
  ```

- **Magic numbers.** Use named constants when a number's meaning is not obvious.
- **Dead code.** Remove code that is no longer used.
- **Using `print()` for logging.** Print statements can help during development, but production code generally benefits from structured logging with appropriate severity levels.
- **Poorly organized code.** A typical module starts with imports, followed by function and class definitions, and then its main entry point.
- **Ignoring algorithmic complexity.** Consider the time and space complexity of an approach using Big O notation.
- **Creating a class when a function would suffice.** This can happen when developers apply patterns from languages such as Java without considering simpler Python alternatives.
- **Empty `except` blocks and unhelpful error messages.** Handle exceptions deliberately and provide enough context to diagnose failures.

### What are some Python best practices?

The Zen of Python summarizes several useful principles:

- Simple is better than complex.
- Flat is better than nested.
- Readability counts.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.

### What is the output of this code?

This example deliberately contains a control-flow error:

```python
def analyze_age(age):
    if age < 21:
        print("You are a child")
    if age >= 21:
        print("You are an adult")
    else:
        print("The age must be a non-negative integer!")


analyze_age(18)
```

**Output:**

```text
You are a child
The age must be a non-negative integer!
```

### Why does the code produce this output, and how would you fix it?

The two `if` statements are evaluated independently. The `else` belongs only to the second `if`, so an age of 18 triggers both the first message and the error message.

Use a single `if`/`elif`/`else` chain and check for negative values first. This example assumes that the input is an integer and uses 21 as its illustrative age threshold:

```python
def analyze_age(age):
    if age < 0:
        print("The age must be a non-negative integer!")
    elif age < 21:
        print("You are a child")
    else:
        print("You are an adult")


analyze_age(18)
```

**Output:**

```text
You are a child
```

### What is the difference between `pass`, `continue`, and `break`?

Compare these three examples:

```python
a = [1, 2, 0, 3]
for element in a:
    if not element:
        pass
    print(element)
```

```python
a = [1, 2, 0, 3]
for element in a:
    if not element:
        continue
    print(element)
```

```python
a = [1, 2, 0, 3]
for element in a:
    if not element:
        break
    print(element)
```

**Explanation:**

- `pass` does nothing, so execution continues with `print(element)`. The first example prints `1`, `2`, `0`, and `3`, each on a separate line.
- `continue` skips the rest of the current iteration. The second example prints `1`, `2`, and `3`.
- `break` exits the loop immediately. The third example prints `1` and `2`.

### Without writing code, how would you compare two DataFrames for equality?

I would use pandas and start by inspecting their shapes, column labels, indexes, and data types. `DataFrame.info()` provides a useful overview, while `DataFrame.shape` gives the number of rows and columns. Different shapes mean the DataFrames cannot be equal.

Next, I would establish what equality means for the task, including whether row order, column order, and data types matter. I would only rename, reorder, or convert data when the comparison requirements call for it.

For a Boolean equality check, use `dataframe_a.equals(dataframe_b)`. Corresponding values and their data types must match. For a detailed view of differences between identically labeled DataFrames, use `dataframe_a.compare(dataframe_b)`.

### How would you compare DataFrames that contain `NaN` values?

Although a scalar comparison such as `float("nan") == float("nan")` returns `False`, pandas provides comparison methods that handle missing values:

- `DataFrame.equals()` treats `NaN` values in corresponding positions as equal.
- `DataFrame.compare()` does not report matching `NaN` values as differences. It requires the same shape and identical row and column labels.

There is no need to replace missing values with arbitrary placeholders such as `"nan"` or `999999`, which could be confused with real data.

See the pandas documentation for [`DataFrame.equals()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html) and [`DataFrame.compare()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html).

## Numeric Types

### What is the result of this floating-point comparison?

```python
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)
```

**Output:**

```text
False
```

Many decimal fractions cannot be represented exactly as binary floating-point numbers. In this example, the stored values are approximately:

```text
0.1 -> 0.1000000000000000055511151
x   -> 0.3000000000000000444089210
y   -> 0.2999999999999999888977698
```

Rounding both values to five decimal places produces `True` for this example:

```python
print(round(x, 5) == round(y, 5))  # True
```

For approximate numerical comparisons, [`math.isclose()`](https://docs.python.org/3/library/math.html#math.isclose) lets you specify tolerances appropriate to the problem:

```python
from math import isclose

print(isclose(x, y, rel_tol=1e-9, abs_tol=1e-12))  # True
```

### How would you round an age expressed in years?

If the value represents a non-negative age in years and the goal is to report completed years, use `math.floor()`. For example, someone aged 23 years and 11 months is still 23 in completed years.

### What does `floor()` return for positive and negative values?

```python
from math import floor

print(floor(-10.4))  # -11
print(floor(11.4))   # 11
```

`floor()` returns the greatest integer less than or equal to its argument, so it rounds toward negative infinity.

### What is the difference between `float` and `Decimal` in Python?

`float` uses binary floating-point representation. Some decimal fractions, such as `0.1`, therefore have no exact representation as a `float`.

[`Decimal`](https://docs.python.org/3/library/decimal.html) uses decimal floating-point representation with configurable precision and rounding. It can represent decimal values such as `0.1` exactly when constructed from a string, for example `Decimal("0.1")`. A `Decimal` stores a sign, digits, and an exponent; it is not simply stored as a string.

### What are the advantages of `float` and `Decimal`?

- **`float`:** Generally faster and suitable for many scientific and numerical calculations where small representation errors are acceptable.
- **`Decimal`:** Useful when exact decimal representation and explicit control over precision and rounding matter. Arithmetic is still subject to the configured precision; not every calculation has an exact finite result.
