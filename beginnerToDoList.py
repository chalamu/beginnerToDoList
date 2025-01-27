# | Name | Date | Priority  <- Header for the todo list items.
import os, time  
todo = []  # Initialize an empty list called 'todo' to store the todo items.

def add():  # Define a function called 'add' to add a new todo item.
    time.sleep(1)  # Pause for 1 second.
    os.system("clear")  # Clear the console.
    name = input("Name: ")  # Prompt the user to input the name of the todo item.
    date = input("Date: ")  # Prompt the user to input the date of the todo item.
    priority = input("Priority: ").capitalize()  # Prompt the user to input the priority, capitalize it, and store it.
    row = [name, date, priority]  # Create a list called 'row' containing the name, date, and priority.
    todo.append(row)  # Add the 'row' list to the 'todo' list.
    print("Added Successfully")  # Print a success message.

def view():  # Define a function called 'view' to display the todo items.
    time.sleep(1)  # Pause for 1 second.
    os.system("clear")  # Clear the console.
    options = input("1: Add\n2: By Priority\n3: By Date\n>") #Asks if you want to view all todo items, or by priority or by date
    if options == "1":  # Check if the user wants to view all todo items.
        for row in todo:  # Iterate through each 'row' in the 'todo' list.
            for item in row:  # Iterate through each 'item' in the 'row'.
                print(item, end=" | ")  # Print the 'item' followed by " | ".
            print()  # Print a new line after each row.
    else:  # If the user wants to view items by priority.
        priority = input("What priority?> ").capitalize()  # Prompt for the priority to view and capitalize it.
        for row in todo:  # Iterate through each 'row' in the 'todo' list.
            if priority in row:  # Check if the specified 'priority' is in the current 'row'.
                for item in row:  # Iterate through each 'item' in the 'row'.
                    print(item, end=" | ")  # Print the 'item' followed by " | ".
                print()  # Print a new line after each row.
            time.sleep(1) #Pause 1 second

def edit():  # Define a function called 'edit' to edit a todo item.
    time.sleep(1)  # Pause for 1 second.
    os.system("clear")  # Clear the console.
    find = input("Name of todo to edit> ")  # Prompt the user for the name of the todo item to edit.
    found = False  # Initialize a boolean variable 'found' to False.
    for row in todo:  # Iterate through each 'row' in the 'todo' list.
        if find in row:  # Check if the specified 'find' string is in the current 'row'.
            found = True  # Set 'found' to True if the item is found.
    if not found:  # If the item is not found.
        print("Couldnt find that")  # Print an error message.
        return  # Exit the function.
    for row in todo:
        if find in row:
            todo.remove(row) # Remove the selected row
    name = input("Name: ")  # Prompt the user to input the new name.
    date = input("Date: ")  # Prompt the user to input the new date.
    priority = input("Priority: ").capitalize()  # Prompt the user to input the new priority.
    row = [name, date, priority]  # Create a new row with the updated information.
    todo.append(row)  # Add the new row to the todo list.
    print("Added Successfully")  # Print a success message.

def remove():  # Define a function called 'remove' to remove a todo item.
    time.sleep(1)  # Pause for 1 second.
    os.system("clear")  # Clear the console.
    find = input("Name of todo to remove> ")  # Prompt the user for the name of the item to remove.
    for row in todo:  # Iterate through each 'row' in the 'todo' list.
        if find in row:  # Check if the specified 'find' string is in the current 'row'.
            todo.remove(row)  # Remove the row from the 'todo' list.

while True:  # Start an infinite loop.
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n5: Exit\n>")  # Display a menu and get the user's choice.
    if menu =="1":  # Check if the user chose option 1 (Add).
        add()  # Call the 'add' function.
    elif menu =="2":  # Check if the user chose option 2 (View).
        view()  # Call the 'view' function.
    elif menu =="3":  # Check if the user chose option 3 (Edit).
        edit()  # Call the 'edit' function.
    elif menu =="4":  # Check if the user chose option 4 (Remove).
        remove()  # Call the 'remove' function.
    elif menu =="5": # Check if user chose option 5(exit)
        exit() #Exit the program
time.sleep(1)  # Pause for 1 second.
os.system("clear") # Clear the console.
