import os
import pandas as pd


def validate_ic(ic_number):
  return ic_number.isdigit() and len(ic_number) == 12


def register_user(user_id, ic_number, users_file="users.csv"):
  if not validate_ic(ic_number):
    print("[Error] Invalid IC number. Must be exactly 12 digits.")
    return False


  if os.path.exists(users_file):
    try:
      df_users = pd.read_csv(users_file)
      if (
          not df_users.empty
          and "User_ID" in df_users.columns
          and str(user_id) in df_users["User_ID"].astype(str).values
      ):
        print(f"[Error] User ID '{user_id}' already exists. Choose another.")
        return False
    except pd.errors.EmptyDataError:
      pass

  password = ic_number[-4:]
  user_keys = ["User_ID", "IC_Number", "Password"]
  user_values = [str(user_id), str(ic_number), str(password)]
  new_user_dict = dict(zip(user_keys, user_values))

  df_new = pd.DataFrame([new_user_dict])
  if not os.path.exists(users_file) or os.path.getsize(users_file) == 0:
    df_new.to_csv(users_file, index=False)
  else:
    df_new.to_csv(users_file, mode="a", header=False, index=False)

  print(f"[Success] User '{user_id}' registered successfully!")
  print(f"[Info] Your password is the last 4 digits of your IC: {password}")
  return True


def authenticate_user(user_id, password, users_file="users.csv"):
  if not os.path.exists(users_file):
    print("[Error] No registered users found. Please register first.")
    return False

  try:
    df_users = pd.read_csv(users_file)
    if df_users.empty:
      print("[Error] User database is empty.")
      return False

    match = df_users[
        (df_users["User_ID"].astype(str) == str(user_id))
        & (df_users["Password"].astype(str) == str(password))
    ]
    if not match.empty:
      print(f"[Success] Welcome back, {user_id}!")
      return True
    else:
      print("[Error] Invalid User ID or password.")
      return False
  except Exception as e:
    print(f"[Error] Authentication failed: {e}")
    return False


def calculate_tax(annual_income, tax_relief):
  chargeable_income = max(0.0, float(annual_income) - float(tax_relief))

  tax_brackets = [
      (5000, 0.00),
      (20000, 0.01),
      (35000, 0.03),
      (50000, 0.06),
      (70000, 0.11),
      (100000, 0.19),
      (400000, 0.25),
      (600000, 0.26),
      (2000000, 0.28),
      (float("inf"), 0.30),
  ]

  tax_before_rebate = 0.0
  previous_limit = 0.0

  for limit, rate in tax_brackets:
    if chargeable_income > limit:
      taxable_in_band = limit - previous_limit
      tax_before_rebate += taxable_in_band * rate
      previous_limit = limit
    else:
      taxable_in_band = chargeable_income - previous_limit
      tax_before_rebate += taxable_in_band * rate
      break


  tax_rebate = 400.0 if chargeable_income <= 35000.0 else 0.0

  final_tax_payable = max(0.0, tax_before_rebate - tax_rebate)

  return {
      "Chargeable_Income": round(chargeable_income, 2),
      "Tax_Before_Rebate": round(tax_before_rebate, 2),
      "Tax_Rebate": round(tax_rebate, 2),
      "Final_Tax_Payable": round(final_tax_payable, 2),
  }


def save_tax_record(
    user_id,
    test_case_id,
    year_assessment,
    annual_income,
    tax_relief,
    results,
    records_file="tax_records.csv",
):


  record_keys = [
      "User_ID",
      "Test_Case_ID",
      "Year_Assessment",
      "Annual_Income",
      "Total_Tax_Relief",
      "Chargeable_Income",
      "Tax_Before_Rebate",
      "Tax_Rebate",
      "Final_Tax_Payable",
  ]
  record_values = [
      str(user_id),
      test_case_id if test_case_id else "N/A",
      year_assessment,
      round(float(annual_income), 2),
      round(float(tax_relief), 2),
      results["Chargeable_Income"],
      results["Tax_Before_Rebate"],
      results["Tax_Rebate"],
      results["Final_Tax_Payable"],
  ]


  record_dict = dict(zip(record_keys, record_values))

  df_new = pd.DataFrame([record_dict])

  if not os.path.exists(records_file) or os.path.getsize(records_file) == 0:
    df_new.to_csv(records_file, index=False)
  else:
    df_new.to_csv(records_file, mode="a", header=False, index=False)


def load_and_display_records(records_file="tax_records.csv"):
  if not os.path.exists(records_file) or os.path.getsize(records_file) == 0:
    print("[Info] No tax records found in file.")
    return None

  try:
    df_records = pd.read_csv(records_file)
    print("\n" + "=" * 95)
    print(" SAVED TAX RECORDS (tax_records.csv)")
    print("=" * 95)
    print(df_records.to_string(index=False))
    print("=" * 95)
    return df_records
  except Exception as e:
    print(f"[Error] Failed to load tax records: {e}")
    return None