# stepik_auto_tests_course
Автотесты по курсу AUTOMATION QA *Stepik

Мои автотесты по заданиям в курсе "Automation QA"
=======
# Selenium Automation Testing Course

This repository contains automation scripts created during a Selenium WebDriver course for QA automation testing.

## Project Structure

```
Lessons QA_Auto/
├── Module1/                 # Basic Selenium concepts
│   ├── check1.py            # Form registration test (registration2.html)
│   ├── check2.py            # Alternative form registration test
│   ├── lesson1.py           # Basic form interaction
│   ├── lesson2.py           # Finding elements by link text
│   ├── lesson3.py           # Working with multiple form elements
│   ├── lesson4.py           # Using XPath selectors
│   └── lesson5.py           # Testing registration form
│
├── Module2/                 # Advanced Selenium concepts
│   ├── Alerts/              # Working with browser alerts and windows
│   │   ├── alert1.py        # Handling JavaScript alerts
│   │   └── window1.py       # Working with browser tabs/windows
│   │
│   ├── Waits/               # Explicit and implicit waits
│   │   └── wait1.py         # Using explicit waits with conditions
│   │
│   ├── lesson2.1.py         # Working with math calculations and checkboxes
│   ├── lesson2.2.py         # Getting element attributes
│   ├── lesson2.3.py         # Working with dropdown lists
│   ├── lesson2.4.py         # JavaScript execution in browser
│   └── lesson2.5.py         # File uploads
```

## Prerequisites

- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/d4nc3rqqq/selenium-qa-course.git
   cd selenium-qa-course
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install selenium
   ```

4. Download ChromeDriver from https://chromedriver.chromium.org/downloads (make sure it matches your Chrome version)

## Script Descriptions

### Module 1: Basic Selenium Concepts

- **lesson1.py**: Demonstrates how to find elements using different locators (tag name, name, class name, ID)
- **lesson2.py**: Shows how to find elements by link text using mathematical calculation
- **lesson3.py**: Works with multiple form elements using find_elements
- **lesson4.py**: Demonstrates XPath selectors for finding elements
- **lesson5.py**: Tests a registration form with required fields
- **check1.py & check2.py**: Different approaches to test registration forms

### Module 2: Advanced Selenium Concepts

- **lesson2.1.py**: Works with math calculations, checkboxes, and radio buttons
- **lesson2.2.py**: Shows how to get element attributes using get_attribute()
- **lesson2.3.py**: Demonstrates working with dropdown lists using Select class
- **lesson2.4.py**: Shows how to execute JavaScript in the browser
- **lesson2.5.py**: Demonstrates file uploads in forms

#### Alerts and Windows
- **alert1.py**: Handles JavaScript alerts and confirmations
- **window1.py**: Works with multiple browser tabs/windows

#### Waits
- **wait1.py**: Demonstrates explicit waits with expected conditions

## Usage

Run any script using Python:

```
python Module1/lesson1.py
```

## Notes

- Most scripts use the website http://suninjuly.github.io/ for testing
- Scripts include sleep times to allow viewing the results before browser closes
- Error handling is implemented with try/finally blocks to ensure browser cleanup

## License

This project is licensed under the MIT License - see the LICENSE file for details.
