import os

expenses = []

def addExpense(name, date, money):
    expense = {
        "name" : name,
        "date" : date,
        "money" : money
    }
    expenses.append(expense)
def deleteExpense(name):
    pass
def seeExpenses():
    while True:
        print("""
#########################################
#----------- 1: Search By Date ---------#
#----------- 2: Search By Name ---------#
#----------- 3: Search By Ammount ------#
#----------- 4: See All ----------------#
#----------- 0: Back -------------------#
#########################################
""")
        #Get User Option
        print("----- Choose An Option -----")
        option = input("===> ")
        try:
            option = int(option)
            if not (option > -1 and option < 5):
                os.system("cls")
                print("---------- Wrong Option, Choose Again ----------")
                continue
        except ValueError:
            os.system("cls")
            print("---------- Wrong Option, Choose Again ----------")
            continue
        os.system("cls")
        
        if option == 1:
            print("#----------- Searching By Date --------------#")
            print("#----------- Insert date (dd/mm/yyyy) ---------#")
            date = input("===> ")
            results = []
            number = 1
            for i in expenses:
                if i["date"] == date:
                    results.append(i)
            for i in results:
                print(f"{number}: {i}")


if __name__ == "__main__":
    print("""
#########################################
#---------------------------------------#
#------------\033[1;3mMade By Djonetti\033[0m-----------#
#---------------------------------------#
#########################################
""")
    while True:
        print("""
#########################################
#----------- 1: Add Expense ------------#
#----------- 2: Delete Expense ---------#
#----------- 3: View Tracked Expenses --#
#########################################
""")
        
#Get User Option
        print("----- Choose An Option -----")
        option = input("===> ")
        try:
            option = int(option)
            if not (option > 0 and option < 4):
                os.system("cls")
                print("---------- Wrong Option, Choose Again ----------")
                continue
        except ValueError:
            os.system("cls")
            print("---------- Wrong Option, Choose Again ----------")
            continue
        os.system("cls")
        if option == 1:
            addExpense()
        elif option == 2:
            deleteExpense()
        else:
            seeExpenses()
