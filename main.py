# Community Water Monitoring System
# SDG 6: Clean Water and Sanitation

records = []

# Function 1: Add Record
def add_record():
    while True:
        name = str(input("Enter Community Name: "))
        if name.replace(" ", "").isalpha():
            break
        print("Please Enter letters only.")

    while True:
        district = str(input("Enter District Name: "))
        if district.replace(" ", "").isalpha():
            break
        print("Please Enter letters only.")

    while True:
        condition = input("Water Condition (Clean/Dirty): ").lower()
        if condition in ["clean", "dirty"]:
            break
        print("Please Enter Clean or Dirty only.")

    while True:
        try:
            people = int(input("Number of People Using Source: "))
            if people > 0:
                break
        except ValueError:
            print("Please Enter numbers only.")

    while True:
        availability = input("Water Available (Yes/No): ").lower()
        if availability in ["yes", "no"]:
            break
        print("Please Enter Yes or No only.")

    status = "Unsafe" if condition == "dirty" else "Safe"
    demand = "High" if people > 100 else "Low"

    if condition == "dirty" and availability == "no":
        risk = "CRITICAL"
    elif condition == "dirty":
        risk = "HIGH"
    elif availability == "no":
        risk = "MEDIUM"
    else:
        risk = "LOW"

    records.append([name, district, status, demand, risk])

    print("\nRecord Added Successfully")


# Function 2: View Results
def view_results():
    if len(records) == 0:
        print("No records available.")
    else:
        print("\nProcessed Results")
        for r in records:
            print("Community:", r[0])
            print("District:", r[1])
            print("Water Status:", r[2])
            print("Demand Level:", r[3])
            print("Risk Level:", r[4])
            print("-------------------")


# Main Program
while True:
    print("\n1. Add Record")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()

    elif choice == "2":
        view_results()

    elif choice == "3":
        print("Thank you for using this system.")
        break

    else:
        print("Invalid choice.")

