# SQITK3073--Tax-Program
# Malaysian Tax Input Program (SQITK3073 Individual Project)

A Python-based command-line application developed for **SQITK3073 Business Analytics Programming** to manage user authentication, calculate Malaysian resident individual income tax for **Year of Assessment (YA) 2026**, and perform data processing and CSV storage using `pandas`.

---

## 🚀 Key Features & Objectives
1. **User Authentication System**: Secure user registration and login using User ID and the last 4 digits of a 12-digit IC number as the password.
2. **Personal Income Tax Calculation (YA 2026)**: Computes chargeable income, progressive tax rates (0% to 30%), individual tax rebates (RM400 for chargeable income $\le$ RM35,000), and final tax payable.
3. **Data Structures & Pandas Integration**: Organizes data using Python lists and dictionaries, converts them into `pandas` DataFrames, and performs structured CSV file management.
4. **Automated Test Cases**: Automatically executes and validates the 5 required project test cases (**T01 - T05**).
5. **Data Persistence**: Safely stores and retrieves records using `users.csv` and `tax_records.csv` while preserving historical entries.

---

## 📂 Project Directory Structure

```text
SQITK3073-Tax-Program/
│
├── main.py             # Main program logic, CLI menu, and user interaction loop
├── functions.py        # Core utility functions (authentication, tax math, pandas operations)
├── users.csv           # Stores registered User IDs, IC numbers, and passwords
├── tax_records.csv     # Stores tax calculation records (User ID, Test Case ID, Income, Relief, Tax Payable)
└── README.md           # Project documentation
