def main():
    print("Welcome to Fleet Manager.")
    display_menu()


def display_menu():
    fullName = input("What is your full name?").strip().title()
    print("Welcome", fullName)
    
    while True:
        print("\n == Fleet Manager Menu == \n 1. Display Roster \n 2. Add Member \n 3. Remove Member \n 4. Update Rank \n 5. Search Crew \n 6. Filter by Division \n 7. Calculate Payroll \n 8. Count Officers \n 9. Exit")
        choice = input("Select an option: ")

        if choice == "9":
            print("\n Thank you for using Fleet Manager, Goodbye.")
            break
        
        else:
            print("\n Invalid Option.")

main()