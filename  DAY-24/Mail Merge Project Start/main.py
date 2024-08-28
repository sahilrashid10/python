#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as file:
    old_letter = file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = old_letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt",'a')as new_file:
            new_file.write(new_letter)
