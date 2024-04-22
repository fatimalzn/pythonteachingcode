import os
url = 'https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt'
file_name = 'elements1_20.txt'
cmd = f"curl {url} -o {file_name}"
os.system(cmd)

# open file 
elements_file = open('elements1_20.txt','r')
elements = elements_file.readline().strip()
element_names = []

while elements:
    element_names.append(elements.lower())
    elements = elements_file.readline().strip()

# get names function
def get_names():
    response = []
    count = 0
    while count < 5:
        answer = input("Welcome Fatima. List any 5 of the first 20 elements in the periodic table:")
        if answer in response:
            print("Can't enter the element twice. Try again")
            continue
        if answer == '': 
            print("Must enter an element")
            continue
        response.append(answer)
        count += 1
    return response
        
names = get_names()
# calculate the % correct
correct = []
incorrect=[]

for line in names:
    if line in element_names:
        correct.append(line.title())
    else:
        incorrect.append(line.title())

percent = len(correct) * 20

# print output 
print(percent,'%', 'correct')
print("Correct:\n",correct)
print("Incorrect:\n", incorrect)

elements_file.close()