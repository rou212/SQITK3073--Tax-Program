
from function import (
    authenticate_user,
    calculate_tax,
    load_and_display_records,
    register_user,
    save_tax_record,
)


def run_test_cases(current_user):
  test_cases = [
      {"id": "T01", "income": 9000, "relief": 9000},
      {"id": "T02", "income": 40000, "relief": 9000},
      {"id": "T03", "income": 65000, "relief": 14000},
      {"id": "T04", "income": 120000, "relief": 18000},
      {"id": "T05", "income": 83000, "relief": 12000},
  ]

  print("\n--- Executing Required Tax Calculation Test Cases (YA 2026) ---")
  for tc in test_cases:
    res = calculate_tax(tc["income"], tc["relief"])
    save_tax_record(
        user_id=current_user,
        test_case_id=tc["id"],
        year_assessment=2026,
        annual_income=tc["income"],
        tax_relief=tc["relief"],
        results=res,
    )
    print(
        f"Test Case {tc['id']} processed & saved -> Chargeable: RM{res['Chargeable_Income']:,.2f} | Final Tax: RM{res['Final_Tax_Payable']:,.2f}"
    )
  print("[Success] All 5 test cases successfully calculated and saved to tax_records.csv!\n")


def main():
  current_user = None

  while True:
    print("\n==============================================")
    print(" MALAYSIAN TAX INPUT & CALCULATION PROGRAM")
    print("==============================================")
    if current_user:
      print(f" Status: Logged in as [{current_user}]")
    else:
      print(" Status: Not Logged In")
    print("----------------------------------------------")
    print("1. Register New User")
    print("2. User Login")
    print("3. Calculate Personal Income Tax (YA 2026)")
    print("4. Run & Save 5 Project Test Cases (T01-T05)")
    print("5. View All Saved Tax Records")
    print("6. Logout")
    print("7. Exit Program")
    print("==============================================")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
      print("\n--- User Registration ---")
      u_id = input("Enter desired User ID: ").strip()
      ic = input("Enter 12-digit IC Number (without dashes): ").strip()
      if not u_id or not ic:
        print("[Error] Fields cannot be empty.")
      elif not u_id.isdigit():
        print("[Error] please enter userid")
      else:
        register_user(u_id, ic)

    elif choice == "2":
      print("\n--- User Login ---")
      u_id = input("Enter User ID: ").strip()
      pwd = input("Enter Password (last 4 digits of IC): ").strip()
      if not u_id or not pwd:
        print("[Error] Fields cannot be empty.")
      elif not u_id.isdigit():
        print("[Error] please enter userid")
      else:
        if authenticate_user(u_id, pwd):
          current_user = u_id

    elif choice == "3":
      if not current_user:
        print("[Error] Please log in first before calculating tax.")
        continue

      print(f"\n--- Personal Income Tax Calculation (YA 2026) [{current_user}] ---")
      try:
        income_input = input("Enter Annual Income (RM): ").strip()
        relief_input = input("Enter Total Eligible Tax Relief (RM): ").strip()

        annual_income = float(income_input)
        tax_relief = float(relief_input)

        if annual_income < 0 or tax_relief < 0:
          print("[Error] Monetary amounts cannot be negative.")
          continue

        results = calculate_tax(annual_income, tax_relief)

        print("\n" + "-" * 40)
        print(" TAX CALCULATION RESULTS")
        print("-" * 40)
        print(f" Annual Income     : RM {annual_income:,.2f}")
        print(f" Total Tax Relief  : RM {tax_relief:,.2f}")
        print(f" Chargeable Income : RM {results['Chargeable_Income']:,.2f}")
        print(f" Tax Before Rebate : RM {results['Tax_Before_Rebate']:,.2f}")
        print(f" Individual Rebate : RM {results['Tax_Rebate']:,.2f}")
        print(f" Final Tax Payable : RM {results['Final_Tax_Payable']:,.2f}")
        print("-" * 40)

        save_choice = (
            input("Do you wish to save this record to CSV? (y/n): ")
            .strip()
            .lower()
        )
        if save_choice == "y":
          save_tax_record(
              user_id=current_user,
              test_case_id="Custom",
              year_assessment=2026,
              annual_income=annual_income,
              tax_relief=tax_relief,
              results=results,
          )
          print("[Success] Record successfully saved to tax_records.csv!")

      except ValueError:
        print("[Error] Invalid numeric input. Please enter valid numbers.")

    elif choice == "4":
      if not current_user:
        print("[Error] Please log in first to run test cases.")
        continue
      run_test_cases(current_user)

    elif choice == "5":
      if not current_user:
        print("[Error] Please log in first to view saved tax records.")
        continue
      load_and_display_records()

    elif choice == "6":
      if current_user:
        print(f"[Info] User '{current_user}' logged out successfully.")
        current_user = None
      else:
        print("[Info] No user is currently logged in.")

    elif choice == "7":
      print("\nThank you for using the Malaysian Tax Input Program. Goodbye!")
      break
    else:
      print("[Error] Invalid choice! Please select between 1 and 7.")


if __name__ == "__main__":
  main()
