colors = ["red", "blue", "yellow"]

def list_o_matic(color_input,colors):
        if color_input == "":
            popped_item = colors.pop()
            return popped_item, "popped from list"
        elif color_input.lower() in colors:
            colors.remove(color_input.lower())
            return color_input,"removed from list"
        else:
            colors.append(color_input)
            return color_input, "appended in list"

print("Welcome, FATIMA LOZANO. Enter a color or 'quit' to exit.")
while colors: 
    print("Current colors list:", colors)
    color_input = input("Enter a color: ")
    if color_input.lower() == "quit":
        print("Goodbye!")
        break
    else:
        print(list_o_matic(color_input,colors))