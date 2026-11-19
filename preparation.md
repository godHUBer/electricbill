
# CBSE Class 12 Computer Science – Electricity Bill Management System

## 1. Project Introduction

**Project Title:** Electricity Bill Management System  
**Programming Language:** Python 3  
**Subject:** Computer Science – Class XII  
**Project Type:** Menu-driven, file-handling application.

### Objective

To develop a Python application that calculates electricity bills based on previous and current meter readings and maintains customer billing records using CSV files.

### Main Objectives

1. Calculate electricity consumption.
2. Calculate electricity charges using slab-based rates.
3. Generate unique bill IDs.
4. Store bills permanently using CSV files.
5. Search and display existing bills.
6. Correct existing billing records.
7. Generate billing summaries and estimates.

---

## 2. Software and Hardware Requirements

| Component | Requirement |
|---|---|
| Operating System | Windows / Linux / macOS |
| Programming Language | Python 3 |
| IDE | IDLE / VS Code / PyCharm |
| Storage | CSV file |
| Python Modules | csv |
| Hardware | Standard computer |

No external Python packages are required. The project uses Python's built-in CSV module.

---

## 3. Working of the Project

The project follows these steps:

1. Start the Python program.
2. Display the main menu.
3. Ask the user to select an operation.
4. Accept and validate user input.
5. Calculate electricity consumption and charges when required.
6. Read or update customer records in the CSV file.
7. Display the result.
8. Return to the main menu until the user selects Exit.

### Main Operations

- Add Bill
- List Bills
- Search Bill
- Search Customer
- Edit Bill
- Estimate Bill
- Display Statistics
- Filter Bills
- Exit

---

## 4. Python Concepts Used

| Python Concept | Where It Is Used | Purpose |
|---|---|---|
| Variables | units, previous, current | Store values |
| Functions | calculate_bill() | Reusable code |
| Conditional Statements | if, elif, else | Apply billing slabs |
| Loops | while, for | Repeat menu and process records |
| Lists | bills, matches | Store multiple records |
| Dictionaries | bill | Store individual bill details |
| File Handling | open() | Read and write files |
| CSV Module | csv.DictReader() | Read structured CSV data |
| Exception Handling | try, except | Handle invalid input |
| String Formatting | f-strings | Format bill amounts |
| Modules | import csv | Use built-in functionality |
| Path Handling | pathlib.Path | Manage file paths |

### A. Importing Modules

```python
import csv
from pathlib import Path
```

- `csv` provides functions to read and write CSV files.
- `Path` helps locate and manage file paths.

### B. Calculating Electricity Consumption

```python
units = current - previous
```

Example:

- Previous reading = 1200
- Current reading = 1350
- Units consumed = 150

### C. Calculating the Bill

```python
def calculate_bill(units):
    if units <= 100:
        return 50 + units * 4

    if units <= 200:
        return 50 + 100 * 4 + (units - 100) * 6

    return 50 + 100 * 4 + 100 * 6 + (units - 200) * 8
```

This function uses conditional statements to determine how much electricity was consumed in each slab.

### D. Reading CSV Records

```python
def load_bills():
    with BILL_FILE.open(newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))
```

`csv.DictReader()` reads each row as a dictionary.

Example:

```python
{
    'Bill ID': '1',
    'Customer': 'Rahul',
    'Units': '150',
    'Amount (Rs.)': '750.00'
}
```

### E. Writing CSV Records

```python
with BILL_FILE.open('a', newline='', encoding='utf-8') as file:
    csv.DictWriter(file, fieldnames=HEADINGS).writerow(bill)
```

The `'a'` mode means append. It adds a new record without deleting previous records.

---

## 5. Understanding the CSV File

The project uses `bills.csv` to store electricity billing records.

### CSV Columns

- Bill ID
- Customer
- Previous Reading
- Current Reading
- Units
- Amount (Rs.)

### Example Records

| Bill ID | Customer | Previous | Current | Units | Amount |
|---|---|---:|---:|---:|---:|
| 1 | Rahul | 1000 | 1150 | 150 | 750.00 |
| 2 | Aman | 2000 | 2100 | 100 | 450.00 |
| 3 | Priya | 3000 | 3250 | 250 | 1450.00 |

### Why CSV Instead of a Normal Text File?

CSV stores data in a structured tabular format consisting of rows and columns. Python's CSV module makes it easier to read, search, append and update records.

---

## 6. Sample Practical Demonstration

Suppose a customer named Rahul has the following meter readings:

- Customer Name: Rahul
- Previous Reading: 1000
- Current Reading: 1150
- Units Consumed: 150

### Billing Calculation

| Description | Calculation | Amount |
|---|---|---:|
| First 100 units | 100 × 4 | ₹400 |
| Next 50 units | 50 × 6 | ₹300 |
| Fixed Charge | Fixed | ₹50 |
| **Total** | | **₹750** |

### Expected Bill Output

```text
--- Electricity Bill ---
Bill ID: 1
Customer: Rahul
Previous Reading: 1000
Current Reading: 1150
Units: 150
Amount (Rs.): 750.00
```

The actual bill ID depends on existing records in the CSV file.

---

## 7. Important CBSE Viva Questions and Answers

### Basic Project Questions

**Q1. What is the purpose of your project?**

The purpose is to automate electricity bill calculation and maintain customer billing records using Python and CSV file handling.

**Q2. Which programming language did you use?**

Python 3.

**Q3. What is CSV?**

CSV stands for Comma-Separated Values. It is a file format used to store tabular data.

**Q4. Which Python module is used for CSV operations?**

The built-in `csv` module.

**Q5. What is the extension of your database file?**

`.csv`, specifically `bills.csv`.

### Programming Questions

**Q6. What is a function?**

A function is a reusable block of code designed to perform a particular task.

**Q7. Why did you create calculate_bill()?**

To separate billing calculations from the rest of the program and make the calculation reusable.

**Q8. What is the difference between append and write mode?**

- Append (`a`): Adds data to the end of a file.
- Write (`w`): Creates or overwrites a file.

**Q9. What is a dictionary in Python?**

A dictionary is a collection of key-value pairs. This project uses dictionaries to represent individual bills.

**Q10. What is the purpose of try-except?**

It handles exceptions and prevents certain invalid inputs from crashing the program.

**Q11. What is csv.DictReader()?**

It reads CSV records and returns each row as a dictionary using the column headings as keys.

**Q12. What is csv.DictWriter()?**

It writes dictionary records into a CSV file.

### Logic and Calculation Questions

**Q13. How do you calculate electricity consumption?**

Current meter reading minus previous meter reading.

**Q14. What happens if the current reading is less than the previous reading?**

The program rejects the readings because the current reading cannot be lower than the previous reading in this simplified billing model.

**Q15. Why do you use slab-based billing?**

Different portions of electricity consumption are charged at different rates.

**Q16. What is the fixed charge?**

It is a fixed amount added to the electricity bill regardless of consumption. In this project, it is ₹50.

**Q17. What happens when consumption is exactly 200 units?**

The bill is ₹1,050, including the fixed charge.

### File-Handling and Advanced Questions

**Q18. What happens when the program is restarted?**

Previously saved bills remain available because they are stored in `bills.csv`.

**Q19. How is a bill ID generated?**

The program finds the maximum existing bill ID and adds one. If there are no records, it starts with ID 1.

**Q20. Can this project handle thousands of customers?**

It can store many records, but CSV becomes less efficient for larger applications. SQLite or another database would be better.

**Q21. What is the difference between load_bills() and save_bills()?**

`load_bills()` reads records from the CSV file, while `save_bills()` rewrites the records into it.

**Q22. Why is `__name__ == '__main__'` used?**

It ensures that `main()` runs when the Python file is executed directly, rather than when it is imported as a module.

**Q23. What is the purpose of `Path(__file__).with_name('bills.csv')`?**

It locates `bills.csv` in the same directory as the Python script.

**Q24. What is the difference between return and print()?**

`return` sends a value back from a function. `print()` displays information on the screen.

**Q25. What improvements can be made?**

We can introduce a database, customer authentication, PDF bill generation, billing history and a graphical user interface.

---

## 8. Project Report

### Abstract

The Electricity Bill Management System is a Python-based application designed to calculate electricity bills and maintain customer billing records. The application calculates electricity consumption using previous and current meter readings and applies predefined slab-based electricity rates.

The project uses Python functions, conditional statements, loops, dictionaries and CSV file handling. It provides facilities to add, display, search, correct and estimate electricity bills.

### Introduction

Electricity billing is an important administrative activity that requires accurate calculation of electricity consumption and corresponding charges.

This project demonstrates how Python programming can automate basic electricity billing operations and maintain records in a structured CSV file.

### Objectives

1. To calculate electricity consumption from meter readings.
2. To calculate bills using slab-based rates.
3. To maintain customer billing records.
4. To search and retrieve existing bills.
5. To correct previously saved billing information.
6. To generate billing summaries.

### Methodology

The program accepts customer details and meter readings from the user. It calculates the consumed units and determines the bill amount using predefined electricity rates.

The generated bill is stored in a CSV file. The application also allows users to retrieve, search, modify and analyze stored records.

### Technologies Used

- Programming Language: Python 3
- Module: csv
- File Format: CSV
- IDE: Python IDLE / Visual Studio Code

### Conclusion

The Electricity Bill Management System demonstrates the practical application of Python programming concepts, particularly functions, conditional statements, loops and file handling.

It provides a simple and efficient method for calculating electricity bills and maintaining billing records. The project also provides a foundation for developing more advanced billing applications using databases and graphical interfaces.

### Future Scope

The project can be enhanced by adding a graphical user interface, database integration, PDF bill generation, customer authentication and monthly consumption reports.

---

## 9. Important Corrections Before Submitting

- The project uses a CSV file, not a relational database.
- The electricity rates are illustrative educational rates, not official electricity tariffs.
- It is a terminal-based application, not a website.
- The project has no online payment functionality.
- The `estimate_bill()` function calculates an estimate without saving a customer record.
- The `correct_bill()` function asks for confirmation before saving changes.

---

## 10. Final Preparation Checklist

- [ ] Understand the slab-based billing formula.
- [ ] Explain calculate_bill() without reading the code.
- [ ] Understand the difference between CSV reader and writer.
- [ ] Explain lists and dictionaries used in the program.
- [ ] Demonstrate adding a bill.
- [ ] Demonstrate searching for a bill.
- [ ] Demonstrate correcting a bill.
- [ ] Explain exception handling.
- [ ] Explain the purpose of the main() function.
- [ ] Prepare the project abstract and conclusion.

---

## 11. Final Viva Preparation Advice

Practise explaining these four functions particularly well:

1. `calculate_bill()` – Core billing calculation.
2. `load_bills()` – Reading records from CSV.
3. `add_bill()` – Creating and adding a new bill.
4. `save_bills()` – Saving updated records.

These functions cover the core logic, input-to-record process and file handling of the project.

### Original Repository

GitHub: https://github.com/godHUBer/electricbill

Python source code: https://github.com/godHUBer/electricbill/blob/main/electricity_bill.py
