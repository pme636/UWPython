# ------------------------------------------------------------------------ #
# Title: To Do
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# P. Everett 2-17-22, Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # An object that represents a file
objFile = None  # file handle
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""  # A user-input task to add to (or remove from) the To-Do List
strPriority = ""  # A user-input priority to add to the To-Do List
strQuit = ""  # user Y or N to quit program

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)


objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")  # Grab a row of data and split it based on comma location
    dicRow = {"task": strData[0], "priority": strData[1].strip()}  # convert the row to a dictionary row
    lstTable.append(dicRow)  # append the Dictionary Row to the Table list
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
	    Menu of Options
	    1) Show current data
	    2) Add a new item.
	    3) Remove an existing item.
	    4) Save Data to File
	    5) Exit Program
	    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new spacing line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Here's what you have in your To-Do list:\n")
        for row in lstTable:
            print("Task:", row['task'], "|", "Priority:", row['priority'])
        continue


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter the new task you'd like to add: ")
        strPri = input("Enter the priority of that task: ")
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable.append(dicRow)  # append the Dictionary Row to the Table list
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("Here are the tasks in the current list:\n")
        for row in lstTable:
            print(row['task'])  # Display list of tasks to user

        strTask = input("Whattask you would like to remove:")  # ask user for removal choice
        for row in lstTable:
            if row['task'].lower() == strTask.lower():  # compare each task to what the user entered.
                lstTable.remove(row)  # remove the matching task & priority
                print("Task: " + strTask + " removed from list!")
                #  print if matches

        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")  # open the file
        for row in lstTable:  #add tasks to the file by looping thru
            objFile.write(row['task'] + "," + row['priority'] + "\n")

        objFile.close()
        print("Data was saved")  # notify the user that their data is saved
        continue
    # Step 7 - Exit program after verifying user wants to do so
    elif (strChoice.strip() == '5'):
        strQuit = input("\nAre you sure you want to quit?  Enter Y or N:  ")
        if strQuit.lower() == "y":
            break  # and Exit the program
        else:
            continue


    else:
        print("\nError!  Please choose one of menu options by entering a number 1-5.\n")

