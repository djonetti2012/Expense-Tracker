import os
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
        Option = input("===> ")
        try:
            Option = int(Option)
            if not (Option > 0 and Option < 4):
                os.system("cls")
                print("---------- Wrong Option, Choose Again ----------")
                continue
        except ValueError:
            os.system("cls")
            print("---------- Wrong Option, Choose Again ----------")
            continue
        os.system("cls")