#import file
import os 
url = 'https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt'
file_name = "mean_temp.txt"
cmd = f"curl {url} -o {file_name}"
os.system(cmd)

# appending rio
add_rio = open('mean_temp.txt','a+')
add_rio.write("Rio de Janeiro,Brazil,30.0,18.0\n")

#adding headings variable
add_rio.seek(0)
headings = add_rio.readline().split(',')
print(headings)
add_rio.seek(0)

# [] create The Weather
city_temps = add_rio.readline().split(',')
print("FATIMA LOZANO, the weather is:\n")
      
while True:
    city_temps1 = add_rio.readline()
    if not city_temps1:
        break
    city_temps = city_temps1.split(',')
    print(headings[0],"of",city_temps[0],headings[2],"is",city_temps[2])

add_rio.close()