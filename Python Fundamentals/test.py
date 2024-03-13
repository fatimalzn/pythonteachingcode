word = ""
quote_string = input("Input quote")

for character in quote_string: 
    if character.isalpha():
        word += character
        if word.lower() >= "h":
                print(word.upper)
                word = " "
        else: 
                word = " "