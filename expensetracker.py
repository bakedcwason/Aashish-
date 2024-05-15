class expense:
    def __init__(self,date,description,amount):
        self.date=date
        self.description=description 
        self.amount=amount

class expensetracker:
    def __init__(self):
        self.expenses=[]
    def add_expense(self,expense):
        self.expenses.append(expense)
    def remove_expense(self,index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("expense removed successfully")
        else:
            print("invalid expense index") 
    def view_expenses(self):
        if len(self.expenses) == 0:
            print("no expenses found")
        else:
            print("expense list:")
            for i, expenses in enumerate(self.expenses, start=1):
                print(f"{i}. date: {expenses.date}, Description: {expense.description}, amount: $(expense.amount:.2f)")
    def total_expenses(self):
        total=sum(expense.amount for expense in self.expenses)
        print(f"total expenses: ${total:.2f}")     
def main():
    tracker=expensetracker()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. view expenses")
        print("4. total expenses")
        print("5. exit")

        choice = input("enter your choice (1-5:)")

        if choice=="1":
            date =  input("enter the date(YYYY-MM-DD):")
            description=input("enter the description:")
            amount=float(input("enter the amount"))
            tracker.add_expense(expense)
            print("Expense added successfully")
        elif choice=="2":
            index=int(input("enter the expense index to remove:")) - 1
            tracker.remove_expense(index)
        elif choice=="3":
            tracker.view_expenses()
        elif choice=="4":
            tracker.total_expenses() 
        elif choice=="5":
            print("Goodbye")
            break
        else:
            print("invalid choice please try again")  
if __name__ == "__main__":
    main()                
