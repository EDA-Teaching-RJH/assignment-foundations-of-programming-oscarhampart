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

        if choice == "1":
            display_roster(names, ranks, divs, ids)

        elif choice == "2":
            add_members(names, ranks, divs, ids)

        elif choice == "3":
            remove_member(names, ranks, divs, ids)

        elif choice == "9":
            print("\nThank you for using Fleet Manager, Goodbye.")
            break
        
        else:
            print("\nInvalid Option.")

def display_roster(names, ranks, divs, ids):
    print("\nDisplaying Roster...")
    for i in range(len(names)):
        print(names[i], " - ", ranks[i], " - ", divs[i], " - ", ids [i])
    

def add_members(names, ranks, divs, ids):
    valid_ranks = ["Fleet Admiral", "Admiral", "Vice Admiral", "Rear Admiral", "Commodore", "Captain", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant Junior", "Ensign"]

    print("\nAdding New Crew Member...")
    new_name = input("Enter Full Name: ").strip().title()

    while True:
        new_rank = input("Enter Rank: ").strip().title()
        if new_rank not in valid_ranks:
            print("Invalid Rank. Please Re-enter.")
        else:
            break
    
    new_div = input("Enter Division: ").strip().title()

    while True:
        new_id = input("Enter Unique ID: ").strip().upper()
        if new_id in ids:
            print("This ID is taken. Please Re-enter.")
        else:
            break
    
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)

    print(new_name, "has become a new Member.")


def remove_member(names, ranks, divs, ids):
    print("\nRemoving Member...")

    while True:
        remove_id = input("Enter the ID of the Member who will be removed: ").strip()
        if remove_id in ids:
            removeIndex = ids.index(remove_id)
            removed_name = names[removeIndex]

            names.pop(removeIndex)
            ranks.pop(removeIndex)
            divs.pop(removeIndex)
            ids.pop(removeIndex)

            print(removed_name, "has been kicked from the Crew.")
            break

        else:
            print("This member does not exist. Please Re-enter.")
            
    
main()