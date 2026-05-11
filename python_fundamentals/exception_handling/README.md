# Python - Exception Handling

## Description
This project focuses on making Python programs resilient and defensive. It covers the implementation of error-handling mechanisms to manage invalid inputs, missing data, and unexpected runtime failures without crashing the application.

## Learning Objectives
By the end of this project, you will be able to:
* **Try/Except:** Implement error catching blocks to handle runtime issues.
* **Specific Exceptions:** Identify and catch specific errors like `TypeError`, `IndexError`, and `ZeroDivisionError`.
* **Clean Up:** Use `else` and `finally` blocks to manage program flow and resource cleanup.
* **Explicit Raising:** Use the `raise` keyword to trigger exceptions when specific conditions are met.
* **Defensive Coding:** Write functions that fail safely and predictably.

## Requirements
* **Environment:** Ubuntu 20.04 LTS
* **Python Version:** Python 3.8.x
* **Style Guide:** PEP8 compliant (`pycodestyle` 2.7.x)
* **Constraints:** 
    * Every file must start with `#!/usr/bin/env python3`.
    * No external modules or libraries allowed.
    * Files must be executable and end with a newline.
    * No use of `len()` where explicitly forbidden.

## Task Overview
| Task | File | Description |
| :--- | :--- | :--- |
| **0. Safe list printing** | `safe_print_list.py` | Prints `x` elements of a list using try/except without using `len()`. |
| **1. Safe integer printing** | `safe_print_integer.py` | (Upcoming) Prints an integer with `"{:d}".format()`. |
| ... | ... | ... |

---
**Author:** [sagalou](https://github.com/sagalou)