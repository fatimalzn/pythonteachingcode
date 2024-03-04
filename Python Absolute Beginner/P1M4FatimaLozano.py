def str_analysis(user_input):
        while user_input == "":
            user_input = input("FATIMA LOZANO, enter a word or integer:")
            if user_input.isdigit():
                if int(user_input) > 99:
                    print(user_input, "is a big number")
                if int(user_input) < 99:
                    print(user_input, "is a small number")
            elif user_input.isalpha() == True:
                print(user_input, " is all alphabetical")
            elif user_input.isalnum == True:
                print(user_input, "is neither alpha or digits")
str_analysis("")  