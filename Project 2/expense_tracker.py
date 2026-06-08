expenses_list = []  
total_spent = 0.0   

print("Welcome to Expense Tracker")

while True:
    print("\n================ MENU ================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("======================================")

    try:
        choice = int(input("Please Enter Your Choice (1-4): "))
    except ValueError:
        print("\n[Invalid Input] Please enter a valid menu number.")
        continue


    if choice == 1:
        print("\n--- Add New Expense ---")
        
        date = input("Enter the date (DD/MM/YYYY): ").strip()
        
        if len(date) != 10 or date[2] != '/' or date[5] != '/':
            print("\n[Invalid Data] Error: Date must be exactly in DD/MM/YYYY format.")
            continue
            
        try:
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])
        except ValueError:
            print("\n[Invalid Data] Error: Day, Month, and Year must be numbers.")
            continue

     
        if year < 1 or year > 2026:
            print("\n[Invalid Data] Error: Year must be a valid year up to 2026.")
            continue

     
        if month < 1 or month > 12:
            print("\n[Invalid Data] Error: Month must be between 01 and 12.")
            continue

     
        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
       
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                max_days = 29
            else:
                max_days = 28

        if day < 1 or day > max_days:
            print(f"\n[Invalid Data] Error: Day must be between 01 and {max_days} for month {month:02d} in the year {year}.")
            continue

        category = input("Enter the category (e.g., Food, Travel, Books): ").strip()
        if not category or category.isdigit():
            print("\n[Invalid Data] Error: Category must be descriptive text, not a number.")
            continue

        description = input("Enter a brief description: ").strip()
        if not description or description.isdigit():
            print("\n[Invalid Data] Error: Description must be text data, not a pure number.")
            continue
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("\n[Invalid Data] Error: Amount spent must be greater than 0.")
                continue
        except ValueError:
            print("\n[Invalid Data] Error: Amount must be a valid decimal number.")
            continue
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses_list.append(expense)

        total_spent = total_spent + amount
        
        if year == 2026:
            print("\nSuccess! Current expense recorded and total updated successfully.")
        else:
            print("\nSuccess! Historical data recorded and total updated successfully.")
    elif choice == 2:
        print("\n--- All Expenses ---")
        if len(expenses_list) == 0:
            print("No expenses recorded yet. Start adding some!")
        else:
            count = 1
            for each_expense in expenses_list:
                print(f"{count}. Date: {each_expense['date']} | "
                      f"Category: {each_expense['category']} | "
                      f"Description: {each_expense['description']} | "
                      f"Amount: ${each_expense['amount']:.2f}")
                count += 1
    elif choice == 3:
        print("\n--- Total Spending ---")
        print(f"Total Amount Spent: ${total_spent:.2f}")

    elif choice == 4:
        print("\nThank you for using the Expense Tracker. Goodbye!")
        break

    else:
        print("\n[Invalid Choice] Please select an option between 1 and 4.")