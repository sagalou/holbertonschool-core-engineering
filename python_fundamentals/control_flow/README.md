# Python Fundamentals

## Description

This directory contains beginner Python projects completed as part of the Holberton School Core Engineering curriculum. Each project focuses on a specific set of Python concepts, building a solid foundation for software development.

## Projects

### hello_world — Environment & First Programs

Introduction to the Python interpreter, script creation, and development tools.

**Concepts covered:**
- Difference between expressions and statements in the REPL
- Creating and executing a Python script
- Using `pip` to install packages
- Understanding global vs isolated installations with `venv`

**File:**
- `structured_output.py` — prints formatted output using f-strings, floats, and boolean expressions

---

### control_flow — Conditionals and Loops

Introduction to control flow using conditional statements and loops.

**Concepts covered:**
- `if`, `elif`, `else` statements
- Comparison and boolean operators
- `while` and `for` loops with `range()`
- Generating deterministic formatted output

**Files:**
- `positive_or_negative.py` — determines whether a random integer is positive, negative, or zero

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.x
- pycodestyle 2.7.x (PEP8 compliance)
- All files must be executable and end with a newline
- No external libraries or imports allowed

## Usage

Before running any script, make it executable with `chmod`:

```bash
chmod +x filename.py
```

Then run it with:

```bash
./filename.py
```

To check PEP8 compliance before committing:

```bash
pycodestyle filename.py
```

Example for `positive_or_negative.py`:

```bash
chmod +x positive_or_negative.py
./positive_or_negative.py
pycodestyle positive_or_negative.py
```

## Author

Sagalou — Holberton School