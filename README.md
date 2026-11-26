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

```

---

## ⚙️ Prerequisites & Environment Setup

Ensure you have **Python 3.x** installed along with the required library (`pandas`).

1. Install pandas via terminal/command prompt:
```bash
pip install pandas

```



---

## 🚀 How to Run the Program

1. Clone or download this repository to your local machine.
2. Open your terminal or code editor (e.g., VS Code or PyCharm) in the project directory.
3. Run the main program:
```bash
python main.py

```


4. Follow the interactive CLI menu:
* **Option 1**: Register a new user (requires a User ID and 12-digit IC).
* **Option 2**: Log in using your User ID and password (last 4 digits of IC).
* **Option 3**: Calculate personal income tax by entering annual income and total tax relief.
* **Option 4**: Automatically execute and save the 5 required test cases (**T01 – T05**).
* **Option 5**: View all saved tax records formatted as a table via `pandas`.
* **Option 6**: Log out programme
* **Option 7**: Exit Programme



---

## 📊 Tax Calculation Rules (YA 2026 Summary)

* **Chargeable Income** = $\max(0, \text{Annual Income} - \text{Total Tax Relief})$
* **Progressive Tax Rates**: Applied across progressive tax brackets from 0% to 30%.
* **Individual Tax Rebate**: RM400 rebate is granted if chargeable income does not exceed RM35,000.

---

*Developed for Universiti Utara Malaysia (UUM) - SQITK3073 Individual Project.*
