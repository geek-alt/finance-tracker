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

def safa_input():
    try:
        amount=float(input("Enter the amount:\n"))
        category=input("Enter the category: \n")
        date=input("Enter the dat in format of dd-mm-yyyy: \n")
    except ValueError:
        print("Invalid Input, Please review the input and try again!")
