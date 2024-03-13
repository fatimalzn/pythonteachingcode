items = "\n" 
total = 0
def adding_report(report = "T"):
    global total
    while True:
        user_input = input("Enter an integer or Q: ")
        if user_input.isdigit():
            if report == "A":
                total += int(user_input)
                print (items, user_input)
            elif report == "T":
                total += int(user_input)
        elif user_input.startswith("Q"):
            print("total:\n",total,"\nCalculated by: FATIMA LOZANO")
            break
        else:
            print("Invalid")
        
adding_report("T") 