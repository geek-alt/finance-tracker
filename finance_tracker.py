import json
import sys

expenses = []

def add_expense(amount,category,date,currency):
    expenses.append({'amount': amount, 'category':category,'date':date,'currency':currency})

def display_expenses():
    for expense in expenses:
        print(expense)
    
def summarize_expenses():
    summary={}
    for expense in expenses:
        category=expense['category']
        amount=expense['amount']
        summary[category]= summary.get(category, 0) + amount
    return summary

def save_expenses():
    with open('expenses.json', 'w')as file:
        json.dump(expenses,file)

def load_expenses():
    global expenses
    with open('expenses.json','r') as file:
        expenses=json.load(file)

def safe_input():
    while True:
        try:
            amount=float(input("Enter the amount:\n"))
            category=input("Enter the category:\n")
            date=input("Enter the dat in format of dd-mm-yyyy:\n")
            currency=input("Enter type of currency:\n")
            add_expense(amount,category,date,currency)
            break
        except ValueError:
            print("Invalid Input, Please review the input and try again!")
            break

def main():
    print("Welcome to the Expense Tracker")

    while True:
        print("\nMenu")
        print("1. Add new expense")
        print("2. Display all expenses")
        print("3. Summarize expenses")
        print("4. Save expenses to file")
        print("5. Load expenses from file")
        print("6. Exit")
        choice = input("Input the option you want to choose: \n")

        if choice == "1":
            safe_input()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            summary = summarize_expenses()
            print("Summary by category:")
            for category, amount in summary.items():
                print(f"{category}: {amount}")
        elif choice == "4":
            save_expenses()
            print("Expenses saved sucessfully.")
        elif choice == "5":
            load_expenses()
            print("Expenses Loaded sucessfully")
        elif choice == "6":
            print("Exiting....")
            break
        else:
            print("Invalid choice, please enter correct value")
if __name__ == '__main__':
    main()
