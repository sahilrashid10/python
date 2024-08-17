 ####    PASSWORD GENERATOR
import random
letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
print("WELCOME TO PASSWORD GENERATOR")

#get random index
l = int(input( "Enter the no of letters you want:"))

n = int(input( "Enter the no of numbers you want:"))

s = int(input("Enter the no of special characters you want:"))

password = []

#generate random password
for i in range(0,l):
  password.append(random.choice(letters))
for i in range(0,n):
  password.append(random.choice(numbers))
for i in range(0,s):
  password.append(random.choice(special_characters))
 
random.shuffle(password)
print(password)
