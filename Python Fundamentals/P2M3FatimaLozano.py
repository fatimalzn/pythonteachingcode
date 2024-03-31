poem_input = input("Welcome FATIMA LOZANO. Enter a poem: ")
words_list = poem_input.split()
list_length = len(words_list)

for i in range(list_length):
    if len(words_list[i]) <= 3:
        words_list[i]=words_list[i].lower()
    elif len(words_list[i]) >= 7:
        words_list[i]=words_list[i].upper()

new_list = []

def word_mixer(words_list):
    words_list.sort()
    while len(words_list) > 5:
        new_list.append(words_list.pop(-5))
        new_list.append(words_list.pop(0))
        new_list.append(words_list.pop(-1))
    return ' '.join(new_list)
    
print(word_mixer(words_list))