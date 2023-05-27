#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as f:
    letter = f.read()

with open("Input/Names/invited_names.txt") as f:
    names = f.read()

names = names.split("\n")

original = letter
for name in names:
    letter = original.replace("[name]", name)
    name = str.strip(name)

    file_path = f"Output/ReadyToSend/send_letter_to_" + name + ".txt"
    with open(file_path, "w") as f:
        f.write(letter)


