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
