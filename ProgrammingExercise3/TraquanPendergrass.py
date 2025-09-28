from functools import reduce

def main():
    expenses = []

    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ")
        if expense_type.lower() == "done":
            break
        try:
            amount = float(input(f"Enter amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not expenses:
        print("No expenses entered.")
        return

    # Total expense
    total = reduce(lambda x, y: x + y[1], expenses, 0)

    # Highest expense
    highest = reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

    # Lowest expense
    lowest = reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    print("\nExpense Summary:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

if __name__ == "__main__":
    main()
