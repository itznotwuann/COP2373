from functools import reduce

def main():
    expenses = []

    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == "done":
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.")

    if not expenses:
        print("No expenses entered.")
        return

    # Total using reduce
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)

    # Highest using reduce
    highest = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

    # Lowest using reduce
    lowest = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    print("\n--- Expense Report ---")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")

if __name__ == "__main__":
    main()
