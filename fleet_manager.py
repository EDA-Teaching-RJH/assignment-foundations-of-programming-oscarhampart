def main():
    print("Welcome to Fleet Manager.")
    display_menu()

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Kirk"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    divs = ["Command", "Command", "Operations", "Security", "Command"]
    ids = ["SP-937-215", "SC-231-427", "NFN NMI Data", "Son of Mogh", "SC 937-0176 CEC"]
    
    return names, ranks, divs, ids


def display_menu():
    names, ranks, divs, ids = init_database()
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