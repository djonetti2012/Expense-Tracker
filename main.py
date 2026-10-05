import subprocess
import sqlite3
import datetime
connection = sqlite3.connect("Expenses.db")
cursor = connection.cursor()
createTableQuery = '''
CREATE TABLE IF NOT EXISTS Expenses (
    name TEXT NOT NULL,
    date TEXT NOT NULL,º
    ammount INTEGER NOT NULL
)
'''
cursor.execute(createTableQuery)
connection.commit()
expenses = []

def addExpense(name = "", date = "", money = 0):
    if name == "":
        print("--------------Insert Expense Name-----------------")
        name = input("===> ")
        subprocess.run(["cmd", "/c", "cls"])
    if date == "":
        print("--------------Insert Expense Date (dd/mm/yyyy)----")
        date = input("===> ")
        subprocess.run(["cmd", "/c", "cls"])
    if money == 0:
        print("--------------Insert Expense Ammount--------------")
        money = input("===> ")
        subprocess.run(["cmd", "/c", "cls"])
    expense = {
        "name" : name,
        "date" : date,
        "money" : money
    }
    expenses.append(expense)
def deleteExpense(search = "", type = ""):
    if type == "":
        while True:
            print("""
#########################################
#------ Search which one to delete -----#
#---------------------------------------#
#----------- 1: Search By Date ---------#
#----------- 2: Search By Name ---------#
#----------- 3: Search By Ammount ------#
#----------- 4: See All ----------------#
#----------- 0: Back -------------------#
#########################################
""")
            type = input("===> ")
            try:
                type = int(type)
                if not (type > -1 and type < 5):
                    subprocess.run(["cmd", "/c", "cls"])
                    print("---------- Wrong Option, Choose Again ----------")
                    continue
            except ValueError:
                subprocess.run(["cmd", "/c", "cls"])
                print("---------- Wrong Option, Choose Again ----------")
                continue
            subprocess.run(["cmd", "/c", "cls"])

    if search == "":
        pass
def seeExpenses(type = ""):
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
        type = input("===> ")
        try:
            type = int(type)
            if not (type > -1 and type < 5):
                subprocess.run(["cmd", "/c", "cls"])
                print("---------- Wrong Option, Choose Again ----------")
                continue
        except ValueError:
            subprocess.run(["cmd", "/c", "cls"])
            print("---------- Wrong Option, Choose Again ----------")
            continue
        subprocess.run(["cmd", "/c", "cls"])
        
        if type == 1:
            print("#----------- Searching By Date --------------#")
            print("#----------- Insert date (dd/mm/yyyy) ---------#")
            date = input("===> ")
            results = []
            number = 1
            for i in expenses:
                if i["date"] == date:
                    results.append(i)
                    print(f"{number}: {i}")
                    number =+1
            return results
        elif type == 2:
            print("#----------- Searching By Name --------------#")
            print("#----------- Insert Name --------------#")
            name = input("===> ")
            results = []
            number = 1
            for i in expenses:
                if i["name"] == name:
                    results.append(i)
                    print(f"{number}: {i}")
                    number =+1
            return results
        elif type == 3:
            print("#----------- Searching By ammount --------------#")
            print("#----------- Insert Ammount --------------#")
            ammount = input("===> ")
            results = []
            number = 1
            for i in expenses:
                if i["money"] == ammount:
                    results.append(i)
                    print(f"{number}: {i}")
                    number =+1
            return results
        elif type == 4:
            print("#----------- Showing all --------------#")
            number = 1
            for i in expenses:
                print(f"{number}: {i}")
                number =+ 1
        elif type == 0:
            break



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
                subprocess.run(["cmd", "/c", "cls"])
                print("---------- Wrong Option, Choose Again ----------")
                continue
        except ValueError:
            subprocess.run(["cmd", "/c", "cls"])
            print("---------- Wrong Option, Choose Again ----------")
            continue
        subprocess.run(["cmd", "/c", "cls"])
        if option == 1:
            addExpense()
        elif option == 2:
            deleteExpense()
        else:
            seeExpenses()
