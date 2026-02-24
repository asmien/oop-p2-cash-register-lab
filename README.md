# Object-Oriented Programming (OOP) Part 2 – Cash Register Lab
## Overview
This project implements a Cash Register system using Object-Oriented Programming principles in Python.
The CashRegister class simulates core functionality of a real-world e-commerce checkout system, including:
Adding items to a cart
Tracking total price
Applying percentage-based discounts
Voiding previous transactions

This lab demonstrates proper object-oriented design, data validation, and state management.

## OOP Concepts Demonstrated
Class creation and initialization
Instance attributes
Encapsulation using properties
Input validation
Method-driven state updates
Managing collections within objects
Writing and running automated tests using pytest

## Project Structure
```
OOP-P2-CASH-REGISTER-LAB/
│
├── lib/
│   ├── cash_register.py
│   └── testing/
│       └── cash_register_test.py
│
├── pytest.ini
└── README.md
```


## Installation & Setup
1️⃣ Clone the repository
```
git clone <your-repo-url>
cd python-oop1-lab
```

2️⃣ Install dependencies
```
python -m pip install pytest
```


## CashRegister Class
### Attributes
discount – percentage discount (0–100)
total – running total of all items
items – list of item names
previous_transactions – list of previous transaction records

### Methods
add_item(item, price, quantity)
Adds the item to the cart
Updates the total
Stores transaction details
apply_discount()
Applies percentage discount to total
Updates total correctly
Handles cases where no transactions exist
void_last_transaction()
Removes the last transaction
Updates total and item list accordingly
Handles empty transaction history safely

### Discount Validation
Discount must be an integer
Must be between 0–100 (inclusive)
If invalid, prints: "Not valid discount"
This ensures proper input validation and data integrity.

## Running Tests
Run all tests:
```
pytest
```

Run a specific test file:
```
pytest lib/testing/cash_register_test.py
```

## Features Implemented
✔ Add items with quantity
✔ Track running total
✔ Apply percentage discount
✔ Void last transaction
✔ Input validation for discount
✔ Automated testing with pytest

## Requirements
Python 3.12+
pytest
Check your Python version:
python --version


## Status
All required functionality has been implemented and tested.
