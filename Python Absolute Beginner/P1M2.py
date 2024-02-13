# [ ] create, call and test fishstore() function 
fish_entry = input("Type of fish: ")
price_entry = input("Cost of fish: ")
name = input("Your name: ")

def fishstore(): 
    fish = fish_entry.capitalize()
    print('Report for','[',name.upper(),']. Fish Type: ',fish,'costs','$'+ price_entry)
fishstore()